"""Apixaban intestine model."""

from sbmlutils.factory import *
from sbmlutils.metadata import *
from pkdb_models.models.apixaban.models import annotations
from pkdb_models.models.apixaban.models import templates


class U(templates.U):
    """UnitDefinitions"""

    per_hr = UnitDefinition("per_hr", "1/hr")
    mg_per_min = UnitDefinition("mg_per_min", "mg/min")


_m = Model(
    "apixaban_intestine",
    name="Model for apixaban absorption in the small intestine",
    notes="""
    # Model for apixaban absorption
    """
    + templates.terms_of_use,
    creators=templates.creators,
    units=U,
    model_units=templates.model_units,
    annotations=annotations.model + [
        # tissue
        (BQB.OCCURS_IN, "fma/FMA:45615"),  # gut
        (BQB.OCCURS_IN, "bto/BTO:0000545"),  # gut
        (BQB.OCCURS_IN, "NCIT:C12736"),  # intestine
        (BQB.OCCURS_IN, "fma/FMA:7199"),  # intestine
        (BQB.OCCURS_IN, "bto/BTO:0000648"),  # intestine

        (BQB.HAS_PROPERTY, "NCIT:C79369"),  # Pharmacokinetics: Absorption
        (BQB.HAS_PROPERTY, "NCIT:C79372"),  # Pharmacokinetics: Excretion
    ]
)

_m.compartments = [
    Compartment(
        "Vext",
        1.0,
        name="plasma",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        unit=U.liter,
        port=True,
        annotations=annotations.compartments["plasma"],
    ),
    Compartment(
        "Vlumen",
        value=1.0,
        name="lumen",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        unit=U.liter,
        constant=False,
        port=True,
        annotations=annotations.compartments["gu_lumen"],
    ),
    Compartment(
        "Vfeces",
        metaId="meta_Vfeces",
        value=1.0,
        unit=U.liter,
        constant=True,
        name="feces",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        port=True,
        annotations=annotations.compartments["feces"],
    ),
    Compartment(
        "Vstomach",
        metaId="meta_Vstomach",
        value=1,
        unit=U.liter,
        constant=True,
        name="stomach",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        port=True,
        annotations=annotations.compartments["stomach"],
    ),
    Compartment(
        "Vapical",
        NaN,
        name="apical membrane (intestinal membrane enterocytes)",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        unit=U.m2,
        spatialDimensions=2,
        annotations=annotations.compartments["apical"],
    ),
]

_m.species = [
    Species(
        f"api_stomach",
        metaId=f"meta_api_stomach",
        initialConcentration=0.0,
        compartment="Vstomach",
        substanceUnit=U.mmole,
        name=f"apixaban (stomach)",
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["api"],
        boundaryCondition=True,
    ),
    Species(
        "api_ext",
        initialConcentration=0.0,
        name="apixaban (plasma)",
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["api"],
        port=True,
    ),
    Species(
        "api_lumen",
        initialConcentration=0.0,
        name="apixaban (intestinal volume)",
        compartment="Vlumen",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["api"],
        port=True,
    ),
    Species(
        "api_feces",
        initialConcentration=0.0,
        name="apixaban (feces)",
        compartment="Vfeces",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["api"],
        port=True,
    ),
    Species(
        "m1_lumen",
        initialConcentration=0.0,
        name="M1 (intestinal volume)",
        compartment="Vlumen",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m1"],
        port=True,
    ),
    Species(
        "m2_lumen",
        initialConcentration=0.0,
        name="M2 (intestinal volume)",
        compartment="Vlumen",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m2"],
        port=True,
    ),
    Species(
        "m7_lumen",
        initialConcentration=0.0,
        name="M7 (intestinal volume)",
        compartment="Vlumen",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m7"],
        port=True,
    ),
    Species(
        "m1_feces",
        initialConcentration=0.0,
        name="M1 (feces)",
        compartment="Vfeces",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m1"],
        port=True,
    ),
    Species(
        "m2_feces",
        initialConcentration=0.0,
        name="M2 (feces)",
        compartment="Vfeces",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m2"],
        port=True,
    ),
    Species(
        "m7_feces",
        initialConcentration=0.0,
        name="M7 (feces)",
        compartment="Vfeces",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m7"],
        port=True,
    )
]

