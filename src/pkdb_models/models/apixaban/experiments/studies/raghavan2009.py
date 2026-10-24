"""Simulation experiment of the study Raghavan2009."""

from typing import ClassVar, TypedDict, override

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


class PkInfo(TypedDict):
    """Measurements of an observable with the panel and the color of its curves."""

    measurements: list[str]
    kp: int
    color: str


class Raghavan2009(ApixabanSimulationExperiment):
    """Simulation experiment of Raghavan2009.

    Mass balance of a single oral dose of 20 mg [14C]apixaban as a solution in
    healthy males after an overnight fast of at least 10 h: group 1 (n=6)
    without, group 2 (n=4) with a collection of the bile at 3-8 h (which
    removes 2.44 % of the dose from the feces). Body weight is not reported.
    """

    markers: ClassVar[dict[str, str]] = {
        "group1": "s",
        "group2": "o",
    }
    groups: ClassVar[list[str]] = list(markers.keys())
    dose = 20  # [mg]

    infos_pk: ClassVar[dict[str, PkInfo]] = {
        "[Cve_api]": {
            "measurements": ["apixaban", "apixaban2"],
            "kp": 0,
            "color": "black",
        },
        "[Cve_m1]": {"measurements": ["m1"], "kp": 1, "color": "black"},
        "Aurine_api": {"measurements": ["apixaban_urine"], "kp": 2, "color": "black"},
        "Aurine_m1": {"measurements": ["m1_urine"], "kp": 3, "color": "black"},
        "Aurine_m7": {"measurements": ["m7_urine"], "kp": 3, "color": "grey"},
        "Afeces_api": {"measurements": ["apixaban_feces"], "kp": 4, "color": "black"},
        "Afeces_m1": {"measurements": ["m1_feces"], "kp": 5, "color": "black"},
        "Afeces_m2": {
            "measurements": ["m2_m10_m13_feces"],
            "kp": 5,
            "color": "#1f77b4",
        },
        "Afeces_m7": {"measurements": ["m7_feces"], "kp": 5, "color": "grey"},
    }

    linestyle: ClassVar[dict[str, str]] = {
        "apixaban": "solid",
        "apixaban2": "dashed",
        "m1": "dashed",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        # Fig1: apixaban [ng/ml] (the total radioactivity is not used)
        df = self.load_dataframe("Fig1")
        for label, df_label in df.groupby("label"):
            label = str(label)
            if "total" in label:
                continue
            dset = DataSet.from_df(df_label, self.ureg)
            dset.unit_conversion("mean", 1 / self.Mr.api)
            dsets[label] = dset

        # Tab3: apixaban and M1 [µM] estimated from the radioactivity
        df = self.load_dataframe("Tab3")
        for label, df_label in df.groupby("label"):
            dsets[str(label)] = DataSet.from_df(df_label, self.ureg)

        # Tab4: recovery in urine and feces [% of the radioactive dose]; the
        # radioactivity counts apixaban equivalents, so every species is
        # converted to an amount with the molecular weight of apixaban.
        df = self.load_dataframe("Tab4")
        df = df[~df["label"].str.contains("total")]
        recovery_to_amount = Q(self.dose, "mg") / Q(100, "percent") / self.Mr.api
        for label, df_label in df.groupby("label"):
            dset = DataSet.from_df(df_label, self.ureg)
            dset.unit_conversion("mean", recovery_to_amount)
            dsets[str(label)] = dset

        # M2 of the model includes its products M10 and M13: their fecal
        # recoveries are summed (not detected = 0).
        for group in self.groups:
            df_m2 = df[df["label"] == f"m2_feces_{group}"].copy()
            for metabolite in ["m10", "m13"]:
                df_metabolite = df[df["label"] == f"{metabolite}_feces_{group}"]
                df_m2["mean"] = (
                    df_m2["mean"].fillna(0).to_numpy()
                    + df_metabolite["mean"].fillna(0).to_numpy()
                )
            df_m2["label"] = f"m2_m10_m13_feces_{group}"
            dset = DataSet.from_df(df_m2, self.ureg)
            dset.unit_conversion("mean", recovery_to_amount)
            dsets[f"m2_m10_m13_feces_{group}"] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims: dict[str, Simulation] = {}
        tcsims["control"] = Simulation(
            time_unit="hr",
            end=301,
            preinit_changes={
                **self.default_changes(),
                "SOLDOSE_api": Q(self.dose, "mg"),
            },
        )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings: dict[str, FitMapping] = {}
        for group in self.groups:
            for sid, info in self.infos_pk.items():
                for name in info["measurements"]:
                    if "urine" in name:
                        tissue = Tissue.URINE
                    elif "feces" in name:
                        tissue = Tissue.FECES
                    else:
                        tissue = Tissue.PLASMA
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
                            task="task_control",
                            xid="time",
                            yid=sid,
                        ),
                        metadata=PKPDMappingMetaData(
                            tissue=tissue,
                            route=Route.PO,
                            application_form=ApplicationForm.SOLUTION,
                            dosing=Dosing.SINGLE,
                            health=Health.HEALTHY,
                            fasting=Fasting.FASTED,
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
        """Apixaban and its metabolites in plasma, urine and feces."""
        fig = Figure(
            experiment=self,
            sid="PK",
            name=f"{self.__class__.__name__}",
            num_cols=2,
            num_rows=3,
            height=self.panel_height * 3 * 1.1,
            width=self.panel_width * 2.8,
        )
        # the legends hide data points inside the panels
        fig.settings = {**fig.settings, "legend_position": "outside"}
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        for sid, info in self.infos_pk.items():
            kp = info["kp"]
            if "urine" in sid and "m1" in sid:
                label = "metabolites urine"
            elif "feces" in sid and "m1" in sid:
                label = "metabolites feces"
            elif ("urine" in sid or "feces" in sid) and (
                "m1" not in sid and "api" not in sid
            ):
                # the other metabolites share the panel of M1
                continue
            else:
                label = self.labels[sid]
            plots[kp].set_yaxis(label, unit=self.units[sid])
            if sid.startswith("[Cve"):
                xaxis = plots[kp].xaxis
                if xaxis is not None:  # set by `create_plots`
                    xaxis.min = -1
                    xaxis.max = 81

        for group in self.groups:
            for sid, info in self.infos_pk.items():
                names = info["measurements"]
                kp = info["kp"]
                if group == "group1":
                    # simulation
                    plots[kp].add_data(
                        task="task_control",
                        xid="time",
                        yid=sid,
                        label=f"sim {self.dose}mg SOL"
                        if "api" in sid or ("m1" in sid and kp == 1)
                        else f"{sid.split('_')[1].upper()} sim {self.dose}mg SOL",
                        color=info["color"],
                    )
                for name in names:
                    if sid.startswith("[Cve"):
                        label = (
                            f"group {group[-1]}: {self.dose}mg SOL (LC-MS/MS)"
                            if name == "apixaban"
                            else f"group {group[-1]}: {self.dose}mg SOL (radioactivity)"
                        )
                    else:
                        metabolite = sid.split("_")[1].upper()
                        if metabolite == "M2":
                            metabolite = "M2+M10+M13"
                        label = (
                            f"group {group[-1]}: {self.dose}mg SOL"
                            if "api" in sid
                            else f"{metabolite} group {group[-1]}: {self.dose}mg SOL"
                        )
                    # data
                    plots[kp].add_data(
                        dataset=f"{name}_{group}",
                        xid="time",
                        yid="mean",
                        count="count",
                        label=label,
                        color=info["color"],
                        linestyle=self.linestyle[name] if "[Cve" in sid else "",
                        marker=self.markers[group],
                        markeredgecolor=info["color"],
                    )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Raghavan2009, output_dir=Raghavan2009.__name__)
