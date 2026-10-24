"""Simulation experiment of the study Cui2013."""

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


class Cui2013(ApixabanSimulationExperiment):
    """Simulation experiment of Cui2013.

    12 healthy Chinese subjects: a single dose of 10 mg apixaban on day 1 and
    10 mg twice daily on days 4 to 9 (the last dose in the morning of day 9),
    in the fasted state.
    """

    dose = 10.0
    bodyweight = 63.1  # [kg]
    height = 163.7  # [cm]

    colors: ClassVar[dict[str, str]] = {
        "API10": "black",  # single dose
        "API10M": "tab:blue",  # multiple doses
    }
    interventions: ClassVar[list[str]] = list(colors.keys())

    infos_pk: ClassVar[dict[str, str]] = {
        "[Cve_api]": "apixaban",
    }
    #: the anti-Xa activity of day 1 (Fig2, the squares of the left panel);
    #: the anti-Xa activity of day 9 is not curated
    infos_pd: ClassVar[dict[str, str]] = {
        "antiXa_activity": "antiXa_activity",
    }
    pd_interventions: ClassVar[list[str]] = ["API10"]
    info_figpd_scatter: ClassVar[dict[str, str]] = {
        "antiXa_vs_apixaban": "antiXa_activity",
    }

    legends: ClassVar[dict[str, str]] = {
        "API10": "single 10mg PO",  # single dose
        "API10M": "multiple 10mg PO",  # multiple doses
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets: dict[str, DataSet] = {}

        # timecourse data
        for fig_id in ["Fig1", "Fig2"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                dset = DataSet.from_df(df_label, self.ureg)
                if "apixaban" in str(label).lower():
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[str(label)] = dset

        # scatter fig3
        df = self.load_dataframe("Fig3")
        for ylab, df_label in df.groupby("y_label"):
            dset = DataSet.from_df(df_label, self.ureg)
            dset.unit_conversion("x", 1 / self.Mr.api)
            dsets[str(ylab)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims: dict[str, Simulation] = {}

        preinit_changes = {
            **self.default_changes(),
            "BW": Q(self.bodyweight, "kg"),
            "HEIGHT": Q(self.height, "cm"),
            "PODOSE_api": Q(self.dose, "mg"),
        }

        # single dose (day 1)
        tcsims["API10"] = Simulation(
            time_unit="hr",
            end=96,
            preinit_changes=preinit_changes,
        )

        # the single dose of day 1 at 0 hr, then 11 doses every 12 hr from day 4
        # (72 hr) to the morning of day 9 (192 hr), the time 0 of the data
        tcsims["API10M"] = Simulation(
            time_unit="hr",
            end=264,
            preinit_changes=preinit_changes,
            changes=[
                self.add_doses(
                    [72 + 12 * k for k in range(11)],
                    {"PODOSE_api": Q(self.dose, "mg")},
                ),
            ],
            time_shift=-192,
        )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings: dict[str, FitMapping] = {}

        for intervention in self.interventions:
            infos = dict(self.infos_pk)
            if intervention in self.pd_interventions:
                infos.update(self.infos_pd)
            for sid, name in infos.items():
                mappings[f"fm_{name}_{intervention}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"{name}_{intervention}",
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=f"task_{intervention}",
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE
                        if intervention == "API10"
                        else Dosing.MULTIPLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure(),
        }

    def figure(self) -> dict[str, Figure]:
        """Figure of the pharmacokinetics and the anti-factor Xa activity."""
        fig = Figure(
            experiment=self,
            sid="Fig1",
            name=f"{self.__class__.__name__}",
            num_cols=3,
            num_rows=1,
            height=self.panel_height,
            width=self.panel_width * 3 * 1.05,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=-20, max=75),
            legend=True,
        )
        for kp, sid in enumerate(self.infos_pk):
            plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid])

        for kp, sid in enumerate(self.infos_pd):
            plots[kp + 1].set_yaxis(self.labels[sid], unit=self.units[sid])

        for intervention in self.interventions:
            plots[0].add_data(
                task=f"task_{intervention}",
                xid="time",
                yid="[Cve_api]",
                label=f"sim {self.legends[intervention]}",
                color=self.admin_colors["single"]
                if intervention == "API10"
                else self.admin_colors["multiple"],
            )

            plots[0].add_data(
                dataset=f"apixaban_{intervention}",
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
                label=f"exp {self.legends[intervention]}",
                color=self.admin_colors["single"]
                if intervention == "API10"
                else self.admin_colors["multiple"],
            )
            for _kp, sid in enumerate(self.infos_pd):
                name = self.infos_pd[sid]
                plots[1].add_data(
                    task=f"task_{intervention}",
                    xid="time",
                    yid=sid,
                    label=f"sim {self.legends[intervention]}",
                    color=self.admin_colors["single"]
                    if intervention == "API10"
                    else self.admin_colors["multiple"],
                )
                if intervention not in self.pd_interventions:
                    continue
                plots[1].add_data(
                    dataset=f"{name}_{intervention}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp {self.legends[intervention]}",
                    color=self.admin_colors["single"]
                    if intervention == "API10"
                    else self.admin_colors["multiple"],
                )

        plots[2].set_xaxis(self.labels["[Cve_api]"], unit=self.units["[Cve_api]"])
        plots[2].set_yaxis(
            self.labels["antiXa_activity"],
            unit=self.units["antiXa_activity"],
            scale="linear",
        )
        plots[2].add_data(
            task="task_API10",
            xid="[Cve_api]",
            yid="antiXa_activity",
            label="sim: 10mg PO",
            color="black",
            linestyle="solid",
        )

        plots[2].add_data(
            dataset="antiXa_vs_apixaban",
            xid="x",
            yid="y",
            label="exp individ: 10mg PO",
            color="white",
            markeredgecolor="black",
            marker="o",
            linestyle="",
        )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Cui2013, output_dir=Cui2013.__name__)
