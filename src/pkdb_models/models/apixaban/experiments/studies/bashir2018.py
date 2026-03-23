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


class Bashir2018(ApixabanSimulationExperiment):
    """Simulation experiment of Bashir2018."""

    colors = {
        "apixaban_API10_A":         "black",
        "apixaban_API10, CYC100":   "tab:blue",
        "apixaban_API10, TAC5":     "tab:orange",
    }
    # markers = {
    #     "apixaban_API10_A":         "s",   # squares
    #     "apixaban_API10, CYC100":   "s",
    #     "apixaban_API10, TAC5":     "s",
    # }
    labels = {
        "apixaban_API10_A":         "api 10mg PO",
        "apixaban_API10, CYC100":   "api 10mg, cyc 100mg PO",
        "apixaban_API10, TAC5":     "api 10mg, tac 5mg PO",
    }

    dataset_labels = list(colors.keys())

    infos_pk = {
        "[Cve_api]": "apixaban",
    }


    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2", "Fig3"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
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
            "apixaban_API10_A":       Coadministration.NONE,
            "apixaban_API10, CYC100": Coadministration.CYCLOSPORINE,
            "apixaban_API10, TAC5":   Coadministration.TACROLIMUS,
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
                    count="count",
                    label=f"exp: {self.labels[label]}",
                    color=self.colors[label],
                    # marker=self.markers[label],
                )

        return {fig.sid: fig}


if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / Bashir2018.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Bashir2018, output_dir=Bashir2018.__name__)