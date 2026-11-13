"""Simulation experiment of the study VandenBosch2021."""

from collections.abc import Mapping
from types import MappingProxyType
from typing import ClassVar, override

from pkpdsim.metadata import (
    ApplicationForm,
    Dosing,
    Fasting,
    Health,
    PKPDMappingMetaData,
    Route,
    Tissue,
)
from pkpdsim.pbpk import Sex
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

    The patients dosed 2.5 mg after the dialysis are mostly women (4 of 6) and
    run on the female build, with the end stage renal disease of the female
    build; the patients dosed 5 mg (3 women of 6, no majority) run on the male
    build.
    """

    simulation_sexes: ClassVar[Mapping[str, Sex]] = MappingProxyType(
        {
            "api_PO2p5": Sex.FEMALE,
        }
    )

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
        "Carm_api": "apixaban",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        df = self.load_dataframe("Fig1")
        for intervention, group in self.groups.items():
            # the means of the groups (the samples below the limit of
            # quantification counted as 0), the means below the limit of
            # quantification are left out (but the predose point)
            df_mean = df[df["label"] == f"{intervention}_apixaban_{group}_mean"]
            df_mean = df_mean[
                (df_mean["time"] < self.end_data)
                & ((df_mean["mean"] >= self.loq) | (df_mean["time"] == 0.0))
            ]
            dset = DataSet.from_df(df_mean, self.ureg)
            dset.unit_conversion("mean", 1 / self.Mr["api"])
            dsets[self.to_sid(f"{intervention}_apixaban_{group}_mean")] = dset

            # the samples of a group as one scatter (the samples below the limit
            # of quantification have no value); plotted only
            df_samples = df[
                (
                    df["label"]
                    == "concentration_apixaban_plasma_"
                    + f"{intervention}_{group}".replace(".", "_")
                )
                & (df["time"] < self.end_data)
            ]
            dset = DataSet.from_df(df_samples, self.ureg)
            dset.unit_conversion("mean", 1 / self.Mr["api"])
            dsets[self.to_sid(f"{intervention}_apixaban_{group}_individual")] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        for intervention in self.interventions:
            key = self.to_sid(f"api_{intervention}")
            # the classes of the build of the group (`simulation_sexes`)
            renal_map = self.renal_map_of(simulation=key)
            tcsims[key] = Simulation(
                time_unit="hr",
                end=54,
                preinit_changes={
                    **self.default_changes(),
                    "PODOSE_api": Q(self.doses[intervention], "mg"),
                    "f_renal_function": Q(
                        renal_map["End stage renal disease"], "dimensionless"
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
                    yid="mean",
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
