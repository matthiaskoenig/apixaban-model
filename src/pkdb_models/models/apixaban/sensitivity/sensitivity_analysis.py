"""Sensitivity analysis of the apixaban model.

The outputs are the pharmacokinetic parameters of apixaban and its metabolites
M1 and M7 after a single oral dose (the non-compartmental analysis of
`pkpdutils`) and the maxima of the pharmacodynamics. The parameters are the
parameters of the model with bounds of +-15 % around their value, the fitted
parameters with the bounds of the fits. The analyses are run as a script, the
local analysis by default:

    python -m pkdb_models.models.apixaban.sensitivity.sensitivity_analysis
    python -m pkdb_models.models.apixaban.sensitivity.sensitivity_analysis local sampling

The analyses run on `pkpdsim.sensitivity.SensitivityRunner`, which writes the
table of the parameters into `results/sensitivity` of the model and the tables
and figures of sbmlsim 0.8.5 of an analysis into `results/sensitivity/<analysis>`.
The groups are the control and the classes of renal and hepatic impairment of
the base experiment (`renal_map`, `cirrhosis_map`). An analysis does not vary a
parameter which one of its groups sets (`pkpdsim.sensitivity.free_parameters`):
`sampling`, over the seven groups, leaves out `KI__f_renal_function`
(`f_cirrhosis`, 0 in the model, is no parameter of the analyses). The environment variable `PKPDSIM_SENSITIVITY_N`
replaces the numbers of samples of the global analyses for a quick run, see
`pkpdsim.sensitivity.sample_size`.
"""

from collections.abc import Mapping
from typing import NamedTuple

from pkpdsim.sensitivity import (
    FastAnalysis,
    LocalAnalysis,
    ParameterType,
    SamplingAnalysis,
    SensitivityGroup,
    SensitivityOutput,
    SensitivityParameter,
    SensitivityRunner,
    SobolAnalysis,
    parameters_from_sbml,
    set_bounds,
    set_relative_bounds,
)
from sbmlsim import Q
from sbmlsim.simulation import PK, Formula, Simulation

from pkdb_models.models.apixaban import MODEL, MODEL_PATH
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)
from pkdb_models.models.apixaban.fitting.parameters import (
    parameters_pd,
    parameters_pk,
)

#: oral dose of the analysis [mg]
DOSE_API = 5
#: fraction of the bounds of a parameter relative to its value
BOUNDS_FRACTION = 0.15

#: outputs of the non-compartmental analysis of pkpdutils of apixaban -> unit
PK_OUTPUTS_API: dict[str, str] = {
    "auc_inf_obs": "mM*min",
    "cmax": "mM",
    "thalf": "min",
    "vz_f": "l",
    "cl_f": "ml/min",
    "lambda_z": "1/min",
}
#: outputs of the non-compartmental analysis of pkpdutils of the metabolites
#: -> unit; the metabolites have no dose and therefore no clearance and volume
PK_OUTPUTS_METABOLITES: dict[str, str] = {
    "auc_inf_obs": "mM*min",
    "cmax": "mM",
    "thalf": "min",
}
#: the pharmacodynamic outputs, their maximum is the output
PD_OUTPUTS: dict[str, str] = {
    "PT": "s",
    "mPT": "s",
    "aPTT": "s",
    "INR": "dimensionless",
    "antiXa_activity_gram": "ng/ml",
}
#: the outputs whose unit has the amount of the dose: the dose is a mass
#: (`PODOSE_api` in mg), so they are divided by the molecular weight (its value
#: at the start, a value per simulation like the parameter of the analysis)
PK_PER_DOSE_MASS: frozenset[str] = frozenset({"vz_f", "cl_f"})
#: the labels of the pharmacokinetic parameters in the names of the outputs
PK_LABELS: dict[str, str] = {
    "auc_inf_obs": "AUC∞",
    "cmax": "Cmax",
    "thalf": "Half-life",
    "vz_f": "Vz/F",
    "cl_f": "CL/F",
    "lambda_z": "λz",
}


class Substance(NamedTuple):
    """A substance of the pharmacokinetic outputs, its concentration in plasma."""

    #: the concentration, which the non-compartmental analysis reads
    selection: str
    #: the name of the substance in the names of the outputs
    name: str
    #: the id of the non-compartmental analysis, no id of the model
    pk_id: str
    #: the outputs of the analysis -> unit
    outputs: dict[str, str]
    #: the dose, of apixaban only
    dose: str | None


#: the substances of the pharmacokinetic outputs
SUBSTANCES: list[Substance] = [
    Substance("[Cve_api]", "API", "pk_api", PK_OUTPUTS_API, "PODOSE_api"),
    Substance("[Cve_m1]", "M1", "pk_m1", PK_OUTPUTS_METABOLITES, None),
    Substance("[Cve_m7]", "M7", "pk_m7", PK_OUTPUTS_METABOLITES, None),
]

#: the outputs: the id of a pharmacokinetic output names the concentration with
#: its brackets (`[Cve_api]_cmax`), as the tables of sbmlsim 0.8.5, its
#: observable has the id without them (`Cve_api_cmax`)
OUTPUTS: list[SensitivityOutput] = [
    *(
        SensitivityOutput(
            f"{s.selection}_{key}",
            f"{s.name} {PK_LABELS[key]}",
            f"{s.selection.strip('[]')}_{key}",
        )
        for s in SUBSTANCES
        for key in s.outputs
    ),
    *(SensitivityOutput(f"{sid}_max", f"max {sid}") for sid in PD_OUTPUTS),
]


