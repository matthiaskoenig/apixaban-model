"""Apixaban model factory.

Builds the model of the definition with the PBPK library and writes its files
and the COMBINE archive (`pkpdsim.pbpk.create_archive`): the comp model, the
flattened model which is simulated, the ODEs and the antimony of the flat
model of the male and of the female build (`SEXES`), the figure of the model
and the license texts.
"""

from pathlib import Path
from typing import Any

from pkpdsim.pbpk import create_archive

from pkdb_models.models.apixaban import MODEL_BASE_PATH
from pkdb_models.models.apixaban.models.definition import DEFINITION, SEXES


def create_apixaban_models(model_output_dir: Path) -> dict[str, dict[str, Any]]:
    """Build the apixaban model.

    Args:
        model_output_dir: directory of the models, the COMBINE archive and the
            license texts are written into its parent.

    Returns:
        The files of the model with their entries in the COMBINE archive.
    """
    return create_archive(
        DEFINITION,
        model_output_dir,
        model="apixaban",
        copyright="2025-2026 Matthias König",
        readme=MODEL_BASE_PATH.parent / "README.md",
        sexes=SEXES,
    )


if __name__ == "__main__":
    create_apixaban_models(MODEL_BASE_PATH)
