import math
from typing import Dict

from sbmlsim.data import DataSet, load_pkdb_dataframe
from sbmlsim.fit import FitMapping, FitData
from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Timecourse, TimecourseSim
from sbmlutils.console import console

from pkdb_models.models import apixaban
from pkdb_models.models.apixaban.experiments.base_experiment import ApixabanSimulationExperiment
from pkdb_models.models.apixaban.experiments.metadata import Tissue, Route, Dosing, ApplicationForm, Health, \
    Fasting, ApixabanMappingMetaData

from pkdb_models.models.apixaban.helpers import run_experiments


class Frost2018(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2018."""

    doses = {
        "placebo": 0,
        "API2.5": 2.5,
        "API10": 10.0,
        "API25": 25.0,
        "API50": 50.0,
    }
    dose_keys = list(doses.keys())
    colors = {
        "placebo": "tab:grey",
        "API2.5": "#fff5eb",
        "API10": "#fdb97d",
        "API25": "#e95e0d",
        "API50": "#7f2704",
    }
    ethnicities = {
        "japanese": "D",
        "caucasian": "s",
    }
    bodyweight ={
        "japanese_placebo": 66,
        "japanese": 65.6,
        "caucasian": 70.1,
        "caucasian_placebo": 68,
    }
    bodyheight ={
        "japanese_placebo": math.sqrt(66 / 22),
        "japanese": math.sqrt(65.6 / 23.1),
        "caucasian": math.sqrt(70.1 / 21.9),
        "caucasian_placebo": math.sqrt(68 / 22.1),
    }
    info_fig1 = {
        "[Cve_api]": "apixaban",
        "Aurine_api": "cumulative amount"
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1", "Fig3", "Tab2"]:
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby("label"):
                dset = DataSet.from_df(df_label, self.ureg)
                if "API" in label and "mPT" not in label and "aPTT" not in label and "inr" not in label and fig_id != "Tab2":
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                elif "cumulative amount" in label:
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                    # console.print(dset)
                elif fig_id == "Tab2":
                    continue
                dsets[label] = dset

        return dsets

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims: Dict[str, TimecourseSim] = {}
        for key, dose in self.doses.items():
            for group, bw in self.bodyweight.items():
                tcsims[f"{key}_{group}"] = TimecourseSim([
                    Timecourse(
                        start=0,
                        end=100 * 60,  # minutes
                        steps=500,
                        changes={
                            **self.default_changes(),
                            "PODOSE_api": Q_(dose, "mg"),
                            "BW": Q_(bw, "kg"),
                            "HEIGHT": Q_(self.bodyheight[group], "m"),
                        },
                    )
                ])
        return tcsims

    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings = {}

        mapping_configs = [
            ("api", "", "[Cve_api]"), # Cve_api: prefix, dataset_suffix, observable
            ("cumulative amount", "", "Aurine_api"),  # Cve_api: prefix, dataset_suffix, observable
            ("mPT", "_mPT", "mPT_relchange"), # mPT_relchange: prefix, dataset_suffix, observable
            ("aPTT", "_aPTT", "aPTT_relchange"), # aPTT_relchange: prefix, dataset_suffix, observable
            ("INR", "_inr", "INR_relchange")
        ]

        for prefix, dataset_suffix, observable in mapping_configs:
            for key, dose in self.doses.items():
                if key == "placebo" and prefix in ["api", "cumulative amount"]:
                    continue

                for ethnicity in self.ethnicities.keys():
                    label = f"{prefix}_{ethnicity}_{key}" if prefix == "cumulative amount" else f"{ethnicity}{dataset_suffix}_{key}"
                    mapping_id = f"fm_{prefix}_{key}_{ethnicity}"

                    mappings[mapping_id] = FitMapping(
                        self,
                        reference=FitData(
                            self,
                            dataset=label,
                            xid="time",
                            yid="mean",
                            count="count",
                        ),
                        observable=FitData(
                            self,
                            task=f"task_{key}_{ethnicity}",
                            xid="time",
                            yid=observable,
                        ),
                        metadata=ApixabanMappingMetaData(
                            tissue=Tissue.URINE if prefix == "cumulative amount" else Tissue.PLASMA,
                            route=Route.PO,
                            application_form=ApplicationForm.TABLET,
                            dosing=Dosing.SINGLE,
                            health=Health.HEALTHY,
                            fasting=Fasting.FASTED,
                        ),
                    )

        return mappings

    def figures(self) -> Dict[str, Figure]:
        return {
            **self.figures_pk(),
            **self.figure_pd(),
        }

    def figures_pk(self) -> Dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="Fig1",
            num_rows=2,
            num_cols=2,
            name=f"{self.__class__.__name__}",
            height=self.panel_height * 2,
            width=self.panel_width * 2,
        )
        Figure.legend_fontsize = 9.5
        plots = fig.create_plots(xaxis=Axis(self.label_time, unit=self.unit_time), legend=True)

        # Configuration for each plot
        plot_configs = [
            (0, "[Cve_api]", self.label_api_plasma, self.unit_api, True),  # Cve_api plot
            (1, "Aurine_api", self.label_api_urine, self.unit_api_urine, True),
        ]

        for plot_idx, yid, ylabel, yunit, skip_placebo_data in plot_configs:
            plots[plot_idx].set_yaxis(ylabel, unit=yunit)
            plots[plot_idx + 2].set_yaxis(ylabel, unit=yunit)

            # simulation
            for key, dose in self.doses.items():
                if dose == 0:
                    continue
                for ethnicity in self.bodyweight.keys():
                    if "placebo" in ethnicity:
                        continue
                    if ethnicity == "caucasian":
                        idx = plot_idx + 2
                    else:
                        idx = plot_idx
                    task_id = f"task_{key}_{ethnicity}"
                    plots[idx].add_data(
                        task=task_id,
                        xid="time",
                        yid=yid,
                        label=f"sim {ethnicity}: {dose:g} mg PO",
                        color=self.colors.get(key),
                    )
                    label = f"{ethnicity}_{key}" if yid == "[Cve_api]" else f"cumulative amount_{ethnicity}_{key}"
                    plots[idx].add_data(
                        dataset=label,
                        xid="time",
                        yid="mean",
                        count="count",
                        label=f"exp {ethnicity}: {dose:g} mg PO",
                        color=self.colors[key],
                        marker=self.ethnicities[ethnicity],
                    )

        return {fig.sid: fig}

    def figure_pd(self) -> Dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="Fig2",
            num_rows=2,
            num_cols=3,
            name=f"{self.__class__.__name__}",
            height=self.panel_height * 2,
            width=self.panel_width * 3 * 1.05,
        )
        Figure.legend_fontsize = 9.5
        plots = fig.create_plots(xaxis=Axis(self.label_time, unit=self.unit_time), legend=True)

        # Configuration for each plot
        plot_configs = [
            (0, "mPT_relchange", self.labels["mPT_relchange"], "%", "_mPT", False),  # mPT plot
            (1, "aPTT_relchange", self.labels["aPTT_relchange"], "%", "_aPTT", False),  # aPTT plot
            (2, "INR_relchange", self.labels["INR_relchange"], "%", "_inr", False),
        ]

        for plot_idx, yid, ylabel, yunit, dataset_suffix, skip_placebo_data in plot_configs:
            plots[plot_idx].set_yaxis(ylabel, unit=yunit)
            plots[plot_idx+3].set_yaxis(ylabel, unit=yunit)

            # simulation
            for key, dose in self.doses.items():
                for ethnicity in self.bodyweight.keys():
                    if "placebo" in ethnicity:
                        continue
                    if ethnicity == "caucasian":
                        idx = plot_idx + 3
                    else:
                        idx = plot_idx
                    task_id = f"task_{key}_{ethnicity}"
                    plots[idx].add_data(
                        task=task_id,
                        xid="time",
                        yid=yid,
                        label=f"sim {ethnicity}: {dose:g} mg PO",
                        color=self.colors.get(key),
                    )
                    label = f"{ethnicity}{dataset_suffix}_{key}"
                    plots[idx].add_data(
                        dataset=label,
                        xid="time",
                        yid="mean",
                        count="count",
                        label=f"exp {ethnicity}: {dose:g} mg PO",
                        color=self.colors[key],
                        marker=self.ethnicities[ethnicity],
                    )


        return {fig.sid: fig}



if __name__ == "__main__":
    out = apixaban.RESULTS_PATH_SIMULATION / Frost2018.__name__
    out.mkdir(parents=True, exist_ok=True)
    run_experiments(Frost2018, output_dir=Frost2018.__name__)