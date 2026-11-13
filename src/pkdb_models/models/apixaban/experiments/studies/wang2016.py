"""Simulation experiment of the study Wang2016."""

import math
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
from sbmlsim import Q
from sbmlsim.data import DataSet
from sbmlsim.fit import FitData, FitMapping
from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Simulation

from pkdb_models.models.apixaban import MODEL
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)


class Wang2016(ApixabanSimulationExperiment):
    """Simulation experiment of Wang2016.

    A single oral dose of 5 mg apixaban (tablet) in 8 healthy subjects (CLcr
    125 ml/min) and 8 patients with end stage renal disease on hemodialysis
    (ESRD), twice: period 1 with a hemodialysis 2 to 6 h after the dose (P1),
    period 2 with the dose immediately after a hemodialysis (P2). The model has
    no dialysis: P1 is simulated like P2 (the dialysis removed 6.7 % of the
    dose). The GFR of the ESRD patients is the one of the class of end stage
    renal disease (10.5 ml/min), but the measured renal clearance of
    apixaban is 0.02 against 11.3 ml/min in the healthy subjects (3 of 8
    patients anuric): the model overestimates the urinary excretion of the
    patients. The urinary amounts are derived (CLR x AUCinf of Table 2).

    The subjects are mostly men (4 women of 16, 2 of 8 in each group) and run
    on the male build.
    """

    colors: ClassVar[dict[str, str]] = {
        "healthy": "black",
        "esrd_P1": "#41ab5d",
        "esrd_P2": "#006d5e",
    }
    markers: ClassVar[dict[str, str]] = {
        "healthy": "D",
        "esrd_P1": "^",
        "esrd_P2": "o",
    }
    legends: ClassVar[dict[str, str]] = {
        "healthy": "5mg PO",
        "esrd_P1": "ESRD on HD: 5mg PO",
        "esrd_P2": "ESRD off HD: 5mg PO",
    }
    bodyweights: ClassVar[dict[str, float]] = {  # [kg]
        "healthy": 87.4,
        "esrd_P1": 92.5,  # the dose before the hemodialysis
        "esrd_P2": 90.7,  # dry weight, the dose after the hemodialysis
    }
    bodyheights: ClassVar[dict[str, float]] = {  # [m]
        "healthy": math.sqrt(87.4 / 29.7),
        "esrd_P1": math.sqrt(92.5 / 29.7),
        "esrd_P2": math.sqrt(92.5 / 29.7),
    }

    inrs: ClassVar[dict[str, float]] = {
        "healthy": 0.97,
        "esrd_P1": 1.07,  # post-apixaban hemodialysis
        "esrd_P2": 1.09,  # pre-apixaban hemodialysis
    }
    pts: ClassVar[dict[str, float]] = {  # [s]
        "healthy": 11.42,
        "esrd_P1": 12.79,  # post-apixaban hemodialysis
        "esrd_P2": 12.99,  # pre-apixaban hemodialysis
    }
    aptts: ClassVar[dict[str, float]] = {  # [s]
        "healthy": 34.33,
        "esrd_P1": 36.28,  # post-apixaban hemodialysis
        "esrd_P2": 31.56,  # pre-apixaban hemodialysis
    }

    #: the GFR of the simulations [ml/min] (`renal_function`): the measured
    #: creatinine clearance of the healthy subjects, the GFR of the class of
    #: end stage renal disease for the patients
    gfr: ClassVar[dict[str, float]] = {
        "healthy": 125.0,
        "esrd_P1": ApixabanSimulationExperiment.renal_class_gfr[
            "End stage renal disease"
        ],
        "esrd_P2": ApixabanSimulationExperiment.renal_class_gfr[
            "End stage renal disease"
        ],
    }
    groups: ClassVar[list[str]] = [
        "healthy",
        "esrd_P1",
        "esrd_P2",
    ]
    #: the groups with urinary data and the labels of their urinary amounts
    #: (without a spread)
    groups_urine: ClassVar[dict[str, str]] = {
        "healthy": "cumulative_amount_apixaban_urine_API5_healthy",
        "esrd_P2": "cumulative_amount_apixaban_urine_API5_DIALYSIS_PRE_esrd",
    }
    infos_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
        "Aurine_api": "cumulative amount",
    }
    infos_pd: ClassVar[dict[str, str]] = {
        "COAG__INR": "inr",
        "COAG__PT": "pt",
        "COAG__aPTT": "aptt",
        "COAG__antiXa_activity": "xa",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1", "Fig2", "Fig3"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                if fig_id == "Fig3":
                    # the anti-Xa activity against apixaban
                    dset.unit_conversion("x", 1 / self.Mr["api"])
                    label = "apixaban_vs_xa_" + label.removeprefix("xa_vs_apixaban_")
                elif label.startswith("apixaban_"):
                    dset.unit_conversion("mean", 1 / self.Mr["api"])
                dsets[self.to_sid(label)] = dset

        df = self.load_dataframe("Tab2")
        for group, label in self.groups_urine.items():
            dset = DataSet.from_df(df[df["label"] == label], self.ureg)
            dset.unit_conversion("mean", 1 / self.Mr["api"])
            dsets[self.to_sid(f"{group}_cumulative amount")] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims: dict[str, Simulation] = {}
        for group in self.groups:
            tcsims[self.to_sid(group)] = Simulation(
                time_unit="hr",
                end=74,
                preinit_changes={
                    **self.default_changes(),
                    "PODOSE_api": Q(5, "mg"),
                    "BW": Q(self.bodyweights[group], "kg"),
                    "f_renal_function": self.renal_function(
                        self.gfr[group],
                        bw=self.bodyweights[group],
                        height=100 * self.bodyheights[group],
                    ),
                    "COAG__INR_ref": Q(self.inrs[group], "dimensionless"),
                    "COAG__aPTT_ref": Q(self.aptts[group], "second"),
                    "COAG__PT_ref": Q(self.pts[group], "second"),
                    "HEIGHT": Q(self.bodyheights[group], "m"),
                },
            )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings: dict[str, FitMapping] = {}
        infos = {
            **self.infos_pk,
            **self.infos_pd,
        }
        for group in self.groups:
            for sid, name in infos.items():
                if sid == "Aurine_api" and group not in self.groups_urine:
                    continue
                tissue = Tissue.URINE if "cumulative" in name else Tissue.PLASMA
                mappings[self.to_sid(f"fm_{name}_{group}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(
                            f"{name}_{group}"
                            if "cumulative" not in name
                            else f"{group}_cumulative amount"
                        ),
                        xid="time",
                        yid="mean",
                        yid_sd=None if sid == "Aurine_api" else "mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_{group}"),
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=tissue,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY
                        if group == "healthy"
                        else Health.RENAL_IMPAIRMENT,
                        fasting=Fasting.NR,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure_pk(),
            **self.figure_pd(),
            **self.figure_scatter(),
        }

    def figure_pk(self) -> dict[str, Figure]:
        """Apixaban in plasma and urine of the healthy subjects and the ESRD patients."""
        fig = Figure(
            experiment=self,
            sid="PK",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 2,
            num_cols=2,
            num_rows=1,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        for kp, sid in enumerate(self.infos_pk):
            plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid])

        for group in self.groups:
            for kp, (sid, name) in enumerate(self.infos_pk.items()):
                if sid == "Aurine_api" and group not in self.groups_urine:
                    continue
                # simulation
                plots[kp].add_data(
                    task=self.to_sid(f"task_{group}"),
                    xid="time",
                    yid=sid,
                    label=f"sim: {self.legends[group]}",
                    color=self.colors[group],
                )
                # data
                plots[kp].add_data(
                    dataset=self.to_sid(
                        f"{group}_cumulative amount"
                        if "cumulative" in name
                        else f"{name}_{group}"
                    ),
                    xid="time",
                    yid="mean",
                    yid_sd=None if sid == "Aurine_api" else "mean_sd",
                    count="count",
                    label=f"exp: {self.legends[group]}",
                    color=self.colors[group],
                    linestyle="" if "cumulative" in name else "-",
                )

        return self.figures_by_sid(fig)

    def figure_pd(self) -> dict[str, Figure]:
        """INR, PT, aPTT and anti-factor Xa activity."""
        fig = Figure(
            experiment=self,
            sid="PD",
            name=f"{self.__class__.__name__}",
            num_cols=2,
            num_rows=2,
            height=self.panel_height * 2,
            width=self.panel_width * 2,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        for kp, sid in enumerate(self.infos_pd):
            plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid])

        for kp, (sid, name) in enumerate(self.infos_pd.items()):
            for group in self.groups:
                # simulation
                plots[kp].add_data(
                    task=self.to_sid(f"task_{group}"),
                    xid="time",
                    yid=sid,
                    label=f"sim: {self.legends[group]}",
                    color=self.colors[group],
                )
                # data
                plots[kp].add_data(
                    dataset=self.to_sid(f"{name}_{group}"),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp: {self.legends[group]}",
                    color=self.colors[group],
                )

        return self.figures_by_sid(fig)

    def figure_scatter(self) -> dict[str, Figure]:
        """Anti-factor Xa activity against the apixaban concentration in plasma."""
        fig = Figure(
            experiment=self,
            sid="PD_scatter",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.labels["Carm_api"], unit=self.units["Carm_api"]),
            legend=True,
        )
        plots[0].set_yaxis(
            self.labels["COAG__antiXa_activity"],
            unit=self.units["COAG__antiXa_activity"],
            scale="linear",
        )
        for group in self.groups:
            plots[0].add_data(
                task=self.to_sid(f"task_{group}"),
                xid="Carm_api",
                yid="COAG__antiXa_activity",
                label=f"sim: {self.legends[group]}",
                color=self.colors[group],
            )
            plots[0].add_data(
                dataset=self.to_sid(f"apixaban_vs_xa_{group}"),
                xid="x",
                yid="y",
                label=f"exp individ: {self.legends[group]}",
                linestyle="",
                color="white",
                markeredgecolor=self.colors[group],
                marker=self.markers[group],
            )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Wang2016, output_dir=Wang2016.__name__)
