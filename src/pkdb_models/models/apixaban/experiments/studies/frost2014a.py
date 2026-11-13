"""Simulation experiment of the study Frost2014a."""

from typing import ClassVar, override

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


class Frost2014a(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2014a.

    A single dose of 10 mg apixaban alone and with naproxen 500 mg in 21
    healthy men. The arm with naproxen is simulated and plotted, but not
    mapped: `pkpdsim.metadata.Coadministration` has no member for naproxen.

    The subjects are men (21) and run on the male build.
    """

    bodyweight = 83.3  # [kg]
    height = 178.0  # [cm]

    #: the baseline INR of the arms (Tab3)
    inr: ClassVar[dict[str, float]] = {
        "API10": 0.94,
        "API10_NAPR500": 0.92,
    }
    #: the arms, the labels of the curation are of the interventions
    arms: ClassVar[list[str]] = ["API10", "API10_NAPR500"]
    colors: ClassVar[dict[str, str]] = {
        "API10": "black",
        "API10_NAPR500": "tab:red",
    }
    legends: ClassVar[dict[str, str]] = {
        "API10": "10mg PO",
        "API10_NAPR500": "10mg PO, naproxen 500mg",
    }
    #: the interaction factors of the perpetrators, not fitted (validation):
    #: naproxen inhibits the intestinal efflux of apixaban by P-gp (no
    #: inhibition of CYP3A4); the study observed AUCinf x1.54 and Cmax x1.61,
    #: the factor gives AUC x1.42 and Cmax x1.16 with the adopted fits (the
    #: increase of the Cmax is not reproduced)
    interactions: ClassVar[dict[str, dict[str, float]]] = {
        "API10": {},
        "API10_NAPR500": {"GU__f_abcb1": 0.1},
    }

    infos_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
    }
    #: the INR before and 3 hr after the dose, the anti-Xa activity 3 hr after
    #: the dose (Tab3; the values below the limit of quantification before the
    #: dose are not curated)
    infos_pd: ClassVar[dict[str, str]] = {
        "COAG__INR": "inr",
        "COAG__antiXa_activity": "Anti-factor Xa activity",
    }

    @staticmethod
    def label(arm: str, name: str) -> str:
        """Get the label of the curation of an arm and a measurement."""
        if name == "apixaban":
            return f"{arm}_all_apixaban"
        if name == "inr":
            return f"{arm}_inr_all"
        return f"Anti_factor_Xa_activity_plasma_{arm}_all"

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        labels = {
            self.label(arm, name)
            for arm in self.arms
            for name in [*self.infos_pk.values(), *self.infos_pd.values()]
        }
        for fig_id in ["Fig2", "Tab3"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                if label not in labels:
                    continue
                dset = DataSet.from_df(df_label, self.ureg)
                if label.endswith("_all_apixaban"):
                    dset.unit_conversion("mean", 1 / self.Mr["api"])
                dsets[self.to_sid(label)] = dset

        # individual anti-Xa activity against the concentration (Fig3)
        df = self.load_dataframe("Fig3")
        dset = DataSet.from_df(df, self.ureg)
        dset.unit_conversion("x", 1 / self.Mr["api"])
        dsets["apixaban_vs_antixa_API10"] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        return {
            key: Simulation(
                time_unit="hr",
                end=75,
                preinit_changes={
                    **self.default_changes(),
                    "PODOSE_api": Q(10, "mg"),
                    "BW": Q(self.bodyweight, "kg"),
                    "HEIGHT": Q(self.height, "cm"),
                    "COAG__INR_ref": Q(self.inr[key], "dimensionless"),
                    **{
                        pid: Q(value, "dimensionless")
                        for pid, value in self.interactions[key].items()
                    },
                },
            )
            for key in self.arms
        }

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings: dict[str, FitMapping] = {}
        infos = {
            **self.infos_pk,
            **self.infos_pd,
        }
        for sid, name in infos.items():
            mappings[self.to_sid(f"fm_{name}_healthy")] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=self.to_sid(self.label("API10", name)),
                    xid="time",
                    yid="mean",
                    yid_sd="" if sid == "Carm_api" else "mean_sd",
                    count="count",
                ),
                observable=FitData(
                    self,
                    task="task_API10",
                    xid="time",
                    yid=sid,
                ),
                metadata=PKPDMappingMetaData(
                    tissue=Tissue.PLASMA,
                    route=Route.PO,
                    application_form=ApplicationForm.TABLET,
                    dosing=Dosing.SINGLE,
                    health=Health.HEALTHY,
                    fasting=Fasting.NR,
                    coadministration=Coadministration.NONE,
                ),
            )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure(),
        }

    def figure(self) -> dict[str, Figure]:
        """Figure of the pharmacokinetics and the pharmacodynamics."""
        fig = Figure(
            experiment=self,
            sid="PK",
            name=f"{self.__class__.__name__}",
            num_cols=2,
            num_rows=2,
            height=self.panel_height * 2 * 1.1,
            width=self.panel_width * 2,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        for _kp, sid in enumerate(self.infos_pk):
            plots[0].set_yaxis(self.labels[sid], unit=self.units[sid])
        for kp, sid in enumerate(self.infos_pd):
            plots[kp + 1].set_yaxis(self.labels[sid], unit=self.units[sid])

        for key in self.arms:
            for sid, name in self.infos_pk.items():
                plots[0].add_data(
                    task=f"task_{key}",
                    xid="time",
                    yid=sid,
                    label=f"sim: {self.legends[key]}",
                    color=self.colors[key],
                )
                plots[0].add_data(
                    dataset=self.to_sid(self.label(key, name)),
                    xid="time",
                    yid="mean",
                    count="count",
                    label=f"exp: {self.legends[key]}",
                    color=self.colors[key],
                )
            for kp, (sid, name) in enumerate(self.infos_pd.items()):
                plots[kp + 1].add_data(
                    task=f"task_{key}",
                    xid="time",
                    yid=sid,
                    label=f"sim: {self.legends[key]}",
                    color=self.colors[key],
                )
                plots[kp + 1].add_data(
                    dataset=self.to_sid(self.label(key, name)),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp: {self.legends[key]}",
                    color=self.colors[key],
                )

        plots[3].set_xaxis(self.labels["Carm_api"], unit=self.units["Carm_api"])
        plots[3].set_yaxis(
            self.labels["COAG__antiXa_activity"],
            unit=self.units["COAG__antiXa_activity"],
            scale="linear",
        )

        # simulation
        plots[3].add_data(
            task="task_API10",
            xid="Carm_api",
            yid="COAG__antiXa_activity",
            label="sim: 10mg PO",
            color="black",
            linestyle="solid",
        )

        plots[3].add_data(
            xid="x",
            yid="y",
            dataset="apixaban_vs_antixa_API10",
            label="exp indiv: 10mg PO",
            color="white",
            markeredgecolor="black",
            marker="o",
            linestyle="",
        )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Frost2014a, output_dir=Frost2014a.__name__)
