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


class Kreutz2017(ApixabanSimulationExperiment):
    """Simulation experiment of Kreutz2017."""

    bodyweight = 81.1 #[kg]
    bodyheight = 181 #[cm]

    dose = 5 #[mg]
    route = "PO"

    info_figpk = {
        "api_apixaban": "[Cve_api]",
    }

    info_figpd = {
        "api_prothrombin time ratio": "PT_ratio",
        "api_aPTT ratio": "aPTT_ratio",
        "api_Anti-factor Xa activity_mean_ug": "antiXa_activity_gram",
    }

    info_figpd_scatter = {
        "api_apixaban_plasma_vs_Anti-factor Xa activity_ug": "antiXa_activity_gram",
        "api_apixaban_plasma_vs_mean_Anti-factor Xa activity_ug": "antiXa_activity_gram"
    }


    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id, group_id in zip(["Fig2", "Fig6", "FigS1", "FigS1Mean", "TabS2"], ["label", "label", "x_label", "x_label", "label"]):
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby(group_id):
                if "riv" in label:
                    continue
                dset = DataSet.from_df(df_label, self.ureg)
                if "apixaban" in label:
                    if fig_id in ["FigS1", "FigS1Mean"]:
                        dset.unit_conversion("x", 1 / self.Mr.api)
                    else:
                        dset.unit_conversion("mean", 1 / self.Mr.api)
                if label not in ["api_apixaban_plasma_vs_Anti-factor Xa activity_ug", "api_apixaban_plasma_vs_Anti-factor Xa activity_mean_ug"]:
                    dset.time = dset.time - 6 * 24
                dsets[label] = dset
                #print(label)

        #console.print(dsets)

        return dsets

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims = {}

        tc = Timecourse(
            start=0,
            end=12 * 60,  # [min]
            steps=1000,
            changes={
                **self.default_changes(),
                "BW": Q_(self.bodyweight, "kg"),
                "HEIGHT": Q_(self.bodyheight, "cm"),
                f"{self.route}DOSE_api": Q_(self.dose, "mg"),
                "GU__f_absorption": Q_(self.fasting_map["fed"], "dimensionless")
            },
        )

        tc_end = Timecourse(
            start=0,
            end=73 * 60,  # [min]
            steps=1000,
            changes={
                **self.default_changes(),
                f"{self.route}DOSE_api": Q_(self.dose, "mg"),
                "GU__f_absorption": Q_(self.fasting_map["fed"], "dimensionless")
            },
        )

        tcsims["apixaban"] = TimecourseSim(
            timecourses=[tc] * 13 + [tc_end],
            time_offset= - 6 * 24 * 60
        )

        return tcsims

    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings = {}

        for variables in [self.info_figpk.items(), self.info_figpd.items(), self.info_figpd_scatter.items()]:
            for label, sid in variables:
                if label.endswith("Anti-factor Xa activity_ug"):
                    continue
                mappings[f"fm_{self.route}_{label}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=label,
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task="task_apixaban",
                        xid="time",
                        yid=sid,
                    ),
                    metadata=ApixabanMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.MULTIPLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FED,
                    ),
                )

        return mappings

    def figures(self) -> Dict[str, Figure]:

        return {
            **self.figure_pk(),
            **self.figure_pd(),
            # scatter plot data unreliable (see offset in data)
            # **self.figure_scatter(),
        }

    def figure_pk(self) -> Dict[str, Figure]:

        fig = Figure(
            experiment=self,
            sid="PK",
            name=self.__class__.__name__,
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=-24),
            legend=True,
        )
        plots[0].set_yaxis(self.labels["[Cve_api]"], unit=self.units["[Cve_api]"], scale="linear")

        for label, sid in self.info_figpk.items():
            # simulation
            plots[0].add_data(
                task="task_apixaban",
                xid="time",
                yid=sid,
                label=f"sim fed: {self.dose}mg {self.route}",
                color=self.fasting_colors["fed"],
            )
            # data
            plots[0].add_data(
                dataset=label,
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
                label=f"exp fed: {self.dose}mg {self.route}",
                color=self.fasting_colors["fed"],
            )

        return {fig.sid: fig}

    def figure_pd(self) -> Dict[str, Figure]:

        fig = Figure(
            experiment=self,
            sid="PD",
            name=self.__class__.__name__,
            num_cols=len(self.info_figpd),
            height=self.panel_height,
            width=self.panel_width * 3 * 1.05,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=-24),
            legend=True,
        )
        for kp, (label, sid) in enumerate(self.info_figpd.items()):
            plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid])
            # simulation
            plots[kp].add_data(
                task="task_apixaban",
                xid="time",
                yid=sid,
                label=f"sim fed: {self.dose}mg {self.route}",
                color=self.fasting_colors["fed"],
            )
            # data
            plots[kp].add_data(
                dataset=label,
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
                label=f"exp fed: {self.dose}mg {self.route}",
                color=self.fasting_colors["fed"],
            )

        return {fig.sid: fig}

    def figure_scatter(self) -> Dict[str, Figure]:

        style_mean = {
            "kwargs_sim": {
            "color": self.fasting_colors["fed"],
            "linestyle": "solid",
            },
            "kwargs_exp": {
                "label": f"{self.dose}mg {self.route}",
                "marker": "s",
                "linestyle": "",
                "color": self.fasting_colors["fed"],
                "markeredgecolor": "black",
                "xid_sd": "x_sd",
                "yid_sd": "y_sd",
            }
        }

        style_indiv = {
            "kwargs_sim": {
            "color": "tab:grey",
            "linestyle": "",
            "marker": "o"
            },
            "kwargs_exp": {
                "label": f"exp chronic fed: {self.dose}mg {self.route}",
                "color": "white",
                "markeredgecolor": self.fasting_colors["fed"],
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
                    task=f"task_apixaban",
                    xid="[Cve_api]",
                    yid=sid,
                    label=f"sim chronic fed: {self.dose}mg {self.route}",
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
    out = apixaban.RESULTS_PATH_SIMULATION / Kreutz2017.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Kreutz2017, output_dir=Kreutz2017.__name__)
