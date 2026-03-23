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


class Frost2015a(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2015a."""

    colors = {
        "apixaban_API10_D1_A":       "black",
        "apixaban_API10_D7, KET400": "tab:blue",
        "apixaban_API10_D1_B":       "black",
        "apixaban_API10_D11, DIL360": "tab:orange",
    }
    markers = {
        "apixaban_API10_D1_A":        "s",
        "apixaban_API10_D7, KET400":  "s",
        "apixaban_API10_D1_B":        "D",
        "apixaban_API10_D11, DIL360": "s",
    }
    labels = {
        "apixaban_API10_D1_A":        "api 10mg PO",
        "apixaban_API10_D7, KET400":  "api 10mg, ket 400 mg PO",
        # "apixaban_API10_D1_B":        "API10 D1 (B)", # probably equal to D1_A
        "apixaban_API10_D11, DIL360": "api 10mg, dil 360 mg PO",
    }

    dataset_labels = list(labels.keys())

    infos_pk = {
        "[Cve_api]": "apixaban",
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        df = load_pkdb_dataframe(f"{self.sid}_Fig2", data_path=self.data_path)
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
                        end=75 * 60,  # 72 h in [min]
                        steps=500,
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
        coadmin_map = {
            "apixaban_API10_D1_A":        Coadministration.NONE,
            "apixaban_API10_D7, KET400":  Coadministration.KETOCONAZOLE,
            "apixaban_API10_D1_B":        Coadministration.NONE,
            "apixaban_API10_D11, DIL360": Coadministration.DILTIAZEM,
        }
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
                        fasting=Fasting.NR,
                        coadministration=coadmin_map[label],
                    ),
                )
        return mappings

    def figures(self) -> Dict[str, Figure]:
        return {**self.figure_pk()}

    def figure_pk(self) -> Dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="Fig1",
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
                    label=f"exp: {self.labels[label]}",
                    color=self.colors[label],
                    marker=self.markers[label],
                )

        return {fig.sid: fig}


if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / Frost2015a.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Frost2015a, output_dir=Frost2015a.__name__)