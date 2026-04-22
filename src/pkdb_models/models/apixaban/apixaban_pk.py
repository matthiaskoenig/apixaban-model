import numpy as np
import pandas as pd
from pkdb_analysis.pk.pharmacokinetics import TimecoursePK


def process_substance_pk(experiment, xres, scandim, dose_index, dose_value, substance, keys):
    """Process PK calculations for a substance."""
    Q_ = experiment.Q_

    # Get time and concentration vectors
    t_vec = Q_(xres.dim_mean("time").magnitude, xres.uinfo["time"])
    conc_key = keys["conc_key"]
    c_vec = Q_(
        xres[conc_key].sel({scandim: dose_index}).values,
        xres.uinfo[conc_key]
    )

    # Set up TimecoursePK parameters
    tpkw = {
        "time": t_vec,
        "concentration": c_vec,
        "substance": substance,
        "ureg": experiment.ureg,
        "dose": dose_value if keys.get("dose_used", False) else None
    }

    if keys.get("dose_used", False) and "min_threshold" in keys:
        tpkw["min_treshold"] = keys["min_threshold"]

    # Calculate basic PK parameters
    tcpk = TimecoursePK(**tpkw)
    pk_dict = tcpk.pk.to_dict()
    pk_dict["substance"] = substance

    # manually calculate AUCend(0->12hr, 0->48hr, 0->72hr, 0->96hr)
    t_vec_values = t_vec.magnitude
    for t_end in [12 * 60, 24 * 60, 48 * 60, 72 * 60, 96 * 60]:
        t_vec = t_vec_values[t_vec_values <= t_end]
        t_idx = np.where(t_vec_values <= t_end)[0][-1]
        c_vec_values = c_vec.magnitude[0:t_idx+1]
        auc_end = np.sum((t_vec[1:] - t_vec[0:-1]) * (c_vec_values[1:] + c_vec_values[0:-1]) / 2.0)
        pk_dict[f"aucend_{int(t_end / 60)}"] = auc_end
        pk_dict[f"aucend_{int(t_end / 60)}_unit"] = tcpk.pk.auc.units

    # For metabolites: calculate additional clearance parameters
    if substance in ["api", "m1", "m7"]:
        # Renal clearance
        aurine_key = keys["aurine_key"]
        aurine_vec = Q_(
            xres[aurine_key].sel({scandim: dose_index}).values,
            xres.uinfo[aurine_key]
        )
        pk_dict[aurine_key] = aurine_vec.magnitude[-1]
        pk_dict[f"{aurine_key}_unit"] = aurine_vec.units
        cl_renal = aurine_vec[-1] / tcpk.pk.auc
        pk_dict["cl_renal"] = cl_renal.magnitude
        pk_dict["cl_renal_unit"] = cl_renal.units

        # Fecal clearance
        afeces_key = keys["afeces_key"]
        afeces_vec = Q_(
            xres[afeces_key].sel({scandim: dose_index}).values,
            xres.uinfo[afeces_key]
        )
        pk_dict[afeces_key] = afeces_vec.magnitude[-1]
        pk_dict[f"{afeces_key}_unit"] = afeces_vec.units
        cl_fecal = afeces_vec[-1] / tcpk.pk.auc
        pk_dict["cl_fecal"] = cl_fecal.magnitude
        pk_dict["cl_fecal_unit"] = cl_fecal.units

        # Total clearance (sum of renal and fecal)
        pk_dict["cl_total"] = pk_dict["cl_renal"] + pk_dict["cl_fecal"]
        pk_dict["cl_total_unit"] = pk_dict["cl_renal_unit"]

        # Apparent clearance (dose/AUC)
        if dose_value is not None:
            dose_mmol = dose_value / experiment.Mr.riv
            # Correction factor for metabolites
            # no correction factors due to unknown molecular weights
            correction_factor = 1.0
            cl_apparent = dose_mmol / tcpk.pk.auc * correction_factor
            pk_dict["cl"] = cl_apparent.magnitude
            pk_dict["cl_unit"] = cl_apparent.units
        else:
            pk_dict["cl"] = float('nan')
            pk_dict["cl_unit"] = tcpk.pk.auc.units.replace('*min', '')

        # Add AUC and volume of distribution
        pk_dict["auc"] = tcpk.pk.auc.magnitude
        pk_dict["auc_unit"] = tcpk.pk.auc.units
        pk_dict["vd"] = pk_dict['cl'] / tcpk.pk.kel.magnitude
        pk_dict["vd_unit"] = f"{pk_dict['cl_unit']}/{tcpk.pk.kel.units}"

    return pk_dict


def calculate_apixaban_pk(experiment, xres):
    """Calculate PK parameters for rivaroxaban, and metabolites."""
    # Get scanned dimension and dose vector
    scandim = xres._redop_dims()[0]
    dose_vec = experiment.Q_(xres["PODOSE_api"].values[0], xres.uinfo["PODOSE_api"])

    # Define substance info dictionaries
    substance_info = {
        "api": {
            "conc_key": "[Cve_api]",
            "aurine_key": "Aurine_api",
            "afeces_key": "Afeces_api",
            "dose_used": True,
        },
        "m1": {
            "conc_key": "[Cve_m1]",
            "aurine_key": "Aurine_m1",
            "afeces_key": "Afeces_m1",
            "dose_used": False,
        },
        "m7": {
            "conc_key": "[Cve_m7]",
            "aurine_key": "Aurine_m7",
            "afeces_key": "Afeces_m7",
            "dose_used": False,
        },
    }

    # Process each substance for each dose
    pk_dicts = []
    for substance, keys in substance_info.items():
        for idx, dose in enumerate(dose_vec):
            pk_dict = process_substance_pk(experiment, xres, scandim, idx, dose, substance, keys)
            pk_dicts.append(pk_dict)


    return pd.DataFrame(pk_dicts)

def calculate_apixaban_pd(experiment, xres) -> pd.DataFrame:
    scandim = xres._redop_dims()[0]
    dose_vec = experiment.Q_(xres["PODOSE_api"].values[0], xres.uinfo["PODOSE_api"])

    Q_ = experiment.Q_

    dfs = {}
    for sid in [
        "INR",
        "mPT",
        "PT",
        "aPTT",
        "Xa_inhibition",
        "antiXa_activity",
        "INR_ratio",
        "mPT_ratio",
        "PT_ratio",
        "aPTT_ratio",
    ]:
        pd_dicts = []
        for idx, dose in enumerate(dose_vec):
            # Get values
            values = Q_(
                xres[sid].sel({scandim: idx}).values,
                xres.uinfo[sid]
            )
            pd_dict = {
                "sid": sid,
                "min": values.magnitude.min(),
                "max": values.magnitude.max(),
                "unit": values.units
            }
            pd_dicts.append(pd_dict)
        dfs[sid] = pd.DataFrame(pd_dicts)

    return dfs
