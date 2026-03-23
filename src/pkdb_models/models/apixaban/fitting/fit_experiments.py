"""Parameter fit problems"""
from typing import Dict, List

from sbmlsim.fit.helpers import f_fitexp, filter_empty
from sbmlutils.console import console
from sbmlutils.log import get_logger

from sbmlsim.fit import FitExperiment, FitMapping

from pkdb_models.models.apixaban import APIXABAN_PATH, DATA_PATHS
from pkdb_models.models.apixaban.experiments.metadata import (
    Tissue, Route, Dosing, ApplicationForm, Health,
    Fasting, ApixabanMappingMetaData, Coadministration
)
from pkdb_models.models.apixaban.experiments.studies import *


logger = get_logger(__name__)


# --- Filters ---
def filter_baseline(fit_mapping_key: str, fit_mapping: FitMapping) -> bool:
    """Return baseline experiments/mappings for reference model."""

    metadata: ApixabanMappingMetaData = fit_mapping.metadata

    # only PO and IV (no SL, MU, RE)
    if metadata.route not in {Route.PO, Route.IV}:
        return False

    # filter coadminstration
    if metadata.coadministration != Coadministration.NONE:
        return False

    # filter health (no renal, cardiac impairment, ...)
    if metadata.health not in {Health.HEALTHY}:
        return False

    # filter multiple dosing (only single dosing)
    # if metadata.dosing == Dosing.MULTIPLE:
    #     return False

    # # only fasted subjects
    # if metadata.fasting not in {Fasting.FASTED, Fasting.NR}:
    #     return False

    # remove outliers
    if metadata.outlier is True:
        return False

    return True


# --- Fit experiments ---
f_fitexp_kwargs = dict(
    experiment_classes  = [
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
        Raghavan2009, # FIXME: not tablet, but solution
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
    ],
    base_path=APIXABAN_PATH,
    data_path=DATA_PATHS,
)
# --- Experiment classes ---

def filter_pharmacokinetics(fit_mapping_key: str, fit_mapping: FitMapping) -> bool:
    """Only pharmacokinetic data."""
    yid = "__".join(fit_mapping.observable.y.sid.split("__")[1:])
    if yid not in {
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
    }:
        return False
    return True

def filter_pharmacodynamics(fit_mapping_key: str, fit_mapping: FitMapping) -> bool:
    """Only pharmacodynamics data."""
    yid = "__".join(fit_mapping.observable.y.sid.split("__")[1:])
    if yid not in {
        "INR",
        "INR_change",
        "INR_ratio",
        "INR_relchange",

        "mPT",
        "mPT_change",
        "mPT_ratio",
        "mPT_relchange",

        "PT",
        "PT_change",
        "PT_ratio",
        "PT_relchange",

        "aPTT",
        "aPTT_change",
        "aPTT_ratio",
        "aPTT_relchange",

        "Xa_inhibition",
        "antiXa_activity",
        "antiXa_activity_gram",
    }:
        return False

    return True

def filter_inr(fit_mapping_key: str, fit_mapping: FitMapping) -> bool:
    """Only INR data."""
    yid = "__".join(fit_mapping.observable.y.sid.split("__")[1:])
    if yid not in {
        "INR",
        "INR_change",
        "INR_ratio",
        "INR_relchange",
    }:
        return False

    return True

def filter_mpt(fit_mapping_key: str, fit_mapping: FitMapping) -> bool:
    """Only mPT data."""
    yid = "__".join(fit_mapping.observable.y.sid.split("__")[1:])
    if yid not in {
        "mPT",
        "mPT_change",
        "mPT_ratio",
        "mPT_relchange",
    }:
        return False

    return True

def filter_aptt(fit_mapping_key: str, fit_mapping: FitMapping) -> bool:
    """Only aptt data."""
    yid = "__".join(fit_mapping.observable.y.sid.split("__")[1:])
    if yid not in {
        "aPTT",
        "aPTT_change",
        "aPTT_ratio",
        "aPTT_relchange",
    }:
        return False

    return True

def filter_xa(fit_mapping_key: str, fit_mapping: FitMapping) -> bool:
    """Only xa data."""
    yid = "__".join(fit_mapping.observable.y.sid.split("__")[1:])
    if yid not in {
        "Xa_inhibition",
        "antiXa_activity",
        "antiXa_activity_gram",
    }:
        return False

    return True

def f_fitexp_all():
    """All data."""
    return f_fitexp(metadata_filters=filter_empty, **f_fitexp_kwargs)

def f_fitexp_control() -> Dict[str, List[FitExperiment]]:
    """Control data."""
    return f_fitexp(metadata_filters=[filter_baseline], **f_fitexp_kwargs)

def f_fitexp_pharmacokinetics() -> Dict[str, List[FitExperiment]]:
    """Pharmacodynamics data."""
    return f_fitexp(metadata_filters=[filter_baseline, filter_pharmacokinetics], **f_fitexp_kwargs)

def f_fitexp_pharmacodynamics() -> Dict[str, List[FitExperiment]]:
    """Pharmacodynamics data."""
    return f_fitexp(metadata_filters=[filter_baseline, filter_pharmacodynamics], **f_fitexp_kwargs)

def f_fitexp_inr() -> Dict[str, List[FitExperiment]]:
    """Pharmacodynamics data."""
    return f_fitexp(metadata_filters=[filter_baseline, filter_inr], **f_fitexp_kwargs)

def f_fitexp_mpt() -> Dict[str, List[FitExperiment]]:
    """Pharmacodynamics data."""
    return f_fitexp(metadata_filters=[filter_baseline, filter_mpt], **f_fitexp_kwargs)

def f_fitexp_aptt() -> Dict[str, List[FitExperiment]]:
    """Pharmacodynamics data."""
    return f_fitexp(metadata_filters=[filter_baseline, filter_aptt], **f_fitexp_kwargs)

def f_fitexp_xa() -> Dict[str, List[FitExperiment]]:
    """Pharmacodynamics data."""
    return f_fitexp(metadata_filters=[filter_baseline, filter_xa], **f_fitexp_kwargs)

if __name__ == "__main__":
    """Test construction of FitExperiments."""

    for f in [
        f_fitexp_all,
        # f_fitexp_control,
        # f_fitexp_pharmacokinetics,
        # f_fitexp_pharmacodynamics,
        f_fitexp_inr,
        f_fitexp_mpt,
        f_fitexp_aptt,
        f_fitexp_xa,
    ]:
        console.rule(style="white")
        console.print(f"{f.__name__}")
        fitexp = f()
