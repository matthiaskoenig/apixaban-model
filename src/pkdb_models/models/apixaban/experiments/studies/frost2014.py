"""Simulation experiment of the study Frost2014."""

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


class Frost2014(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2014.

    Apixaban 2.5 mg twice daily for 4 days in 14 healthy subjects (the
    rivaroxaban period of the crossover is not simulated); the profiles of
    day 4 after the morning (0 hr) and the evening dose (12 hr).

    The subjects are mostly men (3 women of 14) and run on the male build.
    """

    bodyweight = 75.9  # [kg]
    height = 181.0  # [cm]

    colors: ClassVar[dict[str, str]] = {
        "mAPI": "purple",
    }

    interventions: ClassVar[list[str]] = list(colors.keys())

    doses: ClassVar[dict[str, float]] = {
        "mAPI": 2.5,  # mg
    }

    infos_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
    }

    #: the observable of the anti-Xa activity and its name in the keys of the
    #: mappings
    infos_pd: ClassVar[dict[str, str]] = {"COAG__antiXa_activity": "antiXa_activity"}

    #: the anti-Xa activity against apixaban (Fig4): the individual values and
    #: the means at the times of the profile
    info_figpd_scatter: ClassVar[dict[str, str]] = {
        "apixaban_vs_antixa": "COAG__antiXa_activity",
        "apixaban_mean_vs_antixa_mean": "COAG__antiXa_activity",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2", "Fig3", "Fig4"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                if "rivaroxaban" in label or "RIV" in label:
                    continue
                dset = DataSet.from_df(df_label, self.ureg)
                if label in self.info_figpd_scatter:
                    dset.unit_conversion("x", 1 / self.Mr["api"])
                elif "apixaban" in label:
                    dset.unit_conversion("mean", 1 / self.Mr["api"])
                dsets[label] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        for intervention in self.interventions:
            dose = self.doses[intervention]
            # 8 doses every 12 hr (days 1 to 4), the seventh dose at 72 hr (the
            # morning dose of day 4) is the time 0 of the data
            tcsims[intervention] = Simulation(
                time_unit="hr",
                end=7 * 12 + 45,
                preinit_changes={
                    **self.default_changes(),
                    "BW": Q(self.bodyweight, "kg"),
                    "HEIGHT": Q(self.height, "cm"),
                    "PODOSE_api": Q(dose, "mg"),
                },
                changes=[
                    self.add_doses(
                        [12 * k for k in range(1, 8)], {"PODOSE_api": Q(dose, "mg")}
                    ),
                ],
                time_shift=-3 * 24,
            )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for intervention in self.interventions:
            # pharmacokinetics
            for _k, sid in enumerate(self.infos_pk.keys()):
                name = self.infos_pk[sid]
                mappings[f"fm_{name}_{intervention}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"{name}_{intervention}",
                        xid="time",
                        yid="mean",
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
                        dosing=Dosing.MULTIPLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.NR,
                    ),
                )
            # PD
            for _ks, sid in enumerate(self.infos_pd):
                name = self.infos_pd[sid]
                mappings[f"fm_{intervention}_{name}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"Xa_{intervention}",
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        # the count falls to 8 (36 hr) and 4 (48 hr), a mapping
                        # has one count: the subjects of the study
                        count=14,
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
                        dosing=Dosing.MULTIPLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.NR,
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
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)

        for intervention in self.interventions:
            for _k, sid in enumerate(self.infos_pk.keys()):
                name = self.infos_pk[sid]
                if "apixaban" in name and "API" in intervention:
                    # simulation
                    plots[0].add_data(
                        task=f"task_{intervention}",
                        xid="time",
                        yid=sid,
                        label="sim: 2.5mg PO BID",
                        color="black",
                    )
                    # data
                    plots[0].add_data(
                        dataset=f"{name}_{intervention}",
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                        label="exp: 2.5mg PO BID",
                        color="black",
                    )
        plots[1].set_yaxis(
            self.labels["COAG__antiXa_activity"],
            unit=self.units["COAG__antiXa_activity"],
        )

        for intervention in self.interventions:
            for _k, sid in enumerate(self.infos_pd):
                if "API" in intervention:
                    # simulation
                    plots[1].add_data(
                        task=f"task_{intervention}",
                        xid="time",
                        yid=sid,
                        label="sim: 2.5mg PO BID",
                        color="black",
                    )
                    # data
                    # the count falls from 14 to 8 (36 hr) and 4 (48 hr)
                    plots[1].add_data(
                        dataset=f"Xa_{intervention}",
                        xid="time",
                        yid="mean",
                        label="exp: 2.5mg PO BID (n=4-14)",
                        color="black",
                    )

        # keyword arguments of `Plot.add_data`, passed on to matplotlib
        style_mean: dict[str, dict[str, Any]] = {
            "kwargs_sim": {
                "color": self.fasting_colors["fasted"],
                "linestyle": "solid",
            },
            "kwargs_exp": {
                "label": "exp: 2.5mg PO BID",
                "marker": "s",
                "linestyle": "",
                "color": self.fasting_colors["fasted"],
                "markeredgecolor": "black",
            },
        }

        style_indiv: dict[str, dict[str, Any]] = {
            "kwargs_sim": {"color": "black", "linestyle": "", "marker": "o"},
            "kwargs_exp": {
                "label": "exp individ: 2.5mg PO BID",
                "color": "white",
                "markeredgecolor": "black",
                "marker": "o",
                "linestyle": "",
            },
        }

        plots[2].set_xaxis(self.labels["Carm_api"], unit=self.units["Carm_api"])
        plots[2].set_yaxis(
            self.labels["COAG__antiXa_activity"],
            unit=self.units["COAG__antiXa_activity"],
            scale="linear",
        )

        for label, sid in self.info_figpd_scatter.items():
            plots[2].set_yaxis(self.labels[sid], unit=self.units[sid], scale="linear")

            style = style_mean if "mean" in label else style_indiv
            if "mean" in label:
                # simulation
                plots[2].add_data(
                    task="task_mAPI",
                    xid="Carm_api",
                    yid=sid,
                    label="sim: 2.5mg PO BID",
                    **style["kwargs_sim"],
                )
            # data
            plots[2].add_data(dataset=label, xid="x", yid="y", **style["kwargs_exp"])

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Frost2014, output_dir=Frost2014.__name__)