_m.parameters = [
    Parameter(
        f"F_api_abs",
        0.66,  # [0.5 - 0.66]
        U.dimensionless,
        constant=True,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        name=f"fraction absorbed apixaban",
    ),
    # Parameter(
    #     "APIABS_k",
    #     0.05,
    #     unit=U.per_min,
    #     name="rate of apixaban absorption",
    #     sboTerm=SBO.KINETIC_CONSTANT,
    # ),
    Parameter(
        "APIABS_Vmax",
        0.05,
        unit=U.mmole_per_min,
        name="rate of apixaban absorption",
        sboTerm=SBO.KINETIC_CONSTANT,
    ),
    Parameter(
        "APIABS_50",
        25,
        unit=U.mg,
        name="amount of apixaban when rate of absorption reaches 50% of maximal rate",
        sboTerm=SBO.MICHAELIS_CONSTANT,
    ),
    Parameter(
        "f_absorption",
        1,
        unit=U.dimensionless,
        name="scaling factor for absorption rate",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""1.0: normal absorption corresponding to tablet under fasting conditions.

        allows to change the velocity of absorption
        """
    ),
    Parameter(
        "MXEXC_k",
        0.10,
        unit=U.per_min,
        name="rate of metabolite excretion",
        sboTerm=SBO.KINETIC_CONSTANT,
    ),
]


_m.parameters.extend([
    Parameter(
        f"PODOSE_api",
        0,
        U.mg,
        constant=False,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        name=f"oral dose apixaban in tablet [mg]",
        port=True,
    ),
    Parameter(
        f"SOLDOSE_api",
        0,
        U.mg,
        constant=False,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        name=f"oral dose apixaban in solution [mg]",
        port=True,
    ),
    Parameter(
        f"Ka_dis_api",
        0.15,
        U.per_hr,
        constant=True,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        name=f"Ka_dis [1/hr] dissolution apixaban in tablet",
        port=True
    ),
    Parameter(
        f"Ksol_dis_api",
        0.15 * 5,
        U.per_hr,
        constant=True,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        name=f"Ksol_dis [1/hr] dissolution apixaban in solution",
        port=True
    ),
    Parameter(
        f"Mr_api",
        459.5,
        U.g_per_mole,
        constant=True,
        name=f"Molecular weight apixaban [g/mole]",
        sboTerm=SBO.MOLECULAR_MASS,
        port=True,
    ),
])

_m.rules.append(
    # AssignmentRule(
    #     "absorption_api",
    #     value="f_absorption * APIABS_k * Vlumen * api_lumen",
    #     unit=U.mmole_per_min,
    #     name="absorption apixaban",
    # ),
    AssignmentRule(
        "absorption_api",
        value="APIABS_Vmax * Vlumen * api_lumen / (APIABS_50 / Mr_api + Vlumen * api_lumen)",
        unit=U.mmole_per_min,
        name="absorption apixaban",
    ),
)

_m.reactions = [
    Reaction(
        "APIABS",
        name="absorption apixaban",
        equation="api_lumen -> api_ext",
        sboTerm=SBO.TRANSPORT_REACTION,
        compartment="Vapical",
        formula=("f_absorption * F_api_abs * absorption_api", U.mmole_per_min),
    ),

    Reaction(
        sid="APIEXC",
        name=f"excretion apixaban (feces)",
        compartment="Vlumen",
        equation=f"api_lumen -> api_feces",
        sboTerm=SBO.TRANSPORT_REACTION,
        formula=(
            f"(1 dimensionless - f_absorption * F_api_abs) * absorption_api",
            U.mmole_per_min,
        )
    ),
    Reaction(
        sid="M1EXC",
        name=f"excretion M1 (feces)",
        compartment="Vlumen",
        equation=f"m1_lumen -> m1_feces",
        sboTerm=SBO.TRANSPORT_REACTION,
        formula=(
            f"MXEXC_k * Vlumen * m1_lumen",
            U.mmole_per_min,
        )
    ),
    Reaction(
        sid="M2EXC",
        name=f"excretion M2 (feces)",
        compartment="Vlumen",
        equation=f"m2_lumen -> m2_feces",
        sboTerm=SBO.TRANSPORT_REACTION,
        formula=(
            f"MXEXC_k * Vlumen * m2_lumen",
            U.mmole_per_min,
        )
    ),
    Reaction(
        sid="M7EXC",
        name=f"excretion M7 (feces)",
        compartment="Vlumen",
        equation=f"m7_lumen -> m7_feces",
        sboTerm=SBO.TRANSPORT_REACTION,
        formula=(
            f"MXEXC_k * Vlumen * m7_lumen",
            U.mmole_per_min,
        )
    ),

]

# -------------------------------------
# Dissolution of tablet/dose in stomach
# -------------------------------------
_m.reactions.extend(
    [
        # fraction dose available for absorption from stomach
        Reaction(
            sid=f"dissolution_api_tabl",
            name=f"dissolution apixaban tablet",
            formula=(
                f"Ka_dis_api/60 min_per_hr * PODOSE_api/Mr_api",
                U.mmole_per_min,
            ),
            equation=f"api_stomach -> api_lumen",
            compartment="Vlumen",
            notes="""Swallowing, dissolution of tablet, and transport into intestine.
            Overall process describing the rates of this processes.
            """
        ),
    ]
)
_m.rate_rules.append(
    RateRule(f"PODOSE_api", f"-dissolution_api_tabl * Mr_api", U.mg_per_min),
)

_m.reactions.extend(
    [
        # fraction dose available for absorption from stomach
        Reaction(
            sid=f"dissolution_api_sol",
            name=f"dissolution apixaban in solution",
            formula=(
                f"Ksol_dis_api/60 min_per_hr * SOLDOSE_api/Mr_api",
                U.mmole_per_min,
            ),
            equation=f"api_stomach -> api_lumen",
            compartment="Vlumen",
            notes="""Swallowing, dissolution of solution, and transport into intestine.
            Overall process describing the rates of this processes.
            """
        ),
    ]
)
_m.rate_rules.append(
    RateRule(f"SOLDOSE_api", f"-dissolution_api_sol * Mr_api", U.mg_per_min),
)

model_intestine = _m


if __name__ == "__main__":
    from sbmlutils.converters import odefac
    from sbmlutils import cytoscape as cyviz
    from pkdb_models.models.apixaban import MODEL_BASE_PATH

    results: FactoryResult = create_model(
        model=model_intestine,
        filepath=MODEL_BASE_PATH / f"{model_intestine.sid}.xml",
        sbml_level=3,
        sbml_version=2,
    )

    # ODE equations
    ode_factory = odefac.SBML2ODE.from_file(sbml_file=results.sbml_path)
    ode_factory.to_markdown(md_file=results.sbml_path.parent / f"{results.sbml_path.stem}.md")

    # visualization in Cytoscape
    cyviz.visualize_sbml(results.sbml_path, delete_session=False)