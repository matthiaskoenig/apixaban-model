"""Simulation experiment of the study Chang2016."""

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


class Chang2016(ApixabanSimulationExperiment):
    """Simulation experiment of Chang2016."""

    groups: ClassVar[list[str]] = [
        "normal",
        "mild",
        "moderate",
        "severe",
    ]  # creatinine clearance in [ml/min]
    colors: ClassVar[dict[str, str]] = {
        "normal": "black",
        "mild": "#66c2a4",
        "moderate": "#2ca25f",
        "severe": "#006d2c",
    }
    short_names: ClassVar[dict[str, str]] = {
        "normal": "",
        "mild": "MiRI",
        "moderate": "MoRI",
        "severe": "SRI",
    }
    bodyweights: ClassVar[dict[str, float]] = {
        "normal": 83.3,
        "mild": 79.3,
        "moderate": 74.5,
        "severe": 84.1,
    }
    #: the renal function is the measured 24-hr creatinine clearance of the
    #: group (Tab1, ml/min) relative to the GFR of 101 ml/min of the model
    renal_functions: ClassVar[dict[str, float]] = {
        "normal": 106.7 / 101,
        "mild": 58.8 / 101,
        "moderate": 38.0 / 101,
        "severe": 24.5 / 101,
    }
    markers: ClassVar[dict[str, str]] = {
        "normal": "s",
        "mild": "*",
        "moderate": "^",
        "severe": "o",
    }

    #: the urinary amounts are not reported: they are derived in the curation
    #: as the renal clearance times the AUCinf of Tab2 (geometric means), with
    #: SDs which are not reported values; the renal clearance of the study is
    #: Ae(0-96)/AUC(0-96), so the amounts overestimate Ae(0-96) slightly
    info_pk: ClassVar[dict[str, str]] = {
        "[Cve_api]": "apixaban",
        "Aurine_api": "cumulative amount",
    }

    info_pd: ClassVar[dict[str, str]] = {
        "INR": "inr",
        "antiXa_activity": "xa",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id, group_id in zip(
            ["Fig1", "Fig4", "Tab2"], ["label", "x_label", "label"], strict=True
        ):
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby(group_id):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                if label.startswith("apixaban_"):
                    if fig_id == "Fig4":
                        dset.unit_conversion("x", 1 / self.Mr.api)
                    else:
                        dset.unit_conversion("mean", 1 / self.Mr.api)
                if fig_id == "Tab2":
                    if "cumulative" in label:
                        dset.unit_conversion("mean", 1 / self.Mr.api)
                        dsets[self.to_sid(label)] = dset
                else:
                    dsets[self.to_sid(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims: dict[str, Simulation] = {}
        for group in self.groups:
            tcsims[self.to_sid(group)] = Simulation(
                time_unit="hr",
                end=100,
                preinit_changes={
                    **self.default_changes(),
                    "BW": Q(self.bodyweights[group], "kg"),
                    "KI__f_renal_function": Q(
                        self.renal_functions[group], "dimensionless"
                    ),
                    "PODOSE_api": Q(10, "mg"),
                },
            )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings: dict[str, FitMapping] = {}

        for group in self.groups:
            for sid, name in self.info_pk.items():
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
                        tissue=Tissue.PLASMA if sid == "[Cve_api]" else Tissue.URINE,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY
                        if group == "normal"
                        else Health.RENAL_IMPAIRMENT,
                        fasting=Fasting.FASTED,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure_pk(),
            **self.figure_scatter_xa(),
            **self.figure_scatter_inr(),
        }

    def figure_pk(self) -> dict[str, Figure]:
        """Figure of the pharmacokinetics in plasma and urine."""
        fig = Figure(
            experiment=self,
            sid="PK",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 2,
            num_cols=2,
            num_rows=1,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )

        for kp, sid in enumerate(self.info_pk):
            plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid])
        # the legend of the plasma names the groups, one in the urine panel
        # would hide the urinary amounts at 96 hr
        plots[1].legend = False

        for group in self.groups:
            for kp, sid in enumerate(self.info_pk):
                name = self.info_pk[sid]

                # simulation
                plots[kp].add_data(
                    task=self.to_sid(f"task_{group}"),
                    xid="time",
                    yid=sid,
                    label="sim: 10mg PO"
                    if group == "normal"
                    else f"sim {self.short_names[group]}: 10mg PO",
                    color=self.colors[group],
                )
                # data
                plots[kp].add_data(
                    dataset=self.to_sid(f"{name}_{group}"),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label="exp: 10mg PO"
                    if group == "normal"
                    else f"exp {self.short_names[group]}: 10mg PO",
                    color=self.colors[group],
                    linestyle="" if "cumulative" in name else "-",
                )

        return self.figures_by_sid(fig)

    def figure_scatter_xa(self) -> dict[str, Figure]:
        """Figure of the anti-factor Xa activity against apixaban in plasma."""
        fig = Figure(
            experiment=self,
            sid="PD_scatter_xa",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.labels["[Cve_api]"], unit=self.units["[Cve_api]"]),
            legend=True,
        )
        plots[0].set_yaxis(
            self.labels["antiXa_activity"],
            unit=self.units["antiXa_activity"],
            scale="linear",
        )
        for group in self.groups:
            plots[0].add_data(
                task=self.to_sid(f"task_{group}"),
                xid="[Cve_api]",
                yid="antiXa_activity",
                label="sim: 10mg PO"
                if group == "normal"
                else f"sim {self.short_names[group]}: 10mg PO",
                color=self.colors[group],
            )
            plots[0].add_data(
                dataset=self.to_sid(f"apixaban_vs_xa_{group}"),
                xid="x",
                yid="y",
                label=f"exp individ {self.short_names[group]}: 10mg PO"
                if group != "normal"
                else "exp individ: 10mg PO",
                linestyle="",
                color="white",
                marker=self.markers[group],
                markeredgecolor=self.colors[group],
            )

        return self.figures_by_sid(fig)

    def figure_scatter_inr(self) -> dict[str, Figure]:
        """Figure of the INR against apixaban in plasma."""
        fig = Figure(
            experiment=self,
            sid="PD_scatter_inr",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.labels["[Cve_api]"], unit=self.units["[Cve_api]"]),
            legend=True,
        )
        plots[0].set_yaxis(
            self.labels["INR"],
            unit=self.units["INR"],
            scale="linear",
        )
        for group in self.groups:
            plots[0].add_data(
                task=self.to_sid(f"task_{group}"),
                xid="[Cve_api]",
                yid="INR",
                label="sim: 10mg PO"
                if group == "normal"
                else f"sim {self.short_names[group]}: 10mg PO",
                color=self.colors[group],
            )
            plots[0].add_data(
                dataset=self.to_sid(f"apixaban_vs_INR_{group}"),
                xid="x",
                yid="y",
                label=f"exp individ {self.short_names[group]}: 10mg PO"
                if group != "normal"
                else "exp individ: 10mg PO",
                linestyle="",
                color="white",
                marker=self.markers[group],
                markeredgecolor=self.colors[group],
            )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Chang2016, output_dir=Chang2016.__name__)
