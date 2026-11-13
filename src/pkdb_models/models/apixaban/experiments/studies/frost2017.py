"""Simulation experiment of the study Frost2017."""

import math
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


class Frost2017(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2017.

    Atenolol study: 15 healthy subjects, randomized crossover of single oral
    doses of apixaban 10 mg (two 5 mg tablets), atenolol 100 mg and both
    together; fasting is not reported.

    The subjects are mostly men (the atenolol study 2 women of 15, the digoxin
    study 24 men) and run on the male build.
    """

    #: body weight [kg] and height [cm] from the BMI 26.4 kg/m^2 (Table 1)
    bodyweight = 80.9
    bodyheight = 100 * math.sqrt(80.9 / 26.4)

    colors: ClassVar[dict[str, str]] = {
        "API10": "black",
        "API10_ATEN": "tab:red",
    }
    group_labels: ClassVar[dict[str, str]] = {
        "API10": "10mg PO",
        "API10_ATEN": "10mg PO + atenolol",
    }
    #: Atenolol is a substrate of P-gp, neither an inhibitor nor an inducer of
    #: CYP3A4 or P-gp, so the arm is simulated without an interaction (the
    #: observed geometric mean ratios are Cmax 0.82, AUCinf 0.85).
    coadministrations: ClassVar[dict[str, Coadministration]] = {
        "API10": Coadministration.NONE,
        "API10_ATEN": Coadministration.ATENOLOL,
    }

    interventions: ClassVar[list[str]] = list(colors.keys())

    infos_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig3"]:
            df = self.load_dataframe(fig_id)
            # the 72 h points of apixaban are digitized as 0 (the figure shows
            # about 1 ng/ml), they are not mapped
            df = df[~((df.substance == "apixaban") & (df.time > 0) & (df["mean"] <= 0))]
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                if "apixaban" in label:
                    dset.unit_conversion("mean", 1 / self.Mr["api"])
                dsets[self.to_sid(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        return {
            "API10": Simulation(
                time_unit="hr",
                end=73,
                preinit_changes={
                    **self.default_changes(),
                    "BW": Q(self.bodyweight, "kg"),
                    "HEIGHT": Q(self.bodyheight, "cm"),
                    "PODOSE_api": Q(10, "mg"),
                },
            )
        }

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for intervention in self.interventions:
            # pharmacokinetics, both arms against the simulation without
            # interaction
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
                        coadministration=self.coadministrations[intervention],
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
            sid="Fig3",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)

        for k, (sid, name) in enumerate(self.infos_pk.items()):
            plots[k].add_data(
                task="task_API10",
                xid="time",
                yid=sid,
                label="sim 10mg PO",
                color="black",
            )
            for intervention in self.interventions:
                plots[k].add_data(
                    dataset=self.to_sid(f"{name}_{intervention}"),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp {self.group_labels[intervention]}",
                    color=self.colors[intervention],
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Frost2017, output_dir=Frost2017.__name__)