def _pk_formula(substance: Substance, key: str) -> str:
    """Get the formula of a pharmacokinetic output of a substance."""
    if key in PK_PER_DOSE_MASS:
        return f"{substance.pk_id}.{key} / at(Mr_api, 0)"
    return f"{substance.pk_id}.{key}"


#: the observables of a simulation, the outputs with their units
OBSERVABLES = [
    *(
        PK(
            s.pk_id,
            s.selection,
            dose=s.dose,
            route="oral" if s.dose else None,
            parameters=list(s.outputs),
        )
        for s in SUBSTANCES
    ),
    *(
        Formula(f"{s.selection.strip('[]')}_{key}", _pk_formula(s, key), unit=unit)
        for s in SUBSTANCES
        for key, unit in s.outputs.items()
    ),
    *(
        Formula(f"{sid}_max", f"max({sid})", unit=unit)
        for sid, unit in PD_OUTPUTS.items()
    ),
]


def sensitivity_simulation(changes: Mapping[str, float]) -> Simulation:
    """Get the simulation of a group: a single oral dose of apixaban."""
    return Simulation(
        end=5 * 24 * 60,
        time_unit="min",
        preinit_changes={"PODOSE_api": Q(DOSE_API, "mg"), **changes},
    )


#: the groups the analyses are run for: the control and the classes of renal
#: and hepatic impairment of the base experiment
SENSITIVITY_GROUPS: list[SensitivityGroup] = [
    SensitivityGroup("control", "Control", sensitivity_simulation({}), "dimgrey"),
    *(
        SensitivityGroup(
            uid,
            name,
            sensitivity_simulation(
                {"KI__f_renal_function": ApixabanSimulationExperiment.renal_map[name]}
            ),
            ApixabanSimulationExperiment.renal_colors[name],
        )
        for uid, name in [
            ("mildRI", "Mild renal impairment"),
            ("modRI", "Moderate renal impairment"),
            ("sevRI", "Severe renal impairment"),
        ]
    ),
    *(
        SensitivityGroup(
            uid,
            f"{name} ({uid})",
            sensitivity_simulation(
                {"f_cirrhosis": ApixabanSimulationExperiment.cirrhosis_map[name]}
            ),
            ApixabanSimulationExperiment.cirrhosis_colors[name],
        )
        for uid, name in [
            ("CPT A", "Mild cirrhosis"),
            ("CPT B", "Moderate cirrhosis"),
            ("CPT C", "Severe cirrhosis"),
        ]
    ),
]


def sensitivity_parameters() -> list[SensitivityParameter]:
    """Get the parameters of the analyses with their bounds and references."""
    parameters = parameters_from_sbml(
        MODEL_PATH,
        exclude_ids={
            # molecular weights
            "Mr_api",
            "Mr_m1",
            "Mr_m7",
            # unchangeable values
            "FQlu",
            "FVhv",
            "FVpo",
            # dosing parameters
            "PODOSE_api",
            "IVDOSE_api",
            "ti_api",
            "Ki_api",
            "Ri_api",
            # fast equilibria between the plasma and the hepatocytes
            "LI__APIIM_k",
            "LI__M1EX_k",
            "LI__M7EX_k",
            # unused volumes
            "Vurine",
            "Vfeces",
            "Vstomach",
            "GU__Vstomach",
            # reference values
            "BW_ref",
            "HEIGHT_ref",
            "PT_ref",
            "mPT_ref",
            "aPTT_ref",
            "INR_ref",
        },
        exclude_na=True,
        exclude_zero=True,
    )

    # the fitted parameters vary within the bounds of the fits
    set_bounds(
        parameters,
        [
            (fp.pid, fp.lower_bound, fp.upper_bound, ParameterType.FIT)
            for fp in parameters_pk + parameters_pd
        ],
    )
    # the scaling factors of the organ functions and the transporters
    set_bounds(
        parameters,
        [
            (uid, 1 - BOUNDS_FRACTION, 1 + BOUNDS_FRACTION, ParameterType.SCALING)
            for uid in ["KI__f_renal_function", "LI__f_cyp3a4", "GU__f_pgp"]
        ],
    )

    # the references of the values from the literature
    references = {
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
        "KI__f_renal_function": r"\cite{Stevens2024}",
    }
    by_uid = {p.uid: p for p in parameters}
    for uid, reference in references.items():
        p = by_uid[uid]
        p.reference = reference
        if p.type == ParameterType.NA:
            p.type = ParameterType.DATA

    # every parameter without bounds varies around its value
    set_relative_bounds(parameters, BOUNDS_FRACTION)
    return parameters


#: the analyses of the script, with the groups and the sizes of sbmlsim 0.8.5
SENSITIVITY = SensitivityRunner(
    model=MODEL,
    parameters=sensitivity_parameters,
    outputs=OUTPUTS,
    observables=OBSERVABLES,
    analyses={
        "local": LocalAnalysis(groups=SENSITIVITY_GROUPS[:1], delta=0.01),
        "sampling": SamplingAnalysis(groups=SENSITIVITY_GROUPS, n=1000),
        "fast": FastAnalysis(groups=SENSITIVITY_GROUPS[:1], n=1000),
        "sobol": SobolAnalysis(groups=SENSITIVITY_GROUPS[:1], n=4096),
    },
    default=("local",),
)


if __name__ == "__main__":
    SENSITIVITY.main()
