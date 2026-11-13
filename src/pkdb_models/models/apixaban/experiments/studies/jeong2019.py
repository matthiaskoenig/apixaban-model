"""Simulation experiment of the study Jeong2019."""

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


class Jeong2019(ApixabanSimulationExperiment):
    """Simulation experiment of Jeong2019.

    Healthy Korean subjects: a single oral dose of 10 mg apixaban (tablet) in
    period 1 (n=23), in period 2 together with a single dose of rosuvastatin
    20 mg (n=16) or lapatinib 250 mg (n=7); fasting is not reported.

    The sex of the 23 subjects is not reported; they run on the male build.
    """

    colors: ClassVar[dict[str, str]] = {
        "apixaban_API10": "black",
        "apixaban_API10_ROS20": "tab:blue",
        "apixaban_API10_LAP250": "tab:orange",
    }
    group_labels: ClassVar[dict[str, str]] = {
        "apixaban_API10": "10mg PO",
        "apixaban_API10_ROS20": "10mg PO + rosuvastatin",
        "apixaban_API10_LAP250": "10mg PO + lapatinib",
    }
    #: the simulation of a dataset
    simulation_keys: ClassVar[dict[str, str]] = {
        "apixaban_API10": "API10",
        "apixaban_API10_ROS20": "API10",
        "apixaban_API10_LAP250": "API10_LAP250",
    }
    coadministrations: ClassVar[dict[str, Coadministration]] = {
        "apixaban_API10": Coadministration.NONE,
        "apixaban_API10_ROS20": Coadministration.ROSUVASTATIN,
        "apixaban_API10_LAP250": Coadministration.LAPATINIB,
    }
    #: The factors of the interactions are not fitted but set from the
    #: literature; the arms are validation data.
    #: Rosuvastatin is a substrate of OATP1B1 and BCRP and inhibits neither
    #: CYP3A4 nor P-gp: simulated without an interaction (observed Cmax 348 ng/ml
    #: vs 372 ng/ml alone).
    #: Lapatinib inhibits P-gp and BCRP and CYP3A4 weakly; observed Cmax
    #: 529 ng/ml vs 372 ng/ml alone (x1.42, unpaired, n=7, no AUC reported).
    #: The factors give AUC x1.32, Cmax x1.11 for 10 mg with the adopted fits.
    interactions: ClassVar[dict[str, dict[str, float]]] = {
        "API10": {},
        "API10_LAP250": {"LI__f_cyp3a4": 0.8, "GU__f_abcb1": 0.5},
    }

    dataset_labels: ClassVar[list[str]] = list(colors.keys())

    infos_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        df = self.load_dataframe("Fig4")
        for label, df_label in df.groupby("label"):
            label = str(label)
            dset = DataSet.from_df(df_label, self.ureg)
            if label.startswith("apixaban"):
                dset.unit_conversion("mean", 1 / self.Mr["api"])
            dsets[self.to_sid(label)] = dset
        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        return {
            key: Simulation(
                time_unit="hr",
                end=25,
                preinit_changes={
                    **self.default_changes(),
                    "PODOSE_api": Q(10, "mg"),
                    **{
                        pid: Q(value, "dimensionless") for pid, value in changes.items()
                    },
                },
            )
            for key, changes in self.interactions.items()
        }

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for label in self.dataset_labels:
            for sid, name in self.infos_pk.items():
                mappings[self.to_sid(f"fm_{name}_{label}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(label),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=f"task_{self.simulation_keys[label]}",
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.NR,
                        coadministration=self.coadministrations[label],
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
            sid="Fig4",
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
            for label in ["apixaban_API10", "apixaban_API10_LAP250"]:
                plots[ks].add_data(
                    task=f"task_{self.simulation_keys[label]}",
                    xid="time",
                    yid=sid,
                    label=f"sim {self.group_labels[label]}",
                    color=self.colors[label],
                )
            for label in self.dataset_labels:
                plots[ks].add_data(
                    dataset=self.to_sid(label),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp {self.group_labels[label]}",
                    color=self.colors[label],
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Jeong2019, output_dir=Jeong2019.__name__)
