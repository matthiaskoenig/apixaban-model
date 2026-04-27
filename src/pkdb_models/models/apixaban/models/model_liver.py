"""Liver model for apixaban."""
import pandas as pd
from sbmlutils.factory import *
from sbmlutils.metadata import *
from pkdb_models.models.apixaban.models import annotations
from pkdb_models.models.apixaban.models import templates


class U(templates.U):
    """UnitDefinitions"""

    pass


_m = Model(
    sid="apixaban_liver",
    name="Model for hepatic apixaban metabolism.",
    notes=f"""
    Model for hepatic apixaban metabolism.
    """ + templates.terms_of_use,
    creators=templates.creators,
    units=U,
    model_units=templates.model_units,
    annotations=annotations.model + [
        # tissue
        (BQB.OCCURS_IN, "fma/FMA:7197"),  # liver
        (BQB.OCCURS_IN, "bto/BTO:0000759"),  # liver
        (BQB.OCCURS_IN, "NCIT:C12392"),  # liver
        (BQB.HAS_PROPERTY, "NCIT:C79371"),  # Pharmacokinetics: Metabolism
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
        "Vli",
        value=1.5,
        unit=U.liter,
        name="liver",
        constant=True,
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments["li"],
        port=True
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
        port=True
    ),
    Compartment(
        "Vbi",
        1.0,
        name="bile",
        unit=U.liter,
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments["bi"],
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
        name="apixaban (plasma)",
        initialConcentration=0.0,
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["api"],
        port=True
    ),
    Species(
        "api",
        name="apixaban (liver)",
        initialConcentration=0.0,
        compartment="Vli",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["api"]
    ),
    Species(
        "m1_ext",
        name="M1 (plasma)",
        initialConcentration=0.0,
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m1"],
        port=True
    ),
    Species(
        "m1",
        name="M1 (liver)",
        initialConcentration=0.0,
        compartment="Vli",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m1"]
    ),
    Species(
        "m1_bi",
        initialConcentration=0.0,
        name="M1 (bile)",
        compartment="Vbi",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m1"]
    ),
    Species(
        "m1_lumen",
        initialConcentration=0.0,
        name="M1 (gut)",
        compartment="Vlumen",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m1"],
        port=True
    ),
    Species(
        "m2",
        name="M2 (liver)",
        initialConcentration=0.0,
        compartment="Vli",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m2"],
    ),
    Species(
        "m2_bi",
        initialConcentration=0.0,
        name="M2 (bile)",
        compartment="Vbi",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m2"],
    ),
    Species(
        "m2_lumen",
        initialConcentration=0.0,
        name="M2 (gut)",
        compartment="Vlumen",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m2"],
        port=True
    ),
    Species(
        "m7_ext",
        name="M7 (plasma)",
        initialConcentration=0.0,
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m7"],
        port=True
    ),
    Species(
        "m7",
        name="M7 (liver)",
        initialConcentration=0.0,
        compartment="Vli",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m7"],
    ),
    Species(
        "m7_bi",
        initialConcentration=0.0,
        name="M7 (bile)",
        compartment="Vbi",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m7"],
    ),
    Species(
        "m7_lumen",
        initialConcentration=0.0,
        name="M7 (gut)",
        compartment="Vlumen",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["m7"],
        port=True
    )
]

