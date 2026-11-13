"""Simulation experiment of the study Frost2018."""

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


class Frost2018(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2018.

    Sequential ascending single oral doses of 2.5, 10, 25 and 50 mg apixaban
    (form not reported) or placebo in healthy Japanese and Caucasian men,
    fasted; pharmacokinetics and the change of mPT, aPTT and INR.

    The subjects are men (32) and run on the male build.
    """

    doses: ClassVar[dict[str, float]] = {
        "placebo": 0,
        "API2.5": 2.5,
        "API10": 10.0,
        "API25": 25.0,
        "API50": 50.0,
    }
    dose_keys: ClassVar[list[str]] = list(doses.keys())
    colors: ClassVar[dict[str, str]] = {
        "placebo": "tab:grey",
        "API2.5": "#fdae6b",
        "API10": "#f16913",
        "API25": "#c44103",
        "API50": "#7f2704",
    }
    ethnicities: ClassVar[dict[str, str]] = {
        "japanese": "D",
        "caucasian": "s",
    }
    #: body weight [kg] of the apixaban groups (Table 1), the placebo is
    #: simulated with the group of its ethnicity
    bodyweight: ClassVar[dict[str, float]] = {
        "japanese": 65.6,
        "caucasian": 70.1,
    }
    #: height [cm] from the body weight and the BMI 22.0 and 21.9 kg/m^2
    bodyheight: ClassVar[dict[str, float]] = {
        "japanese": 100 * math.sqrt(65.6 / 22.0),
        "caucasian": 100 * math.sqrt(70.1 / 21.9),
    }
    info_fig1: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
        "Aurine_api": "cumulative amount",
    }

    def dose_label(self, key: str) -> str:
        """Label of a dose of the legends."""
        return "placebo" if key == "placebo" else f"{self.doses[key]:g}mg PO"

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1", "Fig3"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                if (
                    "API" in label
                    and "mPT" not in label
                    and "aPTT" not in label
                    and "inr" not in label
                ):
                    dset.unit_conversion("mean", 1 / self.Mr["api"])
                dsets[self.to_sid(label)] = dset

        # the urinary amounts at 72 hr (Tab2), without a spread
        df = self.load_dataframe("Tab2")
        for key in self.dose_keys:
            if key == "placebo":
                continue
            for ethnicity in self.ethnicities:
                df_label = df[
                    df["label"]
                    == f"cumulative_amount_apixaban_urine_{key.replace('.', '_')}"
                    f"_{ethnicity}"
                ]
                dset = DataSet.from_df(df_label, self.ureg)
                dset.unit_conversion("mean", 1 / self.Mr["api"])
                dsets[self.to_sid(f"cumulative amount_{ethnicity}_{key}")] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims: dict[str, Simulation] = {}
        for key, dose in self.doses.items():
            for group, bw in self.bodyweight.items():
                tcsims[self.to_sid(f"{key}_{group}")] = Simulation(
                    time_unit="hr",
                    end=100,
                    preinit_changes={
                        **self.default_changes(),
                        "PODOSE_api": Q(dose, "mg"),
                        "BW": Q(bw, "kg"),
                        "HEIGHT": Q(self.bodyheight[group], "cm"),
                    },
                )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}

        mapping_configs = [
            # prefix of the key, suffix of the dataset, observable
            ("api", "", "Carm_api"),
            ("cumulative amount", "", "Aurine_api"),
            ("mPT", "_mPT", "COAG__mPT_relchange"),
            ("aPTT", "_aPTT", "COAG__aPTT_relchange"),
            ("INR", "_inr", "COAG__INR_relchange"),
        ]

        for prefix, dataset_suffix, observable in mapping_configs:
            for key in self.doses:
                if key == "placebo" and prefix in ["api", "cumulative amount"]:
                    continue

                for ethnicity in self.ethnicities:
                    label = (
                        f"{prefix}_{ethnicity}_{key}"
                        if prefix == "cumulative amount"
                        else f"{ethnicity}{dataset_suffix}_{key}"
                    )
                    mapping_id = f"fm_{prefix}_{key}_{ethnicity}"
                    tissue = (
                        Tissue.URINE if prefix == "cumulative amount" else Tissue.PLASMA
                    )

                    mappings[self.to_sid(mapping_id)] = FitMapping(
                        self,
                        reference=FitData(
                            self,
                            dataset=self.to_sid(label),
                            xid="time",
                            yid="mean",
                            count="count",
                        ),
                        observable=FitData(
                            self,
                            task=self.to_sid(f"task_{key}_{ethnicity}"),
                            xid="time",
                            yid=observable,
                        ),
                        metadata=PKPDMappingMetaData(
                            tissue=tissue,
                            route=Route.PO,
                            # the form of the doses is not reported
                            application_form=ApplicationForm.NR,
                            dosing=Dosing.SINGLE,
                            health=Health.HEALTHY,
                            fasting=Fasting.FASTED,
                        ),
                    )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figures_pk(),
            **self.figure_pd(),
        }

    def figures_pk(self) -> dict[str, Figure]:
        """Figure of the pharmacokinetics."""
        fig = Figure(
            experiment=self,
            sid="Fig1",
            num_rows=2,
            num_cols=2,
            name=f"{self.__class__.__name__}",
            height=self.panel_height * 2,
            width=self.panel_width * 2,
            # one legend per row, right of the panels, which share their curves
            settings={"legend_scope": "row", "legend_fontsize": 13},
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )

        # Configuration for each plot
        plot_configs = [
            (0, "Carm_api", self.label_api_plasma, self.unit_api, True),
            (1, "Aurine_api", self.label_api_urine, self.unit_api_urine, True),
        ]

        for plot_idx, yid, ylabel, yunit, _skip_placebo_data in plot_configs:
            plots[plot_idx].set_yaxis(ylabel, unit=yunit)
            plots[plot_idx + 2].set_yaxis(ylabel, unit=yunit)

            # simulation
            for key, dose in self.doses.items():
                if dose == 0:
                    continue
                for ethnicity in self.bodyweight:
                    idx = plot_idx + 2 if ethnicity == "caucasian" else plot_idx
                    task_id = f"task_{key}_{ethnicity}"
                    plots[idx].add_data(
                        task=self.to_sid(task_id),
                        xid="time",
                        yid=yid,
                        label=f"sim {ethnicity}: {dose:g} mg PO",
                        color=self.colors.get(key),
                    )
                    label = (
                        f"{ethnicity}_{key}"
                        if yid == "Carm_api"
                        else f"cumulative amount_{ethnicity}_{key}"
                    )
                    plots[idx].add_data(
                        dataset=self.to_sid(label),
                        xid="time",
                        yid="mean",
                        count="count",
                        label=f"exp {ethnicity}: {dose:g} mg PO",
                        color=self.colors[key],
                        marker=self.ethnicities[ethnicity],
                    )

        return self.figures_by_sid(fig)

    def figure_pd(self) -> dict[str, Figure]:
        """Figure of the pharmacodynamics."""
        fig = Figure(
            experiment=self,
            sid="Fig2",
            num_rows=2,
            num_cols=3,
            name=f"{self.__class__.__name__}",
            height=self.panel_height * 2 * 1.05,
            width=self.panel_width * 3 * 1.05,
            # one legend per row, right of the panels, which share their curves
            settings={"legend_scope": "row", "legend_fontsize": 13},
        )
        plots = fig.create_plots(
            # the data cover 24 h
            xaxis=Axis(self.label_time, unit=self.unit_time, min=-1, max=30),
            legend=True,
        )

        # Configuration for each plot
        plot_configs = [
            (
                0,
                "COAG__mPT_relchange",
                self.labels["COAG__mPT_relchange"],
                "%",
                "_mPT",
                False,
            ),  # mPT plot
            (
                1,
                "COAG__aPTT_relchange",
                self.labels["COAG__aPTT_relchange"],
                "%",
                "_aPTT",
                False,
            ),  # aPTT plot
            (
                2,
                "COAG__INR_relchange",
                self.labels["COAG__INR_relchange"],
                "%",
                "_inr",
                False,
            ),
        ]

        for (
            plot_idx,
            yid,
            ylabel,
            yunit,
            dataset_suffix,
            _skip_placebo_data,
        ) in plot_configs:
            plots[plot_idx].set_yaxis(ylabel, unit=yunit)
            plots[plot_idx + 3].set_yaxis(ylabel, unit=yunit)

            # simulation
            for key in self.doses:
                for ethnicity in self.bodyweight:
                    idx = plot_idx + 3 if ethnicity == "caucasian" else plot_idx
                    task_id = f"task_{key}_{ethnicity}"
                    plots[idx].add_data(
                        task=self.to_sid(task_id),
                        xid="time",
                        yid=yid,
                        label=f"sim {ethnicity}: {self.dose_label(key)}",
                        color=self.colors.get(key),
                    )
                    label = f"{ethnicity}{dataset_suffix}_{key}"
                    plots[idx].add_data(
                        dataset=self.to_sid(label),
                        xid="time",
                        yid="mean",
                        count="count",
                        label=f"exp {ethnicity}: {self.dose_label(key)}",
                        color=self.colors[key],
                        marker=self.ethnicities[ethnicity],
                    )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Frost2018, output_dir=Frost2018.__name__)
