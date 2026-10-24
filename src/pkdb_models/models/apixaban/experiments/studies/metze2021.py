"""Simulation experiment of the study Metze2021."""

from typing import ClassVar, override

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


class Metze2021(ApixabanSimulationExperiment):
    """Simulation experiment of Metze2021.

    Patients (n=20, age 72 yr, 85 % atrial fibrillation) newly started on
    apixaban 5 mg b.i.d. (tablet); the profile after the first dose at 0, 3, 6
    and 12 h, measured with a chromogenic anti-Xa assay calibrated for apixaban
    (ng/ml). Creatinine clearance 66 +- 18 ml/min (Table 1). Body weight and
    fasting are not reported.
    """

    # 1-15
    individuals: ClassVar[list[str]] = [f"IS{k:03d}" for k in range(1, 16)]
    intervention = "API5"
    dose = 5
    #: creatinine clearance of the apixaban group [ml/min] (Table 1)
    crcl = 66

    markers: ClassVar[dict[str, str]] = {"mean": "s", "IS": "o"}

    marker_size: ClassVar[dict[str, float]] = {
        "mean": 7.5,
        "IS": 5.2,
    }

    linewidths: ClassVar[dict[str, float]] = {
        "mean": 1.5,
    }

    infos_pk: ClassVar[dict[str, str]] = {"[Cve_api]": "apixaban"}

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1", "Fig1A"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                if fig_id == "Fig1" and label.startswith("apixaban"):
                    dset.unit_conversion("value", 1 / self.Mr.api)
                elif fig_id == "Fig1A" and label.startswith("apixaban"):
                    dset.unit_conversion("mean", 1 / self.Mr.api)
                dsets[label] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}

        tcsims[self.intervention] = Simulation(
            time_unit="hr",
            end=16,
            preinit_changes={
                **self.default_changes(),
                "PODOSE_api": Q(self.dose, "mg"),
                # renal function relative to a GFR of 101 ml/min
                "KI__f_renal_function": Q(self.crcl / 101, "dimensionless"),
            },
        )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        # The mean is mapped, the individuals of the same subjects are only
        # plotted (15 of the 20 profiles are digitized).
        for sid, name in self.infos_pk.items():
            mappings[f"fm_{name}_{self.intervention}"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=f"{name}_{self.intervention}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                ),
                observable=FitData(
                    self,
                    task=f"task_{self.intervention}",
                    xid="time",
                    yid=sid,
                ),
                metadata=PKPDMappingMetaData(
                    tissue=Tissue.PLASMA,
                    route=Route.PO,
                    application_form=ApplicationForm.TABLET,
                    dosing=Dosing.SINGLE,
                    health=Health.RENAL_IMPAIRMENT,
                    fasting=Fasting.NR,
                    coadministration=Coadministration.NONE,
                    data=PKPDData.PK,
                    data_type=DataType.MEAN,
                ),
            )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {**self.figure_pk()}

    def figure_pk(self) -> dict[str, Figure]:
        """Figure of the pharmacokinetics."""
        fig = Figure(
            experiment=self,
            sid="Fig1",
            name=f"{self.__class__.__name__}",
            height=self.panel_height,
            width=self.panel_width * 0.87,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )
        plots[0].set_yaxis(self.label_api_plasma, unit=self.unit_api)

        for ks, (sid, name) in enumerate(self.infos_pk.items()):
            # simulation
            plots[ks].add_data(
                task=f"task_{self.intervention}",
                xid="time",
                yid=sid,
                label="sim 5mg PO (CrCl 66 ml/min)",
                color=self.renal_colors["Mild renal impairment"],
            )
            # individual data
            for ki, individual in enumerate(self.individuals):
                plots[ks].add_data(
                    dataset=f"{name}_{self.intervention}_{individual}",
                    xid="time",
                    yid="value",
                    yid_sd=None,
                    label="5mg PO (individuals)" if ki == 0 else None,
                    color="white",
                    markeredgecolor=self.renal_colors["Mild renal impairment"],
                    linestyle="",
                    marker=self.markers["IS"],
                    markersize=self.marker_size["IS"],
                )
            # mean data
            plots[ks].add_data(
                dataset=f"{name}_{self.intervention}",
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
                label="5mg PO",
                color=self.renal_colors["Mild renal impairment"],
                linewidth=self.linewidths["mean"],
                marker=self.markers["mean"],
                markersize=self.marker_size["mean"],
            )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Metze2021, output_dir=Metze2021.__name__)
