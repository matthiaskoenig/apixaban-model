"""Simulation experiment of the study Frost2021a."""

import math
from collections.abc import Sequence
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


class Frost2021a(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2021a.

    A single oral dose of 5 mg apixaban in healthy subjects and subjects with
    mild (Child-Pugh A) or moderate (Child-Pugh B) hepatic impairment, fasted.
    The Child-Pugh classes are the severities `CP_severity` 1 and 2
    (`cirrhosis_map`).

    No group has a majority of women (healthy 7 women of 16, mild hepatic
    impairment 4 of 8, moderate 3 of 8); all run on the male build.
    """

    groups: ClassVar[list[str]] = ["healthy", "mild", "moderate"]
    groups_short: ClassVar[dict[str, str]] = {
        "healthy": "healthy",
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
    #: the 24-h creatinine clearance of the groups (Table 1) [ml/min], the GFR
    #: of the simulation (`renal_function`)
    crcl: ClassVar[dict[str, float]] = {
        "healthy": 114.61,
        "mild": 122.00,
        "moderate": 111.68,
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

    #: the sources of the data and the prefix of their datasets by the
    #: prefix of the labels of the curation
    sources: ClassVar[dict[str, tuple[str, str]]] = {
        "Fig1": ("apixaban_", "apixaban_"),
        "Fig2A": ("apixaban_vs_antiXa_", "apixaban_vs_xa_"),
        "Fig2B": ("antiXa_", "xa_"),
        "Fig3A": ("inr_change_", "inr_"),
        "Fig3B": ("aPTT_change_", "aPTT_"),
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id, (prefix, sid_prefix) in self.sources.items():
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                if fig_id == "Fig2A":
                    dset.unit_conversion("x", 1 / self.Mr["api"])
                elif fig_id == "Fig1":
                    dset.unit_conversion("mean", 1 / self.Mr["api"])
                dsets[self.to_sid(sid_prefix + label.removeprefix(prefix))] = dset

        # the urinary amounts over 72 hr are not reported (nor curated): the
        # renal clearance of the study is the amount in urine over the AUC(0-72),
        # so the amount is the renal clearance times the AUC(0-72) (geometric
        # means of Tab2)
        df = self.load_dataframe("Tab2")
        for group in self.groups:
            clr = df[df["label"] == f"clearance_renal_apixaban_plasma_API5_{group}"]
            auc = df[df["label"] == f"auc_end_apixaban_plasma_API5_{group}"]
            amount = (
                Q(clr["gmean"].iloc[0], clr["unit"].iloc[0])
                * Q(auc["gmean"].iloc[0], auc["unit"].iloc[0])
            ).to("mg")
            df_amount = pd.DataFrame(
                {
                    "time": auc["time"].to_numpy(),
                    "time_unit": auc["time_unit"].to_numpy(),
                    "count": auc["count"].to_numpy(),
                    "gmean": [amount.magnitude],
                    "gmean_unit": ["mg"],
                }
            )
            dset = DataSet.from_df(df_amount, self.ureg)
            dset.unit_conversion("gmean", 1 / self.Mr["api"])
            dsets[f"cumulative_amount_{group}"] = dset

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
                    "CP_severity": Q(self.cirrhosis[group], "dimensionless"),
                    "HEIGHT": Q(self.bodyheights[group], "cm"),
                    "COAG__INR_ref": Q(self.inr_ref[group], "dimensionless"),
                    "COAG__aPTT_ref": Q(self.aptt_ref[group], "s"),
                    "f_renal_function": self.renal_function(
                        self.crcl[group],
                        bw=self.bodyweights[group],
                        height=self.bodyheights[group],
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
            return "Carm_api"
        if dset_label.startswith("cumulative_amount"):
            return "Aurine_api"
        if dset_label.startswith("inr_"):
            return "COAG__INR"
        if dset_label.startswith("aPTT_"):
            return "COAG__aPTT"
        if dset_label.startswith(("xa_", "apixaban_vs_xa_")):
            return "COAG__antiXa_activity"
        raise ValueError(f"No observable for the dataset '{dset_label}'.")

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings: dict[str, FitMapping] = {}

        # the individual values against the concentration are plotted only
        for dset_label in self._pk_labels() + self._pd_labels():
            observable_id = self._label_to_observable(dset_label)
            if observable_id == "COAG__INR":
                observable_id = "COAG__INR_relchange"
            elif observable_id == "COAG__aPTT":
                observable_id = "COAG__aPTT_relchange"

            group_of_label = self._label_to_group(dset_label, self.groups)
            # the urinary amounts are geometric means without a spread
            is_urine = observable_id == "Aurine_api"
            tissue = Tissue.URINE if is_urine else Tissue.PLASMA

            mappings[self.to_sid(f"fm_po_{dset_label}")] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=dset_label,
                    xid="time",
                    yid="gmean" if is_urine else "mean",
                    yid_sd=None if is_urine else "mean_sd",
                    count="count",
                ),
                observable=FitData(
                    self,
                    task=self.to_sid(f"task_{group_of_label}"),
                    xid="time",
                    yid=observable_id,
                ),
                metadata=PKPDMappingMetaData(
                    tissue=tissue,
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
            self.labels["Carm_api"], unit=self.units["Carm_api"], scale="linear"
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
                yid="Carm_api" if kp == 0 else "Aurine_api",
                label=f"sim {self.groups_short[group]}: 5mg PO",
                color=self.colors[group],
            )
            plots[kp].add_data(
                dataset=dset_label,
                xid="time",
                yid="gmean" if kp == 1 else "mean",
                yid_sd=None if kp == 1 else "mean_sd",
                count="count",
                label=f"exp {self.groups_short[group]}: 5mg PO",
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
            # one legend right of the panels, which share their curves (inside,
            # the legend covers the error bars)
            settings={"legend_scope": "row", "legend_fontsize": 13},
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )

        cfg = {
            0: ("COAG__INR_relchange", "inr_"),
            1: ("COAG__aPTT_relchange", "aPTT_"),
            2: ("COAG__antiXa_activity", "xa_"),
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
                        label=f"sim {self.groups_short[group]}: 5mg PO",
                        color=self.colors[group],
                    )
                    plots[kp].add_data(
                        dataset=dset_label,
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                        label=f"exp {self.groups_short[group]}: 5mg PO",
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
            xaxis=Axis(self.labels["Carm_api"], unit=self.units["Carm_api"]),
            legend=True,
        )
        plots[0].set_yaxis(
            self.labels["COAG__antiXa_activity"],
            unit=self.units["COAG__antiXa_activity"],
            scale="linear",
        )
        is_legend = True
        for dset_label in self._scatter_labels():
            group = self._label_to_group(dset_label, self.groups)
            plots[0].add_data(
                task=self.to_sid(f"task_{group}"),
                xid="Carm_api",
                yid="COAG__antiXa_activity",
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
                label=f"exp individ {self.groups_short[group]}: 5mg PO",
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
