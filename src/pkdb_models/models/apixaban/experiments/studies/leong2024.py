"""Simulation experiment of the study Leong2024."""

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


class Leong2024(ApixabanSimulationExperiment):
    """Simulation experiment of Leong2024.

    Bioequivalence study of a 5 mg apixaban tablet (test) and Eliquis 5 mg
    (reference) in 26 healthy Indonesian volunteers (60.7 kg, 161 cm) after an
    8 h overnight fast; plasma by LC-MS/MS (LLOQ 1 ng/ml).

    The volunteers are mostly men (12 women of 26) and run on the male build.
    """

    colors: ClassVar[dict[str, str]] = {
        "TEST": "black",
        "REF": "grey",
    }
    groups: ClassVar[list[str]] = list(colors.keys())
    #: body weight [kg] and height [cm] (Table S1)
    bodyweight = 60.7
    height = 161
    #: lower limit of quantification [ng/ml]; the mean values at 72 h are below
    lloq = 1.0

    infos_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
    }
    legend: ClassVar[dict[str, str]] = {
        "TEST": "test: 5mg PO",
        "REF": "ref: 5mg PO",
    }
    markers: ClassVar[dict[str, str]] = {
        "TEST": "s",
        "REF": "o",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1"]:
            df = self.load_dataframe(fig_id)
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
        tcsims: dict[str, Simulation] = {}
        for group in self.groups:
            tcsims[group] = Simulation(
                time_unit="hr",
                end=80,
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
        mappings = {}
        # PK
        for sid, name in self.infos_pk.items():
            for group in self.groups:
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
        """Figure of the pharmacokinetics."""
        fig = Figure(
            experiment=self,
            sid="Fig1",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)
        for ks, (sid, name) in enumerate(self.infos_pk.items()):
            for group in self.groups:
                # simulation
                if group == "TEST":
                    plots[ks].add_data(
                        task=f"task_{group}",
                        xid="time",
                        yid=sid,
                        label="sim 5mg PO",
                        color=self.colors[group],
                    )
                # data
                plots[ks].add_data(
                    dataset=f"{name}_{group}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=self.legend[group],
                    color=self.colors[group],
                    marker=self.markers[group],
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Leong2024, output_dir=Leong2024.__name__)
