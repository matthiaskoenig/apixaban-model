"""Simulation experiment of the study Upreti2013."""

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


class Upreti2013(ApixabanSimulationExperiment):
    """Simulation experiment of Upreti2013.

    A single oral dose of 10 mg apixaban after an overnight fast in healthy
    subjects of low (47 kg, n = 18), reference (75 kg, n = 16 in the analysis)
    and high (137 kg, n = 19) body weight. The urinary amounts (0-72 h) are not
    reported, they are derived from the geometric means of the renal clearance
    and the AUCinf of Table 2.
    """

    bodyweights: ClassVar[dict[str, float]] = {  # [kg]
        "low": 47,
        "reference": 75,
        "high": 137,
    }
    bmis: ClassVar[dict[str, float]] = {  # [kg/m^2]
        "low": 18.8,
        "reference": 26.3,
        "high": 42.6,
    }
    colors: ClassVar[dict[str, str]] = {
        "low": "#0000FF",
        "reference": "black",
        "high": "#FF0000",
    }
    groups: ClassVar[list[str]] = list(bodyweights.keys())

    markers: ClassVar[dict[str, str]] = {
        "low": "o",
        "reference": "P",
        "high": "s",
    }

    info_fig1: ClassVar[dict[str, str]] = {
        "[Cve_api]": "apixaban",
        "Aurine_api": "cumulative amount",
    }

    info_fig_scatter: ClassVar[dict[str, list[str]]] = {
        "apixaban_vs_antiXa": ["[Cve_api]", "antiXa_activity"],
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Tab2", "Fig1", "Fig4"]:
            df = self.load_dataframe(fig_id)
            group_by = "x_label" if fig_id == "Fig4" else "label"
            for label, df_label in df.groupby(group_by):
                label = str(label)
                if fig_id == "Tab2" and not label.startswith("cumulative amount"):
                    # the pharmacokinetic parameters of Tab2 are not used
                    continue
                dset = DataSet.from_df(df_label, self.ureg)
                if fig_id == "Fig4":
                    dset.unit_conversion("x", 1 / self.Mr.api)
                else:
                    # the urinary amounts of Tab2 are derived, the geometric means
                    # of the renal clearance times the AUCinf (Ae0-72)
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[self.to_sid(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        for group in self.groups:
            tcsims[self.to_sid(group)] = Simulation(
                time_unit="hr",
                end=75,
                preinit_changes={
                    **self.default_changes(),
                    "BW": Q(self.bodyweights[group], "kg"),
                    # the height is not reported, it is derived from the body
                    # weight and the body mass index
                    "HEIGHT": Q(
                        math.sqrt(self.bodyweights[group] / self.bmis[group]), "m"
                    ),
                    "PODOSE_api": Q(10, "mg"),
                },
            )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for group in self.groups:
            # pharmacokinetics
            for sid, name in self.info_fig1.items():
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
                        tissue=Tissue.URINE if sid == "Aurine_api" else Tissue.PLASMA,
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
            **self.figure_scatter(),
        }

    def figure_pk(self) -> dict[str, Figure]:
        """Apixaban in plasma and urine by body weight."""
        fig = Figure(
            experiment=self,
            sid="Fig1",
            name=self.__class__.__name__,
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
        plots[1].set_yaxis(self.label_api_urine, unit=self.unit_api_urine)

        for group in self.groups:
            for k, (sid, name) in enumerate(self.info_fig1.items()):
                # simulation
                plots[k].add_data(
                    task=self.to_sid(f"task_{group}"),
                    xid="time",
                    yid=sid,
                    label=f"sim {group}: 10mg PO",
                    color=self.colors[group],
                )
                # data
                plots[k].add_data(
                    dataset=self.to_sid(f"{name}_{group}"),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp {group}: 10mg PO",
                    color=self.colors[group],
                    linestyle="" if sid == "Aurine_api" else "dashed",
                )

        return self.figures_by_sid(fig)

    def figure_scatter(self) -> dict[str, Figure]:
        """Anti-factor Xa activity against the apixaban concentration in plasma."""
        fig = Figure(
            experiment=self,
            sid="FigScatter",
            name=self.__class__.__name__,
            num_cols=1,
            num_rows=1,
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            legend=True,
        )

        for xid, yid in self.info_fig_scatter.values():
            plots[0].set_xaxis(self.labels[xid], unit=self.units[xid])
            plots[0].set_yaxis(self.labels[yid], unit=self.units[yid])
        for group in self.groups:
            for label_id, (xid, yid) in self.info_fig_scatter.items():
                # simulation
                plots[0].add_data(
                    task=self.to_sid(f"task_{group}"),
                    xid=xid,
                    yid=yid,
                    label=f"sim {group}: 10mg PO",
                    color=self.colors[group],
                    linestyle="solid",
                )
                # data
                plots[0].add_data(
                    dataset=self.to_sid(f"{label_id}_{group}"),
                    xid="x",
                    yid="y",
                    label=f"exp individ {group}: 10mg PO",
                    linestyle="",
                    marker=self.markers[group],
                    markeredgecolor=self.colors[group],
                    color="white",
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Upreti2013, output_dir=Upreti2013.__name__)
