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


class Upreti2013(ApixabanSimulationExperiment):
    """Simulation experiment of Upreti2013."""

    bodyweights = {  # [kg]
        "low": 47,
        "reference": 75,
        "high": 137,
    }
    colors = {
        "low": "tab:blue",
        "reference": "tab:orange",
        "high": "tab:green",
    }
    groups = list(bodyweights.keys())

    info_fig1 = {
        "[Cve_api]": "apixaban",
        "Aurine_api": "cumulative amount",
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1", "Tab2"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby("label"):
                dset = DataSet.from_df(df_label, self.ureg)
                if "apixaban" or "cumulative amount" in label:
                    dset.unit_conversion("mean", 1 / self.Mr.api)
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
        }

    def figure_pk(self) -> Dict[str, Figure]:

        fig = Figure(
            experiment=self,
            sid="Fig1",
            name=self.__class__.__name__,
            num_cols=2,
            num_rows=1,
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
    run_experiments(Upreti2013, output_dir=Upreti2013.__name__)
