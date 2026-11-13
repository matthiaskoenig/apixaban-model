"""Simulation experiment of the study Frost2013a."""

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


class Frost2013a(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2013a.

    Multiple doses of apixaban (2.5, 5, 10 and 25 mg twice daily, 10 and 25 mg
    once daily) for 7 days in healthy fasted men.

    The subjects are men (48) and run on the male build.
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
        "Carm_api": "apixaban",
    }

    infos_pd: ClassVar[dict[str, str]] = {
        "COAG__INR": "INR",
        "COAG__aPTT": "aPTT",
        "COAG__mPT": "mPT",
    }

    #: the individual values against apixaban (Fig4) and their panel
    infos_scatter: ClassVar[dict[str, tuple[str, int]]] = {
        "apixaban_vs_inr": ("COAG__INR", 0),
        "apixaban_vs_aptt": ("COAG__aPTT", 1),
        "apixaban_vs_mpt": ("COAG__mPT", 2),
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
        for fig_id in ["Fig1", "Fig3", "Fig4"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                if fig_id == "Fig4":
                    dset.unit_conversion("x", 1 / self.Mr["api"])
                elif "apixaban" in label:
                    dset.unit_conversion("mean", 1 / self.Mr["api"])
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
                    "COAG__INR_ref": Q(self.inr[group], "dimensionless"),
                    "COAG__aPTT_ref": Q(self.aptt[group], "s"),
                    "COAG__mPT_ref": Q(self.mpt[group], "s"),
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

        for ky, yid in enumerate(["COAG__INR", "COAG__aPTT", "COAG__mPT"]):
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
        """Figure of the pharmacodynamics against apixaban in plasma.

        The individual values of all doses (Fig4) in both rows, the simulations
        of the once daily doses in the upper and of the twice daily doses in
        the lower row. The means of the paper's figure are not curated.
        """
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
            xaxis=Axis(self.labels["Carm_api"], unit=self.units["Carm_api"]),
            legend=True,
        )

        for label, (sid, kp) in self.infos_scatter.items():
            for k in [kp, kp + 3]:
                plots_scatter[k].set_yaxis(
                    self.labels[sid], unit=self.units[sid], scale="linear"
                )
            for group in self.groups:
                if group == "placebo":
                    continue
                plots_scatter[kp + 3 if "x2" in group else kp].add_data(
                    task=self.to_sid(f"task_{group}"),
                    xid="Carm_api",
                    yid=sid,
                    label=self.legend(group, "sim"),
                    color=self.colors[group],
                    linestyle="solid",
                )
            for k in [kp, kp + 3]:
                plots_scatter[k].add_data(
                    dataset=self.to_sid(label),
                    xid="x",
                    yid="y",
                    label="exp individ",
                    color="white",
                    markeredgecolor="black",
                    marker="o",
                    linestyle="",
                )

        return self.figures_by_sid(fig_scatter)


if __name__ == "__main__":
    MODEL.run_experiments(Frost2013a, output_dir=Frost2013a.__name__)
