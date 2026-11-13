"""The regional absorption of apixaban, derived with the model from Byon2018.

Released by a capsule as a solution of 2.5 mg, apixaban gave an AUC relative
to an oral solution of about 0.40 in the distal small bowel and 0.16 in the
ascending colon (Byon2018, study CV185007). The model takes the distal small
bowel as the lower ileum (`ile2`) and has one factor of the colon (the
segments caecum to rectum); the factors `f_ka_ile2_api` and `f_ka_colon_api`
(`REGIONAL_ABSORPTION` of `models/definition.py`) are those for which a
solution of 2.5 mg put into the lumen of the lower ileum and of the colon
ascendens gives these ratios, derived with `derive_regional_absorption` of
the library (`pkpdsim.pbpk.regional`), whose `release_auc_ratios` gives the
ratios of the model.

The ratios depend on the fitted absorption (`ka_api`, `fabs_api`, the efflux
`GU__APISEC_k`), so after a refit of the pharmacokinetics the factors are
derived again on the adopted model and, if they change in their rounded
digits, put into `REGIONAL_ABSORPTION` and fitted again from the adopted fit
(`run_fit pkdb_models.models.apixaban --subset PK --start <fit id> --runs 1`),
until the factors derived on the fit are those of the model:

    python -m pkdb_models.models.apixaban.regional_absorption

`test_the_regional_absorption_is_that_of_byon2018` checks the ratios of the
model.
"""

from collections.abc import Mapping
from types import MappingProxyType

import roadrunner
from pkpdsim.pbpk import derive_regional_absorption, release_auc_ratios

from pkdb_models.models.apixaban import MODEL

#: the substance
SUBSTANCE = "api"
#: the AUC of a solution of 2.5 mg released in a segment relative to an oral
#: solution (Byon2018): the lower ileum and the colon ascendens
TARGET: Mapping[str, float] = MappingProxyType({"ile2": 0.40, "asc": 0.16})
#: the dose of the study [mg]
DOSE = 2.5


def load() -> roadrunner.RoadRunner:
    """Load the male build of the model with the tolerances of the derivation."""
    r = MODEL.load_roadrunner()
    r.integrator.absolute_tolerance = 1e-14
    r.integrator.relative_tolerance = 1e-10
    return r


if __name__ == "__main__":
    model = load()
    ratios = release_auc_ratios(model, SUBSTANCE, list(TARGET), DOSE)
    print(f"ratios of the model: {ratios}")
    factors = derive_regional_absorption(model, SUBSTANCE, TARGET, DOSE)
    print(f"derived factors: {factors}")
