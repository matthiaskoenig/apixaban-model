"""Apixaban intestine model."""

from sbmlutils.factory import (
    AssignmentRule,
    Compartment,
    Model,
    NaN,
    Parameter,
    RateRule,
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
    """Units of the intestine model."""

    per_hr = UnitDefinition("per_hr", "1/hr")
    mg_per_min = UnitDefinition("mg_per_min", "mg/min")


_m = Model(
    "apixaban_intestine",
    name="Model for apixaban absorption and intestinal secretion",
    notes="""
    # Model for apixaban absorption and intestinal secretion
    The tablet dissolves with a rate which saturates with the dose
    (`PODOSE_50`), the solution reaches the lumen of the small intestine with
    `Ka_sol_api`. The dissolved apixaban is absorbed with first order kinetics
    (`APIABS_k`) in competition with the small intestinal transit into the
    colon (`SITRANS_k`), which also carries the undissolved tablet, the
    apixaban secreted from the plasma into the small intestine (P-gp/BCRP,
    `APISEC_k`, `f_pgp`) and the metabolites secreted with the bile. Nothing is
    absorbed from the colon, its content is excreted with the fecal transit
    (`LUMEX_k`).
    """
    + templates.terms_of_use,
    creators=templates.creators,
    units=U,
    model_units=templates.model_units,
    annotations=[
        *annotations.model,
        # tissue
        (BQB.OCCURS_IN, "bto/BTO:0000545"),  # gut
        (BQB.OCCURS_IN, "NCIT:C12736"),  # intestine
        (BQB.OCCURS_IN, "fma/FMA:7199"),  # intestine
        (BQB.OCCURS_IN, "bto/BTO:0000648"),  # intestine
        (BQB.HAS_PROPERTY, "NCIT:C79369"),  # Pharmacokinetics: Absorption
        (BQB.HAS_PROPERTY, "NCIT:C79372"),  # Pharmacokinetics: Excretion
    ],
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
        "Vcolon",
        value=1.0,
        unit=U.liter,
        constant=True,
        name="colon lumen",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments["colon"],
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
        "api_stomach",
        metaId="meta_api_stomach",
        initialConcentration=0.0,
        compartment="Vstomach",
        substanceUnit=U.mmole,
        name="apixaban (api_stomach)",
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["api"],
        boundaryCondition=True,
    ),
    Species(
        "api_ext",
        initialConcentration=0.0,
        name="apixaban (api_ext)",
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
        name="apixaban (api_lumen)",
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
        name="apixaban (api_feces)",
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
        name="M1 (m1_lumen)",
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
        name="M2 (m2_lumen)",
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
        name="M7 (m7_lumen)",
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
        name="M1 (m1_feces)",
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
        name="M2 (m2_feces)",
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
        name="M7 (m7_feces)",
        compartment="Vfeces",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m7"],
        port=True,
    ),
]

_m.species.extend(
    [
        Species(
            "api_colon",
            initialConcentration=0.0,
            name="apixaban (api_colon)",
            compartment="Vcolon",
            substanceUnit=U.mmole,
            hasOnlySubstanceUnits=True,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species["api"],
        ),
        Species(
            "m1_colon",
            initialConcentration=0.0,
            name="M1 (m1_colon)",
            compartment="Vcolon",
            substanceUnit=U.mmole,
            hasOnlySubstanceUnits=True,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species["m1"],
        ),
        Species(
            "m2_colon",
            initialConcentration=0.0,
            name="M2 (m2_colon)",
            compartment="Vcolon",
            substanceUnit=U.mmole,
            hasOnlySubstanceUnits=True,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species["m2"],
        ),
        Species(
            "m7_colon",
            initialConcentration=0.0,
            name="M7 (m7_colon)",
            compartment="Vcolon",
            substanceUnit=U.mmole,
            hasOnlySubstanceUnits=True,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species["m7"],
        ),
    ]
)

