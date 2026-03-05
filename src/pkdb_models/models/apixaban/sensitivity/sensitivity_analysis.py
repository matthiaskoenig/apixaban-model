"""Sensitivity analysis."""
from __future__ import annotations

import numpy as np
import pandas as pd
import roadrunner
from pint import UnitRegistry
from sbmlutils.console import console

from pkdb_analysis.pk.pharmacokinetics import TimecoursePK

from sbmlsim.sensitivity.analysis import (
    SensitivitySimulation,
    SensitivityOutput,
    AnalysisGroup,
)
from sbmlsim.sensitivity.parameters import (
    SensitivityParameter,
    ParameterType,
)

from pkdb_models.models.apixaban import MODEL_PATH
from pkdb_models.models.apixaban.fitting.parameters import parameters_all as fit_parameters

# Subgroups to perform sensitivity analysis
sensitivity_groups: list[AnalysisGroup] = [
    AnalysisGroup(
        uid="control",
        name="Control",
        changes={},
        color="dimgrey",
    ),
    AnalysisGroup(
        uid="mildRI",
        name="Mild renal impairment",
        changes={"KI__f_renal_function": 0.5},
        color="#66c2a4",
    ),
    AnalysisGroup(
        uid="modRI",
        name="Moderate renal impairment",
        changes={"KI__f_renal_function": 0.35},
        color="#2ca25f",
    ),
    AnalysisGroup(
        uid="sevRI",
        name="Severe renal impairment",
        changes={"KI__f_renal_function": 0.20},
        color="#006d2c",
    ),
    AnalysisGroup(
        uid="CPT A",
        name="Mild cirrhosis (CPT A)",
        changes={"f_cirrhosis": 0.399},
        color="#74a9cf",
    ),
    AnalysisGroup(
        uid="CPT B",
        name="Moderate cirrhosis (CPT B)",
        changes={"f_cirrhosis": 0.698},
        color="#2b8cbe",
    ),
    AnalysisGroup(
        uid="CPT C",
        name="Severe cirrhosis (CPT C)",
        changes={"f_cirrhosis": 0.813},
        color="#045a8d",
    ),
]


class ApixabanSensitivitySimulation(SensitivitySimulation):
    """Simulation for sensitivity calculation."""


    def simulate(self, r: roadrunner.RoadRunner, changes: dict[str, float]) -> dict[str, float]:
        tend = 5 * 24 * 60  # [min]
        steps = 3000

        # apply changes and simulate
        all_changes = {
            **self.changes_simulation,  # model
            **changes  # sensitivity
        }
        self.apply_changes(r, all_changes, reset_all=True)
        # ensure tolerances
        r.integrator.setValue("absolute_tolerance", self.init_tolerances)
        s = r.simulate(start=0, end=tend, steps=steps)

        # pharmacokinetic parameters
        y: dict[str, float] = {}

        # pharmacokinetics
        ureg = UnitRegistry()
        Q_ = ureg.Quantity

        Mr_api = Q_(459.5, "g/mole")
        time = Q_(s["time"], "min")
        tcpk = TimecoursePK(
            time=time,
            concentration=Q_(s["[Cve_api]"], "mM"),
            substance="apixaban",
            ureg=ureg,
            dose=Q_(5, "mg")/Mr_api,
        )
        pk_dict = tcpk.pk.to_dict()
        # console.print(pk_dict)
        for pk_key in [
            "aucinf",
            "cmax",
            "thalf",
            "vd",
            "cl",
            "kel",
        ]:
            y[f"[Cve_api]_{pk_key}"] = pk_dict[pk_key]

        # metabolites
        for sid in [
            "[Cve_m1]", "[Cve_m7]",
        ]:
            tcpk = TimecoursePK(
                time=time,
                concentration=Q_(s[sid], "mM"),
                substance="apixaban",
                ureg=ureg,
                dose=None,
            )
            pk_dict = tcpk.pk.to_dict()
            # console.print(pk_dict)
            for pk_key in [
                "aucinf",
                "cmax",
                "thalf",
                # "kel",
            ]:
                y[f"{sid}_{pk_key}"] = pk_dict[pk_key]

        # pharmacodynamics
        for sid, f in [
            ("PT", "max"),
            ("mPT", "max"),
            ("aPTT", "max"),
            ("INR", "max"),
            ("Xa_inhibition", "max"),
        ]:
            # minimal and maximal value of readout
            if f == "max":
                y[f"{sid}_max"] = np.max(s[sid])
            elif f == "min":
                y[f"{sid}_min"] = np.min(s[sid])

        return y



