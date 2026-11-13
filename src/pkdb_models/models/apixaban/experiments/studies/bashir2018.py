"""Simulation experiment of the study Bashir2018."""

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


class Bashir2018(ApixabanSimulationExperiment):
    """Simulation experiment of Bashir2018.

    A single dose of 10 mg apixaban alone, with cyclosporine 100 mg and with
    tacrolimus 5 mg (each once daily for 3 days, apixaban with the third dose)
    in 12 healthy fasted men.

    The subjects are men (12) and run on the male build.
    """

    #: the simulation of every dataset (the apixaban arm of Fig2, the
    #: cyclosporine arm of Fig2, the tacrolimus arm of Fig3); the control of
    #: Fig3 (`apixaban_API10_B`) is a second copy of the same arm, not mapped
    dataset_tasks: ClassVar[dict[str, str]] = {
        "apixaban_API10_A": "API10",
        "apixaban_API10_CYC100": "API10_CYC100",
        "apixaban_API10_TAC5": "API10_TAC5",
    }
    colors: ClassVar[dict[str, str]] = {
        "API10": "black",
        "API10_CYC100": "tab:blue",
        "API10_TAC5": "tab:orange",
    }
    legends: ClassVar[dict[str, str]] = {
        "API10": "api 10mg PO",
        "API10_CYC100": "api 10mg PO, cyc 100mg",
        "API10_TAC5": "api 10mg PO, tac 5mg",
    }
    coadministrations: ClassVar[dict[str, Coadministration]] = {
        "API10": Coadministration.NONE,
        "API10_CYC100": Coadministration.CYCLOSPORINE,
        "API10_TAC5": Coadministration.TACROLIMUS,
    }
    #: the interaction factors of the perpetrators, not fitted (validation).
    #: Cyclosporine 100 mg once daily (troughs of 22.4 ng/ml) inhibits the
    #: intestinal efflux by P-gp and BCRP, its inhibition of CYP3A4 is weak at
    #: this exposure; the study observed AUCinf x1.19 and Cmax x1.43, the
    #: factor gives AUC x1.19 and Cmax x1.08 with the adopted fits (the
    #: increase of the Cmax is not reproduced). Tacrolimus 5 mg (troughs of
    #: 3.8 ng/ml) is a substrate of CYP3A4 and P-gp without a relevant
    #: inhibition at this exposure; the observed decrease (AUCinf x0.77, Cmax
    #: x0.87) has no mechanism in the model, so its arm has no change.
    interactions: ClassVar[dict[str, dict[str, float]]] = {
        "API10": {},
        "API10_CYC100": {"GU__f_abcb1": 0.5},
        "API10_TAC5": {},
    }
    #: lower limit of quantification of apixaban (6.0 ng/ml); the means below
    #: it after the dose (48 and 72 hr, digitized as 0 in the arms with a
    #: coadministration) are not used
    lloq = Q(6.0, "ng/ml")

    infos_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2", "Fig3"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                if label.startswith("apixaban"):
                    lloq = self.lloq.to(df_label["unit"].iloc[0]).magnitude
                    df_label = df_label[
                        (df_label["time"] == 0) | (df_label["mean"] >= lloq)
                    ]
                dset = DataSet.from_df(df_label, self.ureg)
                if label.startswith("apixaban"):
                    dset.unit_conversion("mean", 1 / self.Mr["api"])
                dsets[self.to_sid(label)] = dset
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
                    **{
                        pid: Q(value, "dimensionless")
                        for pid, value in self.interactions[key].items()
                    },
                },
            )
            for key in self.colors
        }

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for label, key in self.dataset_tasks.items():
            for sid, name in self.infos_pk.items():
                mappings[self.to_sid(f"fm_{name}_{label}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(label),
                        xid="time",
                        yid="mean",
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
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
                        coadministration=self.coadministrations[key],
                    ),
                )
        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {**self.figure_pk()}

    def figure_pk(self) -> dict[str, Figure]:
        """Figure of the pharmacokinetics with and without coadministration."""
        fig = Figure(
            experiment=self,
            sid="Fig1",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)

        for ks, sid in enumerate(self.infos_pk):
            for label, key in self.dataset_tasks.items():
                # the arm with tacrolimus has no change, its simulation is
                # dotted so that the one of the control stays visible
                plots[ks].add_data(
                    task=f"task_{key}",
                    xid="time",
                    yid=sid,
                    label=f"sim: {self.legends[key]}",
                    color=self.colors[key],
                    linestyle=":" if key == "API10_TAC5" else "-",
                )
                plots[ks].add_data(
                    dataset=self.to_sid(label),
                    xid="time",
                    yid="mean",
                    count="count",
                    label=f"exp: {self.legends[key]}",
                    color=self.colors[key],
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Bashir2018, output_dir=Bashir2018.__name__)
