"""Model for coagulation factors and readouts.

The coagulation model is a PD component of the body (`coagulation_component`
of `definition.py`): it reads the total apixaban concentration of the arm vein
plasma (`Carm_api`) through its input port `C_api`, as the assays measure the
total apixaban of a plasma sample. In the flat model the input is the element
of the body (`Carm_api`, the replaced port disappears in flattening), the other
elements are `COAG__<id>`. No experiment simulates the model on its own.

The values of the fitted parameters come from the adopted PD fit
(`MODEL.adopted_fits()`, `models/fits.py`), fitted on the adopted values of the
pharmacokinetics.
"""

from sbmlutils.factory import (
    AssignmentRule,
    Model,
    NaN,
    Parameter,
    UnitDefinition,
)
from sbmlutils.metadata import (
    BQB,
    SBO,
)

from pkdb_models.models.apixaban.models import annotations, templates
from pkdb_models.models.apixaban.models.fits import FITS


class U(templates.U):
    """Units of the coagulation model."""

    ng_per_ml = UnitDefinition("ng_per_ml", "ng/ml")
    IU_per_ml = UnitDefinition("IU_per_ml", "1/ml")
    ng_per_ml_mM = UnitDefinition("ng_per_ml_mM", "ng/(ml*mmole/l)")
    IU_per_ml_mM = UnitDefinition("IU_per_ml_mM", "1/(ml*mmole/l)")
    per_mM = UnitDefinition("per_mM", "l/mmole")


_m = Model(
    sid="COAG",
    name="Model for coagulation factors and readouts.",
    notes="""
    Model for coagulation factors and readouts.

    The effects depend on the total concentration of apixaban in the arm vein
    plasma `C_api` (input port, `Carm_api` of the body), as the assays measure
    the total drug in a plasma sample:
    the anti-factor Xa activity is linear in the concentration, the INR and
    the prothrombin time (PT) rise linearly with the concentration relative to
    their baseline, the modified prothrombin time (mPT) and the activated
    partial thromboplastin time (aPTT) follow an Emax model of the
    concentration relative to their baseline.
    """
    + templates.terms_of_use,
    creators=templates.creators,
    units=U,
    model_units=templates.model_units,
    annotations=[
        *annotations.model,
        (BQB.HAS_PROPERTY, "NCIT:C15720"),  # pharmacodynamics
    ],
)

