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
# from pkdb_models.models.pvl.simulations.simulate_pvl_model import labels


class Frost2015(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2015."""

    # group definitions
    gender = ["female", "male"]
    gender_gram = ["female1", "male1"] # groups for Anti-Xa data in ng/mL - ng/mL datasets are marked with a trailing "1".
    age = ["young", "elderly"]
    age_gram = ["young1", "elderly1"]  # groups for Anti-Xa data in ng/mL - ng/mL datasets are marked with a trailing "1".
    age_gender = ["young_male","young_female","elderly_male","elderly_female"]
    age_gender_gram = ["young_female1", "young_male1", "elderly_male1", "elderly_female1"]  # groups for Anti-Xa data in ng/mL - ng/mL datasets are marked with a trailing "1".

    # body weights for different groups
    bodyweights = { # [kg]
        "young": 71,
        "elderly": 75,
        "male": 78,
        "female": 68,
        "young_male": 77,
        "young_female": 65,
        "elderly_male": 79,
        "elderly_female": 70,
    }

    # mean start values at t=0
    inrs = {"INR_ref": 1.1}

    dose = "API_20"

    # plot colors
    colors = {
        "young": "black",
        "elderly": "tab:red",
        "male": "tab:blue",
        "female": "tab:green",
        "young_male": "tab:cyan",
        "young_female": "tab:orange",
        "elderly_male": "tab:purple",
        "elderly_female": "tab:brown",
    }

    info_fig1 = {
        "[Cve_api]": "apixaban",
        "Aurine_api": "cumulative amount",
    }

    info_fig3 = {
        "INR": "inr",
        "mPT": "mPT",
        "antiXa_activity_gram": "anti_Xa",
        "antiXa_activity": "anti_Xa",
    }

    info_fig4 = {
        "INR": "inr",
        "mPT": "mPT",
        "antiXa_activity_gram": "Anti-factor Xa activity", # ng/ml
        "antiXa_activity": "Anti-factor Xa activity", # IU/ml
    }

    def datasets(self) -> Dict[str, DataSet]:
        dsets = {}
        for fig_id, group_id in zip(["Fig1", "Fig3", "Fig4", "Tab2", "Tab3"],["label", "label", "x_label", "label", "label"]):
            df = load_pkdb_dataframe(f"{self.sid}_{fig_id}", data_path=self.data_path)
            for label, df_label in df.groupby(group_id):
                dset = DataSet.from_df(df_label, self.ureg)
                if "apixaban" in label:
                    if fig_id in ["Fig2", "Fig4"]:
                        dset.unit_conversion("x", 1 / self.Mr.api)
                    else:
                        dset.unit_conversion("mean", 1 / self.Mr.api)
                elif "cumulative amount" in label:
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                elif fig_id in ["Tab2", "Tab3"]:
                    continue
                dsets[label] = dset
        return dsets

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims = {}
        for group in self.age_gender:
            tcsims[group] = TimecourseSim(
                [Timecourse(
                    start=0,
                    end=96 * 60,  # [min]
                    steps=1000,
                    changes={
                        **self.default_changes(),
                        "BW": Q_(self.bodyweights[group], "kg"),
                        "PODOSE_api": Q_(20, "mg"),
                    },
                )]
            )
        for group in self.gender:
            tcsims[group] = TimecourseSim(
                [Timecourse(
                    start=0,
                    end=96 * 60,  # [min]
                    steps=1000,
                    changes={
                        **self.default_changes(),
                        "BW": Q_(self.bodyweights[group], "kg"),
                        "PODOSE_api": Q_(20, "mg"),
                        # set pharmacodynamic baseline reference parameters (assignment rules use these)
                        "INR_ref": Q_(self.inrs["INR_ref"], self.units["INR"]),
                    },
                )]
            )
        for group in self.age:
            tcsims[group] = TimecourseSim(
                [Timecourse(
                    start=0,
                    end=96 * 60,  # [min]
                    steps=1000,
                    changes={
                        **self.default_changes(),
                        "BW": Q_(self.bodyweights[group], "kg"),
                        "PODOSE_api": Q_(20, "mg"),
                        # set pharmacodynamic baseline reference parameters (assignment rules use these)
                        "INR_ref": Q_(self.inrs["INR_ref"], self.units["INR"]),
                    },
                )]
            )
        return tcsims

    def fit_mappings(self) -> Dict[str, FitMapping]:
        mappings = {}

        datasets_map = getattr(self, "_datasets", {})

        dset_id_plasma = lambda group: f"apixaban_{group}"
        dset_id_urine = lambda group: f"cumulative amount_{group}"

        for groups, dset_id in zip([self.age_gender, self.age + self.gender], [dset_id_plasma, dset_id_urine]):
            for group in groups:
                task_key = f"task_{group}"
                dset_key = dset_id(group)
                if dset_key in datasets_map:
                    mappings[f"fm_apixaban_{group}"] = FitMapping(
                        self,
                        reference=FitData(
                            self,
                            dataset=dset_key,
                            xid="time",
                            yid="mean",
                            count="count",
                        ),
                        observable=FitData(
                            self,
                            task=task_key,
                            xid="time",
                            yid="[Cve_api]",
                        ),
                        metadata=ApixabanMappingMetaData(
                            tissue=Tissue.PLASMA if "apixaban" in dset_key else Tissue.URINE,
                            route=Route.PO,
                            application_form=ApplicationForm.NR,
                            dosing=Dosing.SINGLE,
                            health=Health.HEALTHY,
                            fasting=Fasting.FASTED,
                        )
                    )

        pd_configs = [
            ("INR", "inr", self.age + self.gender),
            ("mPT", "mPT", self.age + self.gender),
            ("antiXa_activity", "anti_Xa", self.age + self.gender),
            ("antiXa_activity_gram", "anti_Xa", self.age_gram + self.gender_gram),
        ]
        
        for sid, name, groups in pd_configs:
            for group in groups:
                task_group = group.rstrip("1")
                task_key = f"task_{task_group}"
                dset_key = f"{name}_{group}_{self.dose}"
                
                if dset_key in datasets_map:
                    mappings[f"fm_{sid}_{group}"] = FitMapping(
                        self,
                        reference=FitData(
                            self,
                            dataset=dset_key,
                            xid="time",
                            yid="mean",
                            count="count",
                        ),
                        observable=FitData(
                            self,
                            task=task_key,
                            xid="time",
                            yid=sid,
                        ),
                        metadata=ApixabanMappingMetaData(
                            tissue=Tissue.PLASMA,
                            route=Route.PO,
                            application_form=ApplicationForm.NR,
                            dosing=Dosing.SINGLE,
                            health=Health.HEALTHY,
                            fasting=Fasting.FASTED,
                        )
                    )

        return mappings

    def figures(self) -> Dict[str, Figure]:

        return {
            **self.figure_pk(),
            **self.figure_pd(),
            **self.figure_scatter()
        }

    # pharmacokinetics: apixaban concentration over time
    def figure_pk(self) -> Dict[str, Figure]:

        dset_id_plasma = lambda group: f"apixaban_{group}"
        dset_id_urine = lambda group: f"cumulative amount_{group}"

        fig = Figure(
            experiment=self,
            sid="Fig1",
            name=self.__class__.__name__,
            num_cols=2,
            num_rows=1,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)
        plots[1].set_yaxis(self.label_api_urine, unit=self.unit_api_urine)

        for kp, (groups, dset_id) in enumerate(zip([self.age_gender, self.age + self.gender], [dset_id_plasma, dset_id_urine])):
            for group in groups:
                task_key = f"task_{group}"
                dset_key = dset_id(group)
                sid = "[Cve_api]" if "apixaban" in dset_key else "Aurine_api"
                # simulation
                plots[kp].add_data(
                    task=task_key,
                    xid="time",
                    yid=sid,
                    label=group,
                    color=self.colors[group],
                )
                # data
                plots[kp].add_data(
                    dataset=dset_key,
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=group,
                    color=self.colors[group],
                )

        return {fig.sid: fig}

    # pharmacodynamics: INR, mPT, anti-Xa over time
    def figure_pd(self) -> Dict[str, Figure]:

        fig = Figure(
            experiment=self,
            sid="Fig3",
            name=self.__class__.__name__,
            num_rows=4,
            num_cols=2,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        plot_configs = [
            ("INR", self.age, self.units.get("INR")),
            ("mPT", self.age, self.units.get("mPT")),
            ("antiXa_activity_gram", self.age_gram, self.units.get("antiXa_activity_gram")),
            ("antiXa_activity", self.age, self.units.get("antiXa_activity")),
            ("INR", self.gender, self.units.get("INR")),
            ("mPT", self.gender, self.units.get("mPT")),
            ("antiXa_activity_gram", self.gender_gram, self.units.get("antiXa_activity_gram")),
            ("antiXa_activity", self.gender, self.units.get("antiXa_activity")),
        ]

        for k, (sid, groups, yunit) in enumerate(plot_configs):
            plots[k].set_yaxis(self.labels.get(sid, sid), unit=yunit)

        for k, (sid, groups, yunit) in enumerate(plot_configs):
            name = self.info_fig3.get(sid)
            data_groups = groups
            sim_groups = []
            for g in groups:
                sim_g = g[:-1] if g.endswith("1") else g
                if sim_g not in sim_groups:
                    sim_groups.append(sim_g)

            for sim_g in sim_groups:
                task_id = f"task_{sim_g}"
                plots[k].add_data(
                    task=task_id,
                    xid="time",
                    yid=sid,
                    label=sim_g,
                    color=self.colors.get(sim_g, "gray"),
                )

            for group in data_groups:
                dset_key = f"{name}_{group}_{self.dose}"
                plots[k].add_data(
                        dataset=dset_key,
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                        label=group,
                        color=self.colors.get(group.rstrip("1"), "black"),
                )

        return {fig.sid: fig}

    # pharmacodynamics scatter: pd vs apixaban concentration
    def figure_scatter(self) -> Dict[str, Figure]:

            fig = Figure(
                experiment=self,
                sid="Fig4",
                name=self.__class__.__name__,
                num_rows=2,
                num_cols=2,
            )
            plots = fig.create_plots(
                xaxis=Axis(self.label_api_plasma, unit=self.unit_api),
                legend=True, # legends are overlapping plots
            )
            plot_configs = [
                ("INR", self.age_gender, self.units.get("INR")),
                ("mPT", self.age_gender, self.units.get("mPT")),
                ("antiXa_activity_gram", self.age_gender_gram, self.units.get("antiXa_activity_gram")),
                ("antiXa_activity", self.age_gender, self.units.get("antiXa_activity")),
            ]

            for k, (sid, groups, yunit) in enumerate(plot_configs):
                plots[k].set_yaxis(self.labels.get(sid, sid), unit=yunit)

                sim_groups = []
                for g in groups:
                    sim_g = g[:-1] if g.endswith("1") else g
                    if sim_g not in sim_groups:
                        sim_groups.append(sim_g)
                is_legend = True
                for sim_g in sim_groups:
                    plots[k].add_data(
                        task=f"task_{sim_g}",
                        xid="[Cve_api]",
                        yid=sid,
                        label="sim" if is_legend else "",
                        color="black",
                        linestyle="solid",
                    )
                    is_legend = False

                info_key = self.info_fig4.get(sid, sid)
                datasets_map = getattr(self, "_datasets", {})

                added = set()
                for group in groups:
                    base = group.rstrip("1")
                    if sid == "antiXa_activity_gram":
                        candidates = (f"{base}1",)
                    else:
                        candidates = (base,)

                    for candidate in candidates:
                        dkey = f"{candidate}_apixaban_vs_{info_key}"
                        if dkey in datasets_map and dkey not in added:
                            plots[k].add_data(
                                dataset=dkey,
                                xid="x",
                                yid="y",
                                label=base,
                                color=self.colors.get(base, "black"),
                                marker="o",
                                linestyle="",
                            )
                            added.add(dkey)

            return {fig.sid: fig}


if __name__ == "__main__":
    run_experiments(Frost2015, output_dir=Frost2015.__name__)
