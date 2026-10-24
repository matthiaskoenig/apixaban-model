"""Apixaban model factory."""

import copy
from pathlib import Path
from typing import Any

from pkpdsim.licenses import License, write_license
from pymetadata.omex import EntryFormat, ManifestEntry, Omex
from sbmlode import OdeSystem
from sbmlutils.comp import flatten_sbml
from sbmlutils.factory import Model, create_model

from pkdb_models.models.apixaban import MODEL_BASE_PATH
from pkdb_models.models.apixaban.models.model_body import model_body
from pkdb_models.models.apixaban.models.model_coagulation import model_coagulation
from pkdb_models.models.apixaban.models.model_intestine import model_intestine
from pkdb_models.models.apixaban.models.model_kidney import model_kidney
from pkdb_models.models.apixaban.models.model_liver import model_liver


def coagulation_of_body() -> Model:
    """Get the coagulation model which is merged into the whole-body model.

    The coagulation model on its own has the apixaban concentration in plasma
    `Cve_api` in its plasma compartment `Vplasma`; the merged model takes the
    concentration from the whole-body model, the compartment is not used. The
    model is a copy, `model_coagulation` keeps them.
    """
    coagulation = copy.copy(model_coagulation)
    coagulation.species = [s for s in model_coagulation.species if s.sid != "Cve_api"]
    coagulation.compartments = [
        c for c in model_coagulation.compartments if c.sid != "Vplasma"
    ]
    return coagulation


def create_apixaban_models(model_output_dir: Path) -> dict[str, dict[str, Any]]:
    """Create the tissue models and the whole-body model.

    Args:
        model_output_dir: directory of the models, the COMBINE archive and the
            license texts are written into its parent.

    Returns:
        The files of the model with their entries in the COMBINE archive.
    """
    model_output_dir.mkdir(parents=True, exist_ok=True)
    results: dict[str, dict[str, Any]] = {
        "README": {
            "path": MODEL_BASE_PATH.parent / "README.md",
            "entry": ManifestEntry(
                location="./README.md",
                format=EntryFormat.MARKDOWN,
                master=False,
            ),
        },
        "cc-by": {
            "path": write_license(model_output_dir.parent, License.CC_BY_SA_4_0),
            "entry": ManifestEntry(
                location="./cc-by-sa-4.0.txt",
                format=EntryFormat.TXT,
                master=False,
            ),
        },
        "mit": {
            "path": write_license(
                model_output_dir.parent,
                License.MIT,
                copyright="2025-2026 Matthias König",
            ),
            "entry": ManifestEntry(
                location="./mit.txt",
                format=EntryFormat.TXT,
                master=False,
            ),
        },
        "model_figure": {
            "path": MODEL_BASE_PATH.parent / "figures" / "apixaban_model.png",
            "entry": ManifestEntry(
                location="./figures/apixaban_model.png",
                format=EntryFormat.PNG,
                master=False,
            ),
        },
    }
    for models in [
        [model_kidney],
        [model_liver],
        [model_intestine],
        [model_coagulation],
        # the whole-body model with the coagulation model merged into it
        [coagulation_of_body(), model_body],
    ]:
        sid = models[-1].sid
        factory_results = create_model(
            model=models,
            filepath=model_output_dir / f"{sid}.xml",
            sbml_level=3,
            sbml_version=2,
        )
        sbml_path = factory_results.sbml_path
        results[sid] = {
            "path": sbml_path,
            "entry": ManifestEntry(
                location=f"./models/{sbml_path.name}",
                format=EntryFormat.SBML_L3V2,
                master=False,
            ),
        }

        # create differential equations
        md_path = model_output_dir / f"{sid}.md"
        ode_system = OdeSystem.from_sbml(sbml_path)
        ode_system.write(md_path)
        results[f"{sid}_md"] = {
            "path": md_path,
            "entry": ManifestEntry(
                location=f"./models/{md_path.name}",
                format=EntryFormat.MARKDOWN,
                master=False,
            ),
        }

    # create whole-body model
    sbml_path = results["apixaban_body"]["path"]
    sbml_path_flat = model_output_dir / f"{model_body.sid}_flat.xml"
    flatten_sbml(sbml_path, sbml_flat_path=sbml_path_flat)

    results["apixaban_body_flat"] = {
        "path": sbml_path_flat,
        "entry": ManifestEntry(
            location=f"./models/{sbml_path_flat.name}",
            format=EntryFormat.SBML_L3V2,
            master=True,
        ),
    }

    # create differential equations
    md_path = model_output_dir / f"{model_body.sid}_flat.md"
    ode_system = OdeSystem.from_sbml(sbml_path_flat)
    ode_system.write(md_path)
    results[f"{model_body.sid}_flat_md"] = {
        "path": md_path,
        "entry": ManifestEntry(
            location=f"./models/{md_path.name}",
            format=EntryFormat.MARKDOWN,
            master=False,
        ),
    }

    # create omex
    omex = Omex()
    for info in results.values():
        omex.add_entry(entry_path=info["path"], entry=info["entry"])
    omex.to_omex(omex_path=model_output_dir.parent / "apixaban_model.omex")

    return results


if __name__ == "__main__":
    # create the models
    create_apixaban_models(MODEL_BASE_PATH)
