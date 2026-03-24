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
    Coadministration
)

from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Timecourse, TimecourseSim

from pkdb_models.models.apixaban.helpers import run_experiments


class Metze2021(ApixabanSimulationExperiment):
    """Simulation experiment of Metze2021."""

    # 1-15
    individuals = [f"IS{k:03d}" for k in range(1, 16)]
    intervention = "API5"
    dose = 5

    markers = {
        "mean": "s",
        "IS": "o"
    }

    marker_size = {
        "mean": 7.5,
        "IS": 5.2,
    }

    linewidths = {
        "mean": 1.5,
        "IS": 0.5,
    }

    infos_pk = {
        "[Cve_api]": "apixaban"
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1", "Fig1A"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby("label"):
                dset = DataSet.from_df(df_label, self.ureg)
                if fig_id == "Fig1" and label.startswith("apixaban"):
                    dset.unit_conversion("value", 1 / self.Mr.api)
                elif fig_id == "Fig1A" and label.startswith("apixaban"):
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[label] = dset

        # console.print(dsets)
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
        for ks, sid in enumerate(self.infos_pk):
            name = self.infos_pk[sid]

            # PK (individual)
            for individual in self.individuals:
                mappings[f"fm_{name}_{self.intervention}_{individual}"] = FitMapping(
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
                        application_form= ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=Health.RENAL_IMPAIRMENT,
                        fasting=Fasting.NR,
                        coadministration=Coadministration.NONE
                    ),
                )

            # PK (mean)
            mappings[f"fm_{name}_{self.intervention}"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=f"{name}_{self.intervention}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
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
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
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
                label="sim MiRI: 5mg PO",
                color=self.renal_colors["Mild renal impairment"],
            )
            # individual data
            for ki, individual in enumerate(self.individuals):
                plots[ks].add_data(
                    dataset=f"{name}_{self.intervention}_{individual}",
                    xid="time",
                    yid="value",
                    yid_sd=None,
                    label="exp individ MiRI: 5mg PO" if ki == 0 else None,
                    color="white",
                    markeredgecolor=self.renal_colors["Mild renal impairment"],
                    linewidth=self.linewidths["IS"],
                    marker=self.markers["IS"],
                    markersize=self.marker_size["IS"],
                )
            # mean data
            plots[ks].add_data(
                dataset=f"{name}_{self.intervention}",
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
                label="exp MiRI: 5mg PO",
                color=self.renal_colors["Mild renal impairment"],
                linewidth=self.linewidths["mean"],
                marker=self.markers["mean"],
                markersize=self.marker_size["mean"],
            )



        return {
            fig.sid: fig,
        }


if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / Metze2021.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Metze2021, output_dir=Metze2021.__name__)