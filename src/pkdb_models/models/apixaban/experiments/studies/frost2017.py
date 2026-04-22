from typing import Dict

from sbmlsim.data import DataSet, load_pkdb_dataframe
from sbmlsim.fit import FitMapping, FitData
from sbmlutils.console import console

from pkdb_models.models import apixaban
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)
from pkdb_models.models.apixaban.experiments.metadata import (
    Tissue,
    Route,
    Dosing,
    Coadministration,
    ApplicationForm,
    Health,
    Fasting,
    ApixabanMappingMetaData,
)

from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Timecourse, TimecourseSim

from pkdb_models.models.apixaban.helpers import run_experiments


class Frost2017(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2017."""

    bodyweights = {
        "ATEN": 80.9,
    }
    colors = {
        "API10": "black",
        "API10, ATEN": "tab:red",
    }

    interventions = list(colors.keys())



    infos_pk = {
        "[Cve_api]": "apixaban",
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig3"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby("label"):
                dset = DataSet.from_df(df_label, self.ureg)
                if "apixaban" in label:
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[label] = dset

        # console.print(dsets)

        return dsets

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims = {}
        bodyweight = self.bodyweights["ATEN"]

        for intervention in self.interventions:
            tcsims[intervention] = TimecourseSim([
                Timecourse(
                    start=0,
                    end=73 * 60,  # [min]
                    steps=1000,
                    changes={
                        **self.default_changes(),
                        "BW": Q_(bodyweight, "kg"),
                        "PODOSE_api": Q_(10, "mg"),
                    },
                )
            ])

        return tcsims

    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings = {}
        for intervention in self.interventions:
            # pharmacokinetics
            for k, sid in enumerate(self.infos_pk.keys()):
                name = self.infos_pk[sid]
                mappings[f"fm_{name}_{intervention}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"{name}_{intervention}",
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=f"task_{intervention}",
                        xid="time",
                        yid=sid,
                    ),
                    metadata=ApixabanMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
                        coadministration=Coadministration.ATENOLOL if "ATEN" in intervention else Coadministration.NONE,
                    )
                )

        return mappings

    def figures(self) -> Dict[str, Figure]:
        return {
            **self.figure_pk()
        }

    def figure_pk(self) -> Dict[str, Figure]:
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

        for intervention in self.interventions:
            for k, sid in enumerate(self.infos_pk.keys()):
                name = self.infos_pk[sid]
                if "ATEN" not in intervention:
                    #simulation
                    plots[k].add_data(
                        task=f"task_{intervention}",
                        xid="time",
                        yid=sid,
                        label="sim: api 10mg, aten 100mg PO" if "ATEN" in intervention else "sim: api 10mg PO",
                        color=self.colors[intervention],
                    )
                # data
                plots[k].add_data(
                    dataset=f"{name}_{intervention}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label="exp: api 10mg, aten 100mg PO" if "ATEN" in intervention else "exp: api 10mg PO",
                    color=self.colors[intervention],
                )

        return {fig.sid: fig}


if __name__ == "__main__":
    run_experiments(Frost2017, output_dir=Frost2017.__name__)

