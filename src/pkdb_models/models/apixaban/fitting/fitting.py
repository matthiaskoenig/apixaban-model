"""Apixaban parameter fitting.

The fit problems of the apixaban model: which fit mapping collections enter a
fit and which parameters are adjusted, see `FIT_DEFINITIONS`. The commands
`run_fit`, `run_report` and `run_identifiability` of pkpdsim run them with the
package of the model:

    run_fit pkdb_models.models.apixaban --subset=PK --runs=3 --cores=3 --seed=1234 --method=DE
    run_fit pkdb_models.models.apixaban --subset=PD --runs=3 --cores=3 --seed=1234 --method=DE

The pharmacokinetics are fitted first, the pharmacodynamics on the adopted
values of the pharmacokinetics (`MODEL.adopted_fits()`). A fit is not followed by the
identifiability analysis of its parameters unless `--identifiability` is given.

The results, figures and the HTML report are written into the fit folder of the
model (`MODEL.fit_dir`), unless `--output_dir` is given. The report of
parameters which were fitted earlier is created with the `run_report` command,
their identifiability is analysed without fitting again with the
`run_identifiability` command:

    run_report pkdb_models.models.apixaban --subset=PK results/fit/PK_<fit id>/parameters.json
    run_identifiability pkdb_models.models.apixaban --subset=PK results/fit/PK_<fit id>/parameters.json
"""

from pkpdsim.fit import default_fit_settings
from sbmlsim.fit.cli import FitDefinition

from pkdb_models.models.apixaban import APIXABAN_PATH, DATA_PATHS
from pkdb_models.models.apixaban.fitting.mapping_collections import (
    f_collections_pd,
    f_collections_pk,
)
from pkdb_models.models.apixaban.fitting.parameters import (
    parameters_pd,
    parameters_pk,
)
from pkdb_models.models.apixaban.tolerances import absolute_tolerance

#: settings of the fits, stored with the result and read back by the report
#: the species get tolerances of their own scale, see `tolerances`
FIT_SETTINGS = default_fit_settings(
    absolute_tolerance=absolute_tolerance(1e-6, species=1e-12)
)

#: the fit problems of the apixaban model, the keys are the `--subset` argument
FIT_DEFINITIONS: dict[str, FitDefinition] = {
    # the pharmacokinetics of apixaban and its metabolites
    "PK": FitDefinition(
        mapping_collections=f_collections_pk,
        parameters=parameters_pk,
        base_path=APIXABAN_PATH,
        data_path=DATA_PATHS,
        settings=FIT_SETTINGS,
    ),
    # the pharmacodynamics: INR, PT, mPT, aPTT and the anti-factor Xa activity
    "PD": FitDefinition(
        mapping_collections=f_collections_pd,
        parameters=parameters_pd,
        base_path=APIXABAN_PATH,
        data_path=DATA_PATHS,
        settings=FIT_SETTINGS,
    ),
}
