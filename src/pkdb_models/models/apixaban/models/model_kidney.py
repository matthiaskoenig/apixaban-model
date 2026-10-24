"""Kidney model for apixaban."""

from sbmlutils.factory import (
    AssignmentRule,
    Compartment,
    Model,
    Parameter,
    Reaction,
    Species,
    UnitDefinition,
    create_model,
)
from sbmlutils.metadata import (
    BQB,
    SBO,
)

from pkdb_models.models.apixaban.models import annotations, templates
from pkdb_models.models.apixaban.models.fits import FITS


class U(templates.U):
    """Units of the kidney model."""

    ml_per_min = UnitDefinition("ml_per_min", "ml/min")
    l_per_ml = UnitDefinition("l_per_ml", "l/ml")


_m = Model(
    sid="apixaban_kidney",
    name="Model for renal apixaban excretion.",
    notes="""
    Model for the renal excretion of apixaban and its metabolites M1 and M7.

    The renal clearances are given relative to the glomerular filtration rate
    (GFR), which scales with the renal function; the GFR does not depend on the
    body weight (Upreti2013: the renal clearance was similar across the groups
    of body weight).
    """
    + templates.terms_of_use,
    creators=templates.creators,
    units=U,
    model_units=templates.model_units,
    annotations=[
        *annotations.model,
        # tissue
        (BQB.OCCURS_IN, "FMA:7203"),  # kidney
        (BQB.OCCURS_IN, "BTO:0000671"),  # kidney
        (BQB.OCCURS_IN, "NCIT:C12415"),  # kidney
        (BQB.HAS_PROPERTY, "NCIT:C79372"),  # Pharmacokinetics: Excretion
    ],
)

_m.compartments = [
    Compartment(
        "Vext",
        value=1.5,
        unit=U.liter,
        name="plasma",
        constant=True,
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments["plasma"],
        port=True,
    ),
    Compartment(
        "Vurine",
        1.0,
        name="urine",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        unit=U.liter,
        port=True,
        annotations=annotations.compartments["urine"],
    ),
]

_m.species = [
    Species(
        "api_ext",
        name="apixaban (api_ext)",
        initialConcentration=0.0,
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,  # this is a concentration
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["api"],
        port=True,
    ),
    Species(
        "api_urine",
        name="apixaban (api_urine)",
        initialConcentration=0.0,
        compartment="Vurine",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["api"],
        port=True,
    ),
    Species(
        "m1_ext",
        name="M1 (m1_ext)",
        initialConcentration=0.0,
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,  # this is a concentration
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m1"],
        port=True,
    ),
    Species(
        "m1_urine",
        name="M1 (m1_urine)",
        initialConcentration=0.0,
        compartment="Vurine",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m1"],
        port=True,
    ),
    Species(
        "m7_ext",
        name="M7 (m7_ext)",
        initialConcentration=0.0,
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,  # this is a concentration
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m7"],
        port=True,
    ),
    Species(
        "m7_urine",
        name="M7 (m7_urine)",
        initialConcentration=0.0,
        compartment="Vurine",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m7"],
        port=True,
    ),
]

# glomerular filtration rate and kidney function
_m.parameters.extend(
    [
        Parameter(
            "f_renal_function",
            name="renal function",
            value=1.0,
            unit=U.dimensionless,
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes="""
            >1.0: increased kidney function
            1.0: normal kidney function (healthy control)
            <1.0: decreased kidney function

            Renal function relative to the healthy glomerular filtration rate
            GFR_base of 101 ml/min; a measured creatinine clearance of X ml/min
            is the renal function X/101 (`pkpdsim.impairment.RENAL_FUNCTION_GFR`).
            """,
        ),
        Parameter(
            "GFR_base",
            101,
            U.ml_per_min,
            name="glomerular filtration rate (healthy)",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes="""
            The GFR of healthy kidneys, independent of the body weight; the GFR
            is `f_renal_function` times this rate.
            """,
        ),
        Parameter(
            "fu_api",
            13.1 / 100,  # [-] unbound in plasma He2011
            U.dimensionless,
            constant=True,
            name="fraction unbound in plasma apixaban",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            port=True,
        ),
        Parameter(
            "APIEX_f",
            **FITS.parameter("KI__APIEX_f", unit=U.dimensionless),
            name="renal clearance of unbound apixaban relative to the GFR",
            sboTerm=SBO.KINETIC_CONSTANT,
            notes="""
            The renal clearance of apixaban is APIEX_f times the filtration of
            its unbound fraction, fu_api * GFR: 1 is filtration alone, above 1 a
            net secretion, below 1 a net reabsorption. Renal clearance 0.93 l/h
            (Frost2021): 0.93 l/h / (0.131 * 6.06 l/h) = 1.17.
            """,
        ),
        Parameter(
            "M1EX_f",
            **FITS.parameter("KI__M1EX_f", unit=U.dimensionless),
            name="renal clearance of M1 relative to the GFR",
            sboTerm=SBO.KINETIC_CONSTANT,
            notes="""The fraction unbound of M1 is not known, it is part of the factor.""",
        ),
        Parameter(
            "M7EX_f",
            **FITS.parameter("KI__M7EX_f", unit=U.dimensionless),
            name="renal clearance of M7 relative to the GFR",
            sboTerm=SBO.KINETIC_CONSTANT,
            notes="""The fraction unbound of M7 is not known, it is part of the factor.""",
        ),
    ]
)

_m.rules.append(
    AssignmentRule(
        "GFR",
        "f_renal_function * GFR_base",
        unit=U.ml_per_min,
        name="glomerular filtration rate",
    ),
)

_m.reactions = [
    Reaction(
        sid="APIEX",
        name="excretion apixaban (APIEX)",
        equation="api_ext -> api_urine",
        sboTerm=SBO.TRANSPORT_REACTION,
        # [ml/min] * [l/ml] * [-] * [-] * [mmole/l]
        formula=(
            "GFR * 0.001 l_per_ml * fu_api * APIEX_f * api_ext",
            U.mmole_per_min,
        ),
    ),
    Reaction(
        sid="M1EX",
        name="excretion M1 (M1EX)",
        equation="m1_ext -> m1_urine",
        sboTerm=SBO.TRANSPORT_REACTION,
        formula=("GFR * 0.001 l_per_ml * M1EX_f * m1_ext", U.mmole_per_min),
    ),
    Reaction(
        sid="M7EX",
        name="excretion M7 (M7EX)",
        equation="m7_ext -> m7_urine",
        sboTerm=SBO.TRANSPORT_REACTION,
        formula=("GFR * 0.001 l_per_ml * M7EX_f * m7_ext", U.mmole_per_min),
    ),
]

model_kidney: Model = _m


if __name__ == "__main__":
    from sbmlode import OdeSystem

    from pkdb_models.models.apixaban import MODEL_BASE_PATH

    results = create_model(
        model=model_kidney,
        filepath=MODEL_BASE_PATH / f"{model_kidney.sid}.xml",
        sbml_level=3,
        sbml_version=2,
    )

    # ODE equations
    ode_system = OdeSystem.from_sbml(results.sbml_path)
    ode_system.write(results.sbml_path.parent / f"{results.sbml_path.stem}.md")
