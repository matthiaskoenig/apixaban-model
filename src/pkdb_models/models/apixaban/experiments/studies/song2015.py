import math
from typing import Dict

from sbmlsim.data import DataSet, load_pkdb_dataframe
from sbmlsim.fit import FitMapping, FitData
from sbmlutils.console import console

from pkdb_models.models import apixaban
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)
from pkdb_models.models.apixaban.experiments.metadata import (
    Tissue, Route, Dosing, ApplicationForm, Health, Fasting, ApixabanMappingMetaData
)

from sbmlsim.plot import Axis, Figure
    # noqa: E402
from sbmlsim.simulation import Timecourse, TimecourseSim

from pkdb_models.models.apixaban.helpers import run_experiments


class Song2015(ApixabanSimulationExperiment):
    """Simulation experiment of Song2015."""

    colors_study_1 = {
        "API10_PO_OS": "tab:grey",
        "API10_PO_TAB": "black",
    }
    bodyweight = { # [kg]
        # study_1
        "API10_PO_OS": 78,
        "API10_PO_TAB": 78,
    }
    groups = list(bodyweight.keys())
    bodyheight = { # [m]
        # study_1
        "API10_PO_OS": math.sqrt(78/25.5),
        "API10_PO_TAB": math.sqrt(78/25.5),
    }
    dose = {
        # study_1
        "API10_PO_OS": 10,
        "API10_PO_TAB": 10,
    }
    legends = {
        # study_1
        "API10_PO_OS": "10mg SOL",
        "API10_PO_TAB": "10mg PO",
    }

    infos_pk = {
        "[Cve_api]": "apixaban",
    }


    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id, group_id in zip(["Fig1"],
                                    ["label"]):
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby(group_id):
                dset = DataSet.from_df(df_label, self.ureg)
                if label.startswith("apixaban_"):
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[label] = dset

        # console.print("datasets:", list(dsets.keys()))
        return dsets

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims: Dict[str, TimecourseSim] = {}
        for group in self.groups:
            if group == "API10_PO_OS":
                tcsims[group] = TimecourseSim([
                    Timecourse(
                        start=0,
                        end=75 * 60,  # [min]
                        steps=500,
                        changes={
                            **self.default_changes(),
                            "SOLDOSE_api": Q_(self.dose[group], "mg"),
                            "BW": Q_(self.bodyweight[group], "kg"),
                            "HEIGHT": Q_(self.bodyheight[group], "m"),
                        },
                    )
                ])
            else:
                tcsims[group] = TimecourseSim([
                    Timecourse(
                        start=0,
                        end=75 * 60,  # [min]
                        steps=500,
                        changes={
                            **self.default_changes(),
                            "PODOSE_api": Q_(self.dose[group], "mg"),
                            "BW": Q_(self.bodyweight[group], "kg"),
                            "HEIGHT": Q_(self.bodyheight[group], "m"),
                        },
                    )
                ])
        return tcsims

    # Fit Mappings
    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings: Dict[str, FitMapping] = {}
        infos = {
            **self.infos_pk,
        }
        for sid, name in infos.items():
            for group in self.groups:
                if group not in ["API10_PO_TAB", "API10_PO_OS"]:
                    continue
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
                    metadata=ApixabanMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET if group == "API10_PO_TAB" else ApplicationForm.SOLUTION,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.NR,
                    ),
                )

        return mappings


    def figures(self) -> Dict[str, Figure]:
        return {
            **self.figure_pk(),
        }

    def figure_pk(self) -> Dict[str, Figure]:

        plot_info = {
            0: ("[Cve_api]", ["API10_PO_OS", "API10_PO_TAB"], self.colors_study_1)
        }

        fig = Figure(
            experiment=self,
            sid="PK",
            name=f"{self.__class__.__name__}",
            num_cols=1,
            num_rows=1,
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        for kp, (sid, groups, colors) in plot_info.items():
            plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid])
            for group in groups:
                name = self.infos_pk[sid]
                dose = self.dose[group]
                # Simulation
                if kp == 0 and group in ["API10_PO_TAB", "API10_PO_OS"]:
                    plots[kp].add_data(
                        task=f"task_{group}",
                        xid="time",
                        yid=sid,
                        label=f"sim: {self.legends[group]}",
                        color=colors[group]
                    )
                # Data
                plots[kp].add_data(
                    dataset=f"{name}_{group}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label= f"exp: {self.legends[group]}",
                    color= colors[group],
                    linestyle="solid",
                )

        return {fig.sid: fig}



if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / Song2015.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Song2015, output_dir=Song2015.__name__)

