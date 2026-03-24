import math
from typing import Dict

from sbmlsim.data import DataSet, load_pkdb_dataframe
from sbmlsim.fit import FitMapping, FitData
from sbmlutils.console import console

from pkdb_models.models import apixaban
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


class Tirona2018(ApixabanSimulationExperiment):
    """Simulation experiment of Tirona2018."""

    colors = {
        "control": "black",
        "nafld": "tab:blue",
    }
    groups = list(colors.keys())
    bodyweight = 65.6  # [kg] # control
    bodyheight = math.sqrt(65.6 / 23.4) # [m]

    infos_pk = {
        "[Cve_api]": "apixaban",
        "Aurine_api": "cumulative amount"
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Tab2", "Fig2"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby("label"):
                dset = DataSet.from_df(df_label, self.ureg)
                if label.endswith("apixaban") and (fig_id == "Fig2" or label.startswith("cumulative")):
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                    dsets[label] = dset

        # console.print("datasets:", list(dsets.keys()))
        return dsets


    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims: Dict[str, TimecourseSim] = {}
        tcsims["control"] = TimecourseSim([
            Timecourse(
                start=0,
                end=30 * 60,  # [min]
                steps=500,
                changes={
                    **self.default_changes(),
                    "PODOSE_api": Q_(2.5, "mg"),
                    "BW": Q_(self.bodyweight, "kg"),
                    "HEIGHT": Q_(self.bodyheight, "m"),
                },
            )
        ])
        return tcsims

    # Fit Mappings
    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings: Dict[str, FitMapping] = {}
        infos = {
            **self.infos_pk,
        }
        for group in self.groups:
            if group == "control":
                for sid, name in infos.items():
                    mappings[f"fm_{name}_{group}"] = FitMapping(
                        self,
                        reference=FitData(
                            self,
                            dataset=f"{group}_{name}" if sid == "[Cve_api]" else f"{name}_{group}_apixaban",
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
                            tissue=Tissue.PLASMA if sid == "[Cve_api]" else Tissue.URINE,
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
            num_cols=2,
            num_rows=1,
            height=self.panel_height,
            width=self.panel_width * 2,
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

                if group == "control":
                    # Simulation
                    plots[kp].add_data(
                        task=f"task_{group}",
                        xid="time",
                        yid=sid,
                        label=f"sim: 2.5mg PO",
                        color=self.colors[group]
                    )
                # Data
                plots[kp].add_data(
                    dataset=f"{group}_{name}" if sid == "[Cve_api]" else f"{name}_{group}_apixaban",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp: 2.5mg PO" if group == "control" else f"exp {group}: 2.5mg PO",
                    color=self.colors[group],
                    linestyle="solid" if sid == "[Cve_api]" else "",
                )

        return {fig.sid: fig}



if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / Tirona2018.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Tirona2018, output_dir=Tirona2018.__name__)

