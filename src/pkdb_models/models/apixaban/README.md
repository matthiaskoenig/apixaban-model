# Apixaban

Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model of the direct factor Xa inhibitor apixaban: the dissolution and absorption of apixaban in the intestine, its distribution, its metabolism by CYP3A4/5 in the liver to O-demethyl apixaban (M2), its sulfate (M1) and hydroxy apixaban (M7), the renal excretion of apixaban, M1 and M7, the intestinal secretion of apixaban (P-gp/BCRP), the biliary excretion of the metabolites and the anticoagulant effect on the anti-factor Xa activity, the INR, the prothrombin time (PT), the modified prothrombin time (mPT) and the activated partial thromboplastin time (aPTT).

## Structure

- `models/`: the tissue models (`model_intestine.py`, `model_liver.py`, `model_kidney.py`), the coagulation model (`model_coagulation.py`) and the whole-body model (`model_body.py`). `models/factory.py` creates the SBML models, the flattened whole-body model which is simulated, the ODEs and the COMBINE archive in `models/output/`.
- `experiments/`: the simulation experiments of the clinical studies (`studies/`), the dose dependency (`misc/`) and the scans of the dose, the renal function, the cirrhosis and the body weight (`scans/`). The fit mappings are described with the vocabulary of `pkpdsim.metadata`.
- `fitting/`: the fit problems of the pharmacokinetics (`PK`) and the pharmacodynamics (`PD`) and the selection of the training, validation and outlier data.
- `sensitivity/`: the sensitivity analysis of the pharmacokinetic and pharmacodynamic parameters.
- `data/`: the data of the studies, a subset of the PK-DB studies (`data/collect_data.py`).

## Model

- Absorption: the tablet dissolves with `GU__Ka_dis_api`, saturating with the undissolved dose (`GU__PODOSE_50`), the solution reaches the lumen with `GU__Ka_sol_api`. The dissolved apixaban is absorbed in the small intestine with first order kinetics (`GU__APIABS_k`) in competition with the small intestinal transit into the colon (`GU__SITRANS_k`), which also carries the undissolved tablet, the secreted apixaban and the metabolites; the fraction absorbed is `GU__F_api_abs = APIABS_k/(APIABS_k + SITRANS_k)`. Nothing is absorbed from the colon, its content goes into the feces with the fecal transit (`GU__LUMEX_k`, about 30 hr). The model has no effect of food.
- Elimination: CYP3A4 metabolism `LI__API2M_k` split by `LI__f_m2` (0.78, Raghavan2009) into M2 and M7, renal excretion relative to the GFR (`KI__GFR = KI__f_renal_function * KI__GFR_base`, 101 ml/min, independent of the body weight; `KI__APIEX_f`, `KI__M1EX_f`, `KI__M7EX_f`) and intestinal secretion of the unbound apixaban (`GU__APISEC_k`).
- Interactions: the CYP3A4 activity `LI__f_cyp3a4` and the P-gp/BCRP activity `GU__f_pgp` (1 normal) are set by the experiments of the coadministrations.
- Body weight: the liver volume scales with the body surface area (`BSA`, Haycock, relative to `BSA_ref` of 75 kg and 170 cm).
- Pharmacodynamics: on the total concentration of apixaban in plasma; the anti-factor Xa activity is linear (`antiXa_slope`, `antiXa_gram_slope`), the INR, PT, mPT and aPTT are Emax models relative to their baselines (`<marker>_ref`, `Emax_<marker>`, `EC50_api_<marker>`).

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
