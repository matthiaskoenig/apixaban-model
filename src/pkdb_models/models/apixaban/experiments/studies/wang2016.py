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
    dose). The renal function of the ESRD patients is the class of end stage
    renal disease of the renal map, but the measured renal clearance of
    apixaban is 0.02 against 11.3 ml/min in the healthy subjects (3 of 8
    patients anuric): the model overestimates the urinary excretion of the
    patients. The urinary amounts are derived (CLR x AUCinf of Table 2).
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

    #: the renal function relative to a GFR of 101 ml/min: the measured
    #: creatinine clearance of the healthy subjects (125 ml/min), the class of
    #: end stage renal disease of the renal map for the patients
    renal_functions: ClassVar[dict[str, float]] = {
        "healthy": 125.0 / 101.0,
        "esrd_P1": ApixabanSimulationExperiment.renal_map["End stage renal disease"],
        "esrd_P2": ApixabanSimulationExperiment.renal_map["End stage renal disease"],
    }
    groups: ClassVar[list[str]] = [
        "healthy",
        "esrd_P1",
        "esrd_P2",
    ]
    #: the groups with urinary data
    groups_urine: ClassVar[list[str]] = ["healthy", "esrd_P2"]
    infos_pk: ClassVar[dict[str, str]] = {
        "[Cve_api]": "apixaban",
        "Aurine_api": "cumulative amount",
    }
    infos_pd: ClassVar[dict[str, str]] = {
        "INR": "inr",
        "PT": "pt",
        "aPTT": "aptt",
        "antiXa_activity": "xa",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id, group_id in zip(
            ["Fig1", "Fig2", "Fig3", "Tab2"],
            ["label", "label", "x_label", "label"],
            strict=True,
        ):
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby(group_id):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                if label.startswith("apixaban_"):
                    if fig_id == "Fig3":
                        dset.unit_conversion("x", 1 / self.Mr.api)
                    else:
                        dset.unit_conversion("mean", 1 / self.Mr.api)
                if fig_id == "Tab2":
                    if "cumulative" in label:
                        dset.unit_conversion("mean", 1 / self.Mr.api)
                        dsets[self.to_sid(label)] = dset
                else:
                    dsets[self.to_sid(label)] = dset

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
                    "KI__f_renal_function": Q(
                        self.renal_functions[group], "dimensionless"
                    ),
                    "INR_ref": Q(self.inrs[group], "dimensionless"),
                    "aPTT_ref": Q(self.aptts[group], "second"),
                    "PT_ref": Q(self.pts[group], "second"),
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
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_{group}"),
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.URINE if "cumulative" in name else Tissue.PLASMA,
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
                    yid_sd="mean_sd",
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
            xaxis=Axis(self.labels["[Cve_api]"], unit=self.units["[Cve_api]"]),
            legend=True,
        )
        plots[0].set_yaxis(
            self.labels["antiXa_activity"],
            unit=self.units["antiXa_activity"],
            scale="linear",
        )
        for group in self.groups:
            plots[0].add_data(
                task=self.to_sid(f"task_{group}"),
                xid="[Cve_api]",
                yid="antiXa_activity",
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