_m.parameters = [
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
        "APIABS_k",
        **FITS.parameter("GU__APIABS_k", unit=U.per_min),
        name="rate of apixaban absorption",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        First order absorption of the dissolved apixaban in the lumen of the
        small intestine. The absorption competes with the small intestinal
        transit into the colon (`SITRANS_k`), the fraction absorbed is
        `F_api_abs = APIABS_k/(APIABS_k + SITRANS_k)`.
        """,
    ),
    Parameter(
        "SITRANS_k",
        **FITS.parameter("GU__SITRANS_k", unit=U.per_min),
        name="rate of the small intestinal transit",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        Transit of the content of the small intestine into the colon, a mean
        transit time of about 3.5 hr (1-8 hr). The transit carries the unabsorbed and the
        secreted apixaban, the undissolved tablet and the metabolites; nothing
        is absorbed from the colon.
        """,
    ),
    Parameter(
        "LUMEX_k",
        1 / (30 * 60),
        unit=U.per_min,
        name="rate of the fecal transit",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        Transit of the content of the colon into the feces, a mean transit time
        of about 30 hr (24-36 hr).
        """,
    ),
    Parameter(
        "APISEC_k",
        **FITS.parameter("GU__APISEC_k", unit=U.l_per_min),
        name="intestinal secretion clearance of unbound apixaban",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        Efflux of apixaban from the enterocytes into the lumen (P-gp, BCRP),
        a clearance of the unbound concentration in the plasma of the gut.
        Apixaban is eliminated unchanged into the gut (Frost2021, Wang2014:
        activated charcoal lowers the AUC). The clearance does not depend on
        the body weight.
        """,
    ),
    Parameter(
        "f_pgp",
        1.0,
        unit=U.dimensionless,
        name="P-gp/BCRP activity",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        port=True,
        notes="""
        Activity of the intestinal efflux transporters (P-gp, BCRP) relative to
        normal: 1.0 normal, <1.0 inhibition, >1.0 induction; set by the
        experiments of the coadministrations, not fitted.
        """,
    ),
]

_m.rules.append(
    AssignmentRule(
        "F_api_abs",
        "APIABS_k/(APIABS_k + SITRANS_k)",
        U.dimensionless,
        name="fraction absorbed apixaban",
        notes="""
        Fraction of the dissolved apixaban in the small intestine which is
        absorbed, the rest leaves with the transit into the colon.
        """,
    ),
)

#: the substances in the lumen and their names
SUBSTANCES_LUMEN: dict[str, str] = {
    "api": "apixaban",
    "m1": "M1",
    "m2": "M2",
    "m7": "M7",
}

_m.reactions = [
    Reaction(
        "APIABS",
        name="absorption apixaban (APIABS)",
        equation="api_lumen -> api_ext",
        sboTerm=SBO.TRANSPORT_REACTION,
        compartment="Vapical",
        formula=("APIABS_k * Vlumen * api_lumen", U.mmole_per_min),
    ),
    Reaction(
        "APISEC",
        name="intestinal secretion apixaban (APISEC)",
        equation="api_ext -> api_lumen",
        sboTerm=SBO.TRANSPORT_REACTION,
        compartment="Vapical",
        formula=("f_pgp * APISEC_k * fu_api * api_ext", U.mmole_per_min),
    ),
    *(
        Reaction(
            sid=f"{sid.upper()}SITR",
            name=f"small intestinal transit {name} ({sid.upper()}SITR)",
            compartment="Vlumen",
            equation=f"{sid}_lumen -> {sid}_colon",
            sboTerm=SBO.TRANSPORT_REACTION,
            formula=(f"SITRANS_k * Vlumen * {sid}_lumen", U.mmole_per_min),
        )
        for sid, name in SUBSTANCES_LUMEN.items()
    ),
    *(
        Reaction(
            sid=f"{sid.upper()}EXC",
            name=f"fecal excretion {name} ({sid.upper()}EXC)",
            compartment="Vcolon",
            equation=f"{sid}_colon -> {sid}_feces",
            sboTerm=SBO.TRANSPORT_REACTION,
            formula=(f"LUMEX_k * {sid}_colon", U.mmole_per_min),
        )
        for sid, name in SUBSTANCES_LUMEN.items()
    ),
]

