"""Kidney model for apixaban."""

from sbmlutils.factory import *
from sbmlutils.metadata import *
from pkdb_models.models.apixaban.models import annotations
from pkdb_models.models.apixaban.models import templates


class U(templates.U):
    """UnitDefinitions"""
    mg_per_g = UnitDefinition("mg_per_g", "mg/g")
    ml_per_l = UnitDefinition("ml_per_l", "ml/l")
    ml_per_min = UnitDefinition("ml_per_min", "ml/min")
    ml_per_min_bsa = UnitDefinition("ml_per_min_bsa", "ml/min/(1.73 * m^2)")


_m = Model(
    sid="apixaban_kidney",
    name="Model for renal apixaban excretion.",
    notes=f"""
    Model for renal excretion of apixaban:
    """ + templates.terms_of_use,
    creators=templates.creators,
    units=U,
    model_units=templates.model_units,
    annotations=annotations.model + [
        # tissue
        (BQB.OCCURS_IN, "FMA:7203"),  # kidney
        (BQB.OCCURS_IN, "BTO:0000671"),  # kidney
        (BQB.OCCURS_IN, "NCIT:C12415"),  # kidney
        (BQB.HAS_PROPERTY, "NCIT:C79372"),  # Pharmacokinetics: Excretion
    ]
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
        port=True
    ),
    Compartment(
        "Vki",
        value=0.3,
        unit=U.liter,
        name="kidney",
        constant=True,
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments["ki"],
        port=True
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
        name="apixaban (plasma)",
        initialConcentration=0.0,
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,  # this is a concentration
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["api"],
        port=True
    ),
    Species(
        "api_urine",
        name="apixaban (urine)",
        initialConcentration=0.0,
        compartment="Vurine",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["api"],
        port=True
    ),
    Species(
        "m1_ext",
        name="M1 (plasma)",
        initialConcentration=0.0,
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,  # this is a concentration
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m1"],
        port=True
    ),
    Species(
        "m1_urine",
        name="M1 (urine)",
        initialConcentration=0.0,
        compartment="Vurine",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m1"],
        port=True
    ),
    Species(
        "m7_ext",
        name="M7 (plasma)",
        initialConcentration=0.0,
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,  # this is a concentration
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m7"],
        port=True
    ),
    Species(
        "m7_urine",
        name="M7 (urine)",
        initialConcentration=0.0,
        compartment="Vurine",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m7"],
        port=True
    ),
]

