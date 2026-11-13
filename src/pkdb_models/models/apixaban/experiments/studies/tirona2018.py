"""Simulation experiment of the study Tirona2018."""

import math
from collections.abc import Mapping
from types import MappingProxyType
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


class Tirona2018(ApixabanSimulationExperiment):
    """Simulation experiment of Tirona2018.

    A single oral dose of 2.5 mg apixaban (tablet) together with 5 mg
    rosuvastatin after an overnight fast in healthy controls (n = 12) and
    patients with nonalcoholic fatty liver disease (NAFLD, n = 22). Rosuvastatin
    does not interact with apixaban (no effect on the transport of apixaban in
    Caco-2 cells, no inhibitor or inducer of CYP3A4 or P-gp), the simulations
    have no interaction factor; the coadministration is part of the metadata.
    The paper explains the lower exposure of the NAFLD patients by their body
    weight (99.9 against 65.6 kg), pkpdsim has no health status NAFLD: the
    patients are obese (BMI 34.0).

    The controls are mostly women (10 of 12) and run on the female build; the
    NAFLD patients (11 women of 22, no majority) run on the male build. The
    curated sex of the whole study (32 women of 34) disagrees with its groups
    (21 women), see TODO.md.
    """

    simulation_sexes: ClassVar[Mapping[str, Sex]] = MappingProxyType(
        {
            "control": Sex.FEMALE,
        }
    )

    colors: ClassVar[dict[str, str]] = {
        "control": "black",
        "nafld": "tab:blue",
    }
    groups: ClassVar[list[str]] = list(colors.keys())
    bodyweights: ClassVar[dict[str, float]] = {  # [kg]
        "control": 65.6,
        "nafld": 99.9,
    }
    bmis: ClassVar[dict[str, float]] = {  # [kg/m^2]
        "control": 23.4,
        "nafld": 34.0,
    }
    health: ClassVar[dict[str, Health]] = {
        "control": Health.HEALTHY,
        "nafld": Health.OBESE,
    }
    legends: ClassVar[dict[str, str]] = {
        "control": "control 2.5mg PO + ROS 5mg",
        "nafld": "NAFLD 2.5mg PO + ROS 5mg",
    }

    infos_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
        "Aurine_api": "cumulative amount",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        labels = {
            self.dataset_key(group, sid)
            for group in self.groups
            for sid in self.infos_pk
        }
        for fig_id in ["Tab2", "Fig2"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                if label not in labels:
                    continue
                dset = DataSet.from_df(df_label, self.ureg)
                dset.unit_conversion("mean", 1 / self.Mr["api"])
                dsets[label] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims: dict[str, Simulation] = {}
        for group in self.groups:
            bodyweight = self.bodyweights[group]
            tcsims[group] = Simulation(
                time_unit="hr",
                end=30,
                preinit_changes={
                    **self.default_changes(),
                    "PODOSE_api": Q(2.5, "mg"),
                    "BW": Q(bodyweight, "kg"),
                    "HEIGHT": Q(math.sqrt(bodyweight / self.bmis[group]), "m"),
                },
            )
        return tcsims

    def dataset_key(self, group: str, sid: str) -> str:
        """Key of the dataset of a group and an observable.

        Args:
            group: the group.
            sid: the observable.

        Returns:
            The key of the dataset.
        """
        if sid == "Carm_api":
            return f"{group}_apixaban"
        return f"cumulative_amount_apixaban_urine_API2_5_ROS5_{group}"

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings: dict[str, FitMapping] = {}
        for group in self.groups:
            for sid, name in self.infos_pk.items():
                tissue = Tissue.PLASMA if sid == "Carm_api" else Tissue.URINE
                mappings[self.to_sid(f"fm_{name}_{group}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.dataset_key(group, sid),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=f"task_{group}",
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=tissue,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=self.health[group],
                        fasting=Fasting.FASTED,
                        coadministration=Coadministration.ROSUVASTATIN,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure_pk(),
        }

    def figure_pk(self) -> dict[str, Figure]:
        """Apixaban in plasma and urine of the controls and the NAFLD patients."""
        fig = Figure(
            experiment=self,
            sid="PK",
            name=f"{self.__class__.__name__}",
            num_cols=2,
            num_rows=1,
            height=self.panel_height,
            width=self.panel_width * 2,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        for kp, sid in enumerate(self.infos_pk):
            plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid])

        for group in self.groups:
            for kp, sid in enumerate(self.infos_pk):
                # simulation
                plots[kp].add_data(
                    task=f"task_{group}",
                    xid="time",
                    yid=sid,
                    label=f"sim: {self.legends[group]}",
                    color=self.colors[group],
                )
                # data
                plots[kp].add_data(
                    dataset=self.dataset_key(group, sid),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp: {self.legends[group]}",
                    color=self.colors[group],
                    linestyle="solid" if sid == "Carm_api" else "",
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Tirona2018, output_dir=Tirona2018.__name__)
