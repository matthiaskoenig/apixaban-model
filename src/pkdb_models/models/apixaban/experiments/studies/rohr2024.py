from typing import Dict

from sbmlsim.data import DataSet, load_pkdb_dataframe
from sbmlsim.fit import FitMapping, FitData
from sbmlutils.console import console

from pkdb_models.models import apixaban
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)
from pkdb_models.models.apixaban.experiments.metadata import Tissue, Route, Dosing, ApplicationForm, Health, Health, \
    Fasting, ApixabanMappingMetaData, Coadministration

from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Timecourse, TimecourseSim

from pkdb_models.models.apixaban.helpers import run_experiments


class Rohr2024(ApixabanSimulationExperiment):
    """Simulation experiment of Rohr2024."""

    colors = {
        "API25, RIV25, EDO50, RITx5": "tab:red",
        "API25, RIV25, EDO50": "tab:pink",
    }

    labels = {
        "API25, RIV25, EDO50, RITx5": "DOACs, rit 100mg PO",
        "API25, RIV25, EDO50": "DOACs",
    }
    interventions = list(colors.keys())

    dose = 0.025  # μg

    infos_pk = {
        "[Cve_api]": "apixaban",
        "Aurine_api": "apixaban_urine"
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2",  "Tab1A"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby("label"):
                dset = DataSet.from_df(df_label, self.ureg)
                if label.startswith("apixaban") and "urine" not in label:
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[label] = dset
        return dsets

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims = {}
        for intervention in self.interventions:
            dose = self.dose
            tcsims[f"{intervention}"] = TimecourseSim(
                [Timecourse(
                    start=0,
                    end=30 * 60,  # [min]
                    steps=500,
                    changes={
                        **self.default_changes(),
                        "PODOSE_api": Q_(dose, "mg"),
                    },
                )]
            )
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
                        tissue=Tissue.URINE if "urine" in name else Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
                        coadministration=Coadministration.RITONAVIR if "RIT" in intervention else Coadministration.EDOXABAN,
                    ),
                )

        return mappings

    def figures(self) -> Dict[str, Figure]:
        return {
            **self.figure_pk()
        }

    def figure_pk(self) -> Dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="Fig1",
            num_cols=2,
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 2,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)
        plots[1].set_yaxis(self.label_api_urine, unit=self.unit_api_urine)

        for ks, sid in enumerate(self.infos_pk):
            is_sim = True
            for intervention in self.interventions:
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
                    label=f"exp: {self.labels[intervention]}",
                    color=self.colors[intervention],
                    linestyle="" if sid == "Aurine_api" else "dashed",
                )

        return {
            fig.sid: fig
        }


if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / Rohr2024.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Rohr2024, output_dir=Rohr2024.__name__)