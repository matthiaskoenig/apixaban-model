"""Simulation experiment of the study VandenBosch2021."""

from typing import ClassVar, override

import pandas as pd
from pkpdsim.metadata import (
    ApplicationForm,
    Dosing,
    Fasting,
    Health,
    PKPDMappingMetaData,
    Route,
    Tissue,
)
from sbmlsim import Q
from sbmlsim.data import DataSet
from sbmlsim.fit import FitData, FitMapping
from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Simulation

from pkdb_models.models.apixaban import MODEL
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)


class VandenBosch2021(ApixabanSimulationExperiment):
    """Simulation experiment of VandenBosch2021.

    A single oral dose of 2.5 or 5 mg apixaban (tablet) in patients with end
    stage renal disease on hemodialysis (n = 6 per group), immediately after a
    dialysis (post) or 30 min before it (pre). The model has no dialysis: only
    the groups dosed after the dialysis are simulated, up to the start of the
    next dialysis (44 h). The renal function is the class of end stage renal
    disease of the renal map (no measured value, 75 % of the patients have a
    urine output below 300 ml/day). The concentrations are measured with a
    chromogenic anti-Xa assay calibrated with apixaban (LOQ 21 ng/ml).
    """

    colors: ClassVar[dict[str, str]] = {"PO2.5": "#31a354", "PO5": "#006d2c"}

    interventions: ClassVar[list[str]] = list(colors.keys())

    doses: ClassVar[dict[str, float]] = {  # [mg]
        "PO2.5": 2.5,
        "PO5": 5,
    }

    groups: ClassVar[dict[str, str]] = {"PO2.5": "post2.5", "PO5": "post5"}

    #: the start of the next dialysis [hr]
    end_data = 45.0

    #: limit of quantification of the anti-Xa assay [ng/ml]
    loq = 21.0

    infos_pk: ClassVar[dict[str, str]] = {
        "[Cve_api]": "apixaban",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        # the means of the groups, the points below the limit of quantification
        # are left out (but the predose point)
        df = self.load_dataframe("Fig1Mean")
        for label, df_label in df.groupby("label"):
            label = str(label)
            if "post" not in label:
                continue
            df_label = df_label[
                (df_label["time"] < self.end_data)
                & ((df_label["mean"] >= self.loq) | (df_label["time"] == 0.0))
            ]
            dset = DataSet.from_df(df_label, self.ureg)
            dset.unit_conversion("mean", 1 / self.Mr.api)
            dsets[self.to_sid(label)] = dset

        # the individual points of a group as one scatter, every digitized point
        # has its own individual id in the data (not a subject); plotted only
        df = self.load_dataframe("Fig1")
        for intervention, group in self.groups.items():
            df_group = df[
                (df["group"] == group)
                & (df["intervention"] == intervention)
                & (df["time"] < self.end_data)
            ]
            df_group = pd.DataFrame(df_group).assign(individual="NA", count=1.0)
            dset = DataSet.from_df(df_group, self.ureg)
            dset.unit_conversion("value", 1 / self.Mr.api)
            dsets[self.to_sid(f"{intervention}_apixaban_{group}_individual")] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        for intervention in self.interventions:
            tcsims[self.to_sid(f"api_{intervention}")] = Simulation(
                time_unit="hr",
                end=54,
                preinit_changes={
                    **self.default_changes(),
                    "PODOSE_api": Q(self.doses[intervention], "mg"),
                    "KI__f_renal_function": Q(
                        self.renal_map["End stage renal disease"], "dimensionless"
                    ),
                },
            )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for intervention in self.interventions:
            group = self.groups[intervention]
            for sid, name in self.infos_pk.items():
                mappings[self.to_sid(f"fm_api_{name}_{intervention}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(f"{intervention}_{name}_{group}_mean"),
                        xid="time",
                        yid="mean",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_api_{intervention}"),
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=Health.RENAL_IMPAIRMENT,
                        fasting=Fasting.NR,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="Fig1",
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

        for kp, intervention in enumerate(self.interventions):
            dose = self.doses[intervention]
            group = self.groups[intervention]
            color = self.colors[intervention]
            plots[kp].set_yaxis(self.label_api_plasma, unit=self.unit_api)
            for sid, name in self.infos_pk.items():
                # simulation
                plots[kp].add_data(
                    task=self.to_sid(f"task_api_{intervention}"),
                    xid="time",
                    yid=sid,
                    label=f"sim ESRD: {dose}mg PO",
                    color=color,
                )
                # data
                plots[kp].add_data(
                    dataset=self.to_sid(f"{intervention}_{name}_{group}_mean"),
                    xid="time",
                    yid="mean",
                    count="count",
                    label=f"exp ESRD: {dose}mg PO",
                    color=color,
                )
                plots[kp].add_data(
                    dataset=self.to_sid(f"{intervention}_{name}_{group}_individual"),
                    xid="time",
                    yid="value",
                    label=f"exp individ ESRD: {dose}mg PO",
                    color=f"{color}60",
                    markeredgecolor=f"{color}60",
                    marker="o",
                    linestyle="",
                    markersize=5.2,
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(VandenBosch2021, output_dir=VandenBosch2021.__name__)
