"""Simulation experiment of the study Wang2014."""

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


class Wang2014(ApixabanSimulationExperiment):
    """Simulation experiment of Wang2014.

    A single oral dose of 20 mg apixaban (four 5 mg tablets) after a fast of at
    least 10 h in 18 healthy subjects (72.2 kg, 169.4 cm), alone or with 50 g
    activated charcoal at 2 h (n = 14) or 6 h (n = 17) after the dose. The
    charcoal binds the apixaban in the lumen of the small intestine (absorbed
    rest and intestinal secretion) and shortens the half-life (13.4 to about
    5 h). The model has no binding in the lumen: the charcoal arms are not
    simulated or mapped, they are shown with the control.
    """

    colors: ClassVar[dict[str, str]] = {
        "control": "black",
    }
    groups: ClassVar[list[str]] = list(colors.keys())

    #: the data of the charcoal arms (not simulated) and their colors
    charcoal: ClassVar[dict[str, tuple[str, str]]] = {
        "API20, AC50_2hr_all_apixaban": ("20mg PO + charcoal at 2 h", "tab:blue"),
        "API20, AC50_6hr_all_apixaban": ("20mg PO + charcoal at 6 h", "tab:orange"),
    }
    bodyweight = 72.2  # [kg] (control)
    bodyheight = 1.694  # [m]

    infos_pk: ClassVar[dict[str, str]] = {
        "[Cve_api]": "apixaban",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[self.to_sid(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims: dict[str, Simulation] = {}
        tcsims["control"] = Simulation(
            time_unit="hr",
            end=75,
            preinit_changes={
                **self.default_changes(),
                "PODOSE_api": Q(20, "mg"),
                "BW": Q(self.bodyweight, "kg"),
                "HEIGHT": Q(self.bodyheight, "m"),
            },
        )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings: dict[str, FitMapping] = {}
        for sid, name in self.infos_pk.items():
            mappings[f"fm_{name}_api_20"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=f"API20_all_{name}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                ),
                observable=FitData(
                    self,
                    task="task_control",
                    xid="time",
                    yid=sid,
                ),
                metadata=PKPDMappingMetaData(
                    tissue=Tissue.PLASMA,
                    route=Route.PO,
                    application_form=ApplicationForm.TABLET,
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
        }

    def figure_pk(self) -> dict[str, Figure]:
        """Apixaban in plasma, the charcoal arms are data only."""
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
        sid = "[Cve_api]"
        name = self.infos_pk[sid]
        for kp, scale in enumerate(["linear", "log"]):
            plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid], scale=scale)
            for group in self.groups:
                # simulation
                plots[kp].add_data(
                    task="task_control",
                    xid="time",
                    yid=sid,
                    label="sim: 20mg PO",
                    color=self.colors[group],
                )
                # data
                plots[kp].add_data(
                    dataset=f"API20_all_{name}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label="exp: 20mg PO",
                    color=self.colors[group],
                    linestyle="solid",
                )
            for label, (legend, color) in self.charcoal.items():
                plots[kp].add_data(
                    dataset=self.to_sid(label),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp: {legend}",
                    color=color,
                    linestyle="dashed",
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Wang2014, output_dir=Wang2014.__name__)
