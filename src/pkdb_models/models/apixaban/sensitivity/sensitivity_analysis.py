"""Sensitivity analysis of the apixaban model.

The outputs are the pharmacokinetic parameters of apixaban and its metabolites
M1 and M7 in the plasma of the arm vein after a single oral dose (the
non-compartmental analysis of `pkpdutils`) and the maxima of the
pharmacodynamics. The parameters are a list (`PARAMETER_IDS`): the covariates
and the impairments of the individual, the fitted parameters, the activities
of CYP3A4 and of the intestinal efflux, the fraction unbound of apixaban and
the reference physiology of the library, with bounds of +-15 % around their
value (a severity, 0 in the healthy individual, from 0 to 15 % of its scale).
A model of the library has hundreds of parameters, most of them initial
assignments of the covariates, which an analysis of all constant parameters
would vary as well. The values which initial assignments read change before
the simulation, as every scan of sbmlsim does. The analyses are run as a
script, the local analysis by default:

    python -m pkdb_models.models.apixaban.sensitivity.sensitivity_analysis
    python -m pkdb_models.models.apixaban.sensitivity.sensitivity_analysis local sampling

The analyses run on `sbmlsim.sensitivity.runner.SensitivityRunner`, which writes the
table of the parameters into `results/sensitivity` of the model and the tables
and figures of an analysis into `results/sensitivity/<analysis>`. The groups
are the control and the classes of renal and hepatic impairment of the base
experiment (`renal_map`, `cirrhosis_map`). An analysis does not vary a
parameter which one of its groups sets (`pkpdsim.sensitivity.free_parameters`):
`sampling`, over the seven groups, leaves out `f_renal_function` and
`CP_severity`. The environment variable `PKPDSIM_SENSITIVITY_N` replaces the
numbers of samples of the global analyses for a quick run, see
`pkpdsim.sensitivity.sample_size`.
"""

from collections.abc import Mapping
from typing import NamedTuple

from pkpdsim.sensitivity import NonzeroLocalAnalysis, library_parameters, pk_observables
from sbmlsim import Q
from sbmlsim.sensitivity.parameters import SensitivityParameter
from sbmlsim.sensitivity.runner import (
    FastAnalysis,
    SamplingAnalysis,
    SensitivityGroup,
    SensitivityOutput,
    SensitivityRunner,
    SobolAnalysis,
)
from sbmlsim.simulation import Formula, Simulation

from pkdb_models.models.apixaban import MODEL, MODEL_PATH
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)
from pkdb_models.models.apixaban.fitting.parameters import parameters_pd, parameters_pk

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
#: the pharmacodynamic outputs of the coagulation model, their maximum is the
#: output -> name, unit
PD_OUTPUTS: dict[str, tuple[str, str]] = {
    "COAG__PT": ("PT", "s"),
    "COAG__mPT": ("mPT", "s"),
    "COAG__aPTT": ("aPTT", "s"),
    "COAG__INR": ("INR", "dimensionless"),
    "COAG__antiXa_activity_gram": ("anti-Xa activity", "ng/ml"),
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
    Substance("Carm_api", "API", "pk_api", PK_OUTPUTS_API, "PODOSE_api"),
    Substance("Carm_api_m1", "M1", "pk_m1", PK_OUTPUTS_METABOLITES, None),
    Substance("Carm_api_m7", "M7", "pk_m7", PK_OUTPUTS_METABOLITES, None),
]

#: the outputs: the id of a pharmacokinetic output names the concentration
#: (`Carm_api_cmax`), the id of a pharmacodynamic output the output of the
#: coagulation model (`COAG__INR_max`); both are their own observables
OUTPUTS: list[SensitivityOutput] = [
    *(
        SensitivityOutput(f"{s.selection}_{key}", f"{s.name} {PK_LABELS[key]}")
        for s in SUBSTANCES
        for key in s.outputs
    ),
    *(
        SensitivityOutput(f"{sid}_max", f"max {name}")
        for sid, (name, _) in PD_OUTPUTS.items()
    ),
]