_m.reactions = [
    Reaction(
        sid="APIIM",
        name="apixaban import (APIIM)",
        equation="api_ext <-> api",
        compartment="Vmem",
        sboTerm=SBO.TRANSPORT_REACTION,
        pars=[
            Parameter(
                "APIIM_k",
                1000.0,
                U.per_min,
                name="rate apixaban import",
                sboTerm=SBO.MAXIMAL_VELOCITY,
            ),
            Parameter(
                "fu_api",
                13.1 / 100,  # [-] unbound in plasma He2011
                U.dimensionless,
                constant=True,
                name=f"fraction unbound in plasma api",
                sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
                port=True,
            ),
        ],
        formula=(
            "APIIM_k * Vli * (api_ext * fu_api - api)"
        ),
        notes="""Assuming fast equilibration."""
    ),

    Reaction(
        sid="API2M2",
        name="apixaban -> M2 (CYP3A4/5)",
        equation="api -> m2",
        compartment="Vli",
        sboTerm=SBO.BIOCHEMICAL_REACTION,
        pars=[
            Parameter(
                "API2M2_k",
                0.16036687106093256,
                U.per_min,
                name="rate api -> m2 conversion",
                sboTerm=SBO.MAXIMAL_VELOCITY,
            ),
        ],
        formula=(
            "API2M2_k * Vli * api"
        ),
    ),
    Reaction(
        sid="API2M7",
        name="apixaban -> M7 (CYP3A4/5)",
        equation="api -> m7",
        compartment="Vli",
        sboTerm=SBO.BIOCHEMICAL_REACTION,
        pars=[
            Parameter(
                "API2M7_k",
                0.0389310457140792,
                U.per_min,
                name="rate api -> m7 conversion",
                sboTerm=SBO.MAXIMAL_VELOCITY,
            ),
        ],
        formula=(
            "API2M7_k * Vli * api"
        ),
    ),
    Reaction(
        sid="M22M1",
        name="M2 -> M1 (SULT1A1)",
        equation="m2 -> m1",
        compartment="Vli",
        sboTerm=SBO.BIOCHEMICAL_REACTION,
        pars=[
            Parameter(
                "M22M1_Vmax", # M22M1_k
                0.03597094464409813,
                U.mmole_per_min,
                name="rate m2 -> m1 conversion",
                sboTerm=SBO.MAXIMAL_VELOCITY,
            ),
            Parameter(
                "M22M1_Km",
                22.420375926289406,
                U.mmole,
                name="rate m2 -> m1 conversion",
                sboTerm=SBO.MAXIMAL_VELOCITY,
            ),
        ],
        formula=(
            "M22M1_Vmax * Vli * m2 / (M22M1_Km + Vli * m2)"
        ),
    ),
    Reaction(
        sid="M1EX",
        name="M1 export (M1EX)",
        equation="m1 <-> m1_ext",
        compartment="Vmem",
        sboTerm=SBO.TRANSPORT_REACTION,
        pars=[
            Parameter(
                "M1EX_k",
                1000.0,
                U.per_min,
                name="rate M1 export",
                sboTerm=SBO.MAXIMAL_VELOCITY,
            ),
        ],
        formula=(
            "M1EX_k * Vli * (m1 - m1_ext)"
        ),
        notes="""Assuming fast equilibration."""
    ),
    Reaction(
        sid="M7EX",
        name="M7 export (M7EX)",
        equation="m7 <-> m7_ext",
        compartment="Vmem",
        sboTerm=SBO.TRANSPORT_REACTION,
        pars=[
            Parameter(
                "M7EX_k",
                1000.0,
                U.per_min,
                name="rate M7 export",
                sboTerm=SBO.MAXIMAL_VELOCITY,
            ),
        ],
        formula=(
            "M7EX_k * Vli * (m7 - m7_ext)"
        ),
        notes="""Assuming fast equilibration."""
    ),


]


_m.parameters.extend([
    Parameter(
        "MXEXBI_k",
        0.010684693804886113,
        unit=U.per_min,
        name="rate for edoxaban metabolites export in bile",
        sboTerm=SBO.KINETIC_CONSTANT,
    ),
]
)

for sid in ["m1", "m2", "m7"]:
    _m.reactions.extend([
        Reaction(
            f"{sid.upper()}EXBI",
            name=f"{sid.upper()} bile export",
            equation=f"{sid} -> {sid}_bi",
            sboTerm=SBO.TRANSPORT_REACTION,
            compartment="Vmem",
            formula=(
                f"MXEXBI_k * Vli * {sid}",
                U.mmole_per_min,
            ),
        ),
        Reaction(
            f"{sid.upper()}EXEHC",
            name=f"{sid.upper()} lumen export",
            equation=f"{sid}_bi -> {sid}_lumen",
            sboTerm=SBO.TRANSPORT_REACTION,
            compartment="Vlumen",
            formula=(
                f"{sid.upper()}EXBI",
                U.mmole_per_min,
            ),
        ),
    ])

model_liver = _m

