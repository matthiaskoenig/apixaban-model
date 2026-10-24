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
    """Test dose dependency of the apixaban application."""

    doses: ClassVar[list[float]] = [0, 5, 10, 25, 50]  # [mg]
    colors: ClassVar[list[str]] = [
        "black",
        "tab:orange",
        "tab:blue",
        "tab:red",
        "tab:green",
    ]
    routes: ClassVar[list[str]] = ["PO"]  # ["IV", "PO"]
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
                                        "Aurine_m1": Q(0, "mmole"),
                                        "Aurine_m7": Q(0, "mmole"),
                                        # reset feces amounts
                                        "Afeces_api": Q(0, "mmole"),
                                        "Afeces_m1": Q(0, "mmole"),
                                        "Afeces_m2": Q(0, "mmole"),
                                        "Afeces_m7": Q(0, "mmole"),
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
                    settings={"legend_scope": "row"},
                )

                # a plot per entry: the panel 31 of the grid stays empty
                infos = [
                    # plasma
                    ("[Cve_api]", 0),
                    ("[Cve_m1]", 1),
                    ("[Cve_m7]", 2),
                    ("GU__APIABS", 3),
                    # urine
                    ("Aurine_api", 4),
                    ("Aurine_m1", 5),
                    ("Aurine_m7", 6),
                    ("GU__APIEXC", 7),
                    # feces
                    ("Afeces_api", 8),
                    ("Afeces_m1", 9),
                    ("Afeces_m2", 10),
                    ("Afeces_m7", 11),
                    ("PT", 12),
                    ("PT_change", 13),
                    ("PT_ratio", 14),
                    ("PT_relchange", 15),
                    ("mPT", 16),
                    ("mPT_change", 17),
                    ("mPT_ratio", 18),
                    ("mPT_relchange", 19),
                    ("aPTT", 20),
                    ("aPTT_change", 21),
                    ("aPTT_ratio", 22),
                    ("aPTT_relchange", 23),
                    ("INR", 24),
                    ("INR_change", 25),
                    ("INR_ratio", 26),
                    ("INR_relchange", 27),
                    ("antiXa_activity", 28),
                    ("antiXa_activity_gram", 29),
                    ("GU__APISEC", 30),
                ]
                for sid, ksid in infos:
                    plot = fig.add_subplot(
                        Plot(sid=f"{fig.sid}__plot{ksid}"),
                        row=ksid // fig.num_cols + 1,
                        col=ksid % fig.num_cols + 1,
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
