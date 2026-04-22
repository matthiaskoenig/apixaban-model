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


class Frost2015b(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2015b."""

    bodyweight = 76.6 #kg

    colors = {
        "PO10": "#e95e0d",
        "PO50": "#7f2704"
    }

    interventions = list(colors.keys())

    doses = {
        "PO10": 10, #mg
        "PO50": 50
    }

    infos_pk = {
        "[Cve_api]": "apixaban",
        "[Cve_m1]": "apixaban-M1"
    }


    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig3"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby("label"):
                dset = DataSet.from_df(df_label, self.ureg)
                if "apixaban-M1" in label:
                    dset.unit_conversion("mean", 1 / self.Mr.m1)
                else:
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[label] = dset

        # console.print(dsets)

        return dsets

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims = {}
        for intervention in self.interventions:
            tc = Timecourse(
                start=0,
                end=24 * 60,  # [min]
                steps=1000,
                changes={
                    **self.default_changes(),
                    "BW": Q_(self.bodyweight, "kg"),
                    "PODOSE_api": Q_(self.doses[intervention], "mg"),
                },
            )

            tc_end = Timecourse(
                start=0,
                end=52 * 60,  # [min]
                steps=1000,
                changes={
                    **self.default_changes(),
                    "BW": Q_(self.bodyweight, "kg"),
                    "PODOSE_api": Q_(self.doses[intervention], "mg"),
                },
            )

            tcsims[f"api_{intervention}"] = TimecourseSim(
                timecourses=[tc] * 2 + [tc_end],
                time_offset= - 2 * 24 * 60
            )

        return tcsims

    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings = {}
        for intervention in self.interventions:
            # pharmacokinetics
            for k, sid in enumerate(self.infos_pk.keys()):

                name = self.infos_pk[sid]
                mappings[f"fm_api_{name}_{intervention}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"{intervention}_{name}",
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=f"task_api_{intervention}",
                        xid="time",
                        yid=sid,
                    ),
                    metadata=ApixabanMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.NR,
                        dosing= Dosing.MULTIPLE,
                        health=Health.HEALTHY,
                        fasting= Fasting.NR,
                    )
                )

        return mappings

    def figures(self) -> Dict[str, Figure]:

        fig = Figure(
            experiment=self,
            sid="Fig3",
            name=f"{self.__class__.__name__}",
            num_rows=1,
            num_cols=2,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )

        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)
        plots[1].set_yaxis(self.label_m1_plasma, unit=self.unit_m1)

        for intervention in self.interventions:
            for k, sid in enumerate(self.infos_pk.keys()):
                    name = self.infos_pk[sid]
                    #simulation
                    plots[k].add_data(
                        task=f"task_api_{intervention}",
                        xid="time",
                        yid=sid,
                        label=f"sim chronic: {intervention[2:4]}mg PO",
                        color=self.colors[intervention],
                    )
                    # data
                    plots[k].add_data(
                        dataset=f"{intervention}_{name}",
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                        label=f"exp chronic: {intervention[2:4]}mg PO",
                        color=self.colors[intervention],
                    )

        return {fig.sid: fig}



if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / Frost2015b.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Frost2015b, output_dir=Frost2015b.__name__)
