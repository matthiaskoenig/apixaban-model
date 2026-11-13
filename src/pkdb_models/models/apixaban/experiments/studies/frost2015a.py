"""Simulation experiment of the study Frost2015a."""

import math
from typing import ClassVar, override

from pkpdsim.metadata import (
    ApplicationForm,
    Coadministration,
    Dosing,
    Fasting,
    Health,
    PKPDMappingMetaData,
    Route,
    Tissue,
)
from sbmlsim import Q
from sbmlsim.data import DataSet
from sbmlsim.fit import FitData, FitMapping
from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Simulation

from pkdb_models.models.apixaban import MODEL
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)


class Frost2015a(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2015a.

    Two crossover studies of the interactions with ketoconazole and diltiazem
    in healthy subjects: a single oral dose of 10 mg apixaban (tablet) alone and
    at the steady state of ketoconazole 400 mg QD (study 1) or diltiazem 360 mg
    QD (study 2), fasted from 10 h before until 4 h after the dose.

    The subjects are mostly men (study 1: 20 men; study 2: 13 men of 18) and
    run on the male build.
    """

    #: the groups of the data (Fig 2): the reference and the interaction arms
    groups: ClassVar[list[str]] = [
        "apixaban_API10_D1_A",
        "apixaban_API10_D7_KET400",
        "apixaban_API10_D1_B",
        "apixaban_API10_D11_DIL360",
    ]
    colors: ClassVar[dict[str, str]] = {
        "apixaban_API10_D1_A": "black",
        "apixaban_API10_D7_KET400": "tab:blue",
        "apixaban_API10_D1_B": "black",
        "apixaban_API10_D11_DIL360": "tab:orange",
    }
    markers: ClassVar[dict[str, str]] = {
        "apixaban_API10_D1_A": "s",
        "apixaban_API10_D7_KET400": "s",
        "apixaban_API10_D1_B": "D",
        "apixaban_API10_D11_DIL360": "D",
    }
    group_labels: ClassVar[dict[str, str]] = {
        "apixaban_API10_D1_A": "10mg PO",
        "apixaban_API10_D7_KET400": "10mg PO + ketoconazole",
        "apixaban_API10_D1_B": "10mg PO",
        "apixaban_API10_D11_DIL360": "10mg PO + diltiazem",
    }
    #: body weight [kg] and BMI [kg/m^2] of the two studies (Table 1)
    bodyweight: ClassVar[dict[str, float]] = {
        "apixaban_API10_D1_A": 79,
        "apixaban_API10_D7_KET400": 79,
        "apixaban_API10_D1_B": 78,
        "apixaban_API10_D11_DIL360": 78,
    }
    bmi: ClassVar[dict[str, float]] = {
        "apixaban_API10_D1_A": 25,
        "apixaban_API10_D7_KET400": 25,
        "apixaban_API10_D1_B": 26,
        "apixaban_API10_D11_DIL360": 26,
    }
    coadministrations: ClassVar[dict[str, Coadministration]] = {
        "apixaban_API10_D1_A": Coadministration.NONE,
        "apixaban_API10_D7_KET400": Coadministration.KETOCONAZOLE,
        "apixaban_API10_D1_B": Coadministration.NONE,
        "apixaban_API10_D11_DIL360": Coadministration.DILTIAZEM,
    }
    #: The factors of the interactions are not fitted but set from the
    #: literature; the arms are validation data.
    #: Ketoconazole 400 mg QD inhibits CYP3A4 strongly and P-gp; observed
    #: geometric mean ratios AUCinf 1.99, Cmax 1.62 with an unchanged half-life,
    #: i.e. mostly a higher bioavailability. The factors give AUC x2.05, Cmax
    #: x1.25 for 10 mg with the adopted fits.
    #: Diltiazem 360 mg QD inhibits CYP3A4 moderately and P-gp weakly; observed
    #: AUCinf 1.40, Cmax 1.31. The factors give AUC x1.36, Cmax x1.11.
    interactions: ClassVar[dict[str, dict[str, float]]] = {
        "apixaban_API10_D1_A": {},
        "apixaban_API10_D7_KET400": {"LI__f_cyp3a4": 0.3, "GU__f_abcb1": 0.3},
        "apixaban_API10_D1_B": {},
        "apixaban_API10_D11_DIL360": {"LI__f_cyp3a4": 0.6, "GU__f_abcb1": 0.7},
    }

    infos_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        df = self.load_dataframe("Fig2")
        for label, df_label in df.groupby("label"):
            label = str(label)
            dset = DataSet.from_df(df_label, self.ureg)
            if label.startswith("apixaban"):
                dset.unit_conversion("mean", 1 / self.Mr["api"])
            dsets[self.to_sid(label)] = dset
        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims: dict[str, Simulation] = {}
        for group in self.groups:
            height = 100 * math.sqrt(self.bodyweight[group] / self.bmi[group])
            tcsims[self.to_sid(f"{group}_sim")] = Simulation(
                time_unit="hr",
                end=75,
                preinit_changes={
                    **self.default_changes(),
                    "PODOSE_api": Q(10, "mg"),
                    "BW": Q(self.bodyweight[group], "kg"),
                    "HEIGHT": Q(height, "cm"),
                    **{
                        pid: Q(value, "dimensionless")
                        for pid, value in self.interactions[group].items()
                    },
                },
            )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for group in self.groups:
            for sid, name in self.infos_pk.items():
                mappings[self.to_sid(f"fm_{name}_{group}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(group),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_{group}_sim"),
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
                        coadministration=self.coadministrations[group],
                    ),
                )
        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {**self.figure_pk()}

    def figure_pk(self) -> dict[str, Figure]:
        """Figure of the pharmacokinetics with and without the inhibitor."""
        fig = Figure(
            experiment=self,
            sid="Fig2",
            num_cols=2,
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=2 * self.panel_width,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            yaxis=Axis(self.label_api_plasma, unit=self.unit_api),
            legend=True,
        )
        plots[0].set_title("ketoconazole")
        plots[1].set_title("diltiazem")

        for sid in self.infos_pk:
            for group in self.groups:
                plot = plots[0 if group.endswith(("_A", "KET400")) else 1]
                plot.add_data(
                    task=self.to_sid(f"task_{group}_sim"),
                    xid="time",
                    yid=sid,
                    label=f"sim {self.group_labels[group]}",
                    color=self.colors[group],
                )
                plot.add_data(
                    dataset=self.to_sid(group),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp {self.group_labels[group]}",
                    color=self.colors[group],
                    marker=self.markers[group],
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Frost2015a, output_dir=Frost2015a.__name__)