# glomerular filtration rate, creatinine clearance & kidney function
_m.parameters.extend([
    Parameter(
        "BSA",
        1.73,
        U.m2,
        constant=False,
        name="body surface area [m^2]",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        port=True
    ),
    Parameter(
        "f_renal_function",
        name="parameter for renal function",
        value=1.0,
        unit=U.dimensionless,
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""scaling factor for renal function. 1.0: normal renal function;
        <1.0: reduced renal function
        """
    ),
    Parameter(
        "egfr",
        NaN,
        unit=U.ml_per_min_bsa,
        constant=False,
        name="estimated GFR [ml/min/(1.73 m^2)]",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        annotations=[
            (BQB.IS, "NCIT:C110935"),
        ],
        port=True,
        notes="""A laboratory test that estimates kidney function. It is calculated using an individual's
        serum creatinine measurement, age, gender, and race."""
    ),
    Parameter(
        "crcl",
        NaN,
        U.ml_per_min,
        constant=False,
        name="creatinine clearance [ml/min]",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        annotations=[
            (BQB.IS, "cmo/CMO:0000765"),
        ],
        port=True,
        notes="""The clearance rate of creatinine, that is, the volume of plasma that is cleared of creatinine
        by the kidneys per unit time. Creatinine clearance is calculated using the level of creatinine in a
        sample of urine, usually one collected over a period of 24 hours, the corresponding plasma creatinine
        level, and the volume of urine excreted. It is used as an approximation of the glomerular
        filtration rate (GFR)."""
    ),
    Parameter(
        sid="egfr_healthy",
        name="estimated glomerular filtration (eGFR) rate healthy",
        value=100.0,
        unit=U.ml_per_min_bsa,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        annotations=[
        ],
        notes="""eGFR is often estimated via creatinine clearance, creatinine urinary amount,
        or creatinine plasma amounts.

        CKD-EPI Creatinine Equation (2021): This is the most recent and recommended equation for
        estimating GFR35. It is more accurate than previous formulas and does not include
        race as a variable.

        MDRD (Modification of Diet in Renal Disease) Study Equation
    """,
    ),
    Parameter(
        "fu_api",
        13.1 / 100, # [-] unbound in plasma He2011
        U.dimensionless,
        constant=True,
        name=f"fraction unbound in plasma api",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        port=True,
    ),
])
_m.rules.extend([
    AssignmentRule(
        "egfr", "f_renal_function * egfr_healthy", unit=U.ml_per_min_bsa,
        name="estimated eGFR"
    ),
    AssignmentRule(
        "crcl", "egfr * BSA/(1.73 dimensionless) * 1.1 dimensionless", unit=U.ml_per_min,
        name="creatinine clearance",
        notes="CrCl typically overestimates GFR by 10-20% due to the active secretion"
              "of creatinine in the proximal tubules."
              "Using a 10 % overestimation in the model."
    ),
])

_m.reactions = [
    Reaction(
        sid="APIEX",
        name="apixaban excretion (APIEX)",
        equation="api_ext -> api_urine",
        compartment="Vki",
        sboTerm=SBO.TRANSPORT_REACTION,
        pars=[
            Parameter(
                "APIEX_k",
                0.1,
                U.per_min,
                name="rate of apixaban urinary excretion",
                sboTerm=SBO.KINETIC_CONSTANT,
            ),
        ],
        formula=(
            "f_renal_function * Vki * APIEX_k * api_ext * fu_api"
        )
    ),
    Reaction(
        sid="M1EX",
        name="M1 excretion (M1EX)",
        equation="m1_ext -> m1_urine",
        compartment="Vki",
        sboTerm=SBO.TRANSPORT_REACTION,
        pars=[
            Parameter(
                "M1EX_k",
                0.1,
                U.per_min,
                name="rate of M1 urinary excretion",
                sboTerm=SBO.KINETIC_CONSTANT,
            ),
        ],
        formula=(
            "f_renal_function * Vki * M1EX_k * m1_ext"
        )
    ),
    Reaction(
        sid="M7EX",
        name="M7 excretion (M7EX)",
        equation="m7_ext -> m7_urine",
        compartment="Vki",
        sboTerm=SBO.TRANSPORT_REACTION,
        pars=[
            Parameter(
                "M7EX_k",
                0.1,
                U.per_min,
                name="rate of M7 urinary excretion",
                sboTerm=SBO.KINETIC_CONSTANT,
            ),
        ],
        formula=(
            "f_renal_function * Vki * M7EX_k * m7_ext"
        )
    ),
]

model_kidney = _m


if __name__ == "__main__":
    from sbmlutils.converters import odefac
    from sbmlutils import cytoscape as cyviz
    from pkdb_models.models.apixaban import MODEL_BASE_PATH

    results: FactoryResult = create_model(
        model=model_kidney,
        filepath=MODEL_BASE_PATH / f"{model_kidney.sid}.xml",
        sbml_level=3, sbml_version=2,
    )

    # ODE equations
    ode_factory = odefac.SBML2ODE.from_file(sbml_file=results.sbml_path)
    ode_factory.to_markdown(md_file=results.sbml_path.parent / f"{results.sbml_path.stem}.md")

    # visualization in Cytoscape
    cyviz.visualize_sbml(sbml_path=results.sbml_path, delete_session=False)


