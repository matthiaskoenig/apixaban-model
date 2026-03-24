from typing import Dict

from sbmlsim.data import DataSet, load_pkdb_dataframe
from sbmlsim.fit import FitMapping, FitData
from sbmlutils.console import console

from pkdb_models.models import apixaban
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)
from pkdb_models.models.apixaban.experiments.metadata import (
    Tissue,
    Route,
    Dosing,
    ApplicationForm,
    Health,
    Fasting,
    ApixabanMappingMetaData,
    Coadministration,
)
from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Timecourse, TimecourseSim

from pkdb_models.models.apixaban.helpers import run_experiments



class Upreti2013a(ApixabanSimulationExperiment):
    """Simulation experiment of Upreti2013a"""

    dose = 10.0
    bodyweight = 73.7

    colors = {
        "apixaban_API10": "black",  # 10mg apixaban
        "apixaban_API10, FAMO40": "tab:red",  # 10mg apixaban after 40mg famotidine
    }
    interventions = list(colors.keys())

    infos_pk = {
        "[Cve_api]": "apixaban",
    }

    labels = {
        "apixaban_API10": "exp: api 10mg PO",
        "apixaban_API10, FAMO40": "exp: api 10mg, 40mg famo PO",
    }
    dataset_labels = list(colors.keys())


    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        df = load_pkdb_dataframe(f"{self.sid}_Fig1", data_path=self.data_path)
        for label, df_label in df.groupby("label"):
            dset = DataSet.from_df(df_label, self.ureg)
            if label.startswith("apixaban"):
                dset.unit_conversion("mean", 1 / self.Mr.api)
            dsets[label] = dset
        return dsets

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        return {
            "API10": TimecourseSim(
                [
                    Timecourse(
                        start=0,
                        end=72 * 60,  # 72 h in [min]
                        steps=1000,
                        changes={
                            **self.default_changes(),
                            "PODOSE_api": Q_(10, "mg"),
                        },
                    )
                ]
            )
        }

    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings = {}

        for label in self.dataset_labels:
            for sid, name in self.infos_pk.items():
                mappings[f"fm_{name}_{label}"] = FitMapping(
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
                        task="task_API10",
                        xid="time",
                        yid=sid,
                    ),
                    metadata=ApixabanMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
                        coadministration=Coadministration.FAMOTIDINE if "FAM" in label else Coadministration.NONE,
                    ),
                )
        return mappings

    def figures(self) -> Dict[str, Figure]:
        return {**self.figure_pk()}

    def figure_pk(self) -> Dict[str, Figure]:
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
                    dataset=label,
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=self.labels[label],
                    color=self.colors[label],
                )

        return {fig.sid: fig}

if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / Upreti2013a.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Upreti2013a, output_dir=Upreti2013a.__name__)