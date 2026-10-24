"""Simulation experiment of the study Vakkalagadda2016."""

import math
from typing import ClassVar, NamedTuple, override

from pkpdsim.metadata import (
    ApplicationForm,
    Coadministration,
    Dosing,
    Fasting,
    Health,
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


class Vakkalagadda2016Arm(NamedTuple):
    """A treatment of Vakkalagadda2016."""

    #: the intervention of the data, the prefix of the labels
    intervention: str
    #: the route of the dose
    route: Route
    #: the dose of apixaban [mg]
    dose: float
    #: the pretreatment with rifampin
    rifampin: bool
    #: the color of the treatment
    color: str


class Vakkalagadda2016(ApixabanSimulationExperiment):
    """Simulation experiment of Vakkalagadda2016.

    20 healthy subjects (74.5 kg, BMI 24.4) received 5 mg apixaban IV (bolus of
    about 10 s, day 1) and 10 mg apixaban PO (tablet, fasted, day 3), and both
    again on day 12 and 14 (randomized sequence) under rifampin 600 mg once
    daily on days 5 to 15 (n = 19). The profiles under rifampin are measured
    after 7 or 9 doses of rifampin, the induction is at steady state and is
    simulated with constant factors.
    """

    arms: ClassVar[dict[str, Vakkalagadda2016Arm]] = {
        "API5IV": Vakkalagadda2016Arm(
            intervention="API5IV",
            route=Route.IV,
            dose=5,
            rifampin=False,
            color="tab:pink",
        ),
        "API10PO": Vakkalagadda2016Arm(
            intervention="API10PO",
            route=Route.PO,
            dose=10,
            rifampin=False,
            color="black",
        ),
        "API5IV_RIF600": Vakkalagadda2016Arm(
            intervention="API5IV_after, RIF600",
            route=Route.IV,
            dose=5,
            rifampin=True,
            color="tab:purple",
        ),
        "API10PO_RIF600": Vakkalagadda2016Arm(
            intervention="API10PO_after, RIF600",
            route=Route.PO,
            dose=10,
            rifampin=True,
            color="tab:gray",
        ),
    }
    bodyweight = 74.5  # [kg]
    bodyheight = math.sqrt(74.5 / 24.4)  # [m]

    #: Rifampin 600 mg once daily, a strong inducer of CYP3A4 and P-gp (PXR).
    #: The study: IV AUCinf x0.61 (CL 2.75 -> 4.51 l/h, t1/2 9.0 -> 4.6 h, Vss
    #: and CLR unchanged), PO AUCinf x0.46, Cmax x0.58, F 0.49 -> 0.37. Hepatic
    #: CYP3A4 activity about 2-fold (systemic clearance of midazolam after
    #: rifampin about 2- to 3-fold) and intestinal P-gp about 2- to 3.5-fold
    #: (duodenal P-gp after rifampin 600 mg, Greiner1999). With the unfitted
    #: model the factors give IV AUC x0.59 and PO AUC x0.57: the model has no
    #: first pass extraction which the induction changes (F is constant), so the
    #: larger effect on the oral dose is not described.
    rifampin_changes: ClassVar[dict[str, float]] = {
        "LI__f_cyp3a4": 2.0,
        "GU__f_pgp": 2.0,
    }

    infos_pk: ClassVar[dict[str, str]] = {
        "[Cve_api]": "apixaban",
        "Aurine_api": "cumulative amount",
    }

    def dataset_key(self, arm: str, sid: str) -> str:
        """Key of the dataset of an arm and an observable.

        Args:
            arm: the key of the arm.
            sid: the observable.

        Returns:
            The key of the dataset.
        """
        intervention = self.arms[arm].intervention
        if sid == "[Cve_api]":
            return self.to_sid(f"{intervention}_all_apixaban")
        return self.to_sid(f"{intervention}_cumulative amount_all_apixaban")

    def label(self, arm: str) -> str:
        """Text of the legend of an arm.

        Args:
            arm: the key of the arm.

        Returns:
            The text of the legend.
        """
        info = self.arms[arm]
        route = "IV" if info.route == Route.IV else "PO"
        return f"{info.dose}mg {route}" + (" + RIF 600mg" if info.rifampin else "")

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Tab2", "Fig2"]:
            df = self.load_dataframe(fig_id)
            if fig_id == "Tab2":
                # the urinary amounts are derived, the geometric means of the
                # renal clearance times the AUC0-T of Table 2
                df = df.rename(
                    columns={
                        "mean": "mean_real",
                        "geomean": "mean",
                    }
                )
            for label, df_label in df.groupby("label"):
                label = str(label)
                if fig_id == "Fig2" or "cumulative" in label:
                    dset = DataSet.from_df(df_label, self.ureg)
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                    dsets[self.to_sid(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims: dict[str, Simulation] = {}
        for key, arm in self.arms.items():
            if arm.route == Route.IV:
                dosing = {
                    "IVDOSE_api": Q(arm.dose, "mg"),
                    "ti_api": Q(10, "s"),
                }
            else:
                dosing = {"PODOSE_api": Q(arm.dose, "mg")}
            rifampin = (
                {
                    pid: Q(value, "dimensionless")
                    for pid, value in self.rifampin_changes.items()
                }
                if arm.rifampin
                else {}
            )

            # the output every 0.01 h resolves the first points after the
            # bolus (0.05 and 0.25 h)
            tcsims[key] = Simulation(
                time_unit="hr",
                end=50,
                preinit_changes={
                    **self.default_changes(),
                    **dosing,
                    **rifampin,
                    "BW": Q(self.bodyweight, "kg"),
                    "HEIGHT": Q(self.bodyheight, "m"),
                },
            )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings: dict[str, FitMapping] = {}
        for key, arm in self.arms.items():
            for sid, name in self.infos_pk.items():
                mappings[self.to_sid(f"fm_{key}_{name}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.dataset_key(key, sid),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd" if sid == "[Cve_api]" else None,
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=f"task_{key}",
                        xid="time",
                        yid=sid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA if sid == "[Cve_api]" else Tissue.URINE,
                        route=arm.route,
                        application_form=ApplicationForm.TABLET
                        if arm.route == Route.PO
                        else ApplicationForm.SOLUTION,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        # the fasting is reported for the oral dose only
                        fasting=Fasting.FASTED if arm.route == Route.PO else Fasting.NR,
                        coadministration=Coadministration.RIFAMPICIN
                        if arm.rifampin
                        else Coadministration.NONE,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure_pk(),
        }

    def figure_pk(self) -> dict[str, Figure]:
        """Apixaban in plasma and urine after the oral and the intravenous dose."""
        fig = Figure(
            experiment=self,
            sid="PK",
            name=f"{self.__class__.__name__}",
            num_cols=3,
            num_rows=1,
            height=self.panel_height,
            width=self.panel_width * 3.6,
            # one legend right of the panels, which share their curves
            settings={"legend_scope": "row"},
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            legend=True,
        )
        panels = [
            ("[Cve_api]", "linear"),
            ("[Cve_api]", "log"),
            ("Aurine_api", "linear"),
        ]
        for kp, (sid, scale) in enumerate(panels):
            plots[kp].set_yaxis(self.labels[sid], unit=self.units[sid], scale=scale)
            for key, arm in self.arms.items():
                # simulation
                plots[kp].add_data(
                    task=f"task_{key}",
                    xid="time",
                    yid=sid,
                    label=f"sim: {self.label(key)}",
                    color=arm.color,
                    linestyle="dashed" if arm.rifampin else "solid",
                )
                # data
                plots[kp].add_data(
                    dataset=self.dataset_key(key, sid),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd" if sid == "[Cve_api]" else None,
                    count="count",
                    label=f"exp: {self.label(key)}",
                    color=arm.color,
                    linestyle="solid" if sid == "[Cve_api]" else "",
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Vakkalagadda2016, output_dir=Vakkalagadda2016.__name__)
