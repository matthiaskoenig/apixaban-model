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


class VandenBosch2021(ApixabanSimulationExperiment):
    """Simulation experiment of VandenBosch2021."""

    colors = {
        "PO2.5":"#006d2c",
        "PO5": "#006d2c"
    }

    interventions = list(colors.keys())

    doses = {
        "PO2.5": 2.5, #mg
        "PO5": 5
    }

    groups = {
        "PO2.5": "post2.5",
        "PO5": "post5"
    }

    infos_pk = {
        "[Cve_api]": "apixaban",
    }

    individual_ids = {
        "PO2.5": {"start": 147, "end": 183},
        "PO5": {"start": 185, "end": 223},
    }


    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1", "Fig1Mean"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby("label"):
                dset = DataSet.from_df(df_label, self.ureg)
                if "post" in label:
                    filtered_dset = dset[dset["time"] < 45.0].copy() # 44 hr - dialysis starts
                    if not filtered_dset.empty:
                        if "mean" in label:
                            filtered_dset.unit_conversion("mean", 1 / self.Mr.api)
                        else:
                            filtered_dset.unit_conversion("value", 1 / self.Mr.api)
                        dsets[label] = filtered_dset

        # console.print(dsets)

        return dsets

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims = {}
        for intervention in self.interventions:
            tcsims[f"api_{intervention}"] = TimecourseSim(
                Timecourse(
                    start=0,
                    end=54 * 60,  # [min]
                    steps=1000,
                    changes={
                        **self.default_changes(),
                        "PODOSE_api": Q_(self.doses[intervention], "mg"),
                        "KI__f_renal_function": Q_(self.renal_map["End stage renal impairment"], "dimensionless"),
                    },
                )
            )

        return tcsims

    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings = {}
        for intervention in self.interventions:
            ids = self.individual_ids[intervention]
            # pharmacokinetics
            for k, sid in enumerate(self.infos_pk.keys()):

                name = self.infos_pk[sid]
                mappings[f"fm_api_{name}_{intervention}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"{intervention}_{name}_{self.groups[intervention]}_mean",
                        xid="time",
                        yid="mean",
                        yid_sd=None,
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
                        application_form=ApplicationForm.TABLET,
                        dosing= Dosing.SINGLE,
                        health=Health.RENAL_IMPAIRMENT,
                        fasting= Fasting.NR,
                    )
                )


                for ki in range(ids["start"], ids["end"]):
                    mappings[f"fm_api_{name}_{intervention}_I{ki}"] = FitMapping(
                        self,
                        reference=FitData(
                            self,
                            dataset=f"{intervention}_{name}_{self.groups[intervention]}_I{ki}",
                            xid="time",
                            yid="value",
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
                            application_form=ApplicationForm.TABLET,
                            dosing=Dosing.SINGLE,
                            health=Health.RENAL_IMPAIRMENT,
                            fasting=Fasting.NR,
                        )
                    )

            return mappings


        return mappings

    def figures(self) -> Dict[str, Figure]:

        fig = Figure(
            experiment=self,
            sid="Fig3",
            name=f"{self.__class__.__name__}",
            num_rows=1,
            num_cols=2,
            height=self.panel_height,
            width=self.panel_width * 2,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )

        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)
        plots[1].set_yaxis(self.label_api_plasma, unit=self.unit_api)

        for kp, intervention in enumerate(self.interventions):
            ids = self.individual_ids[intervention]
            dose = self.doses[intervention]
            for sid in self.infos_pk.keys():
                name = self.infos_pk[sid]
                #simulation
                plots[kp].add_data(
                    task=f"task_api_{intervention}",
                    xid="time",
                    yid=sid,
                    label=f"sim SRI: {dose}mg PO",
                    color=self.colors[intervention],
                )
                # data
                plots[kp].add_data(
                    dataset=f"{intervention}_{name}_{self.groups[intervention]}_mean",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp SRI: {dose}mg PO",
                    color=self.colors[intervention],
                )
                legend = True
                for ki in range(ids["start"], ids["end"]):
                    # scatter
                    plots[kp].add_data(
                        xid="time",
                        yid="value",
                        dataset=f"{intervention}_{name}_{self.groups[intervention]}_I{ki}",
                        label=f"exp individ SRI: {dose}mg PO" if legend else None,
                        color='#006d2c40',
                        markeredgecolor='#006d2c40',
                        marker="o",
                        linestyle="",
                        markersize=5.2,
                    )
                    legend = False

        return {fig.sid: fig}



if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / VandenBosch2021.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(VandenBosch2021, output_dir=VandenBosch2021.__name__)
