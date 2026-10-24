"""Parameter fit problems for apixaban.

The data of a fit is selected from the fit mappings of the studies in three
steps, see `sbmlsim.fit.helpers`: the filters on the metadata of the mappings
select the training data of the fit and exclude the rest, the outliers are
named once for all mappings and are the training data which is not usable, and
the validation data is the part of the training data a fit is evaluated on but
not fitted to. The metadata of a mapping describes its curve, what a fit does
with the curve is decided here.

The training data are single doses of healthy subjects, fasted or with the
fasting not reported, without an interacting drug (the microdose cocktails of
apixaban, rivaroxaban and edoxaban included). The validation data has four
parts, each a different question: the interactions (`INTERACTION_VALIDATION`,
the arms with a coadministered drug, simulated with factors of CYP3A4 and P-gp
which are not fitted), the doses (`DOSE_VALIDATION`, the repeated doses, which
the single doses of the training predict), the populations
(`POPULATION_VALIDATION`, renal impairment, the elderly and the body weight,
which the model describes with the renal function and the body size) and the
limitations (`LIMITATION_VALIDATION`, data of a population, a formulation or a
process the model does not describe). The summaries of data which is fitted
one by one and the arms of the same subjects split another way are excluded
(`AGGREGATE_MAPPINGS`).
"""

from pkpdsim.fit import mapping_metadata, observable_filter, observable_id
from pkpdsim.metadata import Coadministration, Fasting, Health
from sbmlsim.console import console
from sbmlsim.experiment import SimulationExperiment
from sbmlsim.fit import FitMapping, FitMappingCollection, MappingKind
from sbmlsim.fit.helpers import FitMappings, MappingFilter

from pkdb_models.models.apixaban import APIXABAN_PATH, DATA_PATHS
from pkdb_models.models.apixaban.experiments.studies import (
    Abdollahizad2025,
    Bashir2018,
    Chang2016,
    Cui2013,
    Frost2013,
    Frost2013a,
    Frost2014,
    Frost2014a,
    Frost2015,
    Frost2015a,
    Frost2015b,
    Frost2017,
    Frost2018,
    Frost2021,
    Frost2021a,
    Garonzik2019,
    Jeong2019,
    Kreutz2017,
    Lenard2024,
    Lenard2025,
    Leong2024,
    Metze2021,
    Mikus2019,
    Raghavan2009,
    Rohr2024,
    Shaikh2021,
    Song2015,
    Song2016,
    Tirona2018,
    Upreti2013,
    Upreti2013a,
    Vakkalagadda2016,
    VandenBosch2021,
    Wang2014,
    Wang2016,
)

#: the keys of fit mappings by study: the keys of the mappings are SIds of their
#: experiment, which two studies can share, so a named mapping is named with
#: its study
type NamedMappings = dict[str, set[str]]

EXPERIMENT_CLASSES: list[type[SimulationExperiment]] = [
    Abdollahizad2025,
    Bashir2018,
    Chang2016,
    Cui2013,
    Frost2013,
    Frost2013a,
    Frost2014,
    Frost2014a,
    Frost2015,
    Frost2015a,
    Frost2015b,
    Frost2017,
    Frost2018,
    Frost2021,
    Frost2021a,
    Garonzik2019,
    Jeong2019,
    Kreutz2017,
    Lenard2024,
    Lenard2025,
    Leong2024,
    Metze2021,
    Mikus2019,
    Raghavan2009,
    Rohr2024,
    Shaikh2021,
    Song2015,
    Song2016,
    Tirona2018,
    Upreti2013,
    Upreti2013a,
    Vakkalagadda2016,
    VandenBosch2021,
    Wang2014,
    Wang2016,
]

#: observables of the pharmacokinetics
PK_OBSERVABLES: set[str] = {
    "Cve_api",
    "Cve_m1",
    "Cve_m7",
    "Aurine_api",
    "Aurine_m1",
    "Aurine_m7",
    "Afeces_api",
    "Afeces_m1",
    "Afeces_m2",
    "Afeces_m7",
}

#: coadministrations of the training data: none, or the microdoses of
#: rivaroxaban and edoxaban of the cocktails, which do not interact with
#: apixaban
NO_INTERACTION: frozenset[Coadministration] = frozenset(
    {Coadministration.NONE, Coadministration.COCKTAIL}
)

