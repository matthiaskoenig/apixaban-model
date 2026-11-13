"""Simulation experiment of the study Song2015."""

import math
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


class Song2015(ApixabanSimulationExperiment):
    """Simulation experiment of Song2015.

    Three crossover studies in healthy subjects with single doses immediately
    after a 10 h overnight fast. Study 1: 10 mg as 2 x 5 mg tablets or as an
    oral solution. Study 2: 5 mg oral solution by mouth or via a nasogastric
    tube (NGT) flushed with 5 % dextrose (D5W) or infant formula. Study 3: 5 mg
    oral solution by mouth, via NGT followed by a nutritional supplement (Boost
    Plus) or a crushed 5 mg tablet suspended in D5W via NGT. The arm with the
    nutritional supplement is fed (`FED`, the slower gastric emptying of the
    fed state), the other arms are fasted.

    The data are re-digitized from the vector graphic of the figure (log axis);
    the +1 SD bars of overlapping series end at the same height and cannot be
    assigned to a series, so the SDs are not used.

    The subjects are mostly men (18 women of 56; 2 of 14, 8 of 21 and 8 of 21
    in the three studies) and run on the male build.
    """

    #: the studies (panels of the figure) and their arms
    studies: ClassVar[dict[str, list[str]]] = {
        "study 1": ["API10_PO_TAB", "API10_PO_OS"],
        "study 2": ["API5_PO_OS", "API5_NGT_D5W", "API5_NGT_IF"],
        "study 3": ["API5_PO_OS_3", "API5_NGT_NS", "API5_NGT_D5W_crushed"],
    }
    groups: ClassVar[list[str]] = [
        group for groups in studies.values() for group in groups
    ]
    colors: ClassVar[dict[str, str]] = {
        "API10_PO_TAB": "black",
        "API10_PO_OS": "tab:blue",
        "API5_PO_OS": "black",
        "API5_NGT_D5W": "tab:blue",
        "API5_NGT_IF": "tab:purple",
        "API5_PO_OS_3": "black",
        "API5_NGT_NS": "tab:blue",
        "API5_NGT_D5W_crushed": "tab:purple",
    }
    #: body weight [kg] and BMI [kg/m^2] of the studies (Table I)
    bodyweight: ClassVar[dict[str, float]] = {
        "study 1": 78.0,
        "study 2": 75.6,
        "study 3": 75.2,
    }
    bmi: ClassVar[dict[str, float]] = {
        "study 1": 25.5,
        "study 2": 25.4,
        "study 3": 26.1,
    }
    dose: ClassVar[dict[str, float]] = {  # [mg]
        "API10_PO_TAB": 10,
        "API10_PO_OS": 10,
        "API5_PO_OS": 5,
        "API5_NGT_D5W": 5,
        "API5_NGT_IF": 5,
        "API5_PO_OS_3": 5,
        "API5_NGT_NS": 5,
        "API5_NGT_D5W_crushed": 5,
    }
    #: the tablet dissolves, the solutions and the suspension of the crushed
    #: tablet are given as a solution
    dosing_parameter: ClassVar[dict[str, str]] = {
        "API10_PO_TAB": "PODOSE_api",
        "API10_PO_OS": "SOLDOSE_api",
        "API5_PO_OS": "SOLDOSE_api",
        "API5_NGT_D5W": "SOLDOSE_api",
        "API5_NGT_IF": "SOLDOSE_api",
        "API5_PO_OS_3": "SOLDOSE_api",
        "API5_NGT_NS": "SOLDOSE_api",
        "API5_NGT_D5W_crushed": "SOLDOSE_api",
    }
    application_forms: ClassVar[dict[str, ApplicationForm]] = {
        "API10_PO_TAB": ApplicationForm.TABLET,
        "API10_PO_OS": ApplicationForm.SOLUTION,
        "API5_PO_OS": ApplicationForm.SOLUTION,
        "API5_NGT_D5W": ApplicationForm.SOLUTION,
        "API5_NGT_IF": ApplicationForm.SOLUTION,
        "API5_PO_OS_3": ApplicationForm.SOLUTION,
        "API5_NGT_NS": ApplicationForm.SOLUTION,
        "API5_NGT_D5W_crushed": ApplicationForm.SUSPENSION,
    }
    legends: ClassVar[dict[str, str]] = {
        "API10_PO_TAB": "10mg TAB",
        "API10_PO_OS": "10mg SOL",
        "API5_PO_OS": "5mg SOL",
        "API5_NGT_D5W": "5mg SOL NGT + D5W",
        "API5_NGT_IF": "5mg SOL NGT + infant formula",
        "API5_PO_OS_3": "5mg SOL",
        "API5_NGT_NS": "5mg SOL NGT + Boost Plus",
        "API5_NGT_D5W_crushed": "5mg crushed TAB in D5W NGT",
    }

    infos_pk: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
    }

    def study(self, group: str) -> str:
        """Get the study of a group.

        Args:
            group: the arm of a study.

        Returns:
            The study of the arm.
        """
        return next(key for key, groups in self.studies.items() if group in groups)

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        df = self.load_dataframe("Fig1")
        for label, df_label in df.groupby("label"):
            label = str(label)
            dset = DataSet.from_df(df_label, self.ureg)
            if label.startswith("apixaban_"):
                dset.unit_conversion("mean", 1 / self.Mr["api"])
            dsets[label] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims: dict[str, Simulation] = {}
        for group in self.groups:
            study = self.study(group)
            height = 100 * math.sqrt(self.bodyweight[study] / self.bmi[study])
            tcsims[group] = Simulation(
                time_unit="hr",
                end=75,
                preinit_changes={
                    **self.default_changes(),
                    self.dosing_parameter[group]: Q(self.dose[group], "mg"),
                    "BW": Q(self.bodyweight[study], "kg"),
                    "HEIGHT": Q(height, "cm"),
                    # Boost Plus (240 ml) with the dose through the tube
                    "FED": Q(int(group == "API5_NGT_NS"), "dimensionless"),
                },
            )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings: dict[str, FitMapping] = {}
        for sid, name in self.infos_pk.items():
            for group in self.groups:
                mappings[f"fm_{name}_{group}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"{name}_{group}",
                        xid="time",
                        yid="mean",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=f"task_{group}",
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        # the vocabulary has no nasogastric tube
                        route=Route.PO,
                        application_form=self.application_forms[group],
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        # Boost Plus (240 ml) with the dose
                        fasting=Fasting.FED
                        if group == "API5_NGT_NS"
                        else Fasting.FASTED,
                        coadministration=Coadministration.NONE,
                        data=PKPDData.PK,
                        data_type=DataType.MEAN,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure_pk(),
        }

    def figure_pk(self) -> dict[str, Figure]:
        """Apixaban in plasma in the three studies."""
        fig = Figure(
            experiment=self,
            sid="Fig1",
            name=f"{self.__class__.__name__}",
            num_cols=3,
            num_rows=1,
            height=self.panel_height,
            width=self.panel_width * 3,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        for kp, (study, groups) in enumerate(self.studies.items()):
            for sid, name in self.infos_pk.items():
                plots[kp].set_title(study)
                plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid])
                for group in groups:
                    plots[kp].add_data(
                        task=f"task_{group}",
                        xid="time",
                        yid=sid,
                        label=f"sim {self.legends[group]}",
                        color=self.colors[group],
                    )
                    plots[kp].add_data(
                        dataset=f"{name}_{group}",
                        xid="time",
                        yid="mean",
                        count="count",
                        label=self.legends[group],
                        color=self.colors[group],
                        marker="o",
                    )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Song2015, output_dir=Song2015.__name__)
