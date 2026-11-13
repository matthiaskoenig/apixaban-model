"""Simulation experiment of the study Shaikh2021."""

from typing import ClassVar, override

from pkpdsim.metadata import (
    ApplicationForm,
    Coadministration,
    DataType,
    Dosing,
    Fasting,
    Health,
    PKPDData,
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


class Shaikh2021(ApixabanSimulationExperiment):
    """Simulation experiment of Shaikh2021.

    Bioequivalence study of a 5 mg apixaban tablet (test) and Eliquis 5 mg
    (reference) in 23 healthy Indian males after an overnight fast of at least
    10 h; plasma by LC-MS/MS (LLOQ 1.01 ng/ml). The error bars of Fig 5 have a
    constant length at every time point, they are no SDs and are not used.

    The subjects are men (23) and run on the male build.
    """

    colors: ClassVar[dict[str, str]] = {
        "apixaban_API5_R": "black",
        "apixaban_API5_T": "grey",
    }
    legend_labels: ClassVar[dict[str, str]] = {
        "apixaban_API5_T": "test: 5mg PO",
        "apixaban_API5_R": "ref: 5mg PO",
    }
    markers: ClassVar[dict[str, str]] = {
        "apixaban_API5_T": "s",
        "apixaban_API5_R": "o",
    }

    dataset_labels: ClassVar[list[str]] = list(colors.keys())
    #: lower limit of quantification [ng/ml]; the mean values at 48 h are below
    lloq = 1.01

    infos_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        df = self.load_dataframe("Fig5")
        # means below the limit of quantification are not used
        df = df[(df["time"] == 0) | (df["mean"] >= self.lloq)]
        for label, df_label in df.groupby("label"):
            label = str(label)
            dset = DataSet.from_df(df_label, self.ureg)
            if label.startswith("apixaban"):
                dset.unit_conversion("mean", 1 / self.Mr["api"])
            dsets[label] = dset
        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        return {
            "API5": Simulation(
                time_unit="hr",
                end=51,
                preinit_changes={
                    **self.default_changes(),
                    "PODOSE_api": Q(5, "mg"),
                },
            )
        }

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for label in self.dataset_labels:
            for sid in self.infos_pk:
                mappings[f"fm_{label}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=label,
                        xid="time",
                        yid="mean",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task="task_API5",
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
                        coadministration=Coadministration.NONE,
                        data=PKPDData.PK,
                        data_type=DataType.MEAN,
                    ),
                )
        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {**self.figure_pk()}

    def figure_pk(self) -> dict[str, Figure]:
        """Apixaban in plasma after the test and the reference tablet."""
        fig = Figure(
            experiment=self,
            sid="Fig5",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)

        for ks, sid in enumerate(self.infos_pk):
            # single reference simulation
            plots[ks].add_data(
                task="task_API5",
                xid="time",
                yid=sid,
                label="sim 5mg PO",
                color="black",
            )
            # data points
            for label in self.dataset_labels:
                plots[ks].add_data(
                    dataset=label,
                    xid="time",
                    yid="mean",
                    count="count",
                    label=self.legend_labels[label],
                    color=self.colors[label],
                    marker=self.markers[label],
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Shaikh2021, output_dir=Shaikh2021.__name__)