#: mappings which are not fitted, the data is not usable
OUTLIER_MAPPINGS: NamedMappings = {
    # the placebo: the coagulation markers drift by 5-15 % in the day, the
    # model without a dose is constant
    "Frost2013a": {"fm_placebo_INR", "fm_placebo_aPTT", "fm_placebo_mPT"},
    # and the relative changes after 2.5 mg, 1-5 % about 0: the residuals
    # normalized with their mean are not meaningful
    "Frost2018": {
        f"fm_{marker}_{arm}_{group}"
        for marker in ["mPT", "aPTT", "INR"]
        for arm in ["placebo", "API2p5"]
        for group in ["japanese", "caucasian"]
    },
    "Frost2021": {"fm_placebo"},
}

#: the validation of the interactions: the arms with a coadministered drug,
#: simulated with factors of CYP3A4 and P-gp which are not fitted (or without
#: a factor for a drug without an interaction). `filter_coadministration`
#: lets the validation data through for this reason, every other
#: coadministration stays out of the selection altogether
INTERACTION_VALIDATION: NamedMappings = {
    "Bashir2018": {
        "fm_apixaban_apixaban_API10__CYC100",
        "fm_apixaban_apixaban_API10__TAC5",
    },
    "Frost2015a": {
        "fm_apixaban_apixaban_API10_D7__KET400",
        "fm_apixaban_apixaban_API10_D11__DIL360",
    },
    "Frost2017": {"fm_apixaban_API10__ATEN"},
    "Garonzik2019": {"fm_apixaban_API10_CLARI500"},
    "Jeong2019": {
        "fm_apixaban_apixaban_API10__ROS20",
        "fm_apixaban_apixaban_API10__LAP250",
    },
    "Lenard2024": {"fm_apixaban_API25__RIV25__EDO50__CLAR"},
    "Lenard2025": {
        "fm_apixaban_API25__RIV25__EDO50__CAR",
        "fm_apixaban_API25__RIV25__EDO50__GAB",
        "fm_apixaban_API25__RIV25__EDO50__PRE",
    },
    "Mikus2019": {
        "fm_apixaban_API25__RIV25__EDO50__KET",
        "fm_apixaban_urine_API25__RIV25__EDO50__KET",
    },
    "Rohr2024": {
        "fm_apixaban_API25__RIV25__EDO50__RITx5",
        "fm_apixaban_urine_API25__RIV25__EDO50__RITx5",
    },
    # rosuvastatin in every group of the study
    "Tirona2018": {"fm_apixaban_control", "fm_cumulative_amount_control"},
    "Upreti2013a": {"fm_apixaban_apixaban_API10__FAMO40"},
    "Vakkalagadda2016": {
        "fm_API5IV_RIF600_apixaban",
        "fm_API5IV_RIF600_cumulative_amount",
        "fm_API10PO_RIF600_apixaban",
        "fm_API10PO_RIF600_cumulative_amount",
    },
}

#: the validation of the doses: the repeated doses, which the single doses of
#: the training predict
DOSE_VALIDATION: NamedMappings = {
    "Cui2013": {"fm_apixaban_API10M"},
    "Frost2013a": {
        *(
            f"fm_apixaban_{group}"
            for group in ["API2x2", "API5x2", "API10", "API10x2", "API25", "API25x2"]
        ),
        *(
            f"fm_{group}_{marker}"
            for group in ["API2x2", "API5x2", "API10x2", "API25", "API25x2"]
            for marker in ["INR", "aPTT", "mPT"]
        ),
        "fm_API10_aPTT",
        "fm_API10_mPT",
    },
    "Frost2014": {"fm_apixaban_mAPI", "fm_mAPI_antiXa_activity"},
    # twice daily doses with meals
    "Kreutz2017": {
        "fm_PO_api_apixaban",
        "fm_PO_api_prothrombin_time_ratio",
        "fm_PO_api_aPTT_ratio",
        "fm_PO_api_Anti_factor_Xa_activity_mean_ug",
    },
}

#: the validation of the populations which the model describes with its
#: physiology: the renal function, the age and the body size
POPULATION_VALIDATION: NamedMappings = {
    # renal impairment; the AUC of the normal group is a third above the one
    # of the other studies
    "Chang2016": {
        f"fm_{sid}_{group}"
        for sid in ["apixaban", "cumulative_amount"]
        for group in ["normal", "mild", "moderate", "severe"]
    },
    "Frost2015": {
        "fm_apixaban_elderly_male",
        "fm_apixaban_elderly_female",
        "fm_cumulative_amount_elderly",
        "fm_INR_elderly",
        "fm_mPT_elderly",
        "fm_antiXa_activity_elderly",
        "fm_antiXa_activity_gram_elderly1",
    },
    # elderly patients with atrial fibrillation and impaired renal function
    "Metze2021": {"fm_apixaban_API5"},
    # the body weight: 47 kg and 137 kg
    "Upreti2013": {
        f"fm_{sid}_{group}"
        for sid in ["apixaban", "cumulative_amount"]
        for group in ["low", "high"]
    },
}

