import math
from typing import Dict

from sbmlsim.data import DataSet, load_pkdb_dataframe
from sbmlsim.fit import FitMapping, FitData
from sbmlutils.console import console

from pkdb_models.models import apixaban
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)
from pkdb_models.models.apixaban.experiments.metadata import (
    Tissue, Route, Dosing, ApplicationForm, Health, Fasting, ApixabanMappingMetaData, Coadministration
)

from sbmlsim.plot import Axis, Figure
    # noqa: E402
from sbmlsim.simulation import Timecourse, TimecourseSim

from pkdb_models.models.apixaban.helpers import run_experiments


class Frost2014a(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2014a."""

    bodyweight = 83.3  # [kg] # control
    bodyheight = 1.78 # [m]

    inr = 0.94

    infos_pk = {
        "[Cve_api]": "apixaban",
    }
    infos_pd = {
        "antiXa_activity": "Anti-factor Xa activity",
        "INR": "inr",
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2", "Tab3", "Fig3"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            group_by = "x_label" if fig_id == "Fig3" else "label"
            for label, df_label in df.groupby(group_by):
                dset = DataSet.from_df(df_label, self.ureg)
                if label.startswith("API10_all"):
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                    dsets[label] = dset
                if fig_id == "Fig3":
                    dset.unit_conversion("x", 1 / self.Mr.api)
                    dsets[label] = dset
                if ("Anti-factor Xa activity" or "_inr_") and "API10_" in label:
                    dsets[label] = dset

        # console.print("datasets:", list(dsets.keys()))
        return dsets


    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims: Dict[str, TimecourseSim] = {}
        tcsims["control"] = TimecourseSim([
            Timecourse(
                start=0,
                end=75 * 60,  # [min]
                steps=800,
                changes={
                    **self.default_changes(),
                    "PODOSE_api": Q_(10, "mg"),
                    "BW": Q_(self.bodyweight, "kg"),
                    "HEIGHT": Q_(self.bodyheight, "m"),
                    "INR_ref": Q_(self.inr, "dimensionless"),
                },
            )
        ])
        return tcsims

    # Fit Mappings
    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings: Dict[str, FitMapping] = {}
        infos = {
            **self.infos_pk,
            **self.infos_pd,
        }
        for sid, name in infos.items():
            mappings[f"fm_{name}_healthy"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=f"API10_all_{name}" if sid == "[Cve_api]" else f"API10_{name}_all",
                    xid="time",
                    yid="mean",
                    yid_sd="" if sid == "[Cve_api]" else "mean_sd",
                    count="count",
                ),
                observable=FitData(
                    self,
                    task="task_control",
                    xid="time",
                    yid=sid,
                ),
                metadata=ApixabanMappingMetaData(
                    tissue=Tissue.PLASMA,
                    route=Route.PO,
                    application_form=ApplicationForm.TABLET,
                    dosing=Dosing.SINGLE,
                    health=Health.HEALTHY,
                    fasting=Fasting.NR,
                    coadministration=Coadministration.NONE
                ),
            )

        return mappings


    def figures(self) -> Dict[str, Figure]:
        return {
            **self.figure_pk(),
            **self.figure_pd(),
            **self.figure_scatter(),
        }

    def figure_pk(self) -> Dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="PK",
            name=f"{self.__class__.__name__}",
            num_cols=1,
            num_rows=1,
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        for kp, sid in enumerate(self.infos_pk):
            plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid])

        for kp, sid in enumerate(self.infos_pk):
            name = self.infos_pk[sid]
            # Simulation
            plots[kp].add_data(
                task="task_control",
                xid="time",
                yid=sid,
                label="sim: 10mg PO",
                color="black"
            )
            # Data
            plots[kp].add_data(
                dataset=f"API10_all_{name}",
                xid="time",
                yid="mean",
                count="count",
                label="exp: 10mg PO",
                color="black"
            )

        return {fig.sid: fig}

    def figure_pd(self) -> Dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="PD",
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
        for kp, sid in enumerate(self.infos_pd):
            plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid])

        for kp, sid in enumerate(self.infos_pd):
            name = self.infos_pd[sid]
            # Simulation
            plots[kp].add_data(
                task="task_control",
                xid="time",
                yid=sid,
                label="sim: 10mg PO",
                color="black"
            )
            # Data
            plots[kp].add_data(
                dataset=f"API10_{name}_all",
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
                label="exp: 10mg PO",
                color="black"
            )

        return {fig.sid: fig}

    def figure_scatter(self) -> Dict[str, Figure]:

        dset_id = lambda indiv_id: f"API10_concentration_vs_Anti-factor Xa activity_all_I{indiv_id}"

        # Create figures and plots
        fig = Figure(
            experiment=self,
            sid="PD scatter",
            name=self.__class__.__name__,
            num_rows=1,
            num_cols=1,
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_api_plasma, unit=self.unit_api), legend=True,
            yaxis=Axis(self.labels["antiXa_activity"], unit=self.units["antiXa_activity"]),
        )

        # simulation
        plots[0].add_data(
            task="task_control",
            xid="[Cve_api]",
            yid="antiXa_activity",
            label="sim: 10mg PO",
            color="black",
            linestyle="solid",
        )

        for indiv_id in range(21):
            label = "exp indiv: 10mg PO" if indiv_id == 0 else ""
            plots[0].add_data(
                xid="x",
                yid="y",
                dataset=dset_id(indiv_id+1),
                label=label,
                color="white",
                markeredgecolor="black",
                marker="o",
                linestyle="",
            )

        return {fig.sid: fig}


if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / Frost2014a.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Frost2014a, output_dir=Frost2014a.__name__)

