"""Simulation experiment of the study Lenard2024."""

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


class Lenard2024(ApixabanSimulationExperiment):
    """Simulation experiment of Lenard2024.

    Interaction of clarithromycin with the factor Xa inhibitors in 12 healthy
    volunteers: a microdosed cocktail of apixaban 25 µg, edoxaban 50 µg and
    rivaroxaban 25 µg as an oral solution (with midazolam 30 µg) at baseline
    and on day 8 of clarithromycin 500 mg b.i.d. Fasting is not reported.

    The volunteers are mostly women (9 of 12) and run on the female build.
    """

    sex: ClassVar[Sex] = Sex.FEMALE

    interventions: ClassVar[list[str]] = [
        "API25_RIV25_EDO50",
        "API25_RIV25_EDO50_CLAR",
    ]
    colors: ClassVar[dict[str, str]] = {
        "API25_RIV25_EDO50": "black",
        "API25_RIV25_EDO50_CLAR": "tab:pink",
    }
    markers: ClassVar[dict[str, str]] = {
        "API25_RIV25_EDO50": "s",
        "API25_RIV25_EDO50_CLAR": "o",
    }
    legend_labels: ClassVar[dict[str, str]] = {
        "API25_RIV25_EDO50": "25µg SOL",
        "API25_RIV25_EDO50_CLAR": "25µg SOL + clarithromycin 500mg BID",
    }
    coadministrations: ClassVar[dict[str, Coadministration]] = {
        "API25_RIV25_EDO50": Coadministration.COCKTAIL,
        "API25_RIV25_EDO50_CLAR": Coadministration.CLARITHROMYCIN,
    }
    #: The factors of the interaction are not fitted but set from the
    #: literature; the arm is validation data. Clarithromycin 500 mg b.i.d. is a
    #: strong CYP3A4 and a P-gp inhibitor; observed here AUCinf x1.38 and Cmax
    #: x1.17 (geometric mean ratios, Table 1), x1.60 and x1.30 with therapeutic
    #: doses of apixaban (Garonzik2019). The factors give AUC x1.41 and Cmax
    #: x1.09 for the microdose with the adopted fits.
    interactions: ClassVar[dict[str, dict[str, float]]] = {
        "API25_RIV25_EDO50": {},
        "API25_RIV25_EDO50_CLAR": {"LI__f_cyp3a4": 0.6, "GU__f_abcb1": 0.6},
    }

    #: apixaban microdose [mg]
    dose = 0.025

    infos_pk: ClassVar[dict[str, str]] = {"Carm_api": "apixaban"}

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        df = self.load_dataframe("Fig2")
        for label, df_label in df.groupby("label"):
            label = str(label)
            dset = DataSet.from_df(df_label, self.ureg)
            if label.startswith("apixaban"):
                dset.unit_conversion("mean", 1 / self.Mr["api"])
            dsets[self.to_sid(label)] = dset
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
                        tissue=Tissue.PLASMA,
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
            sid="Fig2",
            num_cols=1,
            name=f"{self.__class__.__name__}",
            height=self.panel_height * 1.2,
            width=self.panel_width * 1.1,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )
        plots[0].set_yaxis(self.label_api_plasma, unit="nM")

        for intervention in self.interventions:
            for ks, (sid, name) in enumerate(self.infos_pk.items()):
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
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Lenard2024, output_dir=Lenard2024.__name__)
