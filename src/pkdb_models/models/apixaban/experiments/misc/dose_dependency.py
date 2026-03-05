from copy import deepcopy
from typing import Dict

from sbmlsim.plot import Axis, Figure, Plot
from sbmlsim.simulation import Timecourse, TimecourseSim

from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)
from pkdb_models.models.apixaban.helpers import run_experiments


class DoseDependencyExperiment(ApixabanSimulationExperiment):
    """Tests application."""

    doses = [0, 5, 10, 25, 50]  # [mg]
    colors = ["black", "tab:orange", "tab:blue", "tab:red", "tab:green"]
    routes = ["PO"]  # ["IV", "PO"]
    dosing = ["single"]  # ["single", "multiple"]

    def simulations(self) -> Dict[str, TimecourseSim]:
        Q_ = self.Q_
        tcsims = {}

        for route in self.routes:
            for dose in self.doses:
                for dosing in self.dosing:
                    # single dosing
                    if dosing == "single":
                        tcsims[f"api_{route}_{dose}_{dosing}"] = TimecourseSim(
                            Timecourse(
                                start=0,
                                end=24 * 60,  # [min]
                                steps=1000,
                                changes={
                                    **self.default_changes(),
                                    f"{route}DOSE_api": Q_(dose, "mg"),
                                },
                            )
                        )
                    elif dosing == "multiple":
                        tc0 = Timecourse(
                            start=0,
                            end=24 * 60,  # [min]
                            steps=1000,
                            changes={
                                **self.default_changes(),
                                f"{route}DOSE_api": Q_(dose, "mg"),
                            },
                        )
                        tc1 = Timecourse(
                            start=0,
                            end=24 * 60,  # [min]
                            steps=1000,
                            changes={
                                f"{route}DOSE_api": Q_(dose, "mg"),

                                # # reset urinary amounts
                                "Aurine_api": Q_(0, "mmole"),
                                "Aurine_m1": Q_(0, "mmole"),
                                "Aurine_m7": Q_(0, "mmole"),

                                # reset feces amounts
                                "Afeces_api": Q_(0, "mmole"),
                                "Afeces_m1": Q_(0, "mmole"),
                                "Afeces_m2": Q_(0, "mmole"),
                                "Afeces_m7": Q_(0, "mmole"),
                            },
                        )
                        tcsims[f"api_{route}_{dose}_{dosing}"] = TimecourseSim(
                            [tc0] + [tc1 for _ in range(6)]
                        )

        return tcsims

    def figures(self) -> Dict[str, Figure]:
        return {
            **self.figure_pk(),
        }

    def figure_pk(self) -> Dict[str, Figure]:
        figures = {}

        for route in self.routes:
            for dosing in self.dosing:


                fig = Figure(
                    experiment=self,
                    sid=f"Fig_dose_dependency_pk_{route}_{dosing}",
                    num_rows=8,
                    num_cols=4,
                    name=f"Dose dependency apixaban ({route}, {dosing})",
                )

                plots = fig.create_plots(
                    xaxis=Axis("time", unit="hr" if dosing == "single" else "day"),
                    legend=True
                )
                infos = [
                    # plasma
                    ("[Cve_api]", 0),
                    ("[Cve_m1]", 1),
                    ("[Cve_m7]", 2),

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

                    ("Xa_inhibition", 28),
                    ("antiXa_activity", 29),

                ]
                for sid, ksid in infos:
                    if sid:
                        plots[ksid].set_yaxis(label=self.labels[sid], unit=self.units[sid])

                for sid, ksid in infos:
                    if sid:
                        for kval, dose in enumerate(self.doses):
                            plots[ksid].add_data(
                                task=f"task_api_{route}_{dose}_{dosing}",
                                xid="time",
                                yid=sid,
                                label=f"{dose} mg",
                                color=self.colors[kval],
                            )

                figures[fig.sid] = fig
        return figures


if __name__ == "__main__":
    run_experiments(DoseDependencyExperiment, output_dir=DoseDependencyExperiment.__name__)
