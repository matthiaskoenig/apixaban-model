from typing import Dict

from pymetadata.console import console
from sbmlsim.data import DataSet, load_pkdb_dataframe
from sbmlsim.fit import FitMapping, FitData

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
    Coadministration
)

from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Timecourse, TimecourseSim

from pkdb_models.models.apixaban.helpers import run_experiments


class Metze2021(ApixabanSimulationExperiment):
    """Simulation experiment of Metze2021."""

    color = "#66c2a4"  # Mild renal impairment
    # 1 - 15
    individuals = [f"IS{k:03d}" for k in range(1, 16)]
    intervention = "API5"
    dose = 5

    infos_pk = {
        "[Cve_api]": "apixaban"
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby("label"):
                dset = DataSet.from_df(df_label, self.ureg)
                if label.startswith("apixaban"):
                    dset.unit_conversion("value", 1 / self.Mr.api)
                dsets[label] = dset

        # console.print(dsets.keys())
        return dsets

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims = {}

        tcsims[self.intervention] = TimecourseSim(
                [Timecourse(
                    start=0,
                    end=16 * 60,  # [min]
                    steps=500,
                    changes={
                        **self.default_changes(),
                        "PODOSE_api": Q_(self.dose, "mg"),
                        # renal impairment
                        "KI__f_renal_function": Q_(65/110, "dimensionless"), # based on creatinine clearance
                    },
                )]
            )
        return tcsims

    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings = {}
        # PK
        for ks, sid in enumerate(self.infos_pk):
            for individual in self.individuals:
                name = self.infos_pk[sid]
                mappings[f"fm_{name}_{self.intervention}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"{name}_{self.intervention}_{individual}",
                        xid="time",
                        yid="value",
                        yid_sd=None,
                        count="count",
                    ),
                    observable=FitData(
                        self, task=f"task_{self.intervention}", xid="time", yid=sid,
                    ),
                    metadata=ApixabanMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=Health.RENAL_IMPAIRMENT,
                        fasting=Fasting.NR,
                        coadministration=Coadministration.NONE
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
            name=f"{self.__class__.__name__} (Renal impairment)"
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)

        for ks, sid in enumerate(self.infos_pk):
            name = self.infos_pk[sid]
            # simulation
            plots[ks].add_data(
                task=f"task_{self.intervention}",
                xid="time",
                yid=sid,
                label=self.intervention,
                color=self.color,
            )

            for ki, individual in enumerate(self.individuals):
                # data
                plots[ks].add_data(
                    dataset=f"{name}_{self.intervention}_{individual}",
                    xid="time",
                    yid="value",
                    yid_sd=None,
                    count="count",
                    label=self.intervention if ki == 0 else None,
                    color=self.color,
                )

            # FIXME: add mean data

        return {
            fig.sid: fig,
        }


if __name__ == "__main__":
    run_experiments(Metze2021, output_dir=Metze2021.__name__)