"""Apixaban: PBPK/PD model of apixaban and its anticoagulant effect.

The paths of the model and its model object `MODEL`, which the commands
`run_simulation`, `run_fit`, `run_report` and `run_identifiability` of pkpdsim
run by its package `pkdb_models.models.apixaban`.
"""

from pathlib import Path

from pkpdsim.model import FigureSettings, PKPDModel, PKPDReleaseSettings
from sbmlsim.project import SimulatorSettings
from sbmlsim.release.settings import Author

from pkdb_models.models.apixaban.tolerances import ABSOLUTE_TOLERANCE

APIXABAN_PATH = Path(__file__).parent

MODEL_BASE_PATH = APIXABAN_PATH / "models" / "output" / "models"
MODEL_PATH = MODEL_BASE_PATH / "apixaban_body_flat.xml"
# the female build, on which the studies and groups of mostly women run
FEMALE_MODEL_PATH = MODEL_BASE_PATH / "apixaban_body_female_flat.xml"

DATA_PATH_BASE = APIXABAN_PATH / "data"
DATA_PATH_APIXABAN = DATA_PATH_BASE / "apixaban"
DATA_PATH_EDOXABAN = DATA_PATH_BASE / "edoxaban"
DATA_PATHS = [
    DATA_PATH_APIXABAN,
    DATA_PATH_EDOXABAN,
]

MODEL = PKPDModel(
    name="apixaban",
    package=__name__,
    title="Apixaban PBPK/PD model",
    path=APIXABAN_PATH,
    model_path=MODEL_PATH,
    female_model_path=FEMALE_MODEL_PATH,
    data_paths=tuple(DATA_PATHS),
    archive_path=MODEL_BASE_PATH.parent / "apixaban_model.omex",
    factory=".models.factory:create_apixaban_models",
    experiments=".simulations:EXPERIMENTS",
    fit_definitions=".fitting.fitting:FIT_DEFINITIONS",
    # the contexts of use of the model and their evidence
    credibility=".credibility:CREDIBILITY",
    simulator=SimulatorSettings(
        absolute_tolerance=ABSOLUTE_TOLERANCE, relative_tolerance=1e-10
    ),
    figures=FigureSettings(formats=("svg",), fig_dpi=300, legend_fontsize=9.5),
    fit_identifiability=True,
    # the adopted fits, whose values the factory takes (`models/fits.py`)
    fits=("PK_20261031_104725__64222", "PD_20261104_193909__02221"),
    # the release of the model repository
    release=PKPDReleaseSettings(
        title=(
            "Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model"
            " of apixaban"
        ),
        repository="matthiaskoenig/apixaban-model",
        doi="10.5281/zenodo.18877904",
        authors=(
            Author(
                "Myshkina, Mariia",
                "0009-0000-7769-2154",
                "Humboldt-Universität zu Berlin, Faculty of Life Sciences, Department of Biology, Institute of Theoretical Biology, Systems Medicine of the Liver",
            ),
            Author(
                "Chang, Linh",
                "0009-0004-8004-3314",
                "Humboldt-Universität zu Berlin, Faculty of Life Sciences, Department of Biology",
            ),
            Author(
                "Metternich, Johannes",
                "0009-0004-1700-892X",
                "Technische Universität Berlin",
            ),
            Author("Badon, Shelee", "0009-0005-9147-0028", "Freie Universität Berlin"),
            Author("Babaeva, Mariia", "0009-0007-6659-7638", "Charité Berlin"),
            Author(
                "Elias, Michelle",
                "0009-0005-7959-3164",
                "Humboldt-University Berlin, Institute for Theoretical Biology, Berlin",
            ),
            Author(
                "König, Matthias",
                "0000-0003-1725-179X",
                (
                    "University of Lübeck, Lübeck, Germany; "
                    "University Hospital Schleswig-Holstein, Campus Lübeck, "
                    "First Department of Medicine, Lübeck, Germany; "
                    "Humboldt-Universität zu Berlin, Faculty of Life Sciences, "
                    "Department of Biology, Institute of Theoretical Biology, Berlin, Germany"
                ),
            ),
        ),
        keywords=(
            "model",
            "apixaban",
            "factor Xa inhibitor",
            "anticoagulation",
            "pharmacokinetics",
            "pharmacodynamics",
            "PBPK/PD",
            "physiologically based pharmacokinetic/ pharmacodynamic model",
            "SBML",
        ),
        docker_image="matthiaskoenig/apixaban",
        funding=(
            "Matthias König was supported by the Federal Ministry of Research, Technology and Space (BMFTR, Germany) within ATLAS by grant number 031L0304B and by the German Research Foundation (DFG) within the Research Unit Program FOR 5151 QuaLiPerF (Quantifying Liver Perfusion-Function Relationship in Complex Resection - A Systems Medicine Approach) by grant number 436883643 and by grant number 465194077 (Priority Programme SPP 2311, Subproject SimLivA). This work was supported by the BMBF-funded de.NBI Cloud within the German Network for Bioinformatics Infrastructure (de.NBI) (031A537B, 031A533A, 031A538A, 031A533B, 031A535A, 031A537C, 031A534A, 031A532B)."
        ),
        description=(
            "This repository provides the apixaban physiologically based"
            " pharmacokinetic/pharmacodynamic (PBPK/PD) model: the absorption,"
            " the hepatic metabolism by CYP3A4, the renal excretion and the"
            " intestinal secretion of apixaban, its metabolites and the"
            " anticoagulant effects (anti-factor Xa activity, INR, PT, aPTT)."
        ),
        first_year=2025,
    ),
)
"""The apixaban model: its commands, see `pkpdsim.model`."""
