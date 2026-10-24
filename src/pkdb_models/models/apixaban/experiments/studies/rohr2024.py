"""Simulation experiment of the study Rohr2024."""

from typing import ClassVar, override

from pkpdsim.metadata import (
    ApplicationForm,
    Coadministration,
    DataType,
    Dosing,
    Fasting,
    Health,
    PKPDData,
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


class Rohr2024(ApixabanSimulationExperiment):
    """Simulation experiment of Rohr2024.

    Time course of the ritonavir interaction in 8 healthy volunteers (7
    females): a microdosed cocktail of apixaban 25 µg, edoxaban 50 µg and
    rivaroxaban 25 µg from oral stock solutions (with a CYP probe cocktail) at
    baseline and on day 5 of ritonavir 100 mg b.i.d., fasted from 8 h before
    until 4 h after the dose. Plasma 0.5-24 h, urine 0-24 h (n=7). The data
    are geometric means (95 % CI, the SD is derived from the CI).
    """

    interventions: ClassVar[list[str]] = [
        "API25, RIV25, EDO50",
        "API25, RIV25, EDO50, RITx5",
    ]
    colors: ClassVar[dict[str, str]] = {
        "API25, RIV25, EDO50": "tab:brown",
        "API25, RIV25, EDO50, RITx5": "tab:blue",
    }
    markers: ClassVar[dict[str, str]] = {
        "API25, RIV25, EDO50": "s",
        "API25, RIV25, EDO50, RITx5": "o",
    }
    legend_labels: ClassVar[dict[str, str]] = {
        "API25, RIV25, EDO50": "25µg SOL",
        "API25, RIV25, EDO50, RITx5": "25µg SOL + ritonavir 100mg BID (day 5)",
    }
    coadministrations: ClassVar[dict[str, Coadministration]] = {
        "API25, RIV25, EDO50": Coadministration.COCKTAIL,
        "API25, RIV25, EDO50, RITx5": Coadministration.RITONAVIR,
    }
    #: The factors of the interaction are not fitted but set from the
    #: literature; the arm is validation data. Low-dose ritonavir inhibits
    #: CYP3A4 strongly (midazolam AUC x>10 in this study) and inhibits but after
    #: repeated doses also induces P-gp; observed for apixaban AUC0-24 x1.29 and
    #: Cmax x1.35 (geometric mean ratios, Table 1), i.e. a smaller effect than
    #: ketoconazole. CYP3A4 is reduced, the intestinal secretion is left
    #: unchanged (inhibition and induction of P-gp). The factors give AUC x1.29
    #: and Cmax x1.05 for the microdose with the unfitted model.
    interactions: ClassVar[dict[str, dict[str, float]]] = {
        "API25, RIV25, EDO50": {},
        "API25, RIV25, EDO50, RITx5": {"LI__f_cyp3a4": 0.4},
    }

    #: apixaban microdose [mg]
    dose = 0.025

    infos_pk: ClassVar[dict[str, str]] = {
        "[Cve_api]": "apixaban",
        "Aurine_api": "apixaban_urine",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2", "Tab1A"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                if label.startswith("apixaban") and "urine" not in label:
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[self.to_sid(label)] = dset
        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        for intervention in self.interventions:
            tcsims[self.to_sid(intervention)] = Simulation(
                time_unit="hr",
                end=30,
                preinit_changes={
                    **self.default_changes(),
                    "SOLDOSE_api": Q(self.dose, "mg"),
                    **{
                        pid: Q(value, "dimensionless")
                        for pid, value in self.interactions[intervention].items()
                    },
                },
            )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for intervention in self.interventions:
            # pharmacokinetics
            for sid, name in self.infos_pk.items():
                mappings[self.to_sid(f"fm_{name}_{intervention}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(f"{name}_{intervention}"),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_{intervention}"),
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.URINE if "urine" in name else Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.SOLUTION,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
                        coadministration=self.coadministrations[intervention],
                        data=PKPDData.PK,
                        data_type=DataType.MEAN,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {**self.figure_pk()}

    def figure_pk(self) -> dict[str, Figure]:
        """Apixaban in plasma and urine."""
        fig = Figure(
            experiment=self,
            sid="Fig2",
            num_cols=2,
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 2,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )
        plots[0].set_yaxis(self.label_api_plasma, unit="nM")
        plots[1].set_yaxis(self.label_api_urine, unit="nmole")

        for ks, (sid, name) in enumerate(self.infos_pk.items()):
            for intervention in self.interventions:
                plots[ks].add_data(
                    task=self.to_sid(f"task_{intervention}"),
                    xid="time",
                    yid=sid,
                    label=f"sim {self.legend_labels[intervention]}",
                    color=self.colors[intervention],
                )
                plots[ks].add_data(
                    dataset=self.to_sid(f"{name}_{intervention}"),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=self.legend_labels[intervention],
                    color=self.colors[intervention],
                    marker=self.markers[intervention],
                    linestyle="" if sid == "Aurine_api" else "dashed",
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Rohr2024, output_dir=Rohr2024.__name__)
