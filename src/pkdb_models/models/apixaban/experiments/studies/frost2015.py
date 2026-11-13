"""Simulation experiment of the study Frost2015."""

from collections.abc import Mapping
from types import MappingProxyType
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
from pkpdsim.pbpk import Sex
from sbmlsim import Q
from sbmlsim.data import DataSet
from sbmlsim.fit import FitData, FitMapping
from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Simulation

from pkdb_models.models.apixaban import MODEL
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)


class Frost2015(ApixabanSimulationExperiment):
    """Simulation experiment of Frost2015.

    A single dose of 20 mg apixaban (fasted) in 79 healthy subjects, young and
    elderly men and women; the pharmacodynamics are reported by age and by
    sex.

    The groups of women (all women, young and elderly women) run on the female
    build, their renal function relative to the healthy GFR of the female
    build; the groups of men and the age groups, young (20 women of 40) and
    elderly (19 women of 39), run on the male build (no majority of women).
    """

    simulation_sexes: ClassVar[Mapping[str, Sex]] = MappingProxyType(
        {
            "female": Sex.FEMALE,
            "young_female": Sex.FEMALE,
            "elderly_female": Sex.FEMALE,
        }
    )

    # group definitions
    gender: ClassVar[list[str]] = ["female", "male"]
    gender_gram: ClassVar[list[str]] = [
        "female1",
        "male1",
    ]  # groups for Anti-Xa data in ng/mL - ng/mL datasets are marked with a trailing "1".
    age: ClassVar[list[str]] = ["young", "elderly"]
    age_gram: ClassVar[list[str]] = [
        "young1",
        "elderly1",
    ]  # groups for Anti-Xa data in ng/mL - ng/mL datasets are marked with a trailing "1".
    age_gender: ClassVar[list[str]] = [
        "young_male",
        "young_female",
        "elderly_male",
        "elderly_female",
    ]
    age_gender_gram: ClassVar[list[str]] = [
        "young_female1",
        "young_male1",
        "elderly_male1",
        "elderly_female1",
    ]  # groups for Anti-Xa data in ng/mL - ng/mL datasets are marked with a trailing "1".

    #: the mean body weights of the groups (Tab1)
    bodyweights: ClassVar[dict[str, float]] = {  # [kg]
        "young": 71.1,
        "elderly": 74.8,
        "male": 77.85,
        "female": 67.7,
        "young_male": 76.8,
        "young_female": 65.3,
        "elderly_male": 78.9,
        "elderly_female": 70.2,
    }
    groups: ClassVar[list[str]] = list(bodyweights.keys())

    #: the age group of a group, the baselines of the pharmacodynamics are
    #: reported by age and by sex (Fig3), an age-sex group takes the
    #: baseline of its age group
    age_groups: ClassVar[dict[str, str]] = {
        "young": "young",
        "elderly": "elderly",
        "male": "male",
        "female": "female",
        "young_male": "young",
        "young_female": "young",
        "elderly_male": "elderly",
        "elderly_female": "elderly",
    }

    #: the INR at 0 hr (Fig3a, Fig3b)
    inr: ClassVar[dict[str, float]] = {
        "young": 1.12,
        "elderly": 1.04,
        "male": 1.06,
        "female": 1.11,
    }

    #: the mPT at 0 hr (Fig3c, Fig3d)
    mpt: ClassVar[dict[str, float]] = {
        "young": 52.95,
        "elderly": 57.30,
        "male": 48.60,
        "female": 54.40,
    }

    dose = "API_20"

    # plot colors
    colors: ClassVar[dict[str, str]] = {
        "young": "black",
        "elderly": "#66c2a4",
        "male": "tab:blue",
        "female": "tab:red",
        "young_male": "black",
        "young_female": "black",
        "elderly_male": "#66c2a4",
        "elderly_female": "#66c2a4",
    }

    #: the line of a simulation: dashed for the groups of women (the female
    #: build), solid for the others
    linestyles: ClassVar[dict[str, str]] = {
        group: "--" if group.endswith("female") else "-" for group in bodyweights
    }

    markers: ClassVar[dict[str, str]] = {
        "young": "s",
        "elderly": "s",
        "male": "s",
        "female": "^",
        "young_male": "s",
        "young_female": "^",
        "elderly_male": "s",
        "elderly_female": "^",
    }

    legend: ClassVar[dict[str, str]] = {
        "young": "Y: 20mg PO",
        "elderly": "E: 20mg PO",
        "male": "M: 20mg PO",
        "female": "F: 20mg PO",
        "young_male": "Y M: 20mg PO",
        "young_female": "Y F: 20mg PO",
        "elderly_male": "E M: 20mg PO",
        "elderly_female": "E F: 20mg PO",
    }

    #: the creatinine clearance of the groups (Cockcroft-Gault, Tab1)
    #: [ml/min], the GFR of the simulation (`renal_function`)
    crcl: ClassVar[dict[str, float]] = {
        "young": 119.5,
        "elderly": 79.1,
        "male": 103.05,
        "female": 95.9,
        "young_male": 123.3,
        "young_female": 115.7,
        "elderly_male": 82.8,
        "elderly_female": 75.1,
    }

    #: lower limit of quantification of apixaban (1 ng/ml), the means at or
    #: below it after the dose (young male 96 hr, plotted at the limit) are not
    #: used
    lloq = Q(1.0, "ng/ml")

    info_fig1: ClassVar[dict[str, str]] = {
        "Carm_api": "apixaban",
        "Aurine_api": "cumulative amount",
    }

    info_fig3: ClassVar[dict[str, str]] = {
        "COAG__INR": "inr",
        "COAG__mPT": "mPT",
        "COAG__antiXa_activity_gram": "anti_Xa",
        "COAG__antiXa_activity": "anti_Xa",
    }

    #: the individual values against apixaban (Fig4), the labels of the
    #: curation are `apixaban_vs_<name>_<group>`
    info_fig4: ClassVar[dict[str, str]] = {
        "COAG__INR": "inr",
        "COAG__mPT": "mpt",
        "COAG__antiXa_activity_gram": "antixa_ngml",
        "COAG__antiXa_activity": "antixa_iuml",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1", "Fig3", "Fig4"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                if fig_id == "Fig1":
                    lloq = self.lloq.to(df_label["unit"].iloc[0]).magnitude
                    df_label = df_label[
                        (df_label["time"] == 0) | (df_label["mean"] > lloq)
                    ]
                dset = DataSet.from_df(df_label, self.ureg)
                if fig_id == "Fig4":
                    dset.unit_conversion("x", 1 / self.Mr["api"])
                elif "apixaban" in label:
                    dset.unit_conversion("mean", 1 / self.Mr["api"])
                dsets[self.to_sid(label)] = dset

        # the urinary amounts by age (Tab2) and by sex (Tab3), without a spread
        for fig_id, groups in [("Tab2", self.age), ("Tab3", self.gender)]:
            df = self.load_dataframe(fig_id)
            for group in groups:
                df_group = df[
                    df["label"]
                    == f"cumulative_amount_apixaban_urine_{self.dose}_{group}"
                ]
                dset = DataSet.from_df(df_group, self.ureg)
                dset.unit_conversion("mean", 1 / self.Mr["api"])
                dsets[self.to_sid(f"cumulative amount_{group}")] = dset
        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        for group in self.groups:
            tcsims[self.to_sid(group)] = Simulation(
                time_unit="hr",
                end=120,
                preinit_changes={
                    **self.default_changes(),
                    "BW": Q(self.bodyweights[group], "kg"),
                    "PODOSE_api": Q(20, "mg"),
                    # set pharmacodynamic baseline reference parameters (assignment rules use these)
                    "COAG__INR_ref": Q(
                        self.inr[self.age_groups[group]], self.units["COAG__INR"]
                    ),
                    "COAG__mPT_ref": Q(
                        self.mpt[self.age_groups[group]], self.units["COAG__mPT"]
                    ),
                    "f_renal_function": self.renal_function(
                        self.crcl[group],
                        bw=self.bodyweights[group],
                        simulation=self.to_sid(group),
                    ),
                },
            )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}

        # apixaban in plasma (by age and sex) and the cumulative amount in
        # urine (by age and by sex)
        for groups, dset_prefix, sid in [
            (self.age_gender, "apixaban", "Carm_api"),
            (self.age + self.gender, "cumulative amount", "Aurine_api"),
        ]:
            for group in groups:
                tissue = Tissue.PLASMA if sid == "Carm_api" else Tissue.URINE
                mappings[self.to_sid(f"fm_{dset_prefix}_{group}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(f"{dset_prefix}_{group}"),
                        xid="time",
                        yid="mean",
                        # the urinary amounts have no spread
                        yid_sd="mean_sd" if sid == "Carm_api" else None,
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_{group}"),
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=tissue,
                        route=Route.PO,
                        application_form=ApplicationForm.NR,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
                    ),
                )

        pd_configs = [
            ("COAG__INR", "inr", self.age + self.gender),
            ("COAG__mPT", "mPT", self.age + self.gender),
            ("COAG__antiXa_activity", "anti_Xa", self.age + self.gender),
            ("COAG__antiXa_activity_gram", "anti_Xa", self.age_gram + self.gender_gram),
        ]

        for sid, name, groups in pd_configs:
            for group in groups:
                task_group = group.rstrip("1")
                # the key names the output of the coagulation model
                key = f"fm_{sid.removeprefix('COAG__')}_{group}"
                mappings[self.to_sid(key)] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(f"{name}_{group}_{self.dose}"),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_{task_group}"),
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.NR,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure(),
        }

    def figure(self) -> dict[str, Figure]:
        """Figure of the pharmacokinetics and the pharmacodynamics."""
        fig = Figure(
            experiment=self,
            sid="Fig1",
            name=self.__class__.__name__,
            num_cols=3,
            num_rows=5,
            height=self.panel_height * 5 * 1.2,
            width=self.panel_width * 3 * 1.05,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)
        plots[1].set_yaxis(self.label_api_urine, unit=self.unit_api_urine)

        # pharmacokinetics: apixaban in plasma and the cumulative amount in urine
        for kp, (groups, dset_prefix) in enumerate(
            zip(
                [self.age_gender, self.age + self.gender],
                ["apixaban", "cumulative amount"],
                strict=True,
            )
        ):
            for group in groups:
                task_key = f"task_{group}"
                dset_key = f"{dset_prefix}_{group}"
                sid = "Carm_api" if "apixaban" in dset_key else "Aurine_api"
                # simulation
                plots[kp].add_data(
                    task=self.to_sid(task_key),
                    xid="time",
                    yid=sid,
                    label=f"sim {self.legend[group]}",
                    color=self.colors[group],
                    linestyle=self.linestyles[group],
                )
                # data
                plots[kp].add_data(
                    dataset=self.to_sid(dset_key),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd" if sid == "Carm_api" else None,
                    count="count",
                    label=f"exp {self.legend[group]}",
                    color=self.colors[group],
                    marker=self.markers[group],
                )

        plot_configs = [
            ("COAG__INR", self.age, self.units.get("COAG__INR")),
            ("COAG__mPT", self.age, self.units.get("COAG__mPT")),
            (
                "COAG__antiXa_activity_gram",
                self.age_gram,
                self.units.get("COAG__antiXa_activity_gram"),
            ),
            (
                "COAG__antiXa_activity",
                self.age,
                self.units.get("COAG__antiXa_activity"),
            ),
            ("COAG__INR", self.gender, self.units.get("COAG__INR")),
            ("COAG__mPT", self.gender, self.units.get("COAG__mPT")),
            (
                "COAG__antiXa_activity_gram",
                self.gender_gram,
                self.units.get("COAG__antiXa_activity_gram"),
            ),
            (
                "COAG__antiXa_activity",
                self.gender,
                self.units.get("COAG__antiXa_activity"),
            ),
        ]

        for k, (sid, _groups, yunit) in enumerate(plot_configs):
            plots[k + 2].set_yaxis(self.labels.get(sid, sid), unit=yunit)

        for k, (sid, groups, _yunit) in enumerate(plot_configs):
            name = self.info_fig3.get(sid)
            data_groups = groups
            sim_groups = []
            for g in groups:
                sim_g = g[:-1] if g.endswith("1") else g
                if sim_g not in sim_groups:
                    sim_groups.append(sim_g)

            for sim_g in sim_groups:
                task_id = f"task_{sim_g}"
                plots[k + 2].add_data(
                    task=self.to_sid(task_id),
                    xid="time",
                    yid=sid,
                    label=f"sim {self.legend[sim_g]}",
                    color=self.colors[sim_g],
                    linestyle=self.linestyles[sim_g],
                )

            for group in data_groups:
                dset_key = f"{name}_{group}_{self.dose}"
                group = group.rstrip("1")
                plots[k + 2].add_data(
                    dataset=self.to_sid(dset_key),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"exp {self.legend[group]}",
                    color=self.colors[group],
                    marker=self.markers[group],
                )

        # apixaban in plasma on a log scale (the inset of Fig1)
        plots[14].set_yaxis(
            self.label_api_plasma, unit=self.unit_api, scale="log", min=1e-3
        )
        for group in self.age_gender:
            plots[14].add_data(
                task=self.to_sid(f"task_{group}"),
                xid="time",
                yid="Carm_api",
                label=f"sim {self.legend[group]}",
                color=self.colors[group],
                linestyle=self.linestyles[group],
            )
            plots[14].add_data(
                dataset=self.to_sid(f"apixaban_{group}"),
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
                label=f"exp {self.legend[group]}",
                color=self.colors[group],
                marker=self.markers[group],
            )

        plot_configs = [
            ("COAG__INR", self.age_gender, self.units.get("COAG__INR")),
            ("COAG__mPT", self.age_gender, self.units.get("COAG__mPT")),
            (
                "COAG__antiXa_activity_gram",
                self.age_gender_gram,
                self.units.get("COAG__antiXa_activity_gram"),
            ),
            (
                "COAG__antiXa_activity",
                self.age_gender,
                self.units.get("COAG__antiXa_activity"),
            ),
        ]

        for k, (sid, groups, yunit) in enumerate(plot_configs):
            plots[k + 10].set_yaxis(self.labels.get(sid, sid), unit=yunit)
            plots[k + 10].set_xaxis(self.label_api_plasma, unit=self.unit_api)

            sim_groups = []
            for g in groups:
                sim_g = g[:-1] if g.endswith("1") else g
                if sim_g not in sim_groups:
                    sim_groups.append(sim_g)

            info_key = self.info_fig4.get(sid, sid)
            for group in sim_groups:
                plots[k + 10].add_data(
                    dataset=self.to_sid(f"apixaban_vs_{info_key}_{group}"),
                    xid="x",
                    yid="y",
                    label=f"exp individ {self.legend[group]}",
                    markeredgecolor=self.colors.get(group, "black"),
                    color="white",
                    linestyle="",
                    marker=self.markers[group],
                )

            is_legend = True
            for sim_g in sim_groups:
                plots[k + 10].add_data(
                    task=self.to_sid(f"task_{sim_g}"),
                    xid="Carm_api",
                    yid=sid,
                    label="sim: 20mg PO" if is_legend else "",
                    color="black",
                    linestyle="solid",
                )
                is_legend = False

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Frost2015, output_dir=Frost2015.__name__)
