"""Model for coagulation factors and readouts."""

from sbmlutils.factory import (
    AssignmentRule,
    Compartment,
    Model,
    NaN,
    Parameter,
    Species,
    UnitDefinition,
    ValidationOptions,
    create_model,
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


_m = Model(
    sid="apixaban_coagulation",
    name="Model for coagulation factors and readouts.",
    notes="""
    Model for coagulation factors and readouts.

    The effects depend on the total concentration of apixaban in the venous
    plasma `Cve_api`, as the assays measure the total drug in a plasma sample:
    the anti-factor Xa activity is linear in the concentration, the INR, the
    prothrombin time (PT), the modified prothrombin time (mPT) and the
    activated partial thromboplastin time (aPTT) follow an Emax model of the
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

_m.compartments = [
    Compartment(
        "Vplasma",
        value=5.0,
        unit=U.liter,
        name="plasma",
        constant=True,
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments["plasma"],
        port=True,
    ),
]

_m.species = [
    Species(
        "Cve_api",
        name="apixaban",
        initialConcentration=0,
        compartment="Vplasma",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["api"],
    )
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


# Effect of apixaban on the INR, PT, mPT, aPTT and the anti-FXa activity: the
# Emax models of the clotting times relative to their baseline, the half-maximal
# concentrations are total concentrations of apixaban in plasma
# the Emax and EC50 are fitted, see `fits.FITS`
for sid in ["INR", "PT", "aPTT", "mPT"]:
    _m.parameters.extend(
        [
            Parameter(
                sid=f"Emax_{sid}",
                name=f"maximal relative increase of the {names[sid]}",
                **FITS.parameter(f"Emax_{sid}", unit=U.dimensionless),
                sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            ),
            Parameter(
                sid=f"EC50_api_{sid}",
                name=f"apixaban concentration of the half-maximal effect on the {names[sid]}",
                **FITS.parameter(f"EC50_api_{sid}", unit=U.mM),
                sboTerm=SBO.EC50,
                notes="Total concentration of apixaban in plasma.",
            ),
        ]
    )
    _m.rules.append(
        AssignmentRule(
            sid,
            f"{sid}_ref * (1 dimensionless + Emax_{sid} * Cve_api / (Cve_api + EC50_api_{sid}))",
            unit=unit_values[sid],
        )
    )

# anti-FXa activity, linear in the total concentration of apixaban
_m.parameters.extend(
    [
        Parameter(
            sid="antiXa_slope",
            name="anti-FXa activity per apixaban concentration",
            **FITS.parameter("antiXa_slope", unit=U.IU_per_ml_mM),
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes="Anti-FXa activity in IU/ml (heparin calibrated) per total concentration.",
        ),
        Parameter(
            sid="antiXa_gram_slope",
            name="anti-FXa activity (apixaban calibrated) per apixaban concentration",
            **FITS.parameter("antiXa_gram_slope", unit=U.ng_per_ml_mM),
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes=(
                "Anti-FXa activity in ng/ml (apixaban calibrated) per total "
                "concentration; 1:1 is the molecular weight, 4.595e5 ng/ml per mM."
            ),
        ),
    ]
)
_m.rules.extend(
    [
        AssignmentRule(
            "antiXa_activity",
            "antiXa_slope * Cve_api",
            unit=U.IU_per_ml,
        ),
        AssignmentRule(
            "antiXa_activity_gram",
            "antiXa_gram_slope * Cve_api",
            unit=U.ng_per_ml,
        ),
    ]
)

model_coagulation: Model = _m


if __name__ == "__main__":
    from sbmlode import OdeSystem

    from pkdb_models.models.apixaban import MODEL_BASE_PATH

    results = create_model(
        model=model_coagulation,
        filepath=MODEL_BASE_PATH / f"{model_coagulation.sid}.xml",
        sbml_level=3,
        sbml_version=2,
        validation_options=ValidationOptions(units_consistency=True),
    )
    # create differential equations
    md_path = MODEL_BASE_PATH / f"{model_coagulation.sid}.md"
    ode_system = OdeSystem.from_sbml(results.sbml_path)
    ode_system.write(md_path)
