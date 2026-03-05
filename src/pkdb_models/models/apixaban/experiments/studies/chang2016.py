from typing import Dict

from sbmlsim.data import DataSet, load_pkdb_dataframe
from sbmlsim.fit import FitMapping, FitData
from sbmlutils.console import console

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

    info_fig1 = {
        "[Cve_api]": "apixaban",
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby("label"):
                dset = DataSet.from_df(df_label, self.ureg)
                if "apixaban" in label:
                    dset.unit_conversion("mean", 1 / self.Mr.api)
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
        }

    def figure_pk(self) -> Dict[str, Figure]:

        fig = Figure(
            experiment=self,
            sid="Fig1",
            name=self.__class__.__name__
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)

        for group in self.groups:

            for k, sid in enumerate(self.info_fig1.keys()):
                name = self.info_fig1[sid]

                # simulation
                plots[k].add_data(
                    task=f"task_{group}",
                    xid="time",
                    yid=sid,
                    label=group,
                    color=self.colors[group],
                )
                # data
                plots[k].add_data(
                    dataset=f"{name}_{group}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=group,
                    color=self.colors[group],
                )

        return {fig.sid: fig}


if __name__ == "__main__":
    run_experiments(Chang2016, output_dir=Chang2016.__name__)
