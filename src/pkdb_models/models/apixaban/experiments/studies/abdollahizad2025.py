"""Simulation experiment of the study Abdollahizad2025."""

from typing import ClassVar, override

from pkpdsim.metadata import (
    ApplicationForm,
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


class Abdollahizad2025(ApixabanSimulationExperiment):
    """Simulation experiment of Abdollahizad2025.

    The subjects are mostly men (10 women of 24) and run on the male build.
    """

    colors: ClassVar[dict[str, str]] = {
        "TEST5": "black",
        "REF5": "grey",
    }
    groups: ClassVar[list[str]] = list(colors.keys())
    bodyweight = 71.9  # [kg]
    height = 172.4  # [cm]

    legend: ClassVar[dict[str, str]] = {
        "TEST5": "test: 5mg PO",
        "REF5": "ref: 5mg PO",
    }

    markers: ClassVar[dict[str, str]] = {
        "TEST5": "s",
        "REF5": "o",
    }

    infos_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
    }
    infos_pd: ClassVar[dict[str, str]] = {}

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in [
            "Fig3",
        ]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                if label.startswith("apixaban_"):
                    dset.unit_conversion("mean", 1 / self.Mr["api"])
                dsets[label] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims: dict[str, Simulation] = {}
        for group in self.groups:
            tcsims[group] = Simulation(
                time_unit="hr",
                end=50,
                preinit_changes={
                    **self.default_changes(),
                    "PODOSE_api": Q(5, "mg"),
                    "BW": Q(self.bodyweight, "kg"),
                    "HEIGHT": Q(self.height, "cm"),
                },
            )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings: dict[str, FitMapping] = {}
        infos = {
            **self.infos_pk,
            **self.infos_pd,
        }
        for group in self.groups:
            for sid, name in infos.items():
                mappings[f"fm_{name}_{group}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"{name}_{group}",
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=f"task_{group}",
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
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure_pk(),
        }

    def figure_pk(self) -> dict[str, Figure]:
        """Figure of the pharmacokinetics of the test and the reference tablet."""
        fig = Figure(
            experiment=self,
            sid="PK",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        for kp, sid in enumerate(self.infos_pk):
            plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid])

        for group in self.groups:
            for kp, sid in enumerate(self.infos_pk):
                name = self.infos_pk[sid]
                if group == "TEST5":
                    # Simulation
                    plots[kp].add_data(
                        task=f"task_{group}",
                        xid="time",
                        yid=sid,
                        label="sim: 5mg PO",
                        color=self.colors[group],
                    )
                # Data
                plots[kp].add_data(
                    dataset=f"{name}_{group}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp {self.legend[group]}",
                    color=self.colors[group],
                    marker=self.markers[group],
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Abdollahizad2025, output_dir=Abdollahizad2025.__name__)
