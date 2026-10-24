"""Simulation experiment of the study Frost2015b."""

import math
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
from sbmlsim import Q
from sbmlsim.data import DataSet
from sbmlsim.fit import FitData, FitMapping
from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Simulation

from pkdb_models.models.apixaban import MODEL
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)


class Frost2015b(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2015b.

    Thorough QT study in healthy subjects: apixaban 10 mg and 50 mg QD for 3
    days (form and fasting not reported), the pharmacokinetics of apixaban and
    M1 on day 3.
    """

    bodyweight = 76.6  # kg
    #: the height [cm] from the body weight and the BMI 25.9 kg/m^2 (Table 1)
    bodyheight = 100 * math.sqrt(76.6 / 25.9)

    colors: ClassVar[dict[str, str]] = {"PO10": "#e95e0d", "PO50": "#7f2704"}

    interventions: ClassVar[list[str]] = list(colors.keys())

    doses: ClassVar[dict[str, float]] = {
        "PO10": 10,  # mg
        "PO50": 50,
    }

    infos_pk: ClassVar[dict[str, str]] = {
        "[Cve_api]": "apixaban",
        "[Cve_m1]": "apixaban-M1",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig3"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                if "apixaban-M1" in label:
                    dset.unit_conversion("mean", 1 / self.Mr.m1)
                else:
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[self.to_sid(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        for intervention in self.interventions:
            # doses every 24 hr, the third dose at 48 hr is the time 0 of the data
            tcsims[self.to_sid(f"api_{intervention}")] = Simulation(
                time_unit="hr",
                end=2 * 24 + 52,
                preinit_changes={
                    **self.default_changes(),
                    "BW": Q(self.bodyweight, "kg"),
                    "HEIGHT": Q(self.bodyheight, "cm"),
                    "PODOSE_api": Q(self.doses[intervention], "mg"),
                },
                changes=[
                    self.add_doses(
                        [24, 48], {"PODOSE_api": Q(self.doses[intervention], "mg")}
                    ),
                ],
                time_shift=-2 * 24,
            )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for intervention in self.interventions:
            # pharmacokinetics
            for _k, sid in enumerate(self.infos_pk.keys()):
                name = self.infos_pk[sid]
                mappings[self.to_sid(f"fm_api_{name}_{intervention}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(f"{intervention}_{name}"),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_api_{intervention}"),
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.NR,
                        dosing=Dosing.MULTIPLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.NR,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="Fig3",
            name=f"{self.__class__.__name__}",
            num_rows=1,
            num_cols=2,
        )
        plots = fig.create_plots(
            # the data cover the dosing interval of day 3
            xaxis=Axis(self.label_time, unit=self.unit_time, min=-2, max=26),
            legend=True,
        )

        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)
        plots[1].set_yaxis(self.label_m1_plasma, unit=self.unit_m1)

        for intervention in self.interventions:
            for k, sid in enumerate(self.infos_pk.keys()):
                name = self.infos_pk[sid]
                # simulation
                plots[k].add_data(
                    task=self.to_sid(f"task_api_{intervention}"),
                    xid="time",
                    yid=sid,
                    label=f"sim {self.doses[intervention]:g}mg PO QD, day 3",
                    color=self.colors[intervention],
                )
                # data
                plots[k].add_data(
                    dataset=self.to_sid(f"{intervention}_{name}"),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp {self.doses[intervention]:g}mg PO QD, day 3",
                    color=self.colors[intervention],
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Frost2015b, output_dir=Frost2015b.__name__)
