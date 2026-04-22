from pathlib import Path

APIXABAN_PATH = Path(__file__).parent

MODEL_BASE_PATH = APIXABAN_PATH / "models" / "results" / "models"
MODEL_PATH = MODEL_BASE_PATH / "apixaban_body_flat.xml"

RESULTS_PATH = APIXABAN_PATH / "results"
RESULTS_PATH_SIMULATION = RESULTS_PATH / "simulation"
RESULTS_PATH_FIT = RESULTS_PATH / "fit"

# DATA_PATH_BASE = APIXABAN_PATH / "data"
DATA_PATH_BASE = APIXABAN_PATH.parents[3] / "pkdb_data" / "studies"
DATA_PATH_APIXABAN = DATA_PATH_BASE / "apixaban"
DATA_PATHS = [
    DATA_PATH_APIXABAN,
    DATA_PATH_BASE / "edoxaban"
]
