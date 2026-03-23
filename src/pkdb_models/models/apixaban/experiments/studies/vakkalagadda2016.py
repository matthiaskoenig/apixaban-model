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
    Tissue, Route, Dosing, ApplicationForm, Health, Fasting, ApixabanMappingMetaData, Coadministration
)

from sbmlsim.plot import Axis, Figure
    # noqa: E402
from sbmlsim.simulation import Timecourse, TimecourseSim

from pkdb_models.models.apixaban.helpers import run_experiments


class Vakkalagadda2016(ApixabanSimulationExperiment):
    """Simulation experiment of Vakkalagadda2016."""

    colors = {
        "API10PO": "black",
        "API5IV": "tab:pink",
    }
    groups = list(colors.keys())
    bodyweight = 74.5  # [kg] # control
    bodyheight = math.sqrt(74.5 / 24.4) # [m]

    interventions = {
        "API5IV": 5, # [mg]
        "API10PO": 10
    }

    infos_pk = {
        "[Cve_api]": "apixaban",
        "Aurine_api": "cumulative amount"
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Tab2", "Fig2"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            if fig_id == "Tab2":
                df = df.rename(
                    columns={
                        "mean": "mean_real",
                        "geomean": "mean",
                    }
                )
            for label, df_label in df.groupby("label"):
                dset = DataSet.from_df(df_label, self.ureg)
                if "RIF600" not in label and (fig_id == "Fig2" or "cumulative" in label):
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                    dsets[label] = dset

        # console.print("datasets:", list(dsets.keys()))
        return dsets


    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims: Dict[str, TimecourseSim] = {}
        for intervention in self.interventions:
            if "IV" in intervention:
                sim_kwargs = {
                    "IVDOSE_api": Q_(self.interventions[intervention], "mg"),
                    "ti_api": Q_(10, "s"),
                }
            else:
                sim_kwargs = {
                    "PODOSE_api": Q_(self.interventions[intervention], "mg"),
                }

            tcsims[f"{intervention}_apixaban_healthy"] = TimecourseSim([
                Timecourse(
                    start=0,
                    end=50 * 60,  # [min]
                    steps=500,
                    changes={
                        **self.default_changes(),
                        **sim_kwargs,
                        "BW": Q_(self.bodyweight, "kg"),
                        "HEIGHT": Q_(self.bodyheight, "m"),
                    },
                )
            ])
        return tcsims

    # Fit Mappings
    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings: Dict[str, FitMapping] = {}
        for intervention in self.interventions.keys():
            for sid, name in self.infos_pk.items():
                mappings[f"fm_{intervention}_{name}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"{intervention}_all_{name}" if sid == "[Cve_api]" else f"{intervention}_{name}_all_apixaban",
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd" if sid == "[Cve_api]" else None,
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=f"task_{intervention}_apixaban_healthy",
                        xid="time",
                        yid=sid,
                    ),
                    metadata=ApixabanMappingMetaData(
                        tissue=Tissue.PLASMA if sid == "[Cve_api]" else Tissue.URINE,
                        route=Route.PO if "PO" in intervention else Route.IV,
                        application_form=ApplicationForm.TABLET if "PO" in intervention else ApplicationForm.SOLUTION,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
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

        for intervention, dose in self.interventions.items():
            for kp, sid in enumerate(self.infos_pk):
                name = self.infos_pk[sid]
                # Simulation
                plots[kp].add_data(
                    task=f"task_{intervention}_apixaban_healthy",
                    xid="time",
                    yid=sid,
                    label=f"sim: {dose}mg PO" if "PO" in intervention else f"sim: {dose}mg IV",
                    color=self.colors[intervention]
                )
                # Data
                plots[kp].add_data(
                    dataset=f"{intervention}_all_{name}" if sid == "[Cve_api]" else f"{intervention}_{name}_all_apixaban",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd" if sid == "[Cve_api]" else None,
                    count="count",
                    label=f"exp: {dose}mg PO" if "PO" in intervention else f"exp: {dose}mg IV",
                    color=self.colors[intervention],
                    linestyle="solid" if sid == "[Cve_api]" else "",
                )

        return {fig.sid: fig}



if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / Vakkalagadda2016.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Vakkalagadda2016, output_dir=Vakkalagadda2016.__name__)

