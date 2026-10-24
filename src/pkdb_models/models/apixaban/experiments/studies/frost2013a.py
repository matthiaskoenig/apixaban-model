"""Simulation experiment of the study Frost2013a."""

from typing import Any, ClassVar, override

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


class Frost2013a(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2013a.

    Multiple doses of apixaban (2.5, 5, 10 and 25 mg twice daily, 10 and 25 mg
    once daily) for 7 days in healthy fasted men.
    """

    #: the mean body weights of the panels (Tab1)
    bodyweights: ClassVar[dict[str, float]] = {
        "placebo": 78.9,
        "API2x2": 78.3,
        "API5x2": 72.3,
        "API10": 79.7,
        "API10x2": 70.5,
        "API25": 82.2,
        "API25x2": 82.3,
    }

    colors: ClassVar[dict[str, str]] = {
        "placebo": "tab:grey",
        "API2x2": "#fdd0a2",
        "API5x2": "#fd8d3c",
        "API10": "#e95e0d",
        "API10x2": "#e95e0d",
        "API25": "#7f2704",
        "API25x2": "#7f2704",
    }

    groups: ClassVar[list[str]] = list(colors.keys())

    doses: ClassVar[dict[str, float]] = {
        "placebo": 0,
        "API2x2": 2.5,
        "API5x2": 5,
        "API10": 10,
        "API10x2": 10,
        "API25": 25,
        "API25x2": 25,
    }

    inr: ClassVar[dict[str, float]] = {
        "placebo": 1.09,
        "API2x2": 1.12,
        "API5x2": 1.12,
        "API10": 1.12,
        "API10x2": 1.06,
        "API25": 1.15,
        "API25x2": 1.18,
    }

    aptt: ClassVar[dict[str, float]] = {
        "placebo": 29.94,
        "API2x2": 30.09,
        "API5x2": 31.39,
        "API10": 31.02,
        "API10x2": 28.78,
        "API25": 33.18,
        "API25x2": 30.09,
    }

    mpt: ClassVar[dict[str, float]] = {
        "placebo": 52.86,
        "API2x2": 46.74,
        "API5x2": 51.79,
        "API10": 42.86,
        "API10x2": 50.11,
        "API25": 51.43,
        "API25x2": 53.47,
    }

    infos_pk: ClassVar[dict[str, str]] = {
        "[Cve_api]": "apixaban",
    }

    infos_pd: ClassVar[dict[str, str]] = {"INR": "INR", "aPTT": "aPTT", "mPT": "mPT"}
    #: the INR of 10 mg once daily (`INR_API10`) is a copy of the INR of 5 mg
    #: twice daily in the curation, it is neither mapped nor plotted
    excluded_pd: ClassVar[set[str]] = {"INR_API10"}

    infos_scatter: ClassVar[dict[str, tuple[str, int]]] = {
        "apixaban_inr": ("INR", 0),
        "apixaban_aptt": ("aPTT", 1),
        "apixaban_mpt": ("mPT", 2),
        "apixaban_inr_mean": ("INR", 0),
        "apixaban_aPTT_mean": ("aPTT", 1),
        "apixaban_mPT_mean": ("mPT", 2),
    }

    def legend(self, group: str, kind: str) -> str:
        """Legend of a group, the dose and the regimen.

        Args:
            group: the group of the study.
            kind: `sim` or `exp`.
        """
        if group == "placebo":
            return f"{kind}: placebo"
        regimen = "BID" if "x2" in group else "QD"
        return f"{kind}: {self.doses[group]}mg PO {regimen}"

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1", "Fig3", "Fig4", "Fig4Mean"]:
            df = self.load_dataframe(fig_id)
            group_by = "x_label" if fig_id in ["Fig4", "Fig4Mean"] else "label"
            for label, df_label in df.groupby(group_by):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                if "apixaban" in label:
                    if fig_id in ["Fig4", "Fig4Mean"]:
                        dset.unit_conversion("x", 1 / self.Mr.api)
                    else:
                        dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[self.to_sid(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        for _kg, group in enumerate(self.groups):
            dose = self.doses[group]

            # doses every 12 hr (x2) or 24 hr, the last dose is followed by 50 hr
            if "x2" in group:
                interval = 12
                n_doses = 6 * 2 + 2
            else:
                interval = 24
                n_doses = 7

            tcsims[self.to_sid(group)] = Simulation(
                time_unit="hr",
                end=(n_doses - 1) * interval + 50,
                preinit_changes={
                    **self.default_changes(),
                    "BW": Q(self.bodyweights[group], "kg"),
                    "INR_ref": Q(self.inr[group], "dimensionless"),
                    "aPTT_ref": Q(self.aptt[group], "s"),
                    "mPT_ref": Q(self.mpt[group], "s"),
                    "PODOSE_api": Q(dose, "mg"),
                },
                changes=[
                    self.add_doses(
                        [interval * k for k in range(1, n_doses)],
                        {"PODOSE_api": Q(dose, "mg")},
                    ),
                ],
            )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for group in self.groups:
            # pharmacokinetics
            if "API" in group:
                for _k, sid in enumerate(self.infos_pk.keys()):
                    name = self.infos_pk[sid]

                    mappings[self.to_sid(f"fm_{name}_{group}")] = FitMapping(
                        self,
                        reference=FitData(
                            self,
                            dataset=self.to_sid(f"{name}_{group}"),
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
                            tissue=Tissue.PLASMA,
                            route=Route.PO,
                            application_form=ApplicationForm.TABLET,
                            dosing=Dosing.MULTIPLE,
                            health=Health.HEALTHY,
                            fasting=Fasting.FASTED,
                        ),
                    )
            # PD
            for _ks, sid in enumerate(self.infos_pd):
                name = self.infos_pd[sid]
                if f"{name}_{group}" in self.excluded_pd:
                    continue
                mappings[self.to_sid(f"fm_{group}_{name}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(f"{name}_{group}"),
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
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.MULTIPLE,
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
        """Figure of the pharmacokinetics of the once and twice daily doses."""
        fig = Figure(
            experiment=self,
            sid="Fig1",
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
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)
        plots[1].set_yaxis(self.label_api_plasma, unit=self.unit_api)

        for group in self.groups:
            if "API" in group:
                k = 1 if "x2" in group else 0
                for sid in self.infos_pk:
                    name = self.infos_pk[sid]

                    # simulation
                    plots[k].add_data(
                        task=self.to_sid(f"task_{group}"),
                        xid="time",
                        yid=sid,
                        label=self.legend(group, "sim"),
                        color=self.colors[group],
                    )
                    # data
                    plots[k].add_data(
                        dataset=self.to_sid(f"{name}_{group}"),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                        label=self.legend(group, "exp"),
                        color=self.colors[group],
                    )

        return self.figures_by_sid(fig)

    def figure_pd(self) -> dict[str, Figure]:
        """Figure of the pharmacodynamics of the once and twice daily doses."""
        fig = Figure(
            experiment=self,
            sid="Fig2",
            num_cols=3,
            name=f"{self.__class__.__name__}",
            num_rows=2,
            height=self.panel_height * 2,
            width=self.panel_width * 3 * 1.05,
            # the panels of a row share their curves, one legend per row
            settings={"legend_scope": "row"},
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )

        for ky, yid in enumerate(["INR", "aPTT", "mPT"]):
            plots[ky].set_yaxis(self.labels[yid], unit=self.units[yid])
            plots[ky + 3].set_yaxis(self.labels[yid], unit=self.units[yid])

        for group in self.groups:
            for ks, sid in enumerate(self.infos_pd):
                name = self.infos_pd[sid]
                if group == "placebo":
                    # placebo plotted in both plots
                    ks_items = [ks, ks + 3]
                elif "x2" in group:
                    ks_items = [ks + 3]
                else:
                    ks_items = [ks]

                for ks in ks_items:
                    # simulation
                    plots[ks].add_data(
                        task=self.to_sid(f"task_{group}"),
                        xid="time",
                        yid=sid,
                        label=self.legend(group, "sim"),
                        color=self.colors[group],
                    )
                    # data
                    if f"{name}_{group}" in self.excluded_pd:
                        continue
                    plots[ks].add_data(
                        dataset=self.to_sid(f"{name}_{group}"),
                        xid="time",
                        yid="mean",
                        count="count",
                        label=self.legend(group, "exp"),
                        color=self.colors[group],
                    )

        return self.figures_by_sid(fig)

    def figure_scatter(self) -> dict[str, Figure]:
        """Figure of the pharmacodynamics against apixaban in plasma."""

        # keyword arguments of `Plot.add_data`, passed on to matplotlib
        def style_mean(group: str) -> dict[str, dict[str, Any]]:
            return {
                "kwargs_sim": {
                    "color": self.colors[group],
                    "linestyle": "solid",
                },
                "kwargs_exp": {
                    "marker": "s",
                    "linestyle": "",
                    "color": self.colors[group],
                    "markeredgecolor": "black",
                    "yid_sd": "y_sd",
                    "xid_sd": "x_sd",
                },
            }

        style_indiv: dict[str, dict[str, Any]] = {
            "kwargs_sim": {"color": "black", "linestyle": "", "marker": "o"},
            "kwargs_exp": {
                "label": "exp individ",
                "color": "white",
                "markeredgecolor": "black",
                "marker": "o",
                "linestyle": "",
            },
        }

        fig_scatter = Figure(
            experiment=self,
            sid="PD_scatter",
            name=self.__class__.__name__,
            num_rows=2,
            num_cols=3,
            height=self.panel_height * 2 * 1.4,
            width=self.panel_width * 3 * 1.3,
        )
        plots_scatter = fig_scatter.create_plots(
            xaxis=Axis(self.labels["[Cve_api]"], unit=self.units["[Cve_api]"]),
            legend=True,
        )

        for label, (sid, kp) in self.infos_scatter.items():
            plots_scatter[kp].set_yaxis(
                self.labels[sid], unit=self.units[sid], scale="linear"
            )
            plots_scatter[kp + 3].set_yaxis(
                self.labels[sid], unit=self.units[sid], scale="linear"
            )

            if "mean" in label:
                for group in self.groups:
                    style = style_mean(group)
                    if group != "placebo":
                        k = kp + 3 if "x2" in group else kp
                        # simulation
                        plots_scatter[k].add_data(
                            task=self.to_sid(f"task_{group}"),
                            xid="[Cve_api]",
                            yid=sid,
                            label=self.legend(group, "sim"),
                            **style["kwargs_sim"],
                        )
                        # data
                        plots_scatter[k].add_data(
                            dataset=self.to_sid(f"{label}_{group}"),
                            xid="x",
                            yid="y",
                            label=self.legend(group, "exp"),
                            **style["kwargs_exp"],
                        )
            else:
                style = style_indiv
                # data
                plots_scatter[kp].add_data(
                    dataset=self.to_sid(label), xid="x", yid="y", **style["kwargs_exp"]
                )
                plots_scatter[kp + 3].add_data(
                    dataset=self.to_sid(label), xid="x", yid="y", **style["kwargs_exp"]
                )

        return self.figures_by_sid(fig_scatter)


if __name__ == "__main__":
    MODEL.run_experiments(Frost2013a, output_dir=Frost2013a.__name__)
