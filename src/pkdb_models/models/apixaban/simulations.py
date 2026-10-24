"""The simulation experiments of the apixaban model and their groups.

They are the registry of `MODEL`, the experiments its commands simulate.
"""

from sbmlsim.experiment import SimulationExperiment

from pkdb_models.models.apixaban import MODEL
from pkdb_models.models.apixaban.experiments.misc import DoseDependencyExperiment
from pkdb_models.models.apixaban.experiments.scans.scan_parameters import (
    ApixabanParameterScan,
)
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

EXPERIMENTS: dict[str, list[type[SimulationExperiment]]] = {
    "studies": [
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
        Lenard2024,  # the apixaban groups of the edoxaban study Lenard2024
        Lenard2025,  # the apixaban groups of the edoxaban study Lenard2025
        Leong2024,
        Metze2021,  # the apixaban groups of the edoxaban study Metze2021
        Mikus2019,  # the apixaban groups of the edoxaban study Mikus2019
        Raghavan2009,
        Rohr2024,  # the apixaban groups of the edoxaban study Rohr2024
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
    "pharmacodynamics": [
        Chang2016,
        Cui2013,
        Frost2013,
        Frost2013a,
        Frost2014,
        Frost2014a,
        Frost2015,
        Frost2018,
        Frost2021,
        Frost2021a,
        Kreutz2017,
        Wang2016,
    ],
    "bodyweight": [
        Upreti2013,
    ],
    "dose_dependency": [
        Frost2013,
        Frost2013a,
        Frost2015b,
        Frost2018,
        Frost2021,
        Song2016,
        Vakkalagadda2016,
    ],
    "food": [
        Kreutz2017,
        Frost2013,
        Song2016,
    ],
    "coadministration": [
        Bashir2018,
        Frost2015a,
        Frost2018,
        Jeong2019,
        Lenard2024,
        Lenard2025,
        Mikus2019,
        Rohr2024,
        Upreti2013a,
    ],
    "hepatic_impairment": [
        Frost2021a,
    ],
    "renal_impairment": [
        Chang2016,
        Metze2021,
        VandenBosch2021,
        Wang2016,
    ],
    "misc": [
        DoseDependencyExperiment,
    ],
    "scans": [
        ApixabanParameterScan,
    ],
}
# the studies which are in none of the groups of special populations
EXPERIMENTS["other"] = [
    experiment
    for experiment in EXPERIMENTS["studies"]
    if experiment
    not in EXPERIMENTS["dose_dependency"]
    + EXPERIMENTS["bodyweight"]
    + EXPERIMENTS["food"]
    + EXPERIMENTS["hepatic_impairment"]
    + EXPERIMENTS["renal_impairment"]
]
EXPERIMENTS["all"] = EXPERIMENTS["studies"] + EXPERIMENTS["misc"] + EXPERIMENTS["scans"]


if __name__ == "__main__":
    MODEL.run_simulation_experiments(EXPERIMENTS["all"], MODEL.simulation_dir / "all")
