"""Simulation experiment of the study Lenard2025."""

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


class Lenard2025(ApixabanSimulationExperiment):
    """Simulation experiment of Lenard2025.

    Interactions of carbamazepine, gabapentin and pregabalin with the factor Xa
    inhibitors in three cohorts of healthy volunteers (12, 11 and 12 evaluated):
    a microdosed cocktail of apixaban 25 µg, edoxaban 50 µg and rivaroxaban
    25 µg as an oral solution (with midazolam 30 µg) at baseline and at the
    steady state of the perpetrator. Fasting is not reported.

    The volunteers are mostly women (22 of 36 over the three cohorts, the sex
    of a cohort is not curated) and run on the female build.
    """

    sex: ClassVar[Sex] = Sex.FEMALE

    #: the cohorts: the figure of the data and the baseline and perpetrator arm
    cohorts: ClassVar[dict[str, list[str]]] = {
        "Fig2": ["API25_RIV25_EDO50_1", "API25_RIV25_EDO50_CAR"],
        "Fig3": ["API25_RIV25_EDO50_2", "API25_RIV25_EDO50_GAB"],
        "Fig4": ["API25_RIV25_EDO50_3", "API25_RIV25_EDO50_PRE"],
    }
    interventions: ClassVar[list[str]] = [
        intervention for arms in cohorts.values() for intervention in arms
    ]
    markers: ClassVar[dict[str, str]] = {
        "API25_RIV25_EDO50_1": "s",
        "API25_RIV25_EDO50_CAR": "o",
        "API25_RIV25_EDO50_2": "s",
        "API25_RIV25_EDO50_GAB": "o",
        "API25_RIV25_EDO50_3": "s",
        "API25_RIV25_EDO50_PRE": "o",
    }
    colors: ClassVar[dict[str, str]] = {
        "API25_RIV25_EDO50_1": "black",
        "API25_RIV25_EDO50_CAR": "tab:pink",
        "API25_RIV25_EDO50_2": "black",
        "API25_RIV25_EDO50_GAB": "tab:orange",
        "API25_RIV25_EDO50_3": "black",
        "API25_RIV25_EDO50_PRE": "tab:red",
    }
    legend_labels: ClassVar[dict[str, str]] = {
        "API25_RIV25_EDO50_1": "25µg SOL",
        "API25_RIV25_EDO50_CAR": "25µg SOL + carbamazepine max 200mg BID",
        "API25_RIV25_EDO50_2": "25µg SOL",
        "API25_RIV25_EDO50_GAB": "25µg SOL + gabapentin 400mg TID",
        "API25_RIV25_EDO50_3": "25µg SOL",
        "API25_RIV25_EDO50_PRE": "25µg SOL + pregabalin 300mg BID",
    }
    coadministrations: ClassVar[dict[str, Coadministration]] = {
        "API25_RIV25_EDO50_1": Coadministration.COCKTAIL,
        "API25_RIV25_EDO50_CAR": Coadministration.CARBAMAZEPINE,
        "API25_RIV25_EDO50_2": Coadministration.COCKTAIL,
        "API25_RIV25_EDO50_GAB": Coadministration.GABAPENTIN,
        "API25_RIV25_EDO50_3": Coadministration.COCKTAIL,
        "API25_RIV25_EDO50_PRE": Coadministration.PREGABALIN,
    }
    #: The factors of the interactions are not fitted but set from the
    #: literature; the arms are validation data.
    #: Carbamazepine (titrated to max 200 mg b.i.d., 21 d) induces CYP3A4 and
    #: P-gp; observed AUCinf x0.66 and Cmax x0.88 (geometric mean ratios,
    #: Table 1). The factors give AUC x0.68 and Cmax x0.88 for the microdose
    #: with the adopted fits.
    #: Gabapentin (400 mg t.i.d., 13 d) and pregabalin (300 mg b.i.d., 21 d) are
    #: neither metabolized by nor inhibit or induce CYP3A4 and P-gp; observed
    #: AUCinf x0.93 and x0.98 (Tables 2 and 3), no factors.
    interactions: ClassVar[dict[str, dict[str, float]]] = {
        "API25_RIV25_EDO50_1": {},
        "API25_RIV25_EDO50_CAR": {"LI__f_cyp3a4": 1.5, "GU__f_abcb1": 1.8},
        "API25_RIV25_EDO50_2": {},
        "API25_RIV25_EDO50_GAB": {},
        "API25_RIV25_EDO50_3": {},
        "API25_RIV25_EDO50_PRE": {},
    }

    #: apixaban microdose [mg]
    dose = 0.025

    infos_pk: ClassVar[dict[str, str]] = {"Carm_api": "apixaban"}

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in self.cohorts:
            df = self.load_dataframe(fig_id)
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
        figures: dict[str, Figure] = {}
        for fig_id in self.cohorts:
            figures.update(self.figure_pk(fig_id))
        return figures

    def figure_pk(self, fig_id: str) -> dict[str, Figure]:
        """Figure of the pharmacokinetics of a cohort.

        Args:
            fig_id: figure of the cohort in the publication.

        Returns:
            The figure by its sid.
        """
        fig = Figure(
            experiment=self,
            sid=fig_id,
            name=f"{self.__class__.__name__} ({fig_id})",
            height=self.panel_height,
            width=self.panel_width * 1.1,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )
        plots[0].set_yaxis(self.label_api_plasma, unit="nM")
        for intervention in self.cohorts[fig_id]:
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
    MODEL.run_experiments(Lenard2025, output_dir=Lenard2025.__name__)