#: the observables of a simulation, the outputs with their units: per
#: substance its non-compartmental analysis and its outputs
#: (`pkpdsim.sensitivity.pk_observables`), then the maxima of the
#: pharmacodynamics
OBSERVABLES = [
    *(
        observable
        for s in SUBSTANCES
        for observable in pk_observables(
            s.selection,
            s.selection,
            s.outputs,
            dose=s.dose,
            route="oral" if s.dose else None,
            per_dose_mass=PK_PER_DOSE_MASS,
            mr="Mr_api",
            pk_id=s.pk_id,
        )
    ),
    *(
        Formula(f"{sid}_max", f"max({sid})", unit=unit)
        for sid, (_, unit) in PD_OUTPUTS.items()
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
                {"f_renal_function": ApixabanSimulationExperiment.renal_map[name]}
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
                {"CP_severity": ApixabanSimulationExperiment.cirrhosis_map[name]}
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


#: the fitted parameters of the model on the PBPK library, those of the fits
#: (`fitting/parameters.py`): the distribution of apixaban, the CYP3A4
#: metabolism, the intestinal efflux, the absorption and the dissolution, the
#: renal factors of M1 and M7 (their fractions unbound), the biliary excretion
#: and the sulfation of the metabolites, and the coagulation
FITTED_IDS: tuple[str, ...] = tuple(fp.pid for fp in parameters_pk + parameters_pd)

#: the parameters of the analyses: the covariates and the impairments of the
#: individual, the fitted parameters, the activities of CYP3A4 and of the
#: intestinal efflux (the factors of the interactions), the fraction unbound
#: of apixaban and the reference physiology of the library
PARAMETER_IDS: tuple[str, ...] = (
    "BW",
    "HEIGHT",
    "f_renal_function",
    "CP_severity",
    "HF_severity",
    "f_cardiac_function",
    *FITTED_IDS,
    "LI__f_cyp3a4",
    "GU__f_abcb1",
    "fu_ref_api",
    "HCT_ref",
    "CO_ref",
    "GFR_ref",
)

#: the source of the classes of the renal function (the stages of chronic
#: kidney disease by the GFR), in the form of the sources of the library
STEVENS2024 = (
    "Stevens PE, Ahmed SB, Carrero JJ, et al. (KDIGO CKD Work Group). KDIGO "
    "2024 Clinical Practice Guideline for the Evaluation and Management of "
    "Chronic Kidney Disease. Kidney Int 105(4S), S117-S314, 2024. "
    "doi:10.1016/j.kint.2023.10.018"
)

#: the factors of the organ functions and of the activities of the proteins,
#: 1 in the healthy individual
SCALING_IDS: tuple[str, ...] = (
    "f_cardiac_function",
    "f_renal_function",
    "LI__f_cyp3a4",
    "GU__f_abcb1",
)


def sensitivity_parameters() -> list[SensitivityParameter]:
    """Get the parameters of the analyses with their bounds and references.

    The parameters of `PARAMETER_IDS` (`pkpdsim.sensitivity.library_parameters`):
    the fitted parameters, the scaling factors (`SCALING_IDS`) and the
    severities with their bounds, the references of their notes and the
    guideline of the classes of the renal function, whose notes give no source.
    """
    return library_parameters(
        MODEL_PATH,
        PARAMETER_IDS,
        fit_ids=FITTED_IDS,
        scaling_ids=SCALING_IDS,
        references={"f_renal_function": STEVENS2024},
        relative=BOUNDS_FRACTION,
    )


#: the analyses of the script, with their groups and numbers of samples
SENSITIVITY = SensitivityRunner(
    project=MODEL,
    out=MODEL.results_dir / "sensitivity",
    parameters=sensitivity_parameters,
    outputs=OUTPUTS,
    observables=OBSERVABLES,
    analyses={
        "local": NonzeroLocalAnalysis(groups=SENSITIVITY_GROUPS[:1], delta=0.01),
        "sampling": SamplingAnalysis(groups=SENSITIVITY_GROUPS, n=1000),
        "fast": FastAnalysis(groups=SENSITIVITY_GROUPS[:1], n=1000),
        "sobol": SobolAnalysis(groups=SENSITIVITY_GROUPS[:1], n=4096),
    },
    default=("local",),
)


if __name__ == "__main__":
    SENSITIVITY.main()
