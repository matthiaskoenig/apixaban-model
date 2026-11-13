"""Simulation experiment of the study Kreutz2017."""

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


class Kreutz2017(ApixabanSimulationExperiment):
    """Simulation experiment of Kreutz2017.

    Healthy men: apixaban 5 mg (tablet) twice daily with breakfast and dinner
    for 7 days, the pharmacokinetics and pharmacodynamics (anti-factor Xa
    activity calibrated with apixaban, PT and aPTT ratio) on day 7. The data
    are geometric means, without an absolute spread (the geometric SD of the
    paper is a factor).

    The subjects are men (24) and run on the male build.
    """

    bodyweight = 81.1  # [kg]
    bodyheight = 181  # [cm]

    dose = 5  # [mg]
    route = "PO"

    info_figpk: ClassVar[dict[str, str]] = {
        "api_apixaban": "Carm_api",
    }

    info_figpd: ClassVar[dict[str, str]] = {
        "api_prothrombin time ratio": "COAG__PT_ratio",
        "api_aPTT ratio": "COAG__aPTT_ratio",
        "api_Anti-factor Xa activity_mean_ug": "COAG__antiXa_activity_gram",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2", "Fig6", "TabS2"]:
            df = self.load_dataframe(fig_id)
            if fig_id == "TabS2":
                # the anti-factor Xa activity 24 h after the last dose (180 h,
                # 26.8 ug/l at 12.7 ug/l apixaban) is at the floor of the assay
                # (about 25 ug/l, Fig S1), not mapped
                df = df[df.time < 180]
            for label, df_label in df.groupby("label"):
                label = str(label)
                if "riv" in label:
                    continue
                dset = DataSet.from_df(df_label, self.ureg)
                if "apixaban" in label:
                    dset.unit_conversion("gmean", 1 / self.Mr["api"])
                # the time 0 of the data is the morning dose of day 7
                dset.time = dset.time - 6 * 24
                dsets[self.to_sid(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}

        # doses every 12 hr, the 14th dose at 156 hr is followed by 73 hr; the
        # time 0 of the data is at 144 hr
        tcsims["apixaban"] = Simulation(
            time_unit="hr",
            end=13 * 12 + 73,
            preinit_changes={
                **self.default_changes(),
                "BW": Q(self.bodyweight, "kg"),
                "HEIGHT": Q(self.bodyheight, "cm"),
                f"{self.route}DOSE_api": Q(self.dose, "mg"),
                # the doses with the meals
                "FED": Q(1, "dimensionless"),
            },
            changes=[
                self.add_doses(
                    [12 * k for k in range(1, 14)],
                    {f"{self.route}DOSE_api": Q(self.dose, "mg")},
                ),
            ],
            time_shift=-6 * 24,
        )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}

        for variables in [
            self.info_figpk.items(),
            self.info_figpd.items(),
        ]:
            for label, sid in variables:
                mappings[self.to_sid(f"fm_{self.route}_{label}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(label),
                        xid="time",
                        yid="gmean",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task="task_apixaban",
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.MULTIPLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FED,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure_pk(),
            **self.figure_pd(),
        }

    def figure_pk(self) -> dict[str, Figure]:
        """Figure of the pharmacokinetics."""
        fig = Figure(
            experiment=self,
            sid="PK",
            name=self.__class__.__name__,
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=-24),
            legend=True,
        )
        plots[0].set_yaxis(
            self.labels["Carm_api"], unit=self.units["Carm_api"], scale="linear"
        )

        for label, sid in self.info_figpk.items():
            # simulation
            plots[0].add_data(
                task="task_apixaban",
                xid="time",
                yid=sid,
                label=f"sim fed: {self.dose}mg {self.route}",
                color=self.fasting_colors["fed"],
            )
            # data
            plots[0].add_data(
                dataset=self.to_sid(label),
                xid="time",
                yid="gmean",
                count="count",
                label=f"exp fed: {self.dose}mg {self.route}",
                color=self.fasting_colors["fed"],
            )

        return self.figures_by_sid(fig)

    def figure_pd(self) -> dict[str, Figure]:
        """Figure of the pharmacodynamics."""
        fig = Figure(
            experiment=self,
            sid="PD",
            name=self.__class__.__name__,
            num_cols=len(self.info_figpd),
            height=self.panel_height,
            width=self.panel_width * 3 * 1.05,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=-24),
            legend=True,
        )
        for kp, (label, sid) in enumerate(self.info_figpd.items()):
            plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid])
            # simulation
            plots[kp].add_data(
                task="task_apixaban",
                xid="time",
                yid=sid,
                label=f"sim fed: {self.dose}mg {self.route}",
                color=self.fasting_colors["fed"],
            )
            # data
            plots[kp].add_data(
                dataset=self.to_sid(label),
                xid="time",
                yid="gmean",
                count="count",
                label=f"exp fed: {self.dose}mg {self.route}",
                color=self.fasting_colors["fed"],
            )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Kreutz2017, output_dir=Kreutz2017.__name__)
