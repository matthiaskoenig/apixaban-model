from pathlib import Path

from pkdb_models.models.data import collect_tsv_files


def collect_apixaban_data():
    common_parent: Path = Path(__file__).parents[5]
    source_dir = common_parent / "pkdb_data" / "studies" / "apixaban"
    target_dir = Path(__file__).parent / "apixaban"

    collect_tsv_files(source_dir=source_dir, target_dir=target_dir)

def collect_edoxaban_data():
    common_parent: Path = Path(__file__).parents[5]
    source_dir = common_parent / "pkdb_data" / "studies" / "edoxaban"
    target_dir = Path(__file__).parent / "edoxaban"

    collect_tsv_files(source_dir=source_dir, target_dir=target_dir)

if __name__ == "__main__":
    collect_apixaban_data()
    collect_edoxaban_data()

