"""Model for coagulation factors and readouts."""
import pandas as pd
from sbmlutils.factory import *
from sbmlutils.metadata import *
from pkdb_models.models.apixaban.models import annotations
from pkdb_models.models.apixaban.models import templates


class U(templates.U):
    """UnitDefinitions"""
    ng_per_ml = UnitDefinition("ng_per_ml", "ng/ml")
    IU_per_ml = UnitDefinition("IU_per_ml", "1/ml")
    per_mM = UnitDefinition("per_mM", "1/(mmole/l)")
    ng_per_ml_mM = UnitDefinition("ng_per_ml_mM", "ng/(ml*mmole/l)")
    IU_per_ml_mM = UnitDefinition("IU_per_ml_mM", "1/(ml*mmole/l)")


_m = Model(
    sid="apixaban_coagulation",
    name="Model for coagulation factors and readouts.",
    notes=f"""
    Model for coagulation factors and readouts.        
    """ + templates.terms_of_use,
    creators=templates.creators,
    units=U,
    model_units=templates.model_units,
    annotations=annotations.model + [
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
        port=True
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
    "Xa_inhibition": "inhibition of FXa",
    "antiXa_activity": "anti-FXa activity",
    "antiXa_activity_gram": "anti-FXa activity",
}
reference_values = {
    "INR": 1,  # [-]
    "PT": 12.5,  # [s]
    "aPTT": 28.4,  # [s]
    "mPT": 53.4,  # [s] Foster2021 placebo
    "Xa_inhibition": 0, # [-] not inhibited
    "antiXa_activity": 0,  # [IU/ml]
    "antiXa_activity_gram": 0, #[ng/ml]
}
unit_values = {
    "INR": U.dimensionless,
    "PT": U.second,
    "aPTT": U.second,
    "mPT": U.second,
    "Xa_inhibition": U.dimensionless,
    "antiXa_activity": U.IU_per_ml,
    "antiXa_activity_gram": U.ng_per_ml,
}

for sid in ["INR", "PT", "aPTT", "mPT"]:
    _m.parameters.extend([
        Parameter(
            sid=f"{sid}_ref",
            name=f"{names[sid]} reference",
            value=reference_values[sid],
            unit=unit_values[sid],
            constant=True,
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        ),
    ])

for sid in ["INR", "PT", "aPTT", "mPT", "Xa_inhibition", "antiXa_activity", "antiXa_activity_gram"]:
    _m.parameters.extend([
        Parameter(
            sid=sid,
            name=names[sid],
            value=reference_values[sid],
            unit=unit_values[sid],
            constant=False,
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        )
    ])

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
        AssignmentRule(
            f"{sid}_change", f"{sid}-{sid}_ref", unit=U.second
        )
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
        AssignmentRule(
            f"{sid}_ratio", f"{sid}/{sid}_ref", unit=U.dimensionless
        )
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
            notes=f"Ratio relative to baseline {names[sid]}",
        )
    )
    _m.rules.append(
        AssignmentRule(
            f"{sid}_relchange", f"({sid} - {sid}_ref)/{sid}_ref", unit=U.dimensionless
        )
    )


# Effect of apixaban on INR, PT, aPTT and Xa_inhibition
_m.parameters.extend([
    Parameter(
        "fu_api",
        13.1 / 100, # [-] unbound in plasma He2011
        U.dimensionless,
        constant=True,
        name=f"fraction unbound in plasma {sid}",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        sid="Emax_INR",
        name="Effect constant for INR inhibition",
        value=1.039561836305882,
        unit=U.dimensionless,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        sid="EC50_api_INR",
        name="Effect constant for INR",
        value=0.0001940723569696365,
        unit=U.mM,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        sid="Emax_PT",
        name="Effect constant for PT inhibition",
        value=1.6587220005784251,
        unit=U.dimensionless,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        sid="EC50_api_PT",
        name="Effect constant for PT",
        value=0.00018436022230444452,
        unit=U.mM,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        sid="Emax_aPTT",
        name="Effect constant for aPTT inhibition",
        value=0.5831984416695168,
        unit=U.dimensionless,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        sid="EC50_api_aPTT",
        name="Effect constant for aPTT",
        value=0.0001528970357985037,
        unit=U.mM,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        sid="Emax_mPT",
        name="Effect constant for mPT inhibition",
        value=2.0219222706330124,
        unit=U.dimensionless,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        sid="EC50_api_mPT",
        name="Effect constant for mPT",
        value=5.593387897644722e-05,
        unit=U.mM,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    # Xa
    Parameter(
        sid="Emax_antiXa",
        name="Effect constant for anti-Xa activity",
        value=40774.78983249683,
        unit=U.IU_per_ml_mM,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        sid="Emax_antiXa_gram",
        name="Effect constant for anti-Xa activity",
        value=2593907.3533155103,
        unit=U.ng_per_ml_mM,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),

])

_m.rules.extend([
    AssignmentRule(
        "INR", "INR_ref * (1 dimensionless + Emax_INR * Cve_api * fu_api / (Cve_api * fu_api + EC50_api_INR))", unit=U.second
    ),
    AssignmentRule(
        "PT", "PT_ref * (1 dimensionless + Emax_PT * Cve_api * fu_api / (Cve_api * fu_api + EC50_api_PT))", unit=U.second
    ),
    AssignmentRule(
        "aPTT", "aPTT_ref * (1 dimensionless + Emax_aPTT * Cve_api * fu_api / (Cve_api * fu_api + EC50_api_aPTT))", unit=U.second
    ),
    AssignmentRule(
        "mPT", "mPT_ref * (1 dimensionless + Emax_mPT * Cve_api * fu_api / (Cve_api * fu_api + EC50_api_mPT))", unit=U.second
    ),
    AssignmentRule(
        "antiXa_activity", "Emax_antiXa * Cve_api * fu_api", unit=U.IU_per_ml
    ),
    AssignmentRule(
        "antiXa_activity_gram", "Emax_antiXa_gram * Cve_api * fu_api", unit=U.ng_per_ml
    )
])

model_coagulation = _m


if __name__ == "__main__":
    from pkdb_models.models.apixaban import MODEL_BASE_PATH
    from sbmlutils import cytoscape as cyviz
    from sbmlutils.converters import odefac

    results: FactoryResult = create_model(
        model=model_coagulation,
        filepath=MODEL_BASE_PATH / f"{model_coagulation.sid}.xml",
        sbml_level=3, sbml_version=2,
        validation_options=ValidationOptions(units_consistency=True)
    )
    # create differential equations
    md_path = MODEL_BASE_PATH / f"{model_coagulation.sid}.md"
    ode_factory = odefac.SBML2ODE.from_file(sbml_file=results.sbml_path)
    ode_factory.to_markdown(md_file=md_path)

    # visualization in Cytoscape
    cyviz.visualize_sbml(sbml_path=results.sbml_path, delete_session=True)
