"""Liver model for apixaban."""

from sbmlutils.factory import (
    Compartment,
    Model,
    NaN,
    Parameter,
    Reaction,
    Species,
    create_model,
)
from sbmlutils.metadata import (
    BQB,
    SBO,
)

from pkdb_models.models.apixaban.models import annotations, templates
from pkdb_models.models.apixaban.models.fits import FITS


class U(templates.U):
    """Units of the liver model."""


_m = Model(
    sid="apixaban_liver",
    name="Model for hepatic apixaban metabolism.",
    notes="""
    Model for hepatic apixaban metabolism.

    The unbound apixaban in plasma equilibrates with the hepatocytes and is
    metabolized by CYP3A4/5 (`API2M_k`, activity `f_cyp3a4`) to O-demethyl
    apixaban (M2, fraction `f_m2`) and hydroxy apixaban (M7). M2 is sulfated to
    M1. M1 and M7 are exported into the plasma, M1, M2 and M7 are excreted with
    the bile into the intestinal lumen.
    """
    + templates.terms_of_use,
    creators=templates.creators,
    units=U,
    model_units=templates.model_units,
    annotations=[
        *annotations.model,
        # tissue
        (BQB.OCCURS_IN, "fma/FMA:7197"),  # liver
        (BQB.OCCURS_IN, "bto/BTO:0000759"),  # liver
        (BQB.OCCURS_IN, "NCIT:C12392"),  # liver
        (BQB.HAS_PROPERTY, "NCIT:C79371"),  # Pharmacokinetics: Metabolism
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
        "Vli",
        value=1.5,
        unit=U.liter,
        name="liver",
        constant=True,
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments["li"],
        port=True,
    ),
    Compartment(
        "Vmem",
        value=NaN,
        unit=U.m2,
        name="membrane",
        constant=True,
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments["basolateral"],
        spatialDimensions=2,
        port=True,
    ),
    Compartment(
        "Vlumen",
        1.0,
        name="gut lumen",
        unit=U.liter,
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments["gu"],
        port=True,
    ),
]

_m.species = [
    Species(
        "api_ext",
        name="apixaban (api_ext)",
        initialConcentration=0.0,
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=[
            *annotations.species["api"],
            (BQB.IS, "https://bioregistry.io/PBPKO:00549"),  # concentration in plasma
        ],
        port=True,
    ),
    Species(
        "api",
        name="apixaban (api)",
        initialConcentration=0.0,
        compartment="Vli",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=[
            *annotations.species["api"],
            (BQB.IS, "https://bioregistry.io/PBPKO:00539"),  # concentration in liver
        ],
    ),
    Species(
        "m1_ext",
        name="M1 (m1_ext)",
        initialConcentration=0.0,
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=[
            *annotations.species["m1"],
            (BQB.IS, "https://bioregistry.io/PBPKO:00549"),  # concentration in plasma
        ],
        port=True,
    ),
    Species(
        "m1",
        name="M1 (m1)",
        initialConcentration=0.0,
        compartment="Vli",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=[
            *annotations.species["m1"],
            (BQB.IS, "https://bioregistry.io/PBPKO:00539"),  # concentration in liver
        ],
    ),
    Species(
        "m1_lumen",
        initialConcentration=0.0,
        name="M1 (m1_lumen)",
        compartment="Vlumen",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m1"],
        port=True,
    ),
    Species(
        "m2",
        name="M2 (m2)",
        initialConcentration=0.0,
        compartment="Vli",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m2"],
    ),
    Species(
        "m2_lumen",
        initialConcentration=0.0,
        name="M2 (m2_lumen)",
        compartment="Vlumen",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m2"],
        port=True,
    ),
    Species(
        "m7_ext",
        name="M7 (m7_ext)",
        initialConcentration=0.0,
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m7"],
        port=True,
    ),
    Species(
        "m7",
        name="M7 (m7)",
        initialConcentration=0.0,
        compartment="Vli",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m7"],
    ),
    Species(
        "m7_lumen",
        initialConcentration=0.0,
        name="M7 (m7_lumen)",
        compartment="Vlumen",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m7"],
        port=True,
    ),
]

