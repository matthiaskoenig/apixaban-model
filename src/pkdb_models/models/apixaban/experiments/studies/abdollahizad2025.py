from typing import Dict

from sbmlsim.data import DataSet, load_pkdb_dataframe
from sbmlsim.fit import FitMapping, FitData
from sbmlutils.console import console

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


class Abdollahizad2025(ApixabanSimulationExperiment):
    """Simulation experiment of Wang2016."""

    colors = {
        "TEST5": "black",
        "REF5": "tab:blue",
    }
    groups = list(colors.keys())
    bodyweight = 71.9  # [kg]

    infos_pk = {
        "[Cve_api]": "apixaban",
    }
    infos_pd = {}

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig3",]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby("label"):
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
            tcsims[group] = TimecourseSim([
                Timecourse(
                    start=0,
                    end=50 * 60,  # [min]
                    steps=500,
                    changes={
                        **self.default_changes(),
                        "PODOSE_api": Q_(5, "mg"),
                        "BW": Q_(self.bodyweight, "kg"),
                    },
                )
            ])
        return tcsims

    # Fit Mappings
    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings: Dict[str, FitMapping] = {}
        infos = {
            **self.infos_pk,
            **self.infos_pd,
        }
        for group in self.groups:
            for sid, name in infos.items():
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
            sid="PK",
            name=f"{self.__class__.__name__}",
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        for kp, sid in enumerate(self.infos_pk):
            plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid])

        for group in self.groups:
            for kp, sid in enumerate(self.infos_pk):
                name = self.infos_pk[sid]

                # Simulation
                plots[kp].add_data(
                    task=f"task_{group}",
                    xid="time",
                    yid=sid,
                    label=group,
                    color=self.colors[group]
                )
                # Data
                plots[kp].add_data(
                    dataset=f"{name}_{group}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=group,
                    color=self.colors[group]
                )

        return {fig.sid: fig}



if __name__ == "__main__":
    run_experiments(Abdollahizad2025, output_dir=Abdollahizad2025.__name__)

