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


class Upreti2013(ApixabanSimulationExperiment):
    """Simulation experiment of Upreti2013."""

    bodyweights = {  # [kg]
        "low": 47,
        "reference": 75,
        "high": 137,
    }
    colors = {
        "low": "#0000FF",
        "reference": "black",
        "high": "#FF0000",
    }
    groups = list(bodyweights.keys())

    markers = {
        "low": "*",
        "reference": "o",
        "high": "^",
    }

    info_fig1 = {
        "[Cve_api]": "apixaban",
        "Aurine_api": "cumulative amount",
    }

    info_fig_scatter = {
        "apixaban_vs_antiXa": ["[Cve_api]", "antiXa_activity"],
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Tab2", "Fig1", "Fig4"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            group_by = "x_label" if fig_id == "Fig4" else "label"
            for label, df_label in df.groupby(group_by):
                dset = DataSet.from_df(df_label, self.ureg)
                if "apixaban" or "cumulative amount" in label:
                    if fig_id == "Fig4":
                        dset.unit_conversion("x", 1 / self.Mr.api)
                    else:
                        dset.unit_conversion("mean", 1 / self.Mr.api)
                    dsets[label] = dset
                if fig_id == "Fig1" or "cumulative amount" in label:
                    dsets[label] = dset

        # console.print(dsets)

        return dsets

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims = {}
        for group in self.groups:

            tcsims[group] = TimecourseSim(
                [Timecourse(
                    start=0,
                    end=75 * 60,  # [min]
                    steps=1000,
                    changes={
                        **self.default_changes(),
                        "BW": Q_(self.bodyweights[group], "kg"),
                        "PODOSE_api": Q_(10, "mg"),
                    },
                )]
            )

        return tcsims

    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings = {}
        for group in self.groups:
            # pharmacokinetics

            for k, sid in enumerate(self.info_fig1.keys()):
                name = self.info_fig1[sid]

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
                        tissue=Tissue.URINE if sid == "Aurine_api" else Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
                    ),
                )


        return mappings

    def figures(self) -> Dict[str, Figure]:

        return {
            **self.figure_pk(),
            **self.figure_scatter(),
        }

    def figure_pk(self) -> Dict[str, Figure]:

        fig = Figure(
            experiment=self,
            sid="Fig1",
            name=self.__class__.__name__,
            num_cols=2,
            num_rows=1,
            height=self.panel_height,
            width=self.panel_width * 2,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)
        plots[1].set_yaxis(self.label_api_urine, unit=self.unit_api_urine)

        for group in self.groups:

            for k, sid in enumerate(self.info_fig1.keys()):
                name = self.info_fig1[sid]

                # simulation
                plots[k].add_data(
                    task=f"task_{group}",
                    xid="time",
                    yid=sid,
                    label=f"sim {group}: 10mg PO",
                    color=self.colors[group],
                )
                # data
                plots[k].add_data(
                    dataset=f"{name}_{group}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp {group}: 10mg PO",
                    color=self.colors[group],
                    linestyle="" if sid == "Aurine_api" else "dashed",
                )

        return {fig.sid: fig}

    def figure_scatter(self) -> Dict[str, Figure]:

        fig = Figure(
            experiment=self,
            sid="FigScatter",
            name=self.__class__.__name__,
            num_cols=1,
            num_rows=1,
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            legend=True,
        )

        for label_id, (xid, yid) in self.info_fig_scatter.items():
            plots[0].set_xaxis(self.labels[xid], unit=self.units[xid])
            plots[0].set_yaxis(self.labels[yid], unit=self.units[yid])
        is_legend = True
        for group in self.groups:

            for label_id, (xid, yid) in self.info_fig_scatter.items():

                # simulation
                plots[0].add_data(
                    task=f"task_{group}",
                    xid=xid,
                    yid=yid,
                    label="sim: 10mg PO" if is_legend else "",
                    color=self.colors[group],
                    linestyle="solid"
                )
                is_legend = False
                # data
                plots[0].add_data(
                    dataset=f"{label_id}_{group}",
                    xid="x",
                    yid="y",
                    label=f"exp individ {group}: 10mg PO",
                    linestyle="",
                    marker=self.markers[group],
                    markeredgecolor=self.colors[group],
                    color="white",
                )

        return {fig.sid: fig}


if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / Upreti2013.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Upreti2013, output_dir=Upreti2013.__name__)