_m.parameters.extend(
    [
        Parameter(
            "PODOSE_api",
            0,
            U.mg,
            constant=False,
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            name="oral dose apixaban in tablet [mg]",
            port=True,
        ),
        Parameter(
            "SOLDOSE_api",
            0,
            U.mg,
            constant=False,
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            name="oral dose apixaban in solution [mg]",
            port=True,
        ),
        Parameter(
            "Ka_dis_api",
            **FITS.parameter("GU__Ka_dis_api", unit=U.per_hr),
            constant=True,
            sboTerm=SBO.KINETIC_CONSTANT,
            name="Ka_dis [1/hr] dissolution apixaban in tablet",
            port=True,
        ),
        Parameter(
            "PODOSE_50",
            **FITS.parameter("GU__PODOSE_50", unit=U.mg),
            constant=True,
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            name="undissolved dose of half-maximal dissolution [mg]",
            notes="""
            The dissolution of the tablet saturates with the undissolved dose
            (solubility): the rate is `Ka_dis_api * PODOSE_api/(1 +
            PODOSE_api/PODOSE_50)`, linear for doses well below `PODOSE_50`.
            """,
        ),
        Parameter(
            "Ka_sol_api",
            **FITS.parameter("GU__Ka_sol_api", unit=U.per_hr),
            constant=True,
            sboTerm=SBO.KINETIC_CONSTANT,
            name="Ka_sol [1/hr] transport apixaban in solution",
            port=True,
        ),
        Parameter(
            "Mr_api",
            459.5,
            U.g_per_mole,
            constant=True,
            name="Molecular weight apixaban [g/mole]",
            sboTerm=SBO.MOLECULAR_MASS,
            port=True,
        ),
    ]
)

# -------------------------------------
# Dissolution of tablet/dose in stomach
# -------------------------------------
_m.reactions.extend(
    [
        Reaction(
            sid="APITAB",
            name="tablet dissolution apixaban (APITAB)",
            formula=(
                "Ka_dis_api/60 min_per_hr * PODOSE_api/Mr_api "
                "/ (1 dimensionless + PODOSE_api/PODOSE_50)",
                U.mmole_per_min,
            ),
            equation="api_stomach -> api_lumen",
            compartment="Vlumen",
            notes="""Swallowing, dissolution of the tablet and transport into the
            intestine. The dissolution saturates with the undissolved dose.
            """,
        ),
        Reaction(
            sid="APIUNDIS",
            name="transit undissolved apixaban (APIUNDIS)",
            formula=("SITRANS_k * PODOSE_api/Mr_api", U.mmole_per_min),
            equation="api_stomach -> api_colon",
            compartment="Vlumen",
            notes="""The undissolved apixaban of the tablet leaves the small
            intestine with the transit into the colon.
            """,
        ),
        Reaction(
            sid="APISOL",
            name="solution transport apixaban (APISOL)",
            formula=(
                "Ka_sol_api/60 min_per_hr * SOLDOSE_api/Mr_api",
                U.mmole_per_min,
            ),
            equation="api_stomach -> api_lumen",
            compartment="Vlumen",
            notes="""Swallowing of the solution and transport into the intestine.
            """,
        ),
    ]
)
_m.rate_rules.extend(
    [
        RateRule("PODOSE_api", "-(APITAB + APIUNDIS) * Mr_api", U.mg_per_min),
        RateRule("SOLDOSE_api", "-APISOL * Mr_api", U.mg_per_min),
    ]
)

model_intestine: Model = _m


if __name__ == "__main__":
    from sbmlode import OdeSystem

    from pkdb_models.models.apixaban import MODEL_BASE_PATH

    results = create_model(
        model=model_intestine,
        filepath=MODEL_BASE_PATH / f"{model_intestine.sid}.xml",
        sbml_level=3,
        sbml_version=2,
    )

    # ODE equations
    ode_system = OdeSystem.from_sbml(results.sbml_path)
    ode_system.write(results.sbml_path.parent / f"{results.sbml_path.stem}.md")