#: the validation of the limitations of the model: valid data of a population,
#: a formulation or a process the model does not describe, which would distort
#: the fitted parameters of the processes it does describe
LIMITATION_VALIDATION: NamedMappings = {
    # hepatic impairment: the shared cirrhosis model lowers the hepatic
    # clearance, the AUC of the moderate group is 1.09 times the control
    "Frost2021a": {
        f"fm_po_{sid}_{group}"
        for sid in ["apixaban", "cumulative_amount", "aPTT", "inr", "xa"]
        for group in ["mild", "moderate"]
        if sid != "apixaban"
    }
    | {"fm_po_apixaban_mild_log", "fm_po_apixaban_moderate_log"},
    # end-stage renal disease on hemodialysis: the model has no dialysis, the
    # renal clearance of apixaban is 0.02 against 11.3 ml/min in the control
    "VandenBosch2021": {"fm_api_apixaban_PO2p5", "fm_api_apixaban_PO5"},
    "Wang2016": {
        f"fm_{sid}_esrd_{period}"
        for sid in ["apixaban", "inr", "pt", "aptt", "xa"]
        for period in ["P1", "P2"]
    }
    | {"fm_cumulative_amount_esrd_P2"},
    # an exposure about twice the one of the other studies of the dose
    "Leong2024": {"fm_apixaban_TEST", "fm_apixaban_REF"},
    "Jeong2019": {"fm_apixaban_apixaban_API10"},
    # obese patients with a fatty liver, with rosuvastatin
    "Tirona2018": {"fm_apixaban_nafld", "fm_cumulative_amount_nafld"},
    # food, which the model has no effect for (the AUC +4 % and -20 %)
    "Frost2013": {"fm_apixaban_fed"},
    "Song2016": {
        "fm_apixaban_fed",
        # the crushed tablet in water and in applesauce
        "fm_apixaban_water",
        "fm_apixaban_applesauce",
    },
    # the nasogastric tube and the crushed tablet
    "Song2015": {
        "fm_apixaban_API5_NGT_D5W",
        "fm_apixaban_API5_NGT_IF",
        "fm_apixaban_API5_NGT_NS",
        "fm_apixaban_API5_NGT_D5W_crushed",
    },
    # the bile of the second group was drained, its feces miss the bile
    "Raghavan2009": {
        f"fm_{sid}_feces_group2" for sid in ["apixaban", "m1", "m2_m10_m13", "m7"]
    },
}

#: the summaries of data which the fits use one by one and the subjects of a
#: study split another way, excluded from every fit: they would count the
#: subjects twice
AGGREGATE_MAPPINGS: NamedMappings = {
    # the same subjects as the reference
    "Abdollahizad2025": {"fm_apixaban_TEST5"},
    # the subjects of the young and the elderly split by sex
    "Frost2015": {
        f"fm_{sid}_{sex}"
        for sid in ["cumulative_amount", "INR", "mPT", "antiXa_activity"]
        for sex in ["male", "female"]
    }
    | {"fm_antiXa_activity_gram_male1", "fm_antiXa_activity_gram_female1"},
}

#: the validation data
VALIDATION_MAPPINGS: NamedMappings = {
    study: set().union(
        *(
            mappings.get(study, set())
            for mappings in [
                INTERACTION_VALIDATION,
                DOSE_VALIDATION,
                POPULATION_VALIDATION,
                LIMITATION_VALIDATION,
            ]
        )
    )
    for study in INTERACTION_VALIDATION
    | DOSE_VALIDATION
    | POPULATION_VALIDATION
    | LIMITATION_VALIDATION
}


def study(fit_mapping: FitMapping) -> str:
    """Get the study of a fit mapping, the id of its experiment."""
    return fit_mapping.reference.experiment.sid


def named(
    mappings: NamedMappings, fit_mapping_key: str, fit_mapping: FitMapping
) -> bool:
    """Check whether a fit mapping is one of the named mappings of its study."""
    return fit_mapping_key in mappings.get(study(fit_mapping), set())


def check_named(mappings: NamedMappings, fit_mappings: FitMappings) -> None:
    """Check that the named mappings are fit mappings of their studies.

    Raises:
        ValueError: for a study which is no experiment, or a key which is no fit
            mapping of its study.
    """
    for sid, keys in mappings.items():
        experiment = fit_mappings.experiments.get(sid)
        if experiment is None:
            raise ValueError(f"'{sid}' is no experiment of the fits.")
        if unknown := sorted(keys - set(experiment._fit_mappings)):
            raise ValueError(f"'{unknown}' are no fit mappings of '{sid}'.")


