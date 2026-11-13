"""Simulation experiment of the study Frost2021."""

import math
from collections.abc import Callable
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
from sbmlsim.plot import Axis, Figure, Plot
from sbmlsim.simulation import Simulation

from pkdb_models.models.apixaban import MODEL
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)


class Frost2021(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2021.

    Intravenous single ascending doses (bolus of a solution, 0.5 to 5 mg) and a
    single oral dose of 5 mg (tablet) in the subjects of the 2.5 mg panel after
    a washout, in healthy men fasted for at least 10 h.

    The subjects are men (40) and run on the male build.
    """

    #: body weight [kg] of the panels (Table 1); 5 of the 6 subjects of the
    #: 2.5 mg panel received the oral dose
    bodyweights: ClassVar[dict[str, float]] = {
        "group1": 75.8,
        "group2": 74.8,
        "group3": 80.6,
        "group4": 82.4,
        "group5": 83.1,
        "group_po": 80.6,
    }
    doses: ClassVar[dict[str, float]] = {
        "group1": 0.5,
        "group2": 1.25,
        "group3": 2.5,
        "group4": 3.75,
        "group5": 5,
        "group_po": 5,
    }
    inr: ClassVar[dict[str, float]] = {
        "group1": 1.12,
        "group2": 1.1,
        "group3": 1.13,
        "group4": 1.08,
        "group5": 1.08,
        "group_po": 1.14,
    }
    mpt: ClassVar[dict[str, float]] = {
        "group1": 54.5,
        "group2": 59.2,
        "group3": 54.9,
        "group4": 46.4,
        "group5": 53.9,
        "group_po": 53.3,
        # the baseline of the placebo series of Fig 2A
        "placebo": 53.35,
    }
    #: height [cm] from the body weight and the BMI of the panels (Table 1)
    bodyheight: ClassVar[dict[str, float]] = {
        "group1": 100 * math.sqrt(75.8 / 24.9),
        "group2": 100 * math.sqrt(74.8 / 24.2),
        "group3": 100 * math.sqrt(80.6 / 25),
        "group4": 100 * math.sqrt(82.4 / 26.7),
        "group5": 100 * math.sqrt(83.1 / 26.1),
        "group_po": 100 * math.sqrt(80.6 / 25),
    }
    routes: ClassVar[dict[str, str]] = {
        "group1": "IV0_5",
        "group2": "IV1_25",
        "group3": "IV2_5",
        "group4": "IV3_75",
        "group5": "IV5",
        "group_po": "PO5",
    }
    doses_colors: ClassVar[dict[float, str]] = {
        0: "tab:grey",
        0.5: "#fdae6b",
        1.25: "#fd8d3c",
        2.5: "#f16913",
        3.75: "#d94801",
        5: "#8c2d04",
    }
    markers: ClassVar[dict[str, str]] = {"IV": "s", "PO": "v"}
    linestyle: ClassVar[dict[str, str]] = {"IV": "solid", "PO": "dashed"}

    # Group information
    groups: ClassVar[list[str]] = list(bodyweights.keys())

    # Information mapping for metadata
    info_fig1: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
        "Aurine_api": "cumulative amount",
        "COAG__mPT": "prothrombin time",
        "COAG__antiXa_activity": "antiXa activity IU",
        "COAG__antiXa_activity_gram": "antiXa activity ng",
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
                    dset.unit_conversion("x", 1 / self.Mr["api"])
                elif "apixaban" in label:
                    dset.unit_conversion("mean", 1 / self.Mr["api"])
                dsets[self.to_sid(label)] = dset

        # the urinary amounts over 48 hr (Tab2), derived from the renal
        # clearance, without a spread
        df = self.load_dataframe("Tab2")
        for group in self.groups:
            route = self.routes[group]
            df_label = df[
                df["label"] == f"cumulative_amount_apixaban_kidney_{route}_{group}"
            ]
            dset = DataSet.from_df(df_label, self.ureg)
            dset.unit_conversion("mean", 1 / self.Mr["api"])
            dsets[self.to_sid(f"cumulative amount_{group}_{route}")] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        for group in self.groups:
            tcsims[self.to_sid(group)] = Simulation(
                time_unit="hr",
                end=62,
                preinit_changes={
                    **self.default_changes(),
                    "BW": Q(self.bodyweights[group], "kg"),
                    f"{self.routes[group][0:2]}DOSE_api": Q(self.doses[group], "mg"),
                    "HEIGHT": Q(self.bodyheight[group], "cm"),
                    "COAG__INR_ref": Q(self.inr[group], "dimensionless"),
                    "COAG__mPT_ref": Q(self.mpt[group], "s"),
                },
            )
        # placebo
        tcsims["placebo"] = Simulation(
            time_unit="hr",
            end=75,
            preinit_changes={
                **self.default_changes(),
                "BW": Q(78.7, "kg"),  # iv placebo taken
                "IVDOSE_api": Q(0, "mg"),
                "HEIGHT": Q(100 * math.sqrt(78.7 / 25), "cm"),
                "COAG__INR_ref": Q(1.11, "dimensionless"),
                "COAG__mPT_ref": Q(self.mpt["placebo"], "s"),
            },
        )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}

        # the dataset of an observable by route and group, None for a group
        # without data of the observable (the anti-factor Xa activity is only
        # reported for the groups which got 5 mg)
        antixa_groups = ["group5", "group_po"]
        dataset_ids: dict[str, Callable[[str, str], str | None]] = {
            "Carm_api": lambda route, group: f"{route}_apixaban",
            "Aurine_api": lambda route, group: f"cumulative amount_{group}_{route}",
            "COAG__mPT": lambda route, group: f"{route}_prothrombin time",
            "COAG__antiXa_activity_gram": lambda route, group: (
                f"{route}_Anti-factor Xa activity_ng"
                if group in antixa_groups
                else None
            ),
            "COAG__antiXa_activity": lambda route, group: (
                f"{route}_Anti-factor Xa activity_IU"
                if group in antixa_groups
                else None
            ),
        }

        for group in self.groups:
            route = self.routes[group]
            for sid, name in self.info_fig1.items():
                if sid in dataset_ids:
                    dset_id = dataset_ids[sid](route, group)

                    if dset_id is not None:
                        tissue = Tissue.URINE if sid == "Aurine_api" else Tissue.PLASMA
                        mappings[self.to_sid(f"fm_{name}_{group}_{route}")] = (
                            FitMapping(
                                self,
                                reference=FitData(
                                    self,
                                    dataset=self.to_sid(dset_id),
                                    xid="time",
                                    yid="mean",
                                    # the urinary amounts are derived from
                                    # the renal clearance, without an error
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
                                    route=Route.PO if route[:2] == "PO" else Route.IV,
                                    application_form=ApplicationForm.TABLET
                                    if route[:2] == "PO"
                                    else ApplicationForm.SOLUTION,
                                    dosing=Dosing.SINGLE,
                                    health=Health.HEALTHY,
                                    # fasted for 10 h regardless of the route
                                    fasting=Fasting.FASTED,
                                ),
                            )
                        )

        mappings["fm_placebo"] = FitMapping(
            self,
            reference=FitData(
                self,
                dataset="plb_prothrombin_time",
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
            ),
            observable=FitData(
                self,
                task="task_placebo",
                xid="time",
                yid="COAG__mPT",
            ),
            metadata=PKPDMappingMetaData(
                tissue=Tissue.PLASMA,
                route=Route.IV,  # assumed for mapping, otherwise placebo group contains IV and PO
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
            **self.figure_pk(),
            **self.figure_pd(),
            **self.figure_scatter(),
        }

    def figure_pk(self) -> dict[str, Figure]:
        """Figure of the pharmacokinetics."""
        data = {
            0: ["group1", "group2", "group3", "group4", "group5"],
            1: ["group5", "group_po"],
            2: ["group1", "group2", "group3", "group4", "group5"],
        }

        sids = {0: "Carm_api", 1: "Carm_api", 2: "Aurine_api"}

        y_axes = {
            0: (self.label_api_plasma, self.unit_api, "linear"),
            1: (self.label_api_plasma, self.unit_api, "linear"),
            2: (self.label_api_urine, self.unit_api_urine, "linear"),
        }

        # Dynamic dataset ID and SID determination
        datasets = {
            0: lambda route, group: f"{route}_apixaban",
            1: lambda route, group: f"{route}_apixaban",
            2: lambda route, group: f"cumulative amount_{group}_{route}",
        }

        fig = Figure(
            experiment=self,
            sid="FigPK",
            name=self.__class__.__name__,
            num_rows=1,
            num_cols=3,
            height=self.panel_height,
            width=self.panel_width * 3 * 1.05,
            # one legend right of the panels: inside, it hides the urine of the
            # low doses
            settings={"legend_scope": "row", "legend_fontsize": 13},
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )

        for kp, (label, unit, scale) in y_axes.items():
            plots[kp].set_yaxis(label, unit=unit, scale=scale)

        # Data inspection and group-level additions
        for kp, group_data in data.items():
            for group in group_data:
                dose = self.doses[group]
                route = self.routes[group]

                # Only process the current data if applicable
                if kp in datasets:
                    dset_id = datasets[kp](route, group)
                    sid = sids[kp]

                    # Add simulation data
                    plots[kp].add_data(
                        task=self.to_sid(f"task_{group}"),
                        xid="time",
                        yid=sid,
                        label=f"sim: {dose}mg {route[:2]}",
                        color=self.doses_colors[dose],
                        linestyle=self.linestyle[route[:2]],
                    )

                    # Add experimental data
                    plots[kp].add_data(
                        dataset=self.to_sid(dset_id),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                        label=f"exp: {dose}mg {route[:2]}",
                        color=self.doses_colors[dose],
                        marker=self.markers[route[:2]],
                    )

        return self.figures_by_sid(fig)

    def figure_pd(self) -> dict[str, Figure]:
        """Figure of the pharmacodynamics."""
        data = {
            0: ["group1", "group2", "group3", "group4", "group5"],
            1: ["group5", "group_po"],
            2: ["group5", "group_po"],
            3: ["group5", "group_po"],
        }

        sids = {
            0: "COAG__mPT",
            1: "COAG__mPT",
            2: "COAG__antiXa_activity",
            3: "COAG__antiXa_activity_gram",
        }

        y_axes = {
            0: (self.labels["COAG__mPT"], self.units["COAG__mPT"], "linear"),
            1: (self.labels["COAG__mPT"], self.units["COAG__mPT"], "linear"),
            2: (
                self.labels["COAG__antiXa_activity"],
                self.units["COAG__antiXa_activity"],
                "linear",
            ),
            3: (
                self.labels["COAG__antiXa_activity_gram"],
                self.units["COAG__antiXa_activity_gram"],
                "linear",
            ),
        }

        # Dynamic dataset ID and SID determination
        datasets = {
            0: lambda route: f"{route}_prothrombin time",
            1: lambda route: f"{route}_prothrombin time",
            2: lambda route: f"{route}_Anti-factor Xa activity_IU",
            3: lambda route: f"{route}_Anti-factor Xa activity_ng",
        }

        fig = Figure(
            experiment=self,
            sid="FigPD",
            name=self.__class__.__name__,
            num_rows=2,
            num_cols=2,
            height=self.panel_height * 2 * 1.05,
            width=self.panel_width * 2,
        )
        plots = fig.create_plots(
            # the data cover 24 h
            xaxis=Axis(self.label_time, unit=self.unit_time, min=-1, max=26),
            legend=True,
        )

        for kp, (label, unit, scale) in y_axes.items():
            plots[kp].set_yaxis(label, unit=unit, scale=scale)

        # Handle placebo plotting
        for kp_pt in [0, 1]:
            plots[kp_pt].add_data(
                task="task_placebo",
                xid="time",
                yid="COAG__mPT",
                label="sim: placebo",
                color=self.doses_colors[0],
            )
            plots[kp_pt].add_data(
                dataset="plb_prothrombin_time",
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
                label="exp: placebo",
                color=self.doses_colors[0],
            )

        # Data inspection and group-level additions
        for kp, group_data in data.items():
            for group in group_data:
                dose = self.doses[group]
                route = self.routes[group]

                # Only process the current data if applicable
                if kp in datasets:
                    dset_id = datasets[kp](route)
                    sid = sids[kp]

                    # Add simulation data
                    plots[kp].add_data(
                        task=self.to_sid(f"task_{group}"),
                        xid="time",
                        yid=sid,
                        label=f"sim: {dose}mg {route[:2]}",
                        color=self.doses_colors[dose],
                        linestyle=self.linestyle[route[:2]],
                    )

                    # Add experimental data
                    plots[kp].add_data(
                        dataset=self.to_sid(dset_id),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                        label=f"exp: {dose}mg {route[:2]}",
                        color=self.doses_colors[dose],
                        marker=self.markers[route[:2]],
                    )

        return self.figures_by_sid(fig)

    def figure_scatter(self) -> dict[str, Figure]:
        """Figures of the pharmacodynamics against the plasma concentration.

        The individual values of the paper (Fig3), the mPT of the intravenous
        doses of panel A and of the oral dose of panel B.
        """
        # sid, number of rows, number of columns
        figures_config = [
            ("mPT", 3, 2),
            ("Anti-factor Xa activity", 1, 2),
        ]

        # Create figures and plots
        figures: dict[str, Figure] = {}
        plots_lookup: dict[str, list[Plot]] = {}
        for sid, num_rows, num_cols in figures_config:
            fig = Figure(
                experiment=self,
                sid=self.to_sid(sid),
                name=self.__class__.__name__,
                num_rows=num_rows,
                num_cols=num_cols,
                height=self.panel_height * num_rows,
                width=self.panel_width * num_cols * 1.05,
            )
            plots = fig.create_plots(
                xaxis=Axis(self.label_api_plasma, unit=self.unit_api), legend=True
            )
            figures[self.to_sid(sid)] = fig
            plots_lookup[sid] = plots

        for kp, group in enumerate(self.groups):
            dose = self.doses[group]
            route = self.routes[group]
            panel = "B" if route[:2] == "PO" else "A"

            datasets = [
                (
                    "COAG__mPT",
                    plots_lookup["mPT"],
                    f"{route}_apixaban_vs_mPT_{panel}",
                ),
                (
                    "COAG__antiXa_activity",
                    plots_lookup["Anti-factor Xa activity"],
                    f"{route}_apixaban_vs_antiXa_IU",
                ),
            ]

            for yid, plots, dset_id in datasets:
                if yid == "COAG__antiXa_activity" and group not in [
                    "group5",
                    "group_po",
                ]:
                    continue
                current_kp = kp - 4 if yid == "COAG__antiXa_activity" else kp

                plots[current_kp].set_yaxis(
                    self.labels[yid], unit=self.units[yid], scale="linear"
                )
                # simulation
                plots[current_kp].add_data(
                    task=self.to_sid(f"task_{group}"),
                    xid="Carm_api",
                    yid=yid,
                    label=f"sim: {dose}mg {route[:2]}",
                    color=self.doses_colors[dose],
                    linestyle="solid",
                )
                plots[current_kp].add_data(
                    xid="x",
                    yid="y",
                    dataset=self.to_sid(dset_id),
                    count="count",
                    label=f"exp individ: {dose}mg {route[:2]}",
                    color="white",
                    markeredgecolor="tab:grey",
                    marker="o",
                    linestyle="",
                    markeredgewidth=1,
                )

        return figures


if __name__ == "__main__":
    MODEL.run_experiments(Frost2021, output_dir=Frost2021.__name__)