def apixaban_layout(dx=200, dy=200) -> pd.DataFrame:
    """Layout definition."""

    delta_y = 0.5 * dy
    delta_x = 0.7 * dx

    positions = [
        # sid, x, y

        ["api_ext",  1.7 * delta_x, 0 * delta_y],
        ["m7_ext", 0.2 * delta_x, 0 * delta_y],
        ["m1_ext", 4.7 * delta_x, 0 * delta_y],

        ["APIIM", 1.7 * delta_x, 1 * delta_y],
        ["M7EX", 0.2 * delta_x, 1 * delta_y],
        ["M1EX", 4.7 * delta_x, 1 * delta_y],

        ["api",  1.7 * delta_x, 2 * delta_y],
        ["m7", 0.2 * delta_x, 2 * delta_y],
        ["m2", 3.2 * delta_x, 2 * delta_y],
        ["m1", 4.7 * delta_x, 2 * delta_y],

        ["API2M7", (0.2+1.7)/2 * delta_x, 2.5 * delta_y],
        ["API2M2", (1.7+3.2)/2 * delta_x, 2.5 * delta_y],
        ["M22M1", (3.2+4.7)/2 * delta_x, 2.5 * delta_y],

        ["M7EXBI",  0.2 * delta_x, 3.0 * delta_y],
        ["M2EXBI", 3.2 * delta_x, 3.0 * delta_y],
        ["M1EXBI", 4.7 * delta_x, 3.0 * delta_y],

        ["m7_bi", 0.2  * delta_x, 3.7 * delta_y],
        ["m2_bi", 3.2 * delta_x, 3.7 * delta_y],
        ["m1_bi", 4.7 * delta_x, 3.7 * delta_y],

        ["M7EXEHC", 0.2  * delta_x, 4.5 * delta_y],
        ["M2EXEHC", 3.2 * delta_x, 4.5 * delta_y],
        ["M1EXEHC", 4.7 * delta_x, 4.5 * delta_y],

        ["m7_lumen", 0.2 * delta_x, 5.2 * delta_y],
        ["m2_lumen", 3.2 * delta_x, 5.2 * delta_y],
        ["m1_lumen", 4.7 * delta_x, 5.2 * delta_y],
    ]

    df = pd.DataFrame(positions, columns=["id", "x", "y"])
    df.set_index("id", inplace=True)

    return df


def apixaban_annotations(dx=200, dy=200) -> list:
    COLOR_PLASMA = "#FF796C"
    COLOR_LIVER = "#FFFFFF"
    COLOR_BILE = "#F5F5C6"
    COLOR_LUMEN = "#CFEFFF"

    kwargs = {
        "type": cyviz.AnnotationShapeType.ROUND_RECTANGLE,
        "opacity": 20,
        "border_color": "#000000",
        "border_thickness": 2,
    }

    xpos = -0.5 * dx
    width = 4.4 * dx
    delta_y = 0.5 * dy

    annotations = [
        cyviz.AnnotationShape(
            x_pos=xpos, y_pos=-0.5 * delta_y, width=width, height=1.5 * delta_y,
            fill_color=COLOR_PLASMA, **kwargs
        ),
        cyviz.AnnotationShape(
            x_pos=xpos, y_pos=1.0 * delta_y, width=width, height=2.0 * delta_y,
            fill_color=COLOR_LIVER, **kwargs
        ),
        cyviz.AnnotationShape(
            x_pos=xpos, y_pos=3.0 * delta_y, width=width, height=1.5 * delta_y,
            fill_color=COLOR_BILE, **kwargs
        ),
        cyviz.AnnotationShape(
            x_pos=xpos, y_pos=4.5 * delta_y, width=width, height=1.3 * delta_y,
            fill_color=COLOR_LUMEN, **kwargs
        ),
    ]

    return annotations

if __name__ == "__main__":
    from sbmlutils.converters import odefac
    from pkdb_models.models.apixaban import MODEL_BASE_PATH
    from sbmlutils import cytoscape as cyviz

    results: FactoryResult = create_model(
        model=model_liver,
        filepath=MODEL_BASE_PATH / f"{model_liver.sid}.xml",
        sbml_level=3,
        sbml_version=2,
    )

    # ODE equations
    ode_factory = odefac.SBML2ODE.from_file(sbml_file=results.sbml_path)
    ode_factory.to_markdown(md_file=results.sbml_path.parent / f"{results.sbml_path.stem}.md")

    # visualization in Cytoscape
    cyviz.visualize_sbml(sbml_path=results.sbml_path, delete_session=True)
    cyviz.apply_layout(layout=apixaban_layout())
    cyviz.add_annotations(annotations=apixaban_annotations())
