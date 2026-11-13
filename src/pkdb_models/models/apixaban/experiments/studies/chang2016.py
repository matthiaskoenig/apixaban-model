"""Simulation experiment of the study Chang2016."""

from collections.abc import Mapping
from types import MappingProxyType
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
from pkpdsim.pbpk import Sex
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
    """Simulation experiment of Chang2016.

    The groups of normal renal function (5 women of 8) and of mild renal
    impairment (6 women of 10) are mostly women and run on the female build,
    their renal function relative to the healthy GFR of the female build; the
    moderate (1 woman of 7) and severe (2 women of 7) groups run on the male
    build.
    """

    simulation_sexes: ClassVar[Mapping[str, Sex]] = MappingProxyType(
        {
            "normal": Sex.FEMALE,
            "mild": Sex.FEMALE,
        }
    )

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
    #: the measured 24-hr creatinine clearance of the groups (Tab1) [ml/min],
    #: the GFR of the simulation (`renal_function`)
    crcl: ClassVar[dict[str, float]] = {
        "normal": 106.7,
        "mild": 58.8,
        "moderate": 38.0,
        "severe": 24.5,
    }

    #: the urinary amounts are not reported: they are derived in the curation
    #: as the renal clearance times the AUCinf of Tab2 (geometric means,
    #: without a spread); the renal clearance of the study is Ae(0-96)/AUC(0-96),
    #: so the amounts overestimate Ae(0-96) slightly
    info_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
        "Aurine_api": "cumulative amount",
    }
    #: the statistic of the data and its error, by the name of the data
    yids: ClassVar[dict[str, tuple[str, str | None]]] = {
        "apixaban": ("mean", "mean_sd"),
        "cumulative amount": ("gmean", None),
    }

    info_pd: ClassVar[dict[str, str]] = {
        "COAG__INR": "inr",
        "COAG__antiXa_activity": "xa",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        df = self.load_dataframe("Fig1")
        for label, df_label in df.groupby("label"):
            dset = DataSet.from_df(df_label, self.ureg)
            dset.unit_conversion("mean", 1 / self.Mr["api"])
            dsets[self.to_sid(str(label))] = dset

        # the urinary amounts at 96 hr are geometric means; the amount of 0 at
        # the dose is no geometric mean and not part of the series
        df = self.load_dataframe("Tab2")
        for group in self.groups:
            df_group = df[
                (df["label"] == f"cumulative_amount_apixaban_urine_API10_{group}")
                & df["gmean"].notna()
            ]
            dset = DataSet.from_df(df_group, self.ureg)
            dset.unit_conversion("gmean", 1 / self.Mr["api"])
            dsets[self.to_sid(f"cumulative amount_{group}")] = dset

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
                    "f_renal_function": self.renal_function(
                        self.crcl[group],
                        bw=self.bodyweights[group],
                        simulation=self.to_sid(group),
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
                tissue = Tissue.PLASMA if sid == "Carm_api" else Tissue.URINE
                mappings[self.to_sid(f"fm_{name}_{group}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(f"{name}_{group}"),
                        xid="time",
                        yid=self.yids[name][0],
                        yid_sd=self.yids[name][1],
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_{group}"),
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=tissue,
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
                    yid=self.yids[name][0],
                    yid_sd=self.yids[name][1],
                    count="count",
                    label="exp: 10mg PO"
                    if group == "normal"
                    else f"exp {self.short_names[group]}: 10mg PO",
                    color=self.colors[group],
                    linestyle="" if "cumulative" in name else "-",
                )

        return self.figures_by_sid(fig)

    def figure_scatter_xa(self) -> dict[str, Figure]:
        """Figure of the anti-factor Xa activity against apixaban in plasma.

        The simulations only: the individual values of the paper (Fig4) are not
        curated in pkdb_data.
        """
        fig = Figure(
            experiment=self,
            sid="PD_scatter_xa",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.labels["Carm_api"], unit=self.units["Carm_api"]),
            legend=True,
        )
        plots[0].set_yaxis(
            self.labels["COAG__antiXa_activity"],
            unit=self.units["COAG__antiXa_activity"],
            scale="linear",
        )
        for group in self.groups:
            plots[0].add_data(
                task=self.to_sid(f"task_{group}"),
                xid="Carm_api",
                yid="COAG__antiXa_activity",
                label="sim: 10mg PO"
                if group == "normal"
                else f"sim {self.short_names[group]}: 10mg PO",
                color=self.colors[group],
            )

        return self.figures_by_sid(fig)

    def figure_scatter_inr(self) -> dict[str, Figure]:
        """Figure of the INR against apixaban in plasma.

        The simulations only: the individual values of the paper (Fig4) are not
        curated in pkdb_data.
        """
        fig = Figure(
            experiment=self,
            sid="PD_scatter_inr",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.labels["Carm_api"], unit=self.units["Carm_api"]),
            legend=True,
        )
        plots[0].set_yaxis(
            self.labels["COAG__INR"],
            unit=self.units["COAG__INR"],
            scale="linear",
        )
        for group in self.groups:
            plots[0].add_data(
                task=self.to_sid(f"task_{group}"),
                xid="Carm_api",
                yid="COAG__INR",
                label="sim: 10mg PO"
                if group == "normal"
                else f"sim {self.short_names[group]}: 10mg PO",
                color=self.colors[group],
            )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Chang2016, output_dir=Chang2016.__name__)
