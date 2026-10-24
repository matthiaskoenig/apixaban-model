"""Simulation experiment of the study Garonzik2019."""

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


class Garonzik2019(ApixabanSimulationExperiment):
    """Simulation experiment of Garonzik2019.

    Single sequence crossover in healthy subjects: a single oral dose of 10 mg
    apixaban (two 5 mg tablets) on day 1 and on day 8 at the steady state of
    clarithromycin 500 mg BID (days 4 to 10), fasted from 8 h before until
    4 h after the dose.
    """

    #: the groups of the data (Fig 2), the dataset labels by group
    groups: ClassVar[dict[str, str]] = {
        "API10": "apixaban_TX_API5_1",
        "API10_CLARI500": "concomitant_TX_CLARI_1, TX_API5_2",
    }
    colors: ClassVar[dict[str, str]] = {
        "API10": "black",
        "API10_CLARI500": "tab:blue",
    }
    group_labels: ClassVar[dict[str, str]] = {
        "API10": "10mg PO",
        "API10_CLARI500": "10mg PO + clarithromycin",
    }
    coadministrations: ClassVar[dict[str, Coadministration]] = {
        "API10": Coadministration.NONE,
        "API10_CLARI500": Coadministration.CLARITHROMYCIN,
    }
    #: The factors of the interaction are not fitted but set from the
    #: literature; with the unfitted model they reproduce the ratios observed in
    #: this study roughly, the arm is validation data.
    #: Clarithromycin 500 mg BID inhibits CYP3A4 and P-gp; observed geometric
    #: mean ratios AUCinf 1.60, Cmax 1.30 with an unchanged half-life (mostly a
    #: higher bioavailability), i.e. a moderate effect on apixaban, smaller
    #: than the one of ketoconazole. The factors give AUC x1.58, Cmax x1.15 for
    #: 10 mg.
    interactions: ClassVar[dict[str, dict[str, float]]] = {
        "API10": {},
        "API10_CLARI500": {"LI__f_cyp3a4": 0.5, "GU__f_pgp": 0.5},
    }
    bodyweight = 72.35  # [kg]
    bodyheight = 167.65  # [cm]

    infos_pk: ClassVar[dict[str, str]] = {
        "[Cve_api]": "apixaban",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[self.to_sid(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims: dict[str, Simulation] = {}
        for group in self.groups:
            tcsims[self.to_sid(group)] = Simulation(
                time_unit="hr",
                end=36,
                preinit_changes={
                    **self.default_changes(),
                    "PODOSE_api": Q(10, "mg"),
                    "BW": Q(self.bodyweight, "kg"),
                    "HEIGHT": Q(self.bodyheight, "cm"),
                    **{
                        pid: Q(value, "dimensionless")
                        for pid, value in self.interactions[group].items()
                    },
                },
            )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        # PK
        for sid, name in self.infos_pk.items():
            for group, dset_label in self.groups.items():
                mappings[self.to_sid(f"fm_{name}_{group}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(dset_label),
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
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
                        coadministration=self.coadministrations[group],
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {**self.figure_pk()}

    def figure_pk(self) -> dict[str, Figure]:
        """Figure of the pharmacokinetics with and without clarithromycin."""
        fig = Figure(
            experiment=self,
            sid="Fig2",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)
        for ks, sid in enumerate(self.infos_pk):
            for group, dset_label in self.groups.items():
                # simulation
                plots[ks].add_data(
                    task=self.to_sid(f"task_{group}"),
                    xid="time",
                    yid=sid,
                    label=f"sim {self.group_labels[group]}",
                    color=self.colors[group],
                )
                # data
                plots[ks].add_data(
                    dataset=self.to_sid(dset_label),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp {self.group_labels[group]}",
                    color=self.colors[group],
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Garonzik2019, output_dir=Garonzik2019.__name__)