sensitivity_simulation = ApixabanSensitivitySimulation(
    model_path=MODEL_PATH,
    selections=[
        "time",
        "[Cve_api]",
        "[Cve_m1]",
        "[Cve_m7]",
        "PT",
        "mPT",
        "aPTT",
        "INR",
        "Xa_inhibition",
    ],
    changes_simulation = {
        # ! make sure all the changes from base-experiment are injected here !
        # FIXME: auto-inject changes from base-experiment
        "PODOSE_api": 5,  # [mg]
    },
    outputs=[
        # FIXME: auto-calculate units
        SensitivityOutput(uid='[Cve_api]_aucinf', name='API AUC∞', unit="mM*min"),
        SensitivityOutput(uid='[Cve_api]_cmax', name='API Cmax', unit="mM"),
        SensitivityOutput(uid='[Cve_api]_thalf', name='API Half-life', unit="min"),
        SensitivityOutput(uid='[Cve_api]_vd', name='API Vd', unit="l"),
        SensitivityOutput(uid='[Cve_api]_cl', name='API CL', unit="mole/min/mM"),
        SensitivityOutput(uid='[Cve_api]_kel', name='API kel', unit="1/min"),

        SensitivityOutput(uid='[Cve_m1]_aucinf', name='M1 AUC∞', unit="mM*min"),
        SensitivityOutput(uid='[Cve_m1]_cmax', name='M1 Cmax', unit="mmole/l"),
        SensitivityOutput(uid='[Cve_m1]_thalf', name='M1 Half-life', unit="min"),

        SensitivityOutput(uid='[Cve_m7]_aucinf', name='M7 AUC∞', unit="mM*min"),
        SensitivityOutput(uid='[Cve_m7]_cmax', name='M7 Cmax', unit="mmole/l"),
        SensitivityOutput(uid='[Cve_m7]_thalf', name='M7 Half-life', unit="min"),

        SensitivityOutput(uid='PT_max', name='max PT', unit="s"),
        SensitivityOutput(uid='mPT_max', name='max mPT', unit="s"),
        SensitivityOutput(uid='aPTT_max', name='max aPTT', unit="s"),
        SensitivityOutput(uid='INR_max', name='max INR', unit="dimensionless"),
        SensitivityOutput(uid='Xa_inhibition_max', name='max Xa inhibition', unit="dimensionless"),
    ]
)


