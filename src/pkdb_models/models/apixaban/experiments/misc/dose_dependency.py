"""Dependency of the pharmacokinetics and pharmacodynamics of apixaban on the dose."""

from typing import ClassVar, override

from sbmlsim import Q
from sbmlsim.plot import Figure, Plot
from sbmlsim.simulation import Change, Simulation

from pkdb_models.models.apixaban import MODEL
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)


class DoseDependencyExperiment(ApixabanSimulationExperiment):
    """Test dose dependency of the apixaban application.

    The intestine shows the summed fluxes of the segmented intestine (the
    readouts `Rabs_api`, `Reff_api` and `Rfeces_api`) and the gross absorbed
    fraction of the oral dose (the readout `Fa_api`): the dissolution of the
    tablet saturates with the dose (Frost2013), so a larger dose is absorbed
    less.
    """

    doses: ClassVar[list[float]] = [0, 5, 10, 25, 50]  # [mg]
    colors: ClassVar[list[str]] = [
        "black",
        "tab:orange",
        "tab:blue",
        "tab:red",
        "tab:green",
    ]
    routes: ClassVar[list[str]] = ["PO"]  # ["IV", "PO"]
    #: the outputs of a clotting time of the coagulation model
    pd_suffixes: ClassVar[list[str]] = ["", "_change", "_ratio", "_relchange"]
    dosing: ClassVar[list[str]] = ["single"]  # ["single", "multiple"]

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}

        for route in self.routes:
            for dose in self.doses:
                for dosing in self.dosing:
                    # single dosing
                    if dosing == "single":
                        tcsims[f"api_{route}_{dose}_{dosing}"] = Simulation(
                            time_unit="hr",
                            end=72,
                            preinit_changes={
                                **self.default_changes(),
                                f"{route}DOSE_api": Q(dose, "mg"),
                            },
                        )
                    elif dosing == "multiple":
                        # a dose every 24 hr, the urine and feces are collected
                        # per dosing interval
                        tcsims[f"api_{route}_{dose}_{dosing}"] = Simulation(
                            time_unit="hr",
                            end=7 * 24,
                            preinit_changes={
                                **self.default_changes(),
                                f"{route}DOSE_api": Q(dose, "mg"),
                            },
                            changes=[
                                self.add_doses(
                                    [24 * k for k in range(1, 7)],
                                    {f"{route}DOSE_api": Q(dose, "mg")},
                                ),
                                Change(
                                    [24 * k for k in range(1, 7)],
                                    {
                                        # reset urinary amounts
                                        "Aurine_api": Q(0, "mmole"),
                                        "Aurine_api_m1": Q(0, "mmole"),
                                        "Aurine_api_m7": Q(0, "mmole"),
                                        # reset feces amounts
                                        "Afeces_api": Q(0, "mmole"),
                                        "Afeces_api_m1": Q(0, "mmole"),
                                        "Afeces_api_m2": Q(0, "mmole"),
                                        "Afeces_api_m7": Q(0, "mmole"),
                                    },
                                ),
                            ],
                        )

        return tcsims

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure_pk(),
        }

    def figure_pk(self) -> dict[str, Figure]:
        """Timecourses of apixaban and its metabolites and of the pharmacodynamics."""
        figures = []

        for route in self.routes:
            for dosing in self.dosing:
                fig = Figure(
                    experiment=self,
                    sid=f"Fig_dose_dependency_pk_{route}_{dosing}",
                    num_rows=8,
                    num_cols=4,
                    name=f"Dose dependency apixaban ({route}, {dosing})",
                    # the legend of a row next to its last plot: every row is
                    # full, the legend large enough for the 32 plots
                    settings={"legend_scope": "row", "legend_fontsize": 13},
                )

                # full rows: apixaban (plasma, urine, the anti-factor Xa
                # activity in IU and calibrated in ng/ml), the metabolites M1 and
                # M7 (plasma, urine), the feces of apixaban and of M1, M2 and M7,
                # the intestine (absorption, efflux, loss to the feces and the
                # absorbed fraction), then a row per clotting time
                rows = [
                    [
                        "Carm_api",
                        "Aurine_api",
                        "COAG__antiXa_activity",
                        "COAG__antiXa_activity_gram",
                    ],
                    ["Carm_api_m1", "Aurine_api_m1", "Carm_api_m7", "Aurine_api_m7"],
                    ["Afeces_api", "Afeces_api_m1", "Afeces_api_m2", "Afeces_api_m7"],
                    ["Rabs_api", "Reff_api", "Rfeces_api", "Fa_api"],
                    *(
                        [f"COAG__{marker}{suffix}" for suffix in self.pd_suffixes]
                        for marker in ["PT", "mPT", "aPTT", "INR"]
                    ),
                ]
                infos = [
                    (sid, krow, kcol)
                    for krow, row in enumerate(rows)
                    for kcol, sid in enumerate(row)
                ]
                for sid, krow, kcol in infos:
                    plot = fig.add_subplot(
                        Plot(sid=f"{fig.sid}__plot{krow * fig.num_cols + kcol}"),
                        row=krow + 1,
                        col=kcol + 1,
                    )
                    plot.set_xaxis(
                        label="time", unit="hr" if dosing == "single" else "day"
                    )
                    plot.set_yaxis(label=self.labels[sid], unit=self.units[sid])
                    for kval, dose in enumerate(self.doses):
                        plot.add_data(
                            task=f"task_api_{route}_{dose}_{dosing}",
                            xid="time",
                            yid=sid,
                            label=f"{dose} mg",
                            color=self.colors[kval],
                        )

                figures.append(fig)
        return self.figures_by_sid(*figures)


if __name__ == "__main__":
    MODEL.run_experiments(
        DoseDependencyExperiment, output_dir=DoseDependencyExperiment.__name__
    )
