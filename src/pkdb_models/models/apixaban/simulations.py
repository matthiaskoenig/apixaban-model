"""Run all simulation experiments."""
import shutil
from pathlib import Path

from pymetadata.console import console

from pkdb_models.models.apixaban.experiments.scans.scan_parameters import ApixabanParameterScan
from pkdb_models.models.apixaban.helpers import run_experiments
from pkdb_models.models.apixaban.experiments.studies import *
from pkdb_models.models.apixaban.experiments.misc import *
from sbmlutils import log
from sbmlsim.plot import Figure
from pkdb_models.models import apixaban

Figure.legend_fontsize = 8
Figure.fig_dpi = 300
logger = log.get_logger(__name__)

EXPERIMENTS= {
    "studies": [
        Abdollahizad2025,
        Chang2016,
        Frost2013,  # FIXME fed group
        Frost2013a, # FIXME scatter plot, multiple dosing
        Frost2014,
        Frost2015,
        Frost2015b,
        Frost2018,
        Frost2021,
        Frost2021a,
        Kreutz2017,
        Lenard2024,
        Lenard2025,
        Metze2021,
        Mikus2019,
        Rohr2024,
        Upreti2013,
        VandenBosch2021,
        Wang2016,
    ],
    "pharmacodynamics": [
        Kreutz2017,
        Frost2021,
    ],
    "bodyweight": [
    ],
    "dose_dependency": [
        Frost2013,
        Frost2015b,
        Frost2018,
        Frost2021,
        VandenBosch2021,
    ],
    "food": [
        Kreutz2017,
        Frost2013,
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
        DoseDependencyExperiment
    ],
    "scan": [
        ApixabanParameterScan
    ]

}
EXPERIMENTS["all"] = EXPERIMENTS["studies"] + EXPERIMENTS["misc"] + EXPERIMENTS["scan"]


def run_simulation_experiments(
    selected: str = None,
    experiment_classes: list = None,
    output_dir: Path = None
) -> None:
    """Run apixaban simulation experiments."""

    Figure.fig_dpi = 300
    Figure.legend_fontsize = 10

    # Determine which experiments to run
    if experiment_classes is not None:
        experiments_to_run = experiment_classes
        if output_dir is None:
            output_dir = apixaban.RESULTS_PATH_SIMULATION / "custom_selection"
    elif selected:
        # Using the 'selected' parameter
        if selected not in EXPERIMENTS:
            console.rule(style="red bold")
            console.print(
                f"[red]Error: Unknown group '{selected}'. Valid groups: {', '.join(EXPERIMENTS.keys())}[/red]"
            )
            console.rule(style="red bold")
            return
        experiments_to_run = EXPERIMENTS[selected]
        if output_dir is None:
            output_dir = apixaban.RESULTS_PATH_SIMULATION / selected
    else:
        console.print("\n[red bold]Error: No experiments specified![/red bold]")
        console.print("[yellow]Use selected='all' or selected='studies' or provide experiment_classes=[...][/yellow]\n")
        return

    # Run the experiments
    run_experiments(experiment_classes=experiments_to_run, output_dir=output_dir)

    # Collect figures into one folder
    figures_dir = output_dir / "_figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    for f in output_dir.glob("**/*.png"):
        if f.parent == figures_dir:
            continue
        try:
            shutil.copy2(f, figures_dir / f.name)
        except Exception as err:
            print(f"file {f.name} in {f.parent} fails, skipping. Error: {err}")
    console.print(f"Figures copied to: file://{figures_dir}", style="info")


if __name__ == "__main__":
    """Run experiments."""

    run_simulation_experiments(selected="studies")