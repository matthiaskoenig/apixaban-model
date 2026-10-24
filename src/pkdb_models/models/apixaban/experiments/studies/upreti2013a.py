"""Simulation experiment of the study Upreti2013a."""

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


class Upreti2013a(ApixabanSimulationExperiment):
    """Simulation experiment of Upreti2013a.

    A single oral dose of 10 mg apixaban (two 5 mg tablets) after an 8 hour fast
    in 18 healthy subjects (73.7 kg, 172.7 cm), alone or 3 h after 40 mg
    famotidine. Famotidine does not interact with apixaban (AUCinf ratio 1.007,
    no effect on CYP3A4 or P-gp, the solubility of apixaban does not depend on
    the gastric pH): both arms are the same simulation, the famotidine arm is
    tagged by its coadministration.
    """

    dose = 10.0  # [mg]
    bodyweight = 73.7  # [kg]
    bodyheight = 172.7  # [cm]

    colors: ClassVar[dict[str, str]] = {
        "apixaban_API10": "black",  # 10mg apixaban
        "apixaban_API10, FAMO40": "tab:red",  # 10mg apixaban after 40mg famotidine
    }
    interventions: ClassVar[list[str]] = list(colors.keys())

    infos_pk: ClassVar[dict[str, str]] = {
        "[Cve_api]": "apixaban",
    }

    legend_labels: ClassVar[dict[str, str]] = {
        "apixaban_API10": "exp: api 10mg PO",
        "apixaban_API10, FAMO40": "exp: api 10mg, 40mg famo PO",
    }
    dataset_labels: ClassVar[list[str]] = list(colors.keys())

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        df = self.load_dataframe("Fig1")
        for label, df_label in df.groupby("label"):
            label = str(label)
            dset = DataSet.from_df(df_label, self.ureg)
            if label.startswith("apixaban"):
                dset.unit_conversion("mean", 1 / self.Mr.api)
            dsets[self.to_sid(label)] = dset
        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        return {
            "API10": Simulation(
                time_unit="hr",
                end=72,
                preinit_changes={
                    **self.default_changes(),
                    "PODOSE_api": Q(self.dose, "mg"),
                    "BW": Q(self.bodyweight, "kg"),
                    "HEIGHT": Q(self.bodyheight, "cm"),
                },
            )
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
                        task="task_API10",
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
                        coadministration=Coadministration.FAMOTIDINE
                        if "FAM" in label
                        else Coadministration.NONE,
                    ),
                )
        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {**self.figure_pk()}

    def figure_pk(self) -> dict[str, Figure]:
        """Apixaban in plasma without and with famotidine."""
        fig = Figure(
            experiment=self,
            sid="Fig2",
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
                task="task_API10",
                xid="time",
                yid=sid,
                label="sim: api 10mg PO",
                color="black",
            )
            # data points
            for label in self.dataset_labels:
                plots[ks].add_data(
                    dataset=self.to_sid(label),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=self.legend_labels[label],
                    color=self.colors[label],
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Upreti2013a, output_dir=Upreti2013a.__name__)