_m.parameters = [
    Parameter(
        "C_api",
        0.0,
        U.mM,
        constant=False,
        name="apixaban (arm vein plasma)",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        The total concentration of apixaban in the arm vein plasma
        (`Carm_api`), read through the port; it drives the effects. 0 mM (no
        apixaban, the baselines) in the model on its own.
        """,
        port=True,
    ),
]

names = {
    "INR": "INR",
    "PT": "prothrombin time",
    "aPTT": "activated partial thromboplastin",
    "mPT": "modified prothrombin time",
    "antiXa_activity": "anti-FXa activity",
    "antiXa_activity_gram": "anti-FXa activity (apixaban calibrated)",
}
reference_values = {
    "INR": 1,  # [-]
    "PT": 12.5,  # [s]
    "aPTT": 28.4,  # [s]
    "mPT": 53.4,  # [s] Frost2021 placebo
    "antiXa_activity": 0,  # [IU/ml]
    "antiXa_activity_gram": 0,  # [ng/ml]
}
unit_values = {
    "INR": U.dimensionless,
    "PT": U.second,
    "aPTT": U.second,
    "mPT": U.second,
    "antiXa_activity": U.IU_per_ml,
    "antiXa_activity_gram": U.ng_per_ml,
}

for sid in ["INR", "PT", "aPTT", "mPT"]:
    _m.parameters.extend(
        [
            Parameter(
                sid=f"{sid}_ref",
                name=f"{names[sid]} reference",
                value=reference_values[sid],
                unit=unit_values[sid],
                constant=True,
                sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            ),
        ]
    )

for sid in [
    "INR",
    "PT",
    "aPTT",
    "mPT",
    "antiXa_activity",
    "antiXa_activity_gram",
]:
    _m.parameters.extend(
        [
            Parameter(
                sid=sid,
                name=names[sid],
                value=reference_values[sid],
                unit=unit_values[sid],
                constant=False,
                sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            )
        ]
    )

for sid in ["INR", "PT", "aPTT", "mPT"]:
    # absolute change
    _m.parameters.append(
        Parameter(
            f"{sid}_change",
            name=f"{names[sid]} change",
            value=NaN,
            unit=unit_values[sid],
            constant=False,
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes=f"Absolute change to baseline {names[sid]}",
        )
    )
    _m.rules.append(
        AssignmentRule(f"{sid}_change", f"{sid}-{sid}_ref", unit=unit_values[sid])
    )
    # ratio to baseline
    _m.parameters.append(
        Parameter(
            f"{sid}_ratio",
            name=f"{names[sid]} ratio",
            value=NaN,
            unit=U.dimensionless,
            constant=False,
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes=f"Ratio relative to baseline {names[sid]}",
        )
    )
    _m.rules.append(
        AssignmentRule(f"{sid}_ratio", f"{sid}/{sid}_ref", unit=U.dimensionless)
    )

    # relative change from baseline
    _m.parameters.append(
        Parameter(
            f"{sid}_relchange",
            name=f"{names[sid]} relative change",
            value=NaN,
            unit=U.dimensionless,
            constant=False,
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes=f"Change relative to baseline {names[sid]}",
        )
    )
    _m.rules.append(
        AssignmentRule(
            f"{sid}_relchange", f"({sid} - {sid}_ref)/{sid}_ref", unit=U.dimensionless
        )
    )


# Effect of apixaban on the clotting times relative to their baseline, as
# functions of the total concentration of apixaban in plasma. The INR and the PT
# rise linearly with the concentration: in the PD fit PD_20261031_140250__b09b7
# with Emax models their data lay in the linear range, the Emax and the EC50 of
# the PT were structurally non-identifiable (the EC50 at its lower bound), the
# EC50 of the INR bounded below only; the slope of a linear model is the ratio
# Emax/EC50 they determined. The mPT and the aPTT bend over the measured
# concentrations and keep their Emax models. The model comparison of the refit
# of 2026-11-04 on the training data: a linear PT and a linear INR each lowered
# the BIC by 6, a linear mPT raised it by 63.
LINEAR = ["INR", "PT"]
EMAX = ["mPT", "aPTT"]
for sid in LINEAR:
    _m.parameters.append(
        Parameter(
            sid=f"slope_api_{sid}",
            name=f"relative increase of the {names[sid]} per apixaban concentration",
            **FITS.parameter(f"COAG__slope_api_{sid}", unit=U.per_mM),
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes=(
                "Fitted, the increase relative to the baseline per total "
                "concentration of apixaban in plasma."
            ),
        )
    )
    _m.rules.append(
        AssignmentRule(
            sid,
            f"{sid}_ref * (1 dimensionless + slope_api_{sid} * C_api)",
            unit=unit_values[sid],
        )
    )
for sid in EMAX:
    _m.parameters.extend(
        [
            Parameter(
                sid=f"Emax_{sid}",
                name=f"maximal relative increase of the {names[sid]}",
                **FITS.parameter(f"COAG__Emax_{sid}", unit=U.dimensionless),
                sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
                notes="Fitted, the maximal effect relative to the baseline.",
            ),
            Parameter(
                sid=f"EC50_api_{sid}",
                name=f"apixaban concentration of the half-maximal effect on the {names[sid]}",
                **FITS.parameter(f"COAG__EC50_api_{sid}", unit=U.mM),
                sboTerm=SBO.EC50,
                notes="Fitted, a total concentration of apixaban in plasma.",
            ),
        ]
    )
    _m.rules.append(
        AssignmentRule(
            sid,
            f"{sid}_ref * (1 dimensionless + Emax_{sid} * C_api / (C_api + EC50_api_{sid}))",
            unit=unit_values[sid],
        )
    )

# anti-FXa activity, linear in the total concentration of apixaban
_m.parameters.extend(
    [
        Parameter(
            sid="antiXa_slope",
            name="anti-FXa activity per apixaban concentration",
            **FITS.parameter("COAG__antiXa_slope", unit=U.IU_per_ml_mM),
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes=(
                "Fitted, the anti-FXa activity in IU/ml (heparin calibrated) per "
                "total concentration."
            ),
        ),
        Parameter(
            sid="antiXa_gram_slope",
            name="anti-FXa activity (apixaban calibrated) per apixaban concentration",
            **FITS.parameter("COAG__antiXa_gram_slope", unit=U.ng_per_ml_mM),
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes=(
                "Fitted, the anti-FXa activity in ng/ml (apixaban calibrated) per "
                "total concentration; 1:1 is the molecular weight, 4.595e5 ng/ml "
                "per mM."
            ),
        ),
    ]
)
_m.rules.extend(
    [
        AssignmentRule(
            "antiXa_activity",
            "antiXa_slope * C_api",
            unit=U.IU_per_ml,
        ),
        AssignmentRule(
            "antiXa_activity_gram",
            "antiXa_gram_slope * C_api",
            unit=U.ng_per_ml,
        ),
    ]
)

model_coagulation: Model = _m
