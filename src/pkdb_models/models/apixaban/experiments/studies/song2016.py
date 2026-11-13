"""Simulation experiment of the study Song2016."""

import math
from typing import ClassVar, NamedTuple, override

from pkpdsim.metadata import (
    ApplicationForm,
    Coadministration,
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


class Song2016Group(NamedTuple):
    """A treatment of Song2016."""

    #: the label of the timecourse in the data
    label: str
    #: the dose of apixaban [mg]
    dose: float
    #: the dosing parameter of the model
    dosing: str
    #: the form of the dose
    application_form: ApplicationForm
    #: the food state
    fasting: Fasting
    #: the food the dose is mixed with
    coadministration: Coadministration
    #: the body weight [kg]
    bodyweight: float
    #: the body mass index [kg/m^2]
    bmi: float
    #: the text of the legend
    legend: str
    #: the color of the treatment
    color: str
    #: the line style of the simulation, the simulations of the arms with food
    #: are those without food
    linestyle: str = "solid"


class Song2016(ApixabanSimulationExperiment):
    """Simulation experiment of Song2016.

    Two studies in healthy adults. Study 1 (n = 33, 77.4 kg, BMI 26.1): 10 mg
    apixaban as two 5 mg tablets, whole, crushed and suspended in water or
    crushed and mixed with 30 g applesauce. Study 2 (n = 22, 69.2 kg, BMI 23.6):
    a 5 mg tablet fasted or after a high-fat breakfast. A crushed tablet
    dissolves fast and is simulated as the oral solution (`SOLDOSE_api`): the
    early concentrations of the suspension in water (0.25 h 45, 0.5 h 129 ng/ml)
    are those of a solution, not those of the whole tablet (19 and 97 ng/ml).
    The food effect of the model is the slower gastric emptying of the fed
    state (`FED`) of the fed arm; the model has no effect of the applesauce
    (AUC -16 % and Cmax -21 % against the whole tablet, the mechanism is
    unknown), its arm is simulated like the arm in water.

    The subjects are mostly men (11 women of 55; 7 of 33 in the crushed tablet
    study, 4 of 22 in the food study) and run on the male build.
    """

    groups: ClassVar[dict[str, Song2016Group]] = {
        "tablet": Song2016Group(
            label="API10_tablet_crushed_apixaban",
            dose=10,
            dosing="PODOSE_api",
            application_form=ApplicationForm.TABLET,
            fasting=Fasting.FASTED,
            coadministration=Coadministration.NONE,
            bodyweight=77.4,
            bmi=26.1,
            legend="10mg PO tablet",
            color="black",
        ),
        "water": Song2016Group(
            label="API10_suspension_crushed_apixaban",
            dose=10,
            dosing="SOLDOSE_api",
            application_form=ApplicationForm.SUSPENSION,
            fasting=Fasting.FASTED,
            coadministration=Coadministration.NONE,
            bodyweight=77.4,
            bmi=26.1,
            legend="10mg PO crushed in water",
            color="tab:blue",
        ),
        "applesauce": Song2016Group(
            label="API10_syrup_crushed_apixaban",
            dose=10,
            dosing="SOLDOSE_api",
            application_form=ApplicationForm.SUSPENSION,
            fasting=Fasting.FASTED,
            coadministration=Coadministration.APPLE,
            bodyweight=77.4,
            bmi=26.1,
            legend="10mg PO crushed in applesauce",
            color="tab:green",
            linestyle="dashed",
        ),
        "fasted": Song2016Group(
            label="API5_food_fasted_apixaban",
            dose=5,
            dosing="PODOSE_api",
            application_form=ApplicationForm.TABLET,
            fasting=Fasting.FASTED,
            coadministration=Coadministration.NONE,
            bodyweight=69.2,
            bmi=23.6,
            legend="5mg PO tablet fasted",
            color="black",
        ),
        "fed": Song2016Group(
            label="API5_food_fed_apixaban",
            dose=5,
            dosing="PODOSE_api",
            application_form=ApplicationForm.TABLET,
            fasting=Fasting.FED,
            coadministration=Coadministration.NONE,
            bodyweight=69.2,
            bmi=23.6,
            legend="5mg PO tablet fed",
            color="tab:purple",
            linestyle="dashed",
        ),
    }

    #: the panels of the figure: study 1 (forms) and study 2 (food)
    panels: ClassVar[list[list[str]]] = [
        ["tablet", "water", "applesauce"],
        ["fasted", "fed"],
    ]

    #: lower limit of quantification of apixaban in plasma [ng/ml]
    lloq = 1.0

    infos_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        labels = {group.label for group in self.groups.values()}
        dsets = {}
        for fig_id in ["Fig1", "Fig2"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                if label not in labels:
                    continue
                # the means at 60 and 72 h of study 2 are below the limit of
                # quantification (means over values below it), they are left out
                df_label = df_label[
                    (df_label["mean"] >= self.lloq) | (df_label["time"] == 0.0)
                ]
                dset = DataSet.from_df(df_label, self.ureg)
                dset.unit_conversion("mean", 1 / self.Mr["api"])
                dsets[label] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims: dict[str, Simulation] = {}
        for key, group in self.groups.items():
            tcsims[key] = Simulation(
                time_unit="hr",
                end=75,
                preinit_changes={
                    **self.default_changes(),
                    group.dosing: Q(group.dose, "mg"),
                    "BW": Q(group.bodyweight, "kg"),
                    "HEIGHT": Q(math.sqrt(group.bodyweight / group.bmi), "m"),
                    # the high-fat breakfast of the fed arm
                    "FED": Q(int(group.fasting == Fasting.FED), "dimensionless"),
                },
            )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings: dict[str, FitMapping] = {}
        for sid, name in self.infos_pk.items():
            for key, group in self.groups.items():
                mappings[f"fm_{name}_{key}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=group.label,
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=f"task_{key}",
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=group.application_form,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=group.fasting,
                        coadministration=group.coadministration,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure_pk(),
        }

    def figure_pk(self) -> dict[str, Figure]:
        """Apixaban in plasma by the form of the dose and by food."""
        fig = Figure(
            experiment=self,
            sid="PK",
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
        sid = "Carm_api"
        for kp, keys in enumerate(self.panels):
            for kscale, scale in enumerate(["linear", "log"]):
                plot = plots[kp + 2 * kscale]
                # the data reach 5e-3 µM
                plot.set_yaxis(
                    self.labels[sid],
                    unit=self.units[sid],
                    scale=scale,
                    min=1e-3 if scale == "log" else None,
                )
                for key in keys:
                    group = self.groups[key]
                    plot.add_data(
                        task=f"task_{key}",
                        xid="time",
                        yid=sid,
                        label=f"sim: {group.legend}",
                        color=group.color,
                        linestyle=group.linestyle,
                    )
                    plot.add_data(
                        dataset=group.label,
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                        label=f"exp: {group.legend}",
                        color=group.color,
                        linestyle="solid",
                    )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Song2016, output_dir=Song2016.__name__)
