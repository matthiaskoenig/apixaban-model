# Credibility

[Credibility report](https://matthiaskoenig.github.io/apixaban-model/credibility/index.html)

The assessment of the contexts of use of the model against its adopted fits. A context of use is decided on its validation evidence; a description (C1) is decided on its calibration evidence, the data the model was fitted to.

| Context of use | Title | Level | Risk | Verdict | Decided on |
| --- | --- | --- | --- | --- | --- |
| `describe` | Describe the data of the fits | C1 | low | insufficient evidence | calibration |
| `dose` | Repeated oral doses in healthy adults | C2 | low | supported | validation |
| `renal` | Renal function, age and body weight | C3 | medium | not supported | validation |
| `interaction` | Coadministered drugs | C3 | medium | supported | validation |
| `coagulation` | Clotting times in healthy adults | C5 | low | insufficient evidence | validation |
| `antixa` | Anti-factor Xa activity in healthy adults | C5 | low | not supported | validation |

## describe: Describe the data of the fits

**Question:** Does the model describe the pharmacokinetic data of apixaban and its metabolites and the coagulation data it was fitted to?

**Verdict:** insufficient evidence, decided on the calibration evidence, level C1, model risk low (influence low, consequence low), 1354 of 1427 decisive points evaluable (minimum 5).

| Quantity of interest | Description | Kind | Coverage | Points |
| --- | --- | --- | --- | --- |
| `Carm_api` | the plasma concentration of apixaban | absolute | covered | 514 |
| `Aurine_api` | the cumulative amount of apixaban in urine | absolute | covered | 12 |
| `Carm_api_m1` | the plasma concentration of M1 | absolute | covered | 10 |
| `Aurine_api_m1` | the cumulative amount of M1 in urine | absolute | covered | 2 |
| `Aurine_api_m7` | the cumulative amount of M7 in urine | absolute | covered | 2 |
| `Afeces_api` | the cumulative amount of apixaban in feces | absolute | covered | 1 |
| `Afeces_api_m1` | the cumulative amount of M1 in feces | absolute | covered | 1 |
| `Afeces_api_m2` | the cumulative amount of M2, M10 and M13 in feces | absolute | covered | 1 |
| `Afeces_api_m7` | the cumulative amount of M7 in feces | absolute | covered | 1 |
| `COAG__INR` | the international normalized ratio (INR) | absolute | covered | 56 |
| `COAG__PT` | the prothrombin time (PT) | absolute | uncovered | 0 |
| `COAG__mPT` | the modified prothrombin time (mPT) | absolute | covered | 133 |
| `COAG__aPTT` | the activated partial thromboplastin time (aPTT) | absolute | covered | 49 |
| `COAG__INR_relchange` | the change of the INR relative to its baseline | absolute | covered | 6 |
| `COAG__mPT_relchange` | the change of the mPT relative to its baseline | absolute | uncovered | 0 |
| `COAG__aPTT_relchange` | the change of the aPTT relative to its baseline | absolute | covered | 5 |
| `COAG__antiXa_activity` | the anti-factor Xa activity in IU/ml | absolute | covered | 33 |
| `COAG__antiXa_activity_gram` | the anti-factor Xa activity calibrated with apixaban, in ng/ml | absolute | covered | 20 |

**Claimed domain:**

| Field | Value | Coverage | Points |
| --- | --- | --- | --- |
| `route` | `PO` | calibrated | 1176 |
| `route` | `IV` | calibrated | 178 |
| `health` | `HEALTHY` | calibrated | 1354 |
| `coadministration` | `NONE` | calibrated | 1263 |
| `coadministration` | `COCKTAIL` | calibrated | 91 |
| `dosing` | `SINGLE` | calibrated | 1310 |
| `dosing` | `MULTIPLE` | calibrated | 44 |
| `fasting` | `FASTED` | calibrated | 1137 |
| `application_form` | `TABLET` | calibrated | 549 |
| `application_form` | `SOLUTION` | calibrated | 470 |

Beyond the metadata: the training data of the fits PK and PD in healthy adults: single oral doses of 0.5 to 50 mg as tablet or solution, the 20 mg [14C] solution of Raghavan2009 with the metabolites in plasma, urine and feces, the 25 µg solution of the microdose cocktail of apixaban, rivaroxaban and edoxaban, intravenous doses of 0.5 to 5 mg, and 10 and 50 mg once daily for 3 days (Frost2015b, PK only); the studies with the fasting not reported are simulated fasted and the oral doses with the form not reported as tablets (NR in the coverage) (statement, not assessed)

| Acceptance criterion | Value | Limit | Met |
| --- | --- | --- | --- |
| `within_2fold` | 85.52 | >= 70 | yes |

Inputs, the simulated covariates of the subjects and the doses of 158 of the 158 decisive mappings against the ones their studies report:

| Input | Mappings | Simulated | Equivalent | In range | Differ | Not reported |
| --- | --- | --- | --- | --- | --- | --- |
| `BW` | 158 | 60 to 87.4 kg | 129 | 0 | 0 | 29 |
| `HEIGHT` | 158 | 163 to 180 cm | 9 | 0 | 0 | 149 |
| `IVDOSE_api` (dose) | 19 | 0.5 to 5 mg | 19 | 0 | 0 | 0 |
| `PODOSE_api` (dose) | 100 | 2.5 to 50 mg | 99 | 0 | 0 | 1 |
| `SOLDOSE_api` (dose) | 39 | 0.025 to 20 mg | 39 | 0 | 0 | 0 |

| Verification | Factor | Points | Largest difference | Result |
| --- | --- | --- | --- | --- |
| tolerances | `discretization_error` | 1427 | 9.4e-06 | passed |
| second integration method | `numerical_solver_error` | 1427 | 2.3e-05 | passed |
| setup of the simulations | `use_error` | 1427 |  | passed |

## dose: Repeated oral doses in healthy adults

**Question:** Which plasma concentration of apixaban follows from repeated oral doses of 2.5 to 25 mg once or twice daily in fasted healthy adults?

**Verdict:** supported, decided on the validation evidence, level C2, model risk low (influence medium, consequence low), 211 of 217 decisive points evaluable (minimum 5).

| Quantity of interest | Description | Kind | Coverage | Points |
| --- | --- | --- | --- | --- |
| `Carm_api` | the plasma concentration of apixaban | absolute | covered | 165 |

**Claimed domain:**

| Field | Value | Coverage | Points |
| --- | --- | --- | --- |
| `route` | `PO` | validated | 211 |
| `health` | `HEALTHY` | validated | 211 |
| `coadministration` | `NONE` | validated | 211 |
| `dosing` | `MULTIPLE` | validated | 211 |
| `fasting` | `FASTED` | validated | 165 |

Beyond the metadata: repeated tablets of 2.5 to 25 mg twice daily and 10 and 25 mg once daily for 4 to 7 days, within the single doses of the training (0.5 to 50 mg), fasted; validated on the six regimens of Frost2013a (fasted men, 7 days), 10 mg twice daily of Cui2013 and 2.5 mg twice daily of Frost2014 (its fasting not reported, NR in the coverage, simulated fasted); 5 mg twice daily with the meals of Kreutz2017 is fed, simulated fed and kept as validation evidence outside the claim (FED in the coverage); 10 and 50 mg once daily for 3 days (Frost2015b) are calibration (statement, not assessed)

| Acceptance criterion | Value | Limit | Met |
| --- | --- | --- | --- |
| `within_2fold` | 87.68 | >= 70 | yes |

Temporal validation: no decisive study was collected after its fit (4 collected before).

Inputs, the simulated covariates of the subjects and the doses of 9 of the 9 decisive mappings against the ones their studies report:

| Input | Mappings | Simulated | Equivalent | In range | Differ | Not reported |
| --- | --- | --- | --- | --- | --- | --- |
| `BW` | 9 | 63.1 to 82.3 kg | 9 | 0 | 0 | 0 |
| `HEIGHT` | 9 | 164 to 181 cm | 3 | 0 | 0 | 6 |
| `PODOSE_api` (dose) | 9 | 2.5 to 25 mg | 9 | 0 | 0 | 0 |

| Verification | Factor | Points | Largest difference | Result |
| --- | --- | --- | --- | --- |
| tolerances | `discretization_error` | 217 | 4.8e-06 | passed |
| second integration method | `numerical_solver_error` | 217 | 6.4e-06 | passed |
| setup of the simulations | `use_error` | 217 |  | passed |

## renal: Renal function, age and body weight

**Question:** Which plasma concentration and urinary excretion of apixaban follow from a single oral dose in adults with impaired renal function, in the elderly and at a low or high body weight?

**Verdict:** not supported, decided on the validation evidence, level C3, model risk medium (influence medium, consequence medium), 193 of 219 decisive points evaluable (minimum 10).

| Quantity of interest | Description | Kind | Coverage | Points |
| --- | --- | --- | --- | --- |
| `Carm_api` | the plasma concentration of apixaban | absolute | covered | 186 |
| `Aurine_api` | the cumulative amount of apixaban in urine | absolute | covered | 7 |
| `api_auc_ratio` | the AUC of apixaban in the population over the AUC of a healthy adult of normal renal function and body weight | ratio, no pairing declared | n/a | n/a |

**Claimed domain:**

| Field | Value | Coverage | Points |
| --- | --- | --- | --- |
| `route` | `PO` | validated | 193 |
| `dosing` | `SINGLE` | validated | 193 |
| `health` | `HEALTHY` | validated | 79 |
| `health` | `RENAL_IMPAIRMENT` | validated | 114 |

Beyond the metadata: a single oral tablet of 5 to 20 mg, simulated with the creatinine clearance, the body weight and the height of the group; renal function: creatinine clearance 24.5 to 106.7 ml/min (the four groups of Chang2016, 10 mg) and the first dose of 5 mg in 20 elderly patients with atrial fibrillation (Metze2021, age 72 yr, creatinine clearance 66 ml/min, the individual profiles against the simulation of the mean); age: the healthy elderly of Frost2015 (70 yr, creatinine clearance 79.1 ml/min, 20 mg), the age acts through the renal function and the body size; body weight: 47 and 137 kg (Upreti2013, 10 mg; the reference group of 75 kg is training data); end-stage renal disease on dialysis is a limitation and not claimed (statement, not assessed)

| Acceptance criterion | Value | Limit | Met |
| --- | --- | --- | --- |
| `within_2fold` | 73.06 | >= 80 | no |
| `GMFE` | 1.794 | <= 1.5 | no |

Temporal validation: no decisive study was collected after its fit (4 collected before).

Inputs, the simulated covariates of the subjects and the doses of 35 of the 35 decisive mappings against the ones their studies report:

| Input | Mappings | Simulated | Equivalent | In range | Differ | Not reported |
| --- | --- | --- | --- | --- | --- | --- |
| `BW` | 35 | 47 to 137 kg | 15 | 0 | 0 | 20 |
| `HEIGHT` | 35 | 158 to 179 cm | 0 | 0 | 0 | 35 |
| `PODOSE_api` (dose) | 35 | 5 to 20 mg | 35 | 0 | 0 | 0 |

| Verification | Factor | Points | Largest difference | Result |
| --- | --- | --- | --- | --- |
| tolerances | `discretization_error` | 219 | 5.3e-06 | passed |
| second integration method | `numerical_solver_error` | 219 | 1.6e-05 | passed |
| setup of the simulations | `use_error` | 219 |  | passed |

## interaction: Coadministered drugs

**Question:** Does the model predict the pharmacokinetics of apixaban with coadministered inhibitors and inducers of CYP3A4 and of the intestinal efflux, simulated with factors of their activity from the literature, and with drugs without an interaction?

**Verdict:** supported, decided on the validation evidence, level C3, model risk medium (influence medium, consequence medium), 208 of 223 decisive points evaluable (minimum 10).

| Quantity of interest | Description | Kind | Coverage | Points |
| --- | --- | --- | --- | --- |
| `Carm_api` | the plasma concentration of apixaban | absolute | covered | 203 |
| `Aurine_api` | the cumulative amount of apixaban in urine | absolute | covered | 5 |
| `api_auc_ratio` | the AUC of apixaban with the coadministered drug over the AUC without it | ratio, no pairing declared | n/a | n/a |

**Claimed domain:**

| Field | Value | Coverage | Points |
| --- | --- | --- | --- |
| `route` | `PO` | validated | 195 |
| `route` | `IV` | validated | 13 |
| `health` | `HEALTHY` | validated | 208 |
| `coadministration` | `ATENOLOL` | validated | 11 |
| `coadministration` | `CARBAMAZEPINE` | validated | 16 |
| `coadministration` | `CLARITHROMYCIN` | validated | 24 |
| `coadministration` | `CYCLOSPORINE` | validated | 7 |
| `coadministration` | `DILTIAZEM` | validated | 12 |
| `coadministration` | `FAMOTIDINE` | validated | 11 |
| `coadministration` | `GABAPENTIN` | validated | 16 |
| `coadministration` | `KETOCONAZOLE` | validated | 27 |
| `coadministration` | `LAPATINIB` | validated | 8 |
| `coadministration` | `PREGABALIN` | validated | 16 |
| `coadministration` | `RIFAMPICIN` | validated | 24 |
| `coadministration` | `RITONAVIR` | validated | 12 |
| `coadministration` | `ROSUVASTATIN` | validated | 17 |
| `coadministration` | `TACROLIMUS` | validated | 7 |

Beyond the metadata: single doses of apixaban (the 25 µg microdose to 10 mg orally, 5 mg intravenously) in healthy adults with the regimens of the perpetrators of the arms: inhibitors of CYP3A4 and of the efflux (ketoconazole, clarithromycin, ritonavir, diltiazem, lapatinib), of the efflux (cyclosporine), inducers (rifampicin with oral and intravenous apixaban, carbamazepine) and drugs without an interaction in the model (atenolol, famotidine, gabapentin, pregabalin, rosuvastatin, tacrolimus); the factors of CYP3A4 (`LI__f_cyp3a4`) and of the efflux (`GU__f_abcb1`) are set per drug in the studies, a drug without them is not claimed (statement, not assessed)

| Acceptance criterion | Value | Limit | Met |
| --- | --- | --- | --- |
| `within_2fold` | 84.62 | >= 80 | yes |
| `GMFE` | 1.421 | <= 1.5 | yes |

Temporal validation: no decisive study was collected after its fit (12 collected before).

Inputs, the simulated covariates of the subjects and the doses of 23 of the 23 decisive mappings against the ones their studies report:

| Input | Mappings | Simulated | Equivalent | In range | Differ | Not reported |
| --- | --- | --- | --- | --- | --- | --- |
| `BW` | 23 | 60 to 80.9 kg | 11 | 0 | 0 | 12 |
| `HEIGHT` | 23 | 163 to 178 cm | 2 | 0 | 0 | 21 |
| `IVDOSE_api` (dose) | 2 | 5 mg | 2 | 0 | 0 | 0 |
| `PODOSE_api` (dose) | 13 | 2.5 to 10 mg | 13 | 0 | 0 | 0 |
| `SOLDOSE_api` (dose) | 8 | 0.025 mg | 8 | 0 | 0 | 0 |

| Verification | Factor | Points | Largest difference | Result |
| --- | --- | --- | --- | --- |
| tolerances | `discretization_error` | 223 | 2.2e-05 | passed |
| second integration method | `numerical_solver_error` | 223 | 2.9e-05 | passed |
| setup of the simulations | `use_error` | 223 |  | passed |

## coagulation: Clotting times in healthy adults

**Question:** Which INR, modified prothrombin time and aPTT and which ratios of the prothrombin time and the aPTT over their baseline follow from single and repeated oral doses of apixaban in fasted healthy adults?

**Verdict:** insufficient evidence, decided on the validation evidence, level C5, model risk low (influence medium, consequence low), 352 of 352 decisive points evaluable (minimum 5).

| Quantity of interest | Description | Kind | Coverage | Points |
| --- | --- | --- | --- | --- |
| `COAG__INR` | the international normalized ratio (INR) | absolute | covered | 124 |
| `COAG__mPT` | the modified prothrombin time (mPT) | absolute | covered | 84 |
| `COAG__aPTT` | the activated partial thromboplastin time (aPTT) | absolute | covered | 108 |
| `COAG__PT_ratio` | the PT over its baseline | absolute | uncovered | 0 |
| `COAG__aPTT_ratio` | the aPTT over its baseline | absolute | uncovered | 0 |

**Claimed domain:**

| Field | Value | Coverage | Points |
| --- | --- | --- | --- |
| `route` | `PO` | validated | 352 |
| `health` | `HEALTHY` | validated | 352 |
| `coadministration` | `NONE` | validated | 352 |
| `dosing` | `SINGLE` | validated | 32 |
| `dosing` | `MULTIPLE` | validated | 320 |
| `fasting` | `FASTED` | validated | 316 |

Beyond the metadata: fasted single oral doses of 0.5 to 50 mg and repeated doses of 2.5 to 25 mg once or twice daily; validated on the INR, aPTT and mPT of the repeated doses of Frost2013a and the INR and mPT of a single dose of 20 mg in the healthy elderly of Frost2015 (the only single dose of the validation), and on the PT and aPTT ratios of 5 mg twice daily with the meals of Kreutz2017, which are fed, simulated fed and outside the claim (FED in the coverage), so the two ratios are uncovered quantities; the PT and the relative changes over the baseline have no validation data and are not claimed (`describe`); renal and hepatic impairment are limitations and not claimed (statement, not assessed)

| Acceptance criterion | Value | Limit | Met |
| --- | --- | --- | --- |
| `within_2fold` | 100 | >= 70 | yes |

Temporal validation: no decisive study was collected after its fit (3 collected before).

Inputs, the simulated covariates of the subjects and the doses of 22 of the 22 decisive mappings against the ones their studies report:

| Input | Mappings | Simulated | Equivalent | In range | Differ | Not reported |
| --- | --- | --- | --- | --- | --- | --- |
| `BW` | 22 | 70.5 to 82.3 kg | 22 | 0 | 0 | 0 |
| `HEIGHT` | 22 | 176 to 181 cm | 2 | 0 | 0 | 20 |
| `PODOSE_api` (dose) | 22 | 2.5 to 25 mg | 22 | 0 | 0 | 0 |

| Verification | Factor | Points | Largest difference | Result |
| --- | --- | --- | --- | --- |
| tolerances | `discretization_error` | 352 | 1.7e-07 | passed |
| second integration method | `numerical_solver_error` | 352 | 3e-07 | passed |
| setup of the simulations | `use_error` | 352 |  | passed |

## antixa: Anti-factor Xa activity in healthy adults

**Question:** Which anti-factor Xa activity follows from single and repeated oral doses of apixaban in fasted healthy adults?

**Verdict:** not supported, decided on the validation evidence, level C5, model risk low (influence medium, consequence low), 63 of 65 decisive points evaluable (minimum 5).

| Quantity of interest | Description | Kind | Coverage | Points |
| --- | --- | --- | --- | --- |
| `COAG__antiXa_activity` | the anti-factor Xa activity in IU/ml | absolute | covered | 25 |
| `COAG__antiXa_activity_gram` | the anti-factor Xa activity calibrated with apixaban, in ng/ml | absolute | covered | 15 |

**Claimed domain:**

| Field | Value | Coverage | Points |
| --- | --- | --- | --- |
| `route` | `PO` | validated | 63 |
| `health` | `HEALTHY` | validated | 63 |
| `coadministration` | `NONE` | validated | 63 |
| `dosing` | `SINGLE` | validated | 30 |
| `dosing` | `MULTIPLE` | validated | 33 |
| `fasting` | `FASTED` | validated | 40 |

Beyond the metadata: the activity of the chromogenic assays in IU/ml and, calibrated with apixaban, in ng/ml, after fasted single oral doses of 0.5 to 50 mg and repeated doses of 2.5 to 10 mg twice daily; validated on 10 mg twice daily of Cui2013, 2.5 mg twice daily of Frost2014 (its fasting not reported, NR in the coverage) and on a single dose of 20 mg in the healthy elderly of Frost2015 (the only single dose of the validation), and on the two points in ng/ml of 5 mg twice daily with the meals of Kreutz2017, which are fed, simulated fed and outside the claim (FED in the coverage) (statement, not assessed)

| Acceptance criterion | Value | Limit | Met |
| --- | --- | --- | --- |
| `within_2fold` | 63.49 | >= 70 | no |

Temporal validation: no decisive study was collected after its fit (4 collected before).

Inputs, the simulated covariates of the subjects and the doses of 5 of the 5 decisive mappings against the ones their studies report:

| Input | Mappings | Simulated | Equivalent | In range | Differ | Not reported |
| --- | --- | --- | --- | --- | --- | --- |
| `BW` | 5 | 63.1 to 81.1 kg | 5 | 0 | 0 | 0 |
| `HEIGHT` | 5 | 164 to 181 cm | 3 | 0 | 0 | 2 |
| `PODOSE_api` (dose) | 5 | 2.5 to 20 mg | 5 | 0 | 0 | 0 |

| Verification | Factor | Points | Largest difference | Result |
| --- | --- | --- | --- | --- |
| tolerances | `discretization_error` | 65 | 4.7e-06 | passed |
| second integration method | `numerical_solver_error` | 65 | 1.7e-05 | passed |
| setup of the simulations | `use_error` | 65 |  | passed |

## Study data

The data of every study with points in the adopted fits, as the simulations read it, and the record of its collection from pkdb_data.

| Study | Points | First collected | Latest collection | Released | pkdb_data | Tables |
| --- | --- | --- | --- | --- | --- | --- |
| Abdollahizad2025 | 17 | 2026-03-05 (git) | 2026-10-25 | 2026-03-03 `PKDB01140` | unknown | 5 as collected |
| Bashir2018 | 24 | 2026-03-12 (git) | 2026-10-25 | 2026-04-30 `PKDB01165` | unknown | 6 as collected |
| Chang2016 | 76 | 2025-10-29 (git) | 2026-10-25 | 2026-03-06 `PKDB01148` | unknown | 5 as collected |
| Cui2013 | 48 | 2026-03-04 (git) | 2026-10-25 | 2026-03-04 `PKDB01142` | unknown | 6 as collected |
| Frost2013 | 292 | 2025-10-29 (git) | 2026-10-25 | 2026-03-06 `PKDB01149` | unknown | 7 as collected |
| Frost2013a | 488 | 2025-10-30 (git) | 2026-10-25 | 2026-03-06 `PKDB01147` | unknown | 9 as collected |
| Frost2014 | 43 | 2025-10-30 (git) | 2026-10-25 | 2025-11-19 `PKDB01110` | unknown | 7 as collected |
| Frost2014a | 17 | 2026-03-13 (git) | 2026-10-25 | 2026-04-30 `PKDB01167` | unknown | 7 as collected |
| Frost2015 | 189 | 2025-11-13 (git) | 2026-10-25 | 2025-11-11 `PKDB01098` | unknown | 9 as collected |
| Frost2015a | 48 | 2026-03-12 (git) | 2026-10-25 | 2026-04-30 `PKDB01166` | unknown | 5 as collected |
| Frost2015b | 44 | 2026-03-03 (git) | 2026-10-25 | 2026-03-06 `PKDB01150` | unknown | 5 as collected |
| Frost2017 | 24 | 2026-03-24 (git) | 2026-10-25 | 2026-03-25 `PKDB01158` | unknown | 7 as collected |
| Frost2018 | 282 | 2025-10-29 (git) | 2026-10-25 | 2026-03-06 `PKDB01151` | unknown | 7 as collected |
| Frost2021 | 228 | 2025-10-29 (git) | 2026-10-25 | 2026-03-06 `PKDB01152` | unknown | 7 as collected |
| Frost2021a | 115 | 2025-10-30 (git) | 2026-10-25 | 2026-03-04 `PKDB01143` | unknown | 9 as collected |
| Garonzik2019 | 18 | 2026-03-10 (git) | 2026-10-25 | 2026-04-30 `PKDB01168` | unknown | 5 as collected |
| Jeong2019 | 27 | 2026-03-12 (git) | 2026-10-25 | 2026-04-30 `PKDB01169` | unknown | 5 as collected |
| Kreutz2017 | 62 | 2025-11-03 (git) | 2026-10-25 | 2025-11-09 `PKDB01097` | unknown | 9 as collected |
| Lenard2024 | 34 | 2025-11-11 (git) | 2026-10-25 | 2025-11-11 `PKDB01099` | unknown | 7 as collected |
| Lenard2025 | 102 | 2025-11-17 (git) | 2026-10-25 | 2025-11-11 `PKDB01100` | unknown | 9 as collected |
| Leong2024 | 38 | 2026-03-06 (git) | 2026-10-25 | 2026-03-06 `PKDB01154` | unknown | 5 as collected |
| Metze2021 | 80 | 2026-03-04 (git) | 2026-10-25 | 2026-03-02 `PKDB01137` | unknown | 5 as collected |
| Mikus2019 | 32 | 2026-03-04 (git) | 2026-10-25 | 2026-03-02 `PKDB01138` | unknown | 7 as collected |
| Raghavan2009 | 66 | 2026-03-05 (git) | 2026-10-25 | 2026-03-04 `PKDB01146` | unknown | 7 as collected |
| Rohr2024 | 24 | 2026-03-04 (git) | 2026-10-25 | 2025-11-11 `PKDB01101` | unknown | 5 as collected |
| Shaikh2021 | 50 | 2026-03-13 (git) | 2026-10-25 | 2026-04-30 `PKDB01170` | unknown | 5 as collected |
| Song2015 | 128 | 2026-03-19 (git) | 2026-10-25 | 2026-04-30 `PKDB01171` | unknown | 5 as collected |
| Song2016 | 72 | 2026-03-16 (git) | 2026-10-25 | 2026-04-30 `PKDB01172` | unknown | 6 as collected |
| Tirona2018 | 22 | 2026-03-06 (git) | 2026-10-25 | 2026-03-06 `PKDB01153` | unknown | 7 as collected |
| Upreti2013 | 48 | 2025-10-28 (git) | 2026-10-25 | 2026-03-04 `PKDB01144` | unknown | 7 as collected |
| Upreti2013a | 24 | 2026-03-18 (git) | 2026-10-25 | 2026-04-30 `PKDB01173` | unknown | 5 as collected |
| Vakkalagadda2016 | 51 | 2026-03-13 (git) | 2026-10-25 | 2026-04-30 `PKDB01174` | unknown | 5 as collected |
| VandenBosch2021 | 14 | 2026-03-03 (git) | 2026-10-25 | 2026-03-04 `PKDB01145` | unknown | 5 as collected |
| Wang2014 | 18 | 2026-03-16 (git) | 2026-10-25 | 2026-04-30 `PKDB01175` | unknown | 5 as collected |
| Wang2016 | 190 | 2026-03-05 (git) | 2026-10-25 | 2026-03-04 `PKDB01141` | unknown | 8 as collected |

## Battery of the variants

The variants of the model are checked without data, the same for every context of use; a failed check makes every context not verified.

| Check | Factor | Cases | Largest deviation | Result |
| --- | --- | --- | --- | --- |
| dose states of the model | `use_error` | 2 |  | passed |
| mass balance | `numerical_code_verification` | 10 | 6.4e-15 | passed |
| non-negativity | `numerical_code_verification` | 340 | 6.5e-31 | passed |
| zero dose | `numerical_code_verification` | 340 | 0 | passed |
| steady state | `numerical_code_verification` | 332 | 0 | passed |
| superposition | `numerical_code_verification` | 8 | 0.0011 | passed |
| second simulator | `numerical_code_verification` |  |  | not applicable: AMICI is not installed, install sbmlsim with the extra 'amici'. |
| plausibility of the values | `use_error` | 1509 |  | passed |
| rebuild | `software_quality_assurance` | 10 |  | passed |