def _sensitivity_parameters() -> list[SensitivityParameter]:
    """Definition of parameters and bounds for sensitivity analysis."""
    console.rule("Parameters", style="white")
    # parameters for sensitivity analysis
    parameters: list[SensitivityParameter] = SensitivityParameter.parameters_from_sbml(
        sbml_path=MODEL_PATH,
        exclude_ids={
            # conversion factors
            "conversion_min_per_day",

            # molecular weights
            "Mr_api",
            "Mr_m1",
            "Mr_m7",

            # unchangable values
            "FQlu",
            "FVhv",
            "FVpo",

            # dosing parameters
            "PODOSE_api",
            "IVDOSE_api",
            "ti_api",
            "Ki_api",
            "Ri_api",

            # unused volumes
            "Vurine",
            "Vfeces",
            "Vplasma",
            "Vstomach",
            "LI__Vbi",

            # reference values
            "PT_ref",
            "mPT_ref",
            "aPTT_ref",
            "INR_ref",
        },
        exclude_na=True,
        exclude_zero=True,
    )

    # bounds from fitted parameters
    fit_bounds = [
        (fp.pid, fp.lower_bound, fp.upper_bound, ParameterType.FIT) for fp in fit_parameters
        # (fp.pid, np.nan, np.nan, ParameterType.FIT) for fp in fit_parameters
    ]

    SensitivityParameter.parameters_set_bounds(parameters, bounds=fit_bounds)

    # bounds from scaled parameters
    bounds_fraction = 0.15  # fraction of bounds relative to value
    uids_scaling = [
        "GU__F_api_abs",
        "KI__f_renal_function",
    ]
    scaling_bounds = [
        (uid, 1 - bounds_fraction, 1 + bounds_fraction, ParameterType.SCALING) for uid in uids_scaling
    ]
    SensitivityParameter.parameters_set_bounds(parameters, bounds=scaling_bounds)

    # references for values
    reference_data={
        "HCT": r"\cite{Mondal2025, Fiseha2023}",
        "BW": r"\cite{Ogden2004, Jones2013, Thompson2009, Brown1997}",
        "FQgu": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FQh": r"\cite{Jones2013, Wynne1989, Thompson2009, Brown1997}",
        "FQki": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FVar": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FVgu": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FVki": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FVli": r"\cite{Jones2013, Wynne1989, Thompson2009, Brown1997}",
        "FVlu": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FVve": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "COBW": r"\cite{Cattermole2017, Patel2021, Collis2001}",
        # "HR": r"\cite{Cattermole2017, Patel2021, Collis2001, Thompson2009}",
        "KI__f_renal_function": r"\cite{Stevens2024}",
    }
    p_dict = {p.uid: p for p in parameters}
    for pid, reference in reference_data.items():
        p = p_dict[pid]
        p.reference = reference
        if p.type == ParameterType.NA:
            p.type = ParameterType.DATA

    # setting missing bounds;
    for p in parameters:
        if np.isnan(p.lower_bound) and np.isnan(p.upper_bound):
            p.lower_bound = p.value * (1 - bounds_fraction)
            p.upper_bound = p.value * (1 + bounds_fraction)

    # print parameters
    pd.options.display.float_format = "{:.5g}".format
    df_parameters = SensitivityParameter.parameters_to_df(parameters)
    console.print(df_parameters)

    return parameters

sensitivity_parameters = _sensitivity_parameters()


if __name__ == "__main__":
    import multiprocessing
    from sbmlsim.sensitivity import (
        SobolSensitivityAnalysis,
        LocalSensitivityAnalysis,
        SamplingSensitivityAnalysis,
        FASTSensitivityAnalysis,
    )
    from pkdb_models.models.apixaban import RESULTS_PATH

    sensitivity_path = RESULTS_PATH / "sensitivity"
    sensitivity_path.mkdir(parents=True, exist_ok=True)
    df_parameters = SensitivityParameter.parameters_to_df(sensitivity_parameters)
    df_parameters.to_csv(sensitivity_path / "parameters.tsv", sep="\t", index=False)
    console.print(df_parameters)
    SensitivityParameter.parameter_to_latex(
        tex_path=sensitivity_path / "parameters.tex",
        parameters=sensitivity_parameters,
    )

    settings = {
        "cache_results": False,
        "n_cores": int(round(0.9 * multiprocessing.cpu_count())),
        "seed": 1234
    }

    sa_local = LocalSensitivityAnalysis(
        sensitivity_simulation=sensitivity_simulation,
        parameters=sensitivity_parameters,
        groups=[sensitivity_groups[0]],
        results_path=sensitivity_path / "local",
        difference=0.01,
        **settings,
    )
    sa_sampling = SamplingSensitivityAnalysis(
        sensitivity_simulation=sensitivity_simulation,
        parameters=sensitivity_parameters,
        groups=sensitivity_groups,
        results_path=sensitivity_path / "sampling",
        N=1000,
        **settings,
    )
    sa_fast = FASTSensitivityAnalysis(
        sensitivity_simulation=sensitivity_simulation,
        parameters=sensitivity_parameters,
        groups=[sensitivity_groups[0]],
        results_path=sensitivity_path / "fast",
        N=1000,
        **settings,
    )
    sa_sobol = SobolSensitivityAnalysis(
        sensitivity_simulation=sensitivity_simulation,
        parameters=sensitivity_parameters,
        groups=[sensitivity_groups[0]],
        results_path=sensitivity_path / "sobol",
        N=4096,
        **settings,
    )
    for sa in [
        sa_local,
        # sa_sampling,
        # sa_fast,
        # sa_sobol,
    ]:
        sa.execute()
        sa.plot()
