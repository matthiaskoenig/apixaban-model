from typing import Dict

from sbmlsim.data import DataSet, load_pkdb_dataframe
from sbmlsim.fit import FitMapping, FitData
from sbmlutils.console import console

from pkdb_models.models import apixaban
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)
from pkdb_models.models.apixaban.experiments.metadata import Tissue, Route, Dosing, ApplicationForm, Health, \
    Fasting, ApixabanMappingMetaData, Coadministration

from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Timecourse, TimecourseSim

from pkdb_models.models.apixaban.helpers import run_experiments


class Lenard2024(ApixabanSimulationExperiment):
    """Simulation experiment of Lenard2024."""

    colors = {
        "API25, RIV25, EDO50": "tab:red",
        "API25, RIV25, EDO50, CLAR": "tab:pink",
    }

    interventions = list(colors.keys())

    doses =  {
        "API25, RIV25, EDO50": 0.025,  # [μg] (2 times dosing, first on day1, second on day 5)
        "API25, RIV25, EDO50, CLAR": 0.025,  # 50 µg
    }

    labels = {
        "API25, RIV25, EDO50": ": DOACs PO",
        "API25, RIV25, EDO50, CLAR": ": DOACs, clar 500mg PO",
    }

    infos_pk = {
        "[Cve_api]": "apixaban"
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby("label"):
                dset = DataSet.from_df(df_label, self.ureg)
                if label.startswith("apixaban"):
                        dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[label] = dset
        return dsets

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims = {}
        for intervention in self.interventions:
                dose = self.doses[intervention]
                tcsims[f"{intervention}"] = TimecourseSim(
                        [Timecourse(
                            start=0,
                            end=50 * 60,  # [min]
                            steps=500,
                            changes={
                                **self.default_changes(),
                                "PODOSE_api": Q_(dose, "mg")
                            },
                        )])
        return tcsims

    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings = {}
        for intervention in self.interventions:
                # PK
                for ks, sid in enumerate(self.infos_pk):
                    name = self.infos_pk[sid]
                    mappings[f"fm_{name}_{intervention}"] = FitMapping(
                        self,
                        reference=FitData(
                            self,
                            dataset=f"{name}_{intervention}",
                            xid="time",
                            yid="mean",
                            yid_sd="mean_sd",
                            count="count",
                        ),
                        observable=FitData(
                            self, task=f"task_{intervention}", xid="time", yid=sid,
                        ),
                        metadata=ApixabanMappingMetaData(
                            tissue=Tissue.PLASMA,
                            route=Route.PO,
                            application_form=ApplicationForm.TABLET,
                            dosing=Dosing.SINGLE,
                            health=Health.HEALTHY,
                            fasting=Fasting.NR,
                            coadministration=Coadministration.CLARITHROMYCIN if "CLAR" in intervention else Coadministration.EDOXABAN,
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
            sid="Fig2",
            num_cols=1,
            name=f"{self.__class__.__name__}",
            height=self.panel_height * 1.2,
            width=self.panel_width * 1.1,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )
        plots[0].set_yaxis(self.label_api_plasma, unit="nM")

        is_sim = True
        for intervention in self.interventions:
            for ks, sid in enumerate(self.infos_pk):
                name = self.infos_pk[sid]
                if is_sim:
                    # simulation
                    plots[ks].add_data(
                        task=f"task_{intervention}",
                        xid="time",
                        yid=sid,
                        label="sim: api 25ug PO",
                        color="black",
                    )
                    is_sim = False
                # data
                plots[ks].add_data(
                    dataset=f"{name}_{intervention}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp {self.labels[intervention]}",
                    color=self.colors[f"{intervention}"],
                )

        return {
            fig.sid: fig
        }


if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / Lenard2024.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Lenard2024, output_dir=Lenard2024.__name__)
