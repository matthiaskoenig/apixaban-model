from typing import Dict

from sbmlsim.data import DataSet, load_pkdb_dataframe
from sbmlsim.fit import FitMapping, FitData
from sbmlutils.console import console

from pkdb_models.models import apixaban
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)
from pkdb_models.models.apixaban.experiments.metadata import Tissue, Route, Dosing, ApplicationForm, Health, \
    Fasting, ApixabanMappingMetaData

from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Timecourse, TimecourseSim

from pkdb_models.models.apixaban.helpers import run_experiments


class Frost2014(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2014."""

    bodyweight = 75.9 #kg

    colors = {
        "mAPI":"purple",
    }

    interventions = list(colors.keys())

    doses = {
        "mAPI": 2.5, #mg
    }

    infos_pk = {
        "[Cve_api]": "apixaban",
    }

    infos_pd = {
       "Anti-factor Xa activity": "antiXa_activity"
    }

    info_figpd_scatter = {
        "apixaban": "antiXa_activity",
        "apixaban_mean": "antiXa_activity"
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2", "Fig3", "Fig4", "Fig4Mean"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            group_by = "x_label" if fig_id in ["Fig4", "Fig4Mean"] else "label"
            for label, df_label in df.groupby(group_by):
                dset = DataSet.from_df(df_label, self.ureg)
                if label in ["apixaban", "apixaban_mean"]:
                    dset.unit_conversion("x", 1 / self.Mr.api)
                elif "apixaban" in label:
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                if "rivaroxaban" in label or "RIV" in label:
                    continue
                dsets[label] = dset

        # console.print(dsets)

        return dsets

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims = {}
        for intervention in self.interventions:
            dose = self.doses[intervention]
            tc = Timecourse(
                    start=0,
                    end=12 * 60,  # [min]
                    steps=1000,
                    changes={
                        **self.default_changes(),
                        "BW": Q_(self.bodyweight, "kg"),
                        "PODOSE_api": Q_(dose, "mg"),
                    },
                )

            tc_end = Timecourse(
                    start=0,
                    end=36 * 75,  # [min]
                    steps=1000,
                    changes={
                        **self.default_changes(),
                        "BW": Q_(self.bodyweight, "kg"),
                        "PODOSE_api": Q_(dose, "mg"),
                    },
                )

            tcsims[intervention] = TimecourseSim(
                timecourses=[tc] * 3 * 2 + [tc] + [tc_end],
                time_offset= -3 * 24 * 60
            )

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
                        dosing= Dosing.MULTIPLE,
                        health=Health.HEALTHY,
                        fasting= Fasting.NR,
                        outlier=True  # FIXME: incorrect timepoints
                    )
                )
            #PD
            for ks, sid in enumerate(self.infos_pd):
                name = self.infos_pd[sid]
                mappings[f"fm_{intervention}_{name}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"Xa_{intervention}",
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self, task=f"task_{intervention}", xid="time", yid=name,
                    ),
                    metadata=ApixabanMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.MULTIPLE,
                         health=Health.HEALTHY,
                        fasting=Fasting.NR,
                        outlier = True  # FIXME: incorrect timepoints
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
            sid="Fig1",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        plots[0].set_yaxis(self.label_api_plasma, unit="nM")

        for intervention in self.interventions:
                for k, sid in enumerate(self.infos_pk.keys()):
                    name = self.infos_pk[sid]
                    if "apixaban" in name and "API" in intervention:
                        #simulation
                        plots[0].add_data(
                            task=f"task_{intervention}",
                            xid="time",
                            yid=sid,
                            label="sim multiple: 2.5mg PO",
                            color=self.colors[intervention],
                        )
                        # data
                        plots[0].add_data(
                            dataset=f"{name}_{intervention}",
                            xid="time",
                            yid="mean",
                            yid_sd="mean_sd",
                            count="count",
                            label="exp multiple: 2.5mg PO",
                            color=self.colors[intervention],
                        )

        return {fig.sid: fig}

    def figure_pd(self) -> Dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="Fig2",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        plots[0].set_yaxis(self.labels["antiXa_activity"], unit=self.units["antiXa_activity"])

        for intervention in self.interventions:
            for k, sid in enumerate(self.infos_pd):
                if "API" in intervention:
                    name = self.infos_pd[sid]
                    # simulation
                    plots[k].add_data(
                        task=f"task_{intervention}",
                        xid="time",
                        yid=name,
                        label="sim multiple: 2.5mg PO",
                        color=self.colors[intervention],
                    )
                    # data
                    plots[k].add_data(
                        dataset=f"Xa_{intervention}",
                        xid="time",
                        yid="mean",
                        count="count",
                        label="exp multiple: 2.5mg PO",
                        color=self.colors[intervention],
                    )

        return {fig.sid: fig}

    def figure_scatter(self):
        style_mean = {
            "kwargs_sim": {
            "color": self.fasting_colors["fasted"],
            "linestyle": "solid",
            },
            "kwargs_exp": {
                "label": f"exp chronic: 2.5mg PO",
                "marker": "s",
                "linestyle": "",
                "color": self.fasting_colors["fasted"],
                "markeredgecolor": "black",
            }
        }

        style_indiv = {
            "kwargs_sim": {
            "color": "black",
            "linestyle": "",
            "marker": "o"
            },
            "kwargs_exp": {
                "label": f"exp individ chronic: 2.5mg PO",
                "color": "white",
                "markeredgecolor": "black",
                "marker": "o",
                "linestyle": "",
            }
        }

        fig_Xa = Figure(
            experiment=self,
            sid="PD scatter",
            name=self.__class__.__name__,
            num_rows=1,
            num_cols=1,
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots_Xa = fig_Xa.create_plots(
            xaxis=Axis(self.labels["[Cve_api]"], unit=self.units["[Cve_api]"]),
            legend=True,
        )

        for label, sid in self.info_figpd_scatter.items():
            plots_Xa[0].set_yaxis(self.labels[sid], unit=self.units[sid], scale="linear")

            if "mean" in label:
                style = style_mean
            else:
                style = style_indiv
            if "mean" in label:
                # simulation
                plots_Xa[0].add_data(
                    task=f"task_mAPI",
                    xid="[Cve_api]",
                    yid=sid,
                    label=f"sim chronic: 2.5mg PO",
                    **style["kwargs_sim"]
                )
            # data
            plots_Xa[0].add_data(
                dataset=label,
                xid="x",
                yid="y",
                **style["kwargs_exp"]
            )

        return {
            fig_Xa.sid: fig_Xa,
        }



if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / Frost2014.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Frost2014, output_dir=Frost2014.__name__)
