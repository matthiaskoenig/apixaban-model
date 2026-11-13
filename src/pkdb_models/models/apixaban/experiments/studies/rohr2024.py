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


class Rohr2024(ApixabanSimulationExperiment):
    """Simulation experiment of Rohr2024.

    Time course of the ritonavir interaction in 8 healthy volunteers (7
    females): a microdosed cocktail of apixaban 25 µg, edoxaban 50 µg and
    rivaroxaban 25 µg from oral stock solutions (with a CYP probe cocktail) at
    baseline and on day 5 of ritonavir 100 mg b.i.d., fasted from 8 h before
    until 4 h after the dose. Plasma 0.5-24 h, urine 0-24 h (n=7). The data
    are geometric means (the 95 % CI of the paper is not a spread of the data).

    The volunteers are mostly women (7 of 8) and run on the female build.
    """

    sex: ClassVar[Sex] = Sex.FEMALE

    interventions: ClassVar[list[str]] = [
        "API25_RIV25_EDO50",
        "API25_RIV25_EDO50_RITx5",
    ]
    colors: ClassVar[dict[str, str]] = {
        "API25_RIV25_EDO50": "tab:brown",
        "API25_RIV25_EDO50_RITx5": "tab:blue",
    }
    markers: ClassVar[dict[str, str]] = {
        "API25_RIV25_EDO50": "s",
        "API25_RIV25_EDO50_RITx5": "o",
    }
    legend_labels: ClassVar[dict[str, str]] = {
        "API25_RIV25_EDO50": "25µg SOL",
        "API25_RIV25_EDO50_RITx5": "25µg SOL + ritonavir 100mg BID (day 5)",
    }
    coadministrations: ClassVar[dict[str, Coadministration]] = {
        "API25_RIV25_EDO50": Coadministration.COCKTAIL,
        "API25_RIV25_EDO50_RITx5": Coadministration.RITONAVIR,
    }
    #: The factors of the interaction are not fitted but set from the
    #: literature; the arm is validation data. Low-dose ritonavir inhibits
    #: CYP3A4 strongly (midazolam AUC x>10 in this study) and inhibits but after
    #: repeated doses also induces P-gp; observed for apixaban AUC0-24 x1.29 and
    #: Cmax x1.35 (geometric mean ratios, Table 1), i.e. a smaller effect than
    #: ketoconazole. CYP3A4 is reduced, the intestinal secretion is left
    #: unchanged (inhibition and induction of P-gp). The factors give AUC x1.33
    #: and Cmax x1.06 for the microdose with the adopted fits.
    interactions: ClassVar[dict[str, dict[str, float]]] = {
        "API25_RIV25_EDO50": {},
        "API25_RIV25_EDO50_RITx5": {"LI__f_cyp3a4": 0.4},
    }

    #: apixaban microdose [mg]
    dose = 0.025

    infos_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
        "Aurine_api": "apixaban_urine",
    }

    #: the statistic of the data and its error by the name of the data: the
    #: concentrations (the 95 % CI in the comments) and the urinary amounts
    #: (derived from the recovery of Tab1) are geometric means without a
    #: spread, the value of 0 at the dose is not part of the series
    yids: ClassVar[dict[str, tuple[str, str | None]]] = {
        "apixaban": ("gmean", None),
        "apixaban_urine": ("gmean", None),
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id, name in [("Fig2", "apixaban"), ("Tab1", "apixaban_urine")]:
            df = self.load_dataframe(fig_id)
            yid = self.yids[name][0]
            for intervention in self.interventions:
                df_label = df[df["label"] == f"{name}_{intervention}"]
                df_label = df_label[df_label[yid].notna()]
                dset = DataSet.from_df(df_label, self.ureg)
                if name == "apixaban":
                    dset.unit_conversion(yid, 1 / self.Mr["api"])
                dsets[self.to_sid(f"{name}_{intervention}")] = dset
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
                tissue = Tissue.URINE if "urine" in name else Tissue.PLASMA
                mappings[self.to_sid(f"fm_{name}_{intervention}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(f"{name}_{intervention}"),
                        xid="time",
                        yid=self.yids[name][0],
                        yid_sd=self.yids[name][1],
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_{intervention}"),
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=tissue,
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
                    yid=self.yids[name][0],
                    yid_sd=self.yids[name][1],
                    count="count",
                    label=self.legend_labels[intervention],
                    color=self.colors[intervention],
                    marker=self.markers[intervention],
                    linestyle="" if sid == "Aurine_api" else "dashed",
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Rohr2024, output_dir=Rohr2024.__name__)
