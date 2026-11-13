"""Simulation experiment of the study Mikus2019."""

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


class Mikus2019(ApixabanSimulationExperiment):
    """Simulation experiment of Mikus2019.

    Interaction of ketoconazole with the factor Xa inhibitors in 18 healthy
    volunteers (crossover): a microdosed cocktail of apixaban 25 µg, edoxaban
    50 µg and rivaroxaban 25 µg as oral solutions (with midazolam 10 µg) alone
    and with ketoconazole 400 mg (24.5 h and 0.5 h before and 24 h after the
    cocktail). Plasma to 48 h (Fig 1 to 24 h), urine 0-48 h. Fasting is not
    reported.

    The volunteers are mostly women (11 of 18) and run on the female build.
    """

    sex: ClassVar[Sex] = Sex.FEMALE

    interventions: ClassVar[list[str]] = [
        "API25_RIV25_EDO50",
        "API25_RIV25_EDO50_KET",
    ]
    colors: ClassVar[dict[str, str]] = {
        "API25_RIV25_EDO50": "black",
        "API25_RIV25_EDO50_KET": "tab:blue",
    }
    markers: ClassVar[dict[str, str]] = {
        "API25_RIV25_EDO50": "s",
        "API25_RIV25_EDO50_KET": "o",
    }
    legend_labels: ClassVar[dict[str, str]] = {
        "API25_RIV25_EDO50": "25µg SOL",
        "API25_RIV25_EDO50_KET": "25µg SOL + ketoconazole 400mg",
    }
    coadministrations: ClassVar[dict[str, Coadministration]] = {
        "API25_RIV25_EDO50": Coadministration.COCKTAIL,
        "API25_RIV25_EDO50_KET": Coadministration.KETOCONAZOLE,
    }
    #: The factors of the interaction are not fitted but set from the
    #: literature (as in Frost2015a); the arm is validation data. Ketoconazole
    #: 400 mg inhibits CYP3A4 strongly and P-gp; observed AUCinf x1.90, Cmax
    #: x1.68 and Ae 24.3 -> 37.0 % (geometric means, Table 1). The factors give
    #: AUC x2.03, Cmax x1.17 and Ae 20.3 -> 41.3 % for the microdose with the
    #: adopted fits.
    interactions: ClassVar[dict[str, dict[str, float]]] = {
        "API25_RIV25_EDO50": {},
        "API25_RIV25_EDO50_KET": {"LI__f_cyp3a4": 0.3, "GU__f_abcb1": 0.3},
    }

    #: apixaban microdose [mg]
    dose = 0.025

    infos_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
        "Aurine_api": "apixaban_urine",
    }

    #: the statistic of the data and its error by the name of the data: the
    #: urinary amounts are geometric means (derived from the recovery of Tab1,
    #: without a spread), the amount of 0 at the dose is not part of the series
    yids: ClassVar[dict[str, tuple[str, str | None]]] = {
        "apixaban": ("mean", "mean_sd"),
        "apixaban_urine": ("gmean", None),
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id, name in [("Fig1", "apixaban"), ("Tab1", "apixaban_urine")]:
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
                end=50,
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
            # PK
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
                        fasting=Fasting.NR,
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
        """Figure of the pharmacokinetics."""
        fig = Figure(
            experiment=self,
            sid="Fig1",
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
    MODEL.run_experiments(Mikus2019, output_dir=Mikus2019.__name__)