def filter_aggregates(fit_mapping_key: str, fit_mapping: FitMapping) -> bool:
    """No summaries of data which is fitted one by one, see `AGGREGATE_MAPPINGS`."""
    return not named(AGGREGATE_MAPPINGS, fit_mapping_key, fit_mapping)


def filter_coadministration(fit_mapping_key: str, fit_mapping: FitMapping) -> bool:
    """No interacting drug, besides the validation data."""
    if named(VALIDATION_MAPPINGS, fit_mapping_key, fit_mapping):
        return True
    return mapping_metadata(fit_mapping).coadministration in NO_INTERACTION


def filter_population(fit_mapping_key: str, fit_mapping: FitMapping) -> bool:
    """Healthy subjects, fasted or not reported, besides the validation data."""
    if named(VALIDATION_MAPPINGS, fit_mapping_key, fit_mapping):
        return True
    metadata = mapping_metadata(fit_mapping)
    return metadata.health == Health.HEALTHY and metadata.fasting in {
        Fasting.FASTED,
        Fasting.NR,
    }


def mapping_collections(
    filters: MappingFilter | list[MappingFilter],
    validation: NamedMappings = VALIDATION_MAPPINGS,
) -> dict[str, list[FitMappingCollection]]:
    """Select the data of a fit from the fit mappings of the studies.

    The filters select the training data, the mappings which fail them are
    excluded, and so are the summaries of data which is fitted one by one
    (`AGGREGATE_MAPPINGS`) and the arms with an interacting drug
    (`filter_coadministration`). The outliers are `OUTLIER_MAPPINGS`, the
    validation data is `VALIDATION_MAPPINGS`. Neither kind enters the cost;
    both are simulated and evaluated with the training data, so a report says
    how the fitted parameters describe data they were not fitted on.

    Args:
        filters: filters of the training data.
        validation: the keys of the validation data by study.

    Returns:
        The fit mapping collections of all kinds by experiment id.

    Raises:
        ValueError: if an outlier is a mapping of no study or of several.
    """
    fit_mappings = FitMappings(
        experiment_classes=EXPERIMENT_CLASSES,
        base_path=APIXABAN_PATH,
        data_path=DATA_PATHS,
    )
    for mappings in [OUTLIER_MAPPINGS, AGGREGATE_MAPPINGS, validation]:
        check_named(mappings, fit_mappings)
    # sbmlsim selects the outliers by their keys alone, which must name one
    # mapping of all studies
    outliers = {key for keys in OUTLIER_MAPPINGS.values() for key in keys}
    for key in outliers:
        studies = [
            sid
            for sid, experiment in fit_mappings.experiments.items()
            if key in experiment._fit_mappings
        ]
        if len(studies) != 1:
            raise ValueError(f"The outlier '{key}' is a mapping of {studies}.")
    selection = fit_mappings.select(
        filters=[
            *(filters if isinstance(filters, list) else [filters]),
            filter_aggregates,
            filter_coadministration,
            filter_population,
        ],
        outliers=outliers,
        validation=lambda key, fit_mapping: named(validation, key, fit_mapping),
        print_info=False,
    )
    # the counts per experiment and kind, not the single mappings
    selection.print(detail=False)
    # the validation mappings by the question they answer
    selected = {
        (sid, key)
        for sid, kinds in selection.kinds.items()
        for key, kind in kinds.items()
        if kind is MappingKind.VALIDATION
    }

    def pairs(mappings: NamedMappings) -> set[tuple[str, str]]:
        return {(sid, key) for sid, keys in mappings.items() for key in keys}

    console.print(
        "validation: "
        + ", ".join(
            f"{len(selected & pairs(mappings))} {question}"
            for question, mappings in [
                ("interactions", INTERACTION_VALIDATION),
                ("doses", DOSE_VALIDATION),
                ("populations", POPULATION_VALIDATION),
                ("limitations", LIMITATION_VALIDATION),
            ]
        )
    )
    return selection.collections


#: Only the pharmacokinetic data.
filter_pk = observable_filter(PK_OBSERVABLES)


def filter_pd(fit_mapping_key: str, fit_mapping: FitMapping) -> bool:
    """Only the pharmacodynamic data."""
    return observable_id(fit_mapping) not in PK_OBSERVABLES


def f_collections_pk() -> dict[str, list[FitMappingCollection]]:
    """Pharmacokinetic data."""
    return mapping_collections([filter_pk])


def f_collections_pd() -> dict[str, list[FitMappingCollection]]:
    """Pharmacodynamic data."""
    return mapping_collections([filter_pd])


if __name__ == "__main__":
    for f in [f_collections_pk, f_collections_pd]:
        console.rule(title=f.__name__, align="left", style="white")
        f()
