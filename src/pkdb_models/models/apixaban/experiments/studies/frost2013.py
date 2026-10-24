"""Simulation experiment of the study Frost2013."""

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


class Frost2013(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2013.

    A single ascending dose study (0.5 to 2.5 mg as oral solution, 5 to 50 mg
    as tablets, fasted) and a food study (10 mg fasted or after a high-fat
    breakfast) in healthy men. The model has no effect of food, the fed arm is
    simulated as the fasted one.
    """

    # food study group
    food_study: ClassVar[list[str]] = ["fed", "fasted"]
    # single dose group
    single_dose_study: ClassVar[list[str]] = [
        "D0_5",
        "D1",
        "D2_5",
        "D5",
        "D10",
        "D25",
        "D50",
    ]
    # single dose study divides into solution and tablet
    solution_doses: ClassVar[list[str]] = [
        "D0_5",
        "D1",
        "D2_5",
    ]  # mg 0.5–2.5 → Solution
    tablet_doses: ClassVar[list[str]] = [
        "D5",
        "D10",
        "D25",
        "D50",
    ]  # mg 5–50 → Tablet

    #: the mean body weights of the panels (Tab1) and of the food study
    bodyweights: ClassVar[dict[str, float]] = {  # [kg]
        "fasted": 76.6,
        "fed": 76.6,
        "D0_5": 87.2,
        "D1": 82.2,
        "D2_5": 87.3,
        "D5": 82.4,
        "D10": 73.8,
        "D25": 73.3,
        "D50": 77.0,
    }

    inr: ClassVar[dict[str, float]] = {  # [-]
        "fasted": 1.33 - 0.23,
        "fed": 1.28 - 0.20,
        "D0_5": 1.08,
        "D1": 1.10,
        "D2_5": 1.10,
        "D5": 1.08,
        "D10": 1.14,
        "D25": 1.01,
        "D50": 1.14,
    }

    PT: ClassVar[dict[str, float]] = {
        "fasted": 14.99 - 1.39,
        "fed": 14.66 - 1.30,
    }

    mPT: ClassVar[dict[str, float]] = {  # [s]
        "D0_5": 39.39,
        "D1": 44.85,
        "D2_5": 45.45,
        "D5": 46.97,
        "D10": 55.45,
        "D25": 40.61,
        "D50": 49.09,
    }

    aPTT: ClassVar[dict[str, float]] = {  # [s]
        "fasted": 32.96 - 3.05,
        "fed": 31.55 - 2.90,
        "D0_5": 30.4,
        "D1": 32.29,
        "D2_5": 30.55,
        "D5": 31.46,
        "D10": 29.45,
        "D25": 31.04,
        "D50": 32.70,
    }

    doses: ClassVar[dict[str, float]] = {  # [mg]
        "D0_5": 0.5,
        "D1": 1,
        "D2_5": 2.5,
        "D5": 5,
        "D10": 10,
        "D25": 25,
        "D50": 50,
    }

    colors: ClassVar[dict[str, str]] = {
        "D0_5": "#fdd0a2",
        "D1": "#fdae6b",
        "D2_5": "#fd8d3c",
        "D5": "#f16913",
        "D10": "#d94801",
        "D25": "#a63603",
        "D50": "#7f2704",
        "fasted": "black",
        "fed": "tab:purple",
    }

    groups: ClassVar[list[str]] = list(bodyweights.keys())

    info_fig1: ClassVar[dict[str, str]] = {
        "[Cve_api]": "apixaban",
    }

    info_fig3: ClassVar[dict[str, str]] = {
        "INR": "inr",
        "aPTT": "aPTT",
        "mPT": "mPT",
    }

    #: the relative changes (%) against the concentration (Fig4)
    info_fig4: ClassVar[dict[str, str]] = {
        "mPT_relchange": "mPT",
        "INR_relchange": "inr",
        "aPTT_relchange": "aPTT",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id, group_id in zip(
            ["Fig1A", "Fig1B", "Fig3", "Fig4"],
            ["label", "label", "label", "x_label"],
            strict=True,
        ):
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby(group_id):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                if "apixaban" in label:
                    if fig_id in ["Fig4"]:
                        dset.unit_conversion("x", 1 / self.Mr.api)
                    else:
                        dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[label] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        # pharmacokinetics food study
        for group in self.food_study:
            tcsims[group] = Simulation(
                time_unit="hr",
                end=60,
                preinit_changes={
                    **self.default_changes(),
                    "BW": Q(self.bodyweights[group], "kg"),
                    "PODOSE_api": Q(10, "mg"),
                    "INR_ref": Q(self.inr[group], self.units["INR"]),
                    "aPTT_ref": Q(self.aPTT[group], self.units["aPTT"]),
                    "PT_ref": Q(self.PT[group], self.units["PT"]),
                },
            )
        # pharmacokinetics/pharmacodynamics single dose study
        for group in self.single_dose_study:
            if group in self.solution_doses:
                tcsims[group] = Simulation(
                    time_unit="hr",
                    end=100,
                    preinit_changes={
                        **self.default_changes(),
                        "BW": Q(self.bodyweights[group], "kg"),
                        "SOLDOSE_api": Q(self.doses[group], "mg"),
                        # set pharmacodynamic baseline reference parameters (assignment rules use these)
                        "INR_ref": Q(self.inr[group], self.units["INR"]),
                        "aPTT_ref": Q(self.aPTT[group], self.units["aPTT"]),
                        "mPT_ref": Q(self.mPT[group], self.units["mPT"]),
                    },
                )
            else:
                tcsims[group] = Simulation(
                    time_unit="hr",
                    end=100,
                    preinit_changes={
                        **self.default_changes(),
                        "BW": Q(self.bodyweights[group], "kg"),
                        "PODOSE_api": Q(self.doses[group], "mg"),
                        # set pharmacodynamic baseline reference parameters (assignment rules use these)
                        "INR_ref": Q(self.inr[group], self.units["INR"]),
                        "aPTT_ref": Q(self.aPTT[group], self.units["aPTT"]),
                        "mPT_ref": Q(self.mPT[group], self.units["mPT"]),
                    },
                )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}

        specs = [
            # Fig1A
            (
                self.info_fig1,
                lambda group: PKPDMappingMetaData(
                    tissue=Tissue.PLASMA,
                    route=Route.PO,
                    application_form=(
                        ApplicationForm.SOLUTION
                        if group in self.solution_doses
                        else ApplicationForm.TABLET
                    ),
                    dosing=Dosing.SINGLE,
                    health=Health.HEALTHY,
                    fasting=Fasting.FASTED,
                ),
                self.single_dose_study,
            ),
            # Fig1B
            (
                self.info_fig1,
                lambda group: PKPDMappingMetaData(
                    tissue=Tissue.PLASMA,
                    route=Route.PO,
                    application_form=ApplicationForm.TABLET,
                    dosing=Dosing.SINGLE,
                    health=Health.HEALTHY,
                    fasting=Fasting.FED if group == "fed" else Fasting.FASTED,
                ),
                self.food_study,
            ),
            # Fig3
            (
                self.info_fig3,
                lambda group: PKPDMappingMetaData(
                    tissue=Tissue.PLASMA,
                    route=Route.PO,
                    application_form=(
                        ApplicationForm.SOLUTION
                        if group in self.solution_doses
                        else ApplicationForm.TABLET
                    ),
                    dosing=Dosing.SINGLE,
                    health=Health.HEALTHY,
                    fasting=Fasting.FASTED,
                ),
                self.single_dose_study,
            ),
        ]

        for info_dict, meta_factory, groups_for_spec in specs:
            for group in groups_for_spec:
                for sid, name in info_dict.items():
                    # only the food study (Fig1B) reports SDs
                    mappings[f"fm_{name}_{group}"] = FitMapping(
                        self,
                        reference=FitData(
                            self,
                            dataset=f"{name}_{group}",
                            xid="time",
                            yid="mean",
                            yid_sd="mean_sd" if group in self.food_study else None,
                            count="count",
                        ),
                        observable=FitData(
                            self,
                            task=f"task_{group}",
                            xid="time",
                            yid=sid,
                        ),
                        metadata=meta_factory(group),
                    )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure_pk(),
            **self.figure_pk2(),
            **self.figure_pd(),
            **self.figure_scatter(),
        }

    def figure_pk(self) -> dict[str, Figure]:
        """Figure of the pharmacokinetics of the food study (fasted and fed)."""
        fig = Figure(
            experiment=self,
            sid="Fig1B",
            name=self.__class__.__name__,
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)

        for group in self.food_study:
            for k, sid in enumerate(self.info_fig1.keys()):
                name = self.info_fig1[sid]

                # simulation
                plots[k].add_data(
                    task=f"task_{group}",
                    xid="time",
                    yid=sid,
                    label=f"sim {group}: 10mg PO",
                    color=self.colors[group],
                )
                # data
                plots[k].add_data(
                    dataset=f"{name}_{group}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp {group}: 10mg PO",
                    color=self.colors[group],
                )

        return self.figures_by_sid(fig)

    def figure_pk2(self) -> dict[str, Figure]:
        """Figure of the pharmacokinetics of the single dose study."""
        fig = Figure(
            experiment=self,
            sid="Fig1A",
            name=self.__class__.__name__,
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        # the legend would hide the terminal phase
        fig.settings = {**fig.settings, "legend_position": "outside"}
        # the doses span two orders of magnitude (log scale as in the paper)
        plots[0].set_yaxis(
            self.label_api_plasma, unit=self.unit_api, scale="log", min=1e-3
        )

        for group in self.single_dose_study:
            for k, sid in enumerate(self.info_fig1.keys()):
                name = self.info_fig1[sid]

                # simulation
                plots[k].add_data(
                    task=f"task_{group}",
                    xid="time",
                    yid=sid,
                    label=f"sim: {self.doses[group]}mg SOL"
                    if group in self.solution_doses
                    else f"sim: {self.doses[group]}mg PO",
                    color=self.colors[group],
                )
                # data
                plots[k].add_data(
                    dataset=f"{name}_{group}",
                    xid="time",
                    yid="mean",
                    count="count",
                    label=f"exp: {self.doses[group]}mg SOL"
                    if group in self.solution_doses
                    else f"exp: {self.doses[group]}mg PO",
                    color=self.colors[group],
                )

        return self.figures_by_sid(fig)

    def figure_pd(self) -> dict[str, Figure]:
        """Figure of the pharmacodynamics of the single dose study."""
        fig = Figure(
            experiment=self,
            sid="Fig3",
            name=self.__class__.__name__,
            num_rows=1,
            num_cols=3,
            height=self.panel_height * 1.15,
            width=self.panel_width * 1.15 * 3 * 1.05,
        )
        plots = fig.create_plots(
            xaxis=Axis(
                self.label_time,
                unit=self.unit_time,
                max=70,
            ),
            legend=True,
        )
        plots[0].set_yaxis(self.labels["INR"], unit=self.units["INR"])
        plots[1].set_yaxis(self.labels["aPTT"], unit=self.units["aPTT"])
        plots[2].set_yaxis(self.labels["mPT"], unit=self.units["mPT"])

        for group in self.single_dose_study:
            for k, sid in enumerate(self.info_fig3.keys()):
                name = self.info_fig3[sid]

                # simulation
                plots[k].add_data(
                    task=f"task_{group}",
                    xid="time",
                    yid=sid,
                    label=f"sim: {self.doses[group]}mg SOL"
                    if group in self.solution_doses
                    else f"sim: {self.doses[group]}mg PO",
                    color=self.colors[group],
                )
                # data
                plots[k].add_data(
                    dataset=f"{name}_{group}",
                    xid="time",
                    yid="mean",
                    count="count",
                    label=f"exp: {self.doses[group]}mg SOL"
                    if group in self.solution_doses
                    else f"exp: {self.doses[group]}mg PO",
                    color=self.colors[group],
                )

        return self.figures_by_sid(fig)

    def figure_scatter(self) -> dict[str, Figure]:
        """Figure of the relative changes of the pharmacodynamics against apixaban."""
        fig = Figure(
            experiment=self,
            sid="Fig4",
            name=self.__class__.__name__,
            num_cols=3,
            height=self.panel_height,
            width=self.panel_width * 1.05 * 3,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_api_plasma, unit=self.unit_api),
            legend=True,
        )
        for k, (sid, name) in enumerate(self.info_fig4.items()):
            plots[k].set_yaxis(self.labels[sid], unit=self.units[sid], scale="linear")
            for group in self.single_dose_study:
                form = "SOL" if group in self.solution_doses else "PO"
                plots[k].add_data(
                    task=f"task_{group}",
                    xid="[Cve_api]",
                    yid=sid,
                    label=f"sim: {self.doses[group]}mg {form}",
                    color=self.colors[group],
                )
            plots[k].add_data(
                dataset=f"apixaban_vs_{name}",
                xid="x",
                yid="y",
                label="exp individ",
                color="white",
                markeredgecolor="black",
                marker="o",
                linestyle="",
            )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Frost2013, output_dir=Frost2013.__name__)