_m.reactions = [
    Reaction(
        sid="APIIM",
        name="import apixaban (APIIM)",
        equation="api_ext <-> api",
        compartment="Vmem",
        sboTerm=SBO.TRANSPORT_REACTION,
        pars=[
            Parameter(
                "APIIM_k",
                1000.0,
                U.per_min,
                name="rate apixaban import",
                sboTerm=SBO.KINETIC_CONSTANT,
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
        ],
        formula=("APIIM_k * Vli * (api_ext * fu_api - api)", U.mmole_per_min),
        notes="""Assuming fast equilibration.""",
    ),
    Reaction(
        sid="API2M2",
        name="apixaban -> M2 (API2M2)",
        equation="api -> m2",
        compartment="Vli",
        sboTerm=SBO.BIOCHEMICAL_REACTION,
        formula=("f_cyp3a4 * API2M_k * f_m2 * Vli * api", U.mmole_per_min),
        notes="""O-demethylation by CYP3A4/5.""",
    ),
    Reaction(
        sid="API2M7",
        name="apixaban -> M7 (API2M7)",
        equation="api -> m7",
        compartment="Vli",
        sboTerm=SBO.BIOCHEMICAL_REACTION,
        formula=(
            "f_cyp3a4 * API2M_k * (1 dimensionless - f_m2) * Vli * api",
            U.mmole_per_min,
        ),
        notes="""Hydroxylation by CYP3A4/5.""",
    ),
    Reaction(
        sid="M22M1",
        name="M2 -> M1 (M22M1)",
        equation="m2 -> m1",
        compartment="Vli",
        sboTerm=SBO.BIOCHEMICAL_REACTION,
        pars=[
            Parameter(
                "M22M1_k",
                **FITS.parameter("LI__M22M1_k", unit=U.per_min),
                name="rate of the sulfation M2 -> M1",
                sboTerm=SBO.KINETIC_CONSTANT,
            ),
        ],
        formula=("M22M1_k * Vli * m2", U.mmole_per_min),
        notes="""Sulfation of O-demethyl apixaban (SULT1A1).""",
    ),
    Reaction(
        sid="M1EX",
        name="export M1 (M1EX)",
        equation="m1 <-> m1_ext",
        compartment="Vmem",
        sboTerm=SBO.TRANSPORT_REACTION,
        pars=[
            Parameter(
                "M1EX_k",
                1000.0,
                U.per_min,
                name="rate M1 export",
                sboTerm=SBO.KINETIC_CONSTANT,
            ),
        ],
        formula=("M1EX_k * Vli * (m1 - m1_ext)", U.mmole_per_min),
        notes="""Assuming fast equilibration.""",
    ),
    Reaction(
        sid="M7EX",
        name="export M7 (M7EX)",
        equation="m7 <-> m7_ext",
        compartment="Vmem",
        sboTerm=SBO.TRANSPORT_REACTION,
        pars=[
            Parameter(
                "M7EX_k",
                1000.0,
                U.per_min,
                name="rate M7 export",
                sboTerm=SBO.KINETIC_CONSTANT,
            ),
        ],
        formula=("M7EX_k * Vli * (m7 - m7_ext)", U.mmole_per_min),
        notes="""Assuming fast equilibration.""",
    ),
]


_m.parameters.extend(
    [
        Parameter(
            "API2M_k",
            **FITS.parameter("LI__API2M_k", unit=U.per_min),
            name="rate of the CYP3A4 metabolism of apixaban",
            sboTerm=SBO.KINETIC_CONSTANT,
            notes="""
            Total rate of the metabolism of apixaban by CYP3A4/5 to M2 and M7,
            split by `f_m2`.
            """,
        ),
        Parameter(
            "f_m2",
            0.78,
            U.dimensionless,
            name="fraction of the CYP3A4 metabolism to M2",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes="""
            Fraction of the CYP3A4 metabolism of apixaban by O-demethylation (M2
            and its products M1, M10, M13), the rest is the hydroxylation (M7):
            about 17-18 % vs 5 % of the dose in the urine and feces
            (Raghavan2009, Table 4).
            """,
        ),
        Parameter(
            "f_cyp3a4",
            1.0,
            U.dimensionless,
            name="CYP3A4 activity",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            port=True,
            notes="""
            Activity of CYP3A4 relative to normal: 1.0 normal, <1.0 inhibition
            (e.g. ketoconazole, clarithromycin, diltiazem, ritonavir), >1.0
            induction (e.g. rifampin, carbamazepine); set by the experiments of
            the coadministrations, not fitted.
            """,
        ),
        Parameter(
            "MXEXBI_k",
            **FITS.parameter("LI__MXEXBI_k", unit=U.per_min),
            name="rate of the biliary excretion of the apixaban metabolites",
            sboTerm=SBO.KINETIC_CONSTANT,
        ),
    ]
)

for sid in ["m1", "m2", "m7"]:
    _m.reactions.append(
        Reaction(
            f"{sid.upper()}EXBI",
            name=f"biliary excretion {sid.upper()} ({sid.upper()}EXBI)",
            equation=f"{sid} -> {sid}_lumen",
            sboTerm=SBO.TRANSPORT_REACTION,
            compartment="Vmem",
            formula=(f"MXEXBI_k * Vli * {sid}", U.mmole_per_min),
            notes="""Excretion with the bile into the intestinal lumen.""",
        ),
    )

model_liver: Model = _m


if __name__ == "__main__":
    from sbmlode import OdeSystem

    from pkdb_models.models.apixaban import MODEL_BASE_PATH

    results = create_model(
        model=model_liver,
        filepath=MODEL_BASE_PATH / f"{model_liver.sid}.xml",
        sbml_level=3,
        sbml_version=2,
    )

    # ODE equations
    ode_system = OdeSystem.from_sbml(results.sbml_path)
    ode_system.write(results.sbml_path.parent / f"{results.sbml_path.stem}.md")
