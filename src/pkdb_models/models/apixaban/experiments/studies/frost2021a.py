"""Simulation experiment of the study Frost2021a."""

import math
from collections.abc import Sequence
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


class Frost2021a(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2021a.

    A single oral dose of 5 mg apixaban in healthy subjects and subjects with
    mild (Child-Pugh A) or moderate (Child-Pugh B) hepatic impairment, fasted.
    """

    groups: ClassVar[list[str]] = ["healthy", "mild", "moderate"]
    groups_short: ClassVar[dict[str, str]] = {
        "mild": "MiHI",
        "moderate": "MoHI",
    }
    colors: ClassVar[dict[str, str]] = {
        "healthy": ApixabanSimulationExperiment.cirrhosis_colors["Control"],
        "mild": ApixabanSimulationExperiment.cirrhosis_colors["Mild cirrhosis"],
        "moderate": ApixabanSimulationExperiment.cirrhosis_colors["Moderate cirrhosis"],
    }
    bodyweights: ClassVar[dict[str, float]] = {
        "healthy": 77.6,
        "mild": 86.1,
        "moderate": 83.8,
    }
    #: height [cm] from the body weight and the BMI (Table 1)
    bodyheights: ClassVar[dict[str, float]] = {
        "healthy": 100 * math.sqrt(77.6 / 27.4),
        "mild": 100 * math.sqrt(86.1 / 29),
        "moderate": 100 * math.sqrt(83.8 / 28.4),
    }
    cirrhosis: ClassVar[dict[str, float]] = {
        "healthy": ApixabanSimulationExperiment.cirrhosis_map["Control"],
        "mild": ApixabanSimulationExperiment.cirrhosis_map["Mild cirrhosis"],
        "moderate": ApixabanSimulationExperiment.cirrhosis_map["Moderate cirrhosis"],
    }
    #: the renal function relative to the GFR of 101 ml/min of the model, from
    #: the 24-h creatinine clearance of the groups [ml/min] (Table 1)
    renal_function: ClassVar[dict[str, float]] = {
        "healthy": 114.61 / 101,
        "mild": 122.00 / 101,
        "moderate": 111.68 / 101,
    }
    #: baseline INR and aPTT [s] of the groups (Results)
    inr_ref: ClassVar[dict[str, float]] = {
        "healthy": 1.04,
        "mild": 1.17,
        "moderate": 1.15,
    }
    aptt_ref: ClassVar[dict[str, float]] = {
        "healthy": 29.9,
        "mild": 32.8,
        "moderate": 30.8,
    }
    markers: ClassVar[dict[str, str]] = {
        "healthy": "o",
        "mild": "*",
        "moderate": "^",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id, group_id in zip(
            ["Fig1", "Fig3", "Fig2a", "Fig2b", "Tab2"],
            ["label", "label", "x_label", "label", "label"],
            strict=True,
        ):
            df = self.load_dataframe(fig_id)
            if fig_id == "Fig2b":
                # the anti-factor Xa activity at 0 h and from 48 h on is the floor
                # of the assay (0.10 to 0.11 IU/ml, values below the limit of
                # quantification), not mapped
                df = df[(df.time > 0) & (df.time < 48)]
            for label, df_label in df.groupby(group_id):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                if label.startswith("apixaban_"):
                    if fig_id == "Fig2a":
                        dset.unit_conversion("x", 1 / self.Mr.api)
                    else:
                        dset.unit_conversion("mean", 1 / self.Mr.api)
                if fig_id != "Tab2":
                    dsets[self.to_sid(label)] = dset
                if label.startswith("cumulative amount"):
                    dset["mean"] = dset["geomean"]
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                    dsets[self.to_sid(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims: dict[str, Simulation] = {}
        for group in self.groups:
            tcsims[self.to_sid(group)] = Simulation(
                time_unit="hr",
                end=100,
                preinit_changes={
                    **self.default_changes(),
                    "PODOSE_api": Q(5, "mg"),
                    "BW": Q(self.bodyweights[group], "kg"),
                    "f_cirrhosis": Q(self.cirrhosis[group], "dimensionless"),
                    "HEIGHT": Q(self.bodyheights[group], "cm"),
                    "INR_ref": Q(self.inr_ref[group], "dimensionless"),
                    "aPTT_ref": Q(self.aptt_ref[group], "s"),
                    "KI__f_renal_function": Q(
                        self.renal_function[group], "dimensionless"
                    ),
                },
            )
        return tcsims

    def _pk_labels(self) -> list[str]:
        return [
            k
            for k in self._datasets
            if (
                (k.startswith("apixaban_") and k.endswith("_log"))
                or (k.startswith("cumulative"))
            )
            and not k.startswith("apixaban_vs_xa_")
        ]

    def _pd_labels(self) -> list[str]:
        return [k for k in self._datasets if k.startswith(("inr_", "aPTT_", "xa_"))]

    def _scatter_labels(self) -> list[str]:
        return [k for k in self._datasets if k.startswith("apixaban_vs_xa_")]

    @staticmethod
    def _label_to_group(
        dset_label: str, groups: Sequence[str] = ("healthy", "mild", "moderate")
    ) -> str:
        for g in groups:
            if dset_label.endswith((f"_{g}", f"_{g}_log")):
                return g
        return "healthy"

    @staticmethod
    def _label_to_observable(dset_label: str) -> str:
        if dset_label.startswith("apixaban_"):
            return "[Cve_api]"
        if dset_label.startswith("cumulative_amount"):
            return "Aurine_api"
        if dset_label.startswith("inr_"):
            return "INR"
        if dset_label.startswith("aPTT_"):
            return "aPTT"
        if dset_label.startswith(("xa_", "apixaban_vs_xa_")):
            return "antiXa_activity"
        raise ValueError(f"No observable for the dataset '{dset_label}'.")

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings: dict[str, FitMapping] = {}

        all_labels = self._pk_labels() + self._pd_labels() + self._scatter_labels()
        scatter_set = set(self._scatter_labels())

        for dset_label in all_labels:
            observable_id = self._label_to_observable(dset_label)
            if observable_id == "INR":
                observable_id = "INR_relchange"
            elif observable_id == "aPTT":
                observable_id = "aPTT_relchange"

            group_of_label = self._label_to_group(dset_label, self.groups)

            is_scatter = dset_label in scatter_set
            if is_scatter:
                continue
            ref_xid = "x" if is_scatter else "time"
            ref_yid = "y" if is_scatter else "mean"
            ref_yid_sd = "" if is_scatter else "mean_sd"
            obs_xid = "[Cve_api]" if is_scatter else "time"
            # # FIXME: set obs_yid correctly for scatter

            mappings[self.to_sid(f"fm_po_{dset_label}")] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=dset_label,
                    xid=ref_xid,
                    yid=ref_yid,
                    yid_sd=None if observable_id == "Aurine_api" else ref_yid_sd,
                    count="count",
                ),
                observable=FitData(
                    self,
                    task=self.to_sid(f"task_{group_of_label}"),
                    xid=obs_xid,
                    yid=observable_id,
                ),
                metadata=PKPDMappingMetaData(
                    tissue=Tissue.URINE
                    if observable_id == "Aurine_api"
                    else Tissue.PLASMA,
                    route=Route.PO,
                    application_form=ApplicationForm.TABLET,
                    dosing=Dosing.SINGLE,
                    health=Health.HEALTHY
                    if group_of_label == "healthy"
                    else Health.HEPATIC_IMPAIRMENT,
                    fasting=Fasting.FASTED,
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
        """Figure of the pharmacokinetics."""
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
        plots[0].set_yaxis(
            self.labels["[Cve_api]"], unit=self.units["[Cve_api]"], scale="linear"
        )
        plots[1].set_yaxis(
            self.labels["Aurine_api"], unit=self.units["Aurine_api"], scale="linear"
        )
        # Data
        for dset_label in self._pk_labels():
            group = self._label_to_group(dset_label, self.groups)
            kp = 1 if dset_label.startswith("cumulative_amount") else 0
            plots[kp].add_data(
                task=self.to_sid(f"task_{group}"),
                xid="time",
                yid="[Cve_api]" if kp == 0 else "Aurine_api",
                label="sim: 5mg PO"
                if group == "healthy"
                else f"sim {self.groups_short[group]}: 5mg PO",
                color=self.colors[group],
            )
            plots[kp].add_data(
                dataset=dset_label,
                xid="time",
                yid="mean",
                yid_sd=None if kp == 1 else "mean_sd",
                count="count",
                label="exp: 5mg PO"
                if group == "healthy"
                else f"exp {self.groups_short[group]}: 5mg PO",
                color=self.colors[group],
                linestyle="dashed" if kp == 0 else "",
            )
        return self.figures_by_sid(fig)

    def figure_pd(self) -> dict[str, Figure]:
        """Figure of the pharmacodynamics."""
        fig = Figure(
            experiment=self,
            sid="PD",
            name=f"{self.__class__.__name__}",
            num_cols=3,
            height=self.panel_height,
            width=self.panel_width * 3 * 1.05,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )

        cfg = {
            0: ("INR_relchange", "inr_"),
            1: ("aPTT_relchange", "aPTT_"),
            2: ("antiXa_activity", "xa_"),
        }

        for kp in range(3):
            observable_id, prefix = cfg[kp]
            y_unit = self.units.get(observable_id, None)
            plots[kp].set_yaxis(
                self.labels.get(observable_id, observable_id),
                unit=y_unit,
                scale="linear",
            )

            for dset_label in self._pd_labels():
                if dset_label.startswith(prefix):
                    group = self._label_to_group(dset_label, self.groups)
                    plots[kp].add_data(
                        task=self.to_sid(f"task_{group}"),
                        xid="time",
                        yid=observable_id,
                        label="sim: 5mg PO"
                        if group == "healthy"
                        else f"sim {self.groups_short[group]}: 5mg PO",
                        color=self.colors[group],
                    )
                    plots[kp].add_data(
                        dataset=dset_label,
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                        label="exp: 5mg PO"
                        if group == "healthy"
                        else f"exp {self.groups_short[group]}: 5mg PO",
                        color=self.colors[group],
                    )

        return self.figures_by_sid(fig)

    def figure_scatter(self) -> dict[str, Figure]:
        """Figure of the anti-factor Xa activity against the plasma concentration."""
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
        is_legend = True
        for dset_label in self._scatter_labels():
            group = self._label_to_group(dset_label, self.groups)
            plots[0].add_data(
                task=self.to_sid(f"task_{group}"),
                xid="[Cve_api]",
                yid="antiXa_activity",
                label="sim: 5mg PO" if is_legend else "",
                color="black",
                linestyle="solid",
            )
            is_legend = False
            plots[0].add_data(
                dataset=dset_label,
                xid="x",
                yid="y",
                count="count",
                label="exp individ: 5mg PO"
                if group == "healthy"
                else f"exp individ {self.groups_short[group]}: 5mg PO",
                linestyle="",
                marker=self.markers[group],
                color="white",
                markeredgecolor="tab:grey"
                if group == "healthy"
                else self.colors[group],
                markeredgewidth=1,
            )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Frost2021a, output_dir=Frost2021a.__name__)
