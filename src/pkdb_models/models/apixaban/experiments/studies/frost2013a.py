from typing import Dict

from sbmlsim.data import DataSet, load_pkdb_dataframe
from sbmlsim.fit import FitMapping, FitData
from sbmlutils.console import console

from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)
from pkdb_models.models.apixaban.experiments.metadata import Tissue, Route, Dosing, ApplicationForm, Health, \
    Fasting, ApixabanMappingMetaData

from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Timecourse, TimecourseSim

from pkdb_models.models.apixaban.helpers import run_experiments


class Frost2013a(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2013a."""

    bodyweights = {
        "placebo":78.9,
        "API2x2": 72.3,
        "API5x2": 78.3,
        "API10": 79.7,
        "API10x2": 70.5,
        "API25": 82.2,
        "API25x2":  82.3,
    }

    colors = {
        "placebo":"black",
        "API2x2": "purple",
        "API5x2": "blue",
        "API10": "red",
        "API10x2": "blue",
        "API25": "tab:green",
        "API25x2": "tab:orange",
    }

    groups = list(colors.keys())

    doses = {
        "placebo": 0,
        "API2x2": 2.5,
        "API5x2": 5,
        "API10": 10,
        "API10x2": 10,
        "API25": 25,
        "API25x2": 25
    }

    infos_pk = {
        "[Cve_api]": "apixaban",
    }

    infos_pd = {
        "INR": "INR",
        "aPTT": "aPTT",
        "mPT": "mPT"
    }

    infos_scatter = {
        "apixaban_inr": ("INR", 0),
        "apixaban_aptt": ("aPTT", 1),
        "apixaban_mpt": ("mPT", 2),
        "apixaban_inr_mean": ("INR", 0),
        "apixaban_aPTT_mean": ("aPTT", 1),
        "apixaban_mPT_mean": ("mPT", 2),
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1", "Fig3", "Fig4", "Fig4Mean"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            group_by = "x_label" if fig_id in ["Fig4", "Fig4Mean"] else "label"
            for label, df_label in df.groupby(group_by):
                dset = DataSet.from_df(df_label, self.ureg)
                if "apixaban" in label:
                    if fig_id in ["Fig4", "Fig4Mean"]:
                        dset.unit_conversion("x", 1 / self.Mr.api)
                    else:
                        dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[label] = dset

        return dsets

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims = {}
        for group in self.groups:
            dose = self.doses[group]

            if "x2" in group:
                end_time = 12 * 60
                n_times = 6 * 2 + 1
            else:
                end_time = 24 * 60
                n_times = 6

            tc = Timecourse(
                    start=0,
                    end=end_time,  # [min]
                    steps=1000,
                    changes={
                        **self.default_changes(),
                        "BW": Q_(self.bodyweights[group], "kg"),
                        "PODOSE_api": Q_(dose, "mg"),
                    },
                )
            tc_end = Timecourse(
                start=0,
                end=240 * 60,  # [min]
                steps=200,
                changes={
                    **self.default_changes(),
                    "BW": Q_(self.bodyweights[group], "kg"),
                    "PODOSE_api": Q_(dose, "mg"),
                },
            )

            tcsims[group] = TimecourseSim(
                timecourses=[tc] * n_times + [tc_end],
            )

        return tcsims

    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings = {}
        for group in self.groups:
            # pharmacokinetics
            if "API" in group:
                for k, sid in enumerate(self.infos_pk.keys()):
                    name = self.infos_pk[sid]

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
                        metadata=ApixabanMappingMetaData(
                            tissue=Tissue.PLASMA,
                            route=Route.PO,
                            application_form=ApplicationForm.TABLET,
                            dosing= Dosing.MULTIPLE,
                            health=Health.HEALTHY,
                            fasting= Fasting.FASTED,
                        )
                    )
            # PD
            for ks, sid in enumerate(self.infos_pd):
                name = self.infos_pd[sid]
                mappings[f"fm_{group}_{name}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"{name}_{group}",
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self, task=f"task_{group}", xid="time", yid=sid,
                    ),
                    metadata=ApixabanMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.MULTIPLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED
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
            name=f"{self.__class__.__name__} (healthy)",
            num_cols=2,
            num_rows=1
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)
        plots[1].set_yaxis(self.label_api_plasma, unit=self.unit_api)

        for group in self.groups:
            if "API" in group:
                k = 1 if "x2" in group else 0
                for sid in self.infos_pk.keys():
                    name = self.infos_pk[sid]

                    # simulation
                    plots[k].add_data(
                        task=f"task_{group}",
                        xid="time",
                        yid=sid,
                        label=group,
                        color=self.colors[group],
                    )
                    # data
                    plots[k].add_data(
                        dataset=f"{name}_{group}",
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                        label=group,
                        color=self.colors[group],
                    )

        return {fig.sid: fig}

    def figure_pd(self) -> Dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="Fig2",
            num_cols=3,
            name=f"{self.__class__.__name__} (healthy)",
            num_rows=2,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )

        for ky, yid in enumerate(["INR", "aPTT", "mPT"]):
            plots[ky].set_yaxis(self.labels[yid], unit=self.units[yid])
            plots[ky + 3].set_yaxis(self.labels[yid], unit=self.units[yid])

        for group in self.groups:
            for ks, sid in enumerate(self.infos_pd):
                if "x2" in group:
                    ks += 3
                name = self.infos_pd[sid]
                # simulation
                plots[ks].add_data(
                    task=f"task_{group}",
                    xid="time",
                    yid=sid,
                    label=group,
                    color=self.colors[group],
                )
                # data
                plots[ks].add_data(
                    dataset=f"{name}_{group}",
                    xid="time",
                    yid="mean",
                    count="count",
                    label=group,
                    color=self.colors[group],
                )

        return {fig.sid: fig}

    def figure_scatter(self):
        style_mean = lambda group: {
            "kwargs_sim": {
                "color": "black",
                "linestyle": "solid",
            },
            "kwargs_exp": {
                "marker": "s",
                "linestyle": "",
                "color": self.colors[group],
                "markeredgecolor": "black",
                "yid_sd": "y_sd",
                "xid_sd": "x_sd",
            }
        }

        style_indiv = {
            "kwargs_sim": {
                "color": "black",
                "linestyle": "",
                "marker": "o"
            },
            "kwargs_exp": {
                "label": f"exp chronic I: PO",
                "color": "white",
                "markeredgecolor": "black",
                "marker": "o",
                "linestyle": "",
            }
        }

        fig_scatter = Figure(
            experiment=self,
            sid="PD scatter",
            name=self.__class__.__name__,
            num_rows=1,
            num_cols=3,
        )
        plots_scatter = fig_scatter.create_plots(
            xaxis=Axis(self.labels["[Cve_api]"], unit=self.units["[Cve_api]"]),
            legend=True,
        )

        for label, (sid, kp) in self.infos_scatter.items():
            plots_scatter[kp].set_yaxis(self.labels[sid], unit=self.units[sid], scale="linear")

            if "mean" in label:
                is_legend = True
                for group in self.groups:
                    style = style_mean(group)
                    if group != "placebo":
                        # data
                        plots_scatter[kp].add_data(
                            dataset=f"{label}_{group}",
                            xid="x",
                            yid="y",
                            label=f"exp chronic: {self.doses[group]}mg PO",
                            **style["kwargs_exp"]
                        )
                        # simulation
                        plots_scatter[kp].add_data(
                            task=f"task_{group}",
                            xid="[Cve_api]",
                            yid=sid,
                            label=f"sim chronic: PO" if is_legend else "",
                            **style["kwargs_sim"]
                        )
                        is_legend = False

            else:
                style = style_indiv
                # data
                plots_scatter[kp].add_data(
                    dataset=label,
                    xid="x",
                    yid="y",
                    **style["kwargs_exp"]
                )

        return {
            fig_scatter.sid: fig_scatter,
        }



if __name__ == "__main__":
    run_experiments(Frost2013a, output_dir=Frost2013a.__name__)
