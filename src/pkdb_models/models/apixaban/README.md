# Apixaban

Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model of the direct factor Xa inhibitor apixaban: the dissolution and absorption of apixaban in the intestine, its distribution, its metabolism by CYP3A4/5 in the liver to O-demethyl apixaban (M2), its sulfate (M1) and hydroxy apixaban (M7), the renal excretion of apixaban, M1 and M7, the intestinal secretion of apixaban (P-gp/BCRP), the biliary excretion of the metabolites and the anticoagulant effect on the anti-factor Xa activity, the INR, the prothrombin time (PT), the modified prothrombin time (mPT) and the activated partial thromboplastin time (aPTT).

## Structure

- `models/`: the definition of the model on the PBPK library `pkpdsim.pbpk` (`definition.py`: the substances apixaban, M1, M2 and M7, the metabolism and the biliary excretion in the liver, the efflux, the incomplete and the regional absorption of the segmented intestine and its summed fluxes (the readouts `Rabs_api`, `Reff_api`, `Rfeces_api`), the routes and the coagulation model `model_coagulation.py` as pharmacodynamic component). `models/factory.py` builds the comp model and the flattened whole-body model which is simulated, of the male and of the female reference individual (`SEXES`), the ODEs, the antimony, the figure of the model (`apixaban_body.svg`) and the COMBINE archive in `models/output/`; the values of the fitted parameters come from the adopted fits (`models/fits.py`).
- `experiments/`: the simulation experiments of the clinical studies (`studies/`, a study or a group of mostly women runs on the female build, the sex of its subjects is stated in its docstring), the dose dependency with the summed fluxes of the intestine and the gross absorbed fraction of the oral dose (the readout `Fa_api`, `misc/`) and the scans of the dose, the renal function, the cirrhosis and the body weight (`scans/`). The fit mappings are described with the vocabulary of `pkpdsim.metadata`.
- `fitting/`: the fit problems of the pharmacokinetics (`PK`) and the pharmacodynamics (`PD`) and the selection of the training, validation and outlier data.
- `sensitivity/`: the sensitivity analysis of the pharmacokinetic and pharmacodynamic parameters.
- `regional_absorption.py`: the derivation of the factors of the regional absorption of the lower ileum and the colon from the capsule study of Byon2018 on the model with `derive_regional_absorption` of the library (`python -m pkdb_models.models.apixaban.regional_absorption`), run again after a refit of the pharmacokinetics.
- `data/`: the data of the studies, a subset of the PK-DB studies (`data/collect_data.py`).

## Model

- Absorption: the tablet dissolves with `Ka_dis_api`, saturating with the undissolved dose (`D50_dis_api`, `kdis = Ka_dis*D50/(D50 + D)`), in every segment of the segmented intestine of the library; the solution dissolves in the stomach (`Ka_sol_api`). The dissolved apixaban is absorbed with `ka_api` into the mucosa of the segments, the lower ileum and the colon with the factors of the regional absorption (`f_ka_ile2_api`, `f_ka_colon_api`, derived with the model from the capsule study of Byon2018, not fitted); the fraction `fabs_api` of the absorbed flux enters the body, the rest goes into the feces. The rest of the dissolved apixaban moves on with the transit of the segments into the feces. Food slows the gastric emptying (`FED`, the fed state of the library), which the fed arms of the studies set.
- Elimination: CYP3A4 metabolism in the liver (`LI__API2M_k`, 0.78 into M2 and 0.22 into M7, Raghavan2009), the sulfation of M2 into M1 (`LI__M22M1_k`), the glomerular filtration of the unbound apixaban, M1 and M7 (`fu*GFR`, `GFR = GFR_base * f_renal_function`, `GFR_base` with the body surface area), the efflux of the unbound apixaban from the mucosa into the intestinal lumen (P-gp/BCRP, `GU__APISEC_k`) and the biliary excretion of M1, M2 and M7 (`LI__M1EXBI_k`, `LI__M2EXBI_k`, `LI__M7EXBI_k`; the rate of M2 is not fitted but fixed at that of M1, M2 has no plasma data).
- Interactions: the CYP3A4 activity `LI__f_cyp3a4` and the P-gp/BCRP activity `GU__f_abcb1` (1 normal) are set by the experiments of the coadministrations.
- Body weight and impairment: the organs, the blood flows and the GFR of the individual of the library (`BW`, `HEIGHT`), its renal function (`f_renal_function`) and its Child-Pugh severity (`CP_severity`). The model is built with the male and with the female reference individual (population `european_icrp`); the studies and the groups of mostly women run on the female build (`female_model_path`, `sex` and `simulation_sexes` of the studies).
- Pharmacodynamics: the coagulation model (`COAG`) acts on the total concentration of apixaban in the arm vein plasma (`Carm_api`); the anti-factor Xa activity is linear (`COAG__antiXa_slope`, `COAG__antiXa_gram_slope`), the INR and PT rise linearly relative to their baselines (`COAG__<marker>_ref`, `COAG__slope_api_<marker>`), the mPT and aPTT are Emax models relative to their baselines (`COAG__Emax_<marker>`, `COAG__EC50_api_<marker>`).

## Commands

```bash
# models, simulations
run_simulation pkdb_models.models.apixaban --action factory
run_simulation pkdb_models.models.apixaban --action simulate --experiments all
run_simulation pkdb_models.models.apixaban --action simulate --experiments all --uncertainty

# fits (PD on the adopted PK), adoption of a fit, reports of stored parameters, identifiability
run_fit pkdb_models.models.apixaban --subset=PK --runs=3 --cores=3 --method=DE
run_fit pkdb_models.models.apixaban --subset=PD --runs=3 --cores=3 --method=DE
run_fit pkdb_models.models.apixaban --adopt PK_<fit id>
run_report pkdb_models.models.apixaban --subset=PK results/fit/PK_<fit id>/parameters.json
run_identifiability pkdb_models.models.apixaban --subset=PK results/fit/PK_<fit id>/parameters.json

# sensitivity analysis (local by default)
python -m pkdb_models.models.apixaban.sensitivity.sensitivity_analysis
```

The results are written into `results/` of the model. The open issues of the model are in `TODO.md`.

## Adopted fits and uncertainty

The values of the fitted parameters come from the adopted fits of the model,
not from numbers in the code. `run_fit pkdb_models.models.apixaban --adopt <fit id>`
copies the record of a finished fit (its parameters, problem, profile
likelihood and Fisher information) into `models/output/fits/<fit id>/`, which is
tracked; the ids of the adopted fits are listed in `fits` of the model object
(`__init__.py`). The factory takes the fitted values and their uncertainty from
the records (`models/fits.py`) and writes the uncertainty into the SBML
(`distrib:uncertainty`). `run_simulation ... --uncertainty` runs the
experiments over draws of these distributions and draws the simulations as the
median with a band of quantiles into `results/simulation_uncertainty`. A refit
is: fit, adopt, replace the id in `fits`, rebuild the model. The
pharmacodynamics are fitted on the adopted values of the pharmacokinetics. See
the documentation of the repository on fitting (`docs/fitting.md`).
