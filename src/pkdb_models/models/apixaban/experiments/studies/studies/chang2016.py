from typing import Dict

from sbmlsim.data import DataSet, load_pkdb_dataframe
from sbmlsim.fit import FitMapping, FitData
from sbmlutils.console import console

from pkdb_models.models import apixaban
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)
from pkdb_models.models.apixaban.experiments.metadata import Tissue, Route, Dosing, ApplicationForm, Health, \
    Fasting, ApixabanMappingMetaData

from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Timecourse, TimecourseSim

from pkdb_models.models.apixaban.helpers import run_experiments

class Chang2016(ApixabanSimulationExperiment):
    """Simulation experiment of Chang2016."""

    groups = ["normal", "mild", "moderate", "severe"] #creatinine clearance in [ml/min]
    colors = {
        "normal": "black",
        "mild": "#66c2a4",
        "moderate": "#2ca25f",
        "severe": "#006d2c",
    }
    short_names = {
        "normal": "",
        "mild": "MiRI",
        "moderate": "MoRI",
        "severe": "SRI",
    }
    bodyweights = {
        "normal": 83.3,
        "mild": 79.3,
        "moderate": 74.5,
        "severe": 84.1,
    }
    renal_functions = {
        "normal": 106.7 / 106.7,  # Normalized on NRI
        "mild": 58.8 / 106.7,
        "moderate": 38 / 106.7,
        "severe": 24.5 / 106.7,
    }
    markers = {
        "normal": "s",
        "mild": "*",
        "moderate": "^",
        "severe": "o",
    }

    info_pk = {
        "[Cve_api]": "apixaban",
    }

    info_pd = {
        "INR": "inr",
        "antiXa_activity": "xa",

    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id, group_id in zip(["Fig1", "Fig4"],
                                    ["label", "x_label"]):
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby(group_id):
                dset = DataSet.from_df(df_label, self.ureg)
                if label.startswith("apixaban_"):
                    if fig_id == "Fig4":
                        dset.unit_conversion("x", 1 / self.Mr.api)
                    else:
                        dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[label] = dset

        # console.print(dsets)

        return dsets

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims: Dict[str, TimecourseSim] = {}
        for group in self.groups:

            tcsims[group] = TimecourseSim(
                [Timecourse(
                    start=0,
                    end=100 * 60,  # [min]
                    steps=1000,
                    changes={
                        **self.default_changes(),
                        "BW": Q_(self.bodyweights[group], "kg"),
                        "KI__f_renal_function": Q_(self.renal_functions[group], "dimensionless"),
                        "PODOSE_api": Q_(10, "mg"),
                    },
                )]
            )

        return tcsims

    #Fit Mappings
    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings: Dict[str, FitMapping] = {}

        for group in self.groups:
            for sid, name in self.info_pk.items():
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
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY if group == "normal" else Health.RENAL_IMPAIRMENT,
                        fasting=Fasting.FASTED,
                    ),
                )

        return mappings

    def figures(self) -> Dict[str, Figure]:
        return {
            **self.figure_pk(),
            **self.figure_scatter_xa(),
            **self.figure_scatter_inr(),
        }

    def figure_pk(self) -> Dict[str, Figure]:
        fig = Figure(
            experiment=self,
            #sid="Fig1",
            #name=self.__class__.__name__
            sid = "PK",
            name = f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )

        for kp, sid in enumerate(self.info_pk):
            plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid])

        for group in self.groups:
            for kp, sid in enumerate(self.info_pk):
                name = self.info_pk[sid]

                # simulation
                plots[kp].add_data(
                    task=f"task_{group}",
                    xid="time",
                    yid=sid,
                    label="sim: 10mg PO" if group == "normal" else f"sim {self.short_names[group]}: 10mg PO",
                    color=self.colors[group],
                )
                # data
                plots[kp].add_data(
                    dataset=f"{name}_{group}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label="exp: 10mg PO" if group == "normal" else f"exp {self.short_names[group]}: 10mg PO",
                    color=self.colors[group],
                )

        return {fig.sid: fig}


    #scatterplot for api vs xa
    def figure_scatter_xa(self) -> Dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="PD_scatter_xa",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.labels["[Cve_api]"], unit=self.units["[Cve_api]"]),
            legend=True,
        )
        plots[0].set_yaxis(
            self.labels["antiXa_activity"],
            unit=self.units["antiXa_activity"],
            scale="linear",
        )
        is_legend = True
        for group in self.groups:
            plots[0].add_data(
                task=f"task_{group}",
                xid="[Cve_api]",
                yid="antiXa_activity",
                label="sim: 10mg PO" if is_legend else "",
                color="black"
            )
            is_legend = False
            plots[0].add_data(
                dataset=f"apixaban_vs_xa_{group}",
                xid="x",
                yid="y",
                label=f"exp individ {self.short_names[group]}: 10mg PO" if group != "normal" else "exp individ: 10mg PO",
                linestyle="",
                color="white",
                marker=self.markers[group],
                markeredgecolor=self.colors[group],
            )

        return {fig.sid: fig}

    #scatterplot apixaban vs inr
    def figure_scatter_inr(self) -> Dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="PD_scatter_inr",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.labels["[Cve_api]"], unit=self.units["[Cve_api]"]),
            legend=True,
        )
        plots[0].set_yaxis(
            self.labels["INR"],
            unit=self.units["INR"],
            scale="linear",
        )
        is_legend = True
        for group in self.groups:
            plots[0].add_data(
                task=f"task_{group}",
                xid="[Cve_api]",
                yid="INR",
                label="sim: 10mg PO" if is_legend else "",
                color="black",
            )
            is_legend = False
            plots[0].add_data(
                dataset=f"apixaban_vs_INR_{group}",
                xid="x",
                yid="y",
                label=f"exp individ {self.short_names[group]}: 10mg PO" if group != "normal" else "exp individ: 10mg PO",
                linestyle="",
                color="white",
                marker=self.markers[group],
                markeredgecolor=self.colors[group],
            )

        return {fig.sid: fig}



if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / Chang2016.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Chang2016, output_dir=Chang2016.__name__)