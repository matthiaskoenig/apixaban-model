"""The contexts of use of the apixaban model and the evidence of its credibility.

Every context of use (COU) answers one question with the adopted fits `PK` and
`PD` (`MODEL.adopted_fits()`, the pharmacodynamics fitted on the adopted values of the
pharmacokinetics) and draws its evidence from the validation data of
`fitting/mapping_collections.py`, which is split by the question it answers:
the doses (`DOSE_VALIDATION`, the repeated doses), the interactions
(`INTERACTION_VALIDATION`, the arms with a coadministered drug), the
populations (`POPULATION_VALIDATION`, renal impairment of Chang2016 and
Metze2021, the healthy elderly of Frost2015 and the body weight of
Upreti2013) and the limitations (`LIMITATION_VALIDATION`, data the model does
not describe, subtracted from every COU). The age and the body weight are no
fields of the metadata, so their range is a statement of the domain and their
mappings are evidence of the COU `renal`. The pharmacodynamics are two
COUs: the clotting times, which rise at most about 2-fold over their baseline
for the INR and the aPTT, and the anti-factor Xa activity, which is
proportional to the plasma apixaban; in one COU the clotting times would
decide the verdict of both. Hepatic impairment is not claimed: its data
(Frost2021a) is a limitation. See `docs/credibility.md` of pkpdsim for the
vocabulary.

The questions, levels and domains follow the data. The influence, the
consequence and the rationale of every COU are a draft for the review of the
modeller.
"""

from pkpdsim.fit import metadata_filter
from pkpdsim.metadata import (
    ApplicationForm,
    Coadministration,
    Dosing,
    Fasting,
    Health,
    Route,
)
from sbmlsim.credibility import (
    ContextOfUse,
    CouLevel,
    Credibility,
    Domain,
    Evidence,
    EvidenceRole,
    Level,
    QuantityOfInterest,
)
from sbmlsim.fit.filters import named_filter
from sbmlsim.fit.variability import Variability
from sbmlsim.simulation.sampling import LogNormal

from pkdb_models.models.apixaban.fitting.mapping_collections import (
    DOSE_VALIDATION,
    INTERACTION_VALIDATION,
    LIMITATION_VALIDATION,
    POPULATION_VALIDATION,
)

#: the observables of the PK fit with data (`PK_OBSERVABLES`, the plasma M7
#: has none)
_PLASMA = QuantityOfInterest("Carm_api", "the plasma concentration of apixaban")
_URINE = QuantityOfInterest("Aurine_api", "the cumulative amount of apixaban in urine")
_PK = (
    _PLASMA,
    _URINE,
    QuantityOfInterest("Carm_api_m1", "the plasma concentration of M1"),
    QuantityOfInterest("Aurine_api_m1", "the cumulative amount of M1 in urine"),
    QuantityOfInterest("Aurine_api_m7", "the cumulative amount of M7 in urine"),
    QuantityOfInterest("Afeces_api", "the cumulative amount of apixaban in feces"),
    QuantityOfInterest("Afeces_api_m1", "the cumulative amount of M1 in feces"),
    QuantityOfInterest(
        "Afeces_api_m2", "the cumulative amount of M2, M10 and M13 in feces"
    ),
    QuantityOfInterest("Afeces_api_m7", "the cumulative amount of M7 in feces"),
)

#: the clotting times with training and validation data
_INR = QuantityOfInterest("COAG__INR", "the international normalized ratio (INR)")
_MPT = QuantityOfInterest("COAG__mPT", "the modified prothrombin time (mPT)")
_APTT = QuantityOfInterest(
    "COAG__aPTT", "the activated partial thromboplastin time (aPTT)"
)
#: the clotting times of the PD fit (`filter_pd`, the coagulation model)
_CLOTTING_FITTED = (
    _INR,
    QuantityOfInterest("COAG__PT", "the prothrombin time (PT)"),
    _MPT,
    _APTT,
    QuantityOfInterest(
        "COAG__INR_relchange", "the change of the INR relative to its baseline"
    ),
    QuantityOfInterest(
        "COAG__mPT_relchange", "the change of the mPT relative to its baseline"
    ),
    QuantityOfInterest(
        "COAG__aPTT_relchange", "the change of the aPTT relative to its baseline"
    ),
)
#: the clotting times of the validation: the INR, the mPT and the aPTT, and the
#: ratios of Kreutz2017, which have no training data; the PT and the relative
#: changes have no validation data and are described only (`describe`)
_CLOTTING = (
    _INR,
    _MPT,
    _APTT,
    QuantityOfInterest("COAG__PT_ratio", "the PT over its baseline"),
    QuantityOfInterest("COAG__aPTT_ratio", "the aPTT over its baseline"),
)
#: the anti-factor Xa activity of the PD fit
_ANTIXA = (
    QuantityOfInterest("COAG__antiXa_activity", "the anti-factor Xa activity in IU/ml"),
    QuantityOfInterest(
        "COAG__antiXa_activity_gram",
        "the anti-factor Xa activity calibrated with apixaban, in ng/ml",
    ),
)

#: the renal impairment of `POPULATION_VALIDATION`
_RENAL_IMPAIRMENT = {
    sid: POPULATION_VALIDATION[sid] for sid in ["Chang2016", "Metze2021"]
}
#: the healthy elderly of `POPULATION_VALIDATION`
_ELDERLY = {"Frost2015": POPULATION_VALIDATION["Frost2015"]}
#: the body weight of `POPULATION_VALIDATION`
_BODY_WEIGHT = {"Upreti2013": POPULATION_VALIDATION["Upreti2013"]}

#: oral doses in healthy adults without a coadministered drug, the domain of
#: the doses and of the pharmacodynamics
_HEALTHY_PO = {
    "route": (Route.PO,),
    "health": (Health.HEALTHY,),
    "coadministration": (Coadministration.NONE,),
}

#: the fit mappings of the domain `_HEALTHY_PO`
_HEALTHY_PO_FILTER = metadata_filter(
    route={Route.PO},
    health={Health.HEALTHY},
    coadministration={Coadministration.NONE},
)

#: the domain of the pharmacodynamics: single and repeated oral doses in
#: fasted healthy adults
_PD_DOMAIN = {
    **_HEALTHY_PO,
    "dosing": (Dosing.SINGLE, Dosing.MULTIPLE),
    "fasting": (Fasting.FASTED,),
}

#: the drugs of the interaction arms of `INTERACTION_VALIDATION`
_COADMINISTRATIONS = (
    Coadministration.ATENOLOL,
    Coadministration.CARBAMAZEPINE,
    Coadministration.CLARITHROMYCIN,
    Coadministration.CYCLOSPORINE,
    Coadministration.DILTIAZEM,
    Coadministration.FAMOTIDINE,
    Coadministration.GABAPENTIN,
    Coadministration.KETOCONAZOLE,
    Coadministration.LAPATINIB,
    Coadministration.PREGABALIN,
    Coadministration.RIFAMPICIN,
    Coadministration.RITONAVIR,
    Coadministration.ROSUVASTATIN,
    Coadministration.TACROLIMUS,
)

#: the variability between the subjects and between the studies, the input of the
#: visual predictive check (`run_credibility --variability`). The coefficients of
#: variation are a draft for the review of the modeller, typical values of the
#: between-subject variability of population PK analyses, not estimated: the
#: hepatic metabolism (the clearance), the absorption, the body weight and the
#: sensitivity of the modified prothrombin time of a subject, and the metabolism
#: and absorption of a study (its population, formulation and assay)
VARIABILITY = Variability(
    {
        "LI__API2M_k": LogNormal(cv=0.3),
        "ka_api": LogNormal(cv=0.4),
        "BW": LogNormal(cv=0.15),
        "COAG__EC50_api_mPT": LogNormal(cv=0.3),
    },
    between=Variability(
        {"LI__API2M_k": LogNormal(cv=0.3), "ka_api": LogNormal(cv=0.3)}
    ),
)

CREDIBILITY = Credibility(
    contexts=(
        ContextOfUse(
            id="describe",
            title="Describe the data of the fits",
            question=(
                "Does the model describe the pharmacokinetic data of apixaban and "
                "its metabolites and the coagulation data it was fitted to?"
            ),
            level=CouLevel.C1,
            influence=Level.LOW,
            consequence=Level.LOW,
            quantities=(*_PK, *_CLOTTING_FITTED, *_ANTIXA),
            domain=Domain(
                metadata={
                    "route": (Route.PO, Route.IV),
                    "health": (Health.HEALTHY,),
                    "coadministration": (
                        Coadministration.NONE,
                        Coadministration.COCKTAIL,
                    ),
                    "dosing": (Dosing.SINGLE, Dosing.MULTIPLE),
                    "fasting": (Fasting.FASTED,),
                    "application_form": (
                        ApplicationForm.TABLET,
                        ApplicationForm.SOLUTION,
                    ),
                },
                statement=(
                    "the training data of the fits PK and PD in healthy adults: "
                    "single oral doses of 0.5 to 50 mg as tablet or solution, the "
                    "20 mg [14C] solution of Raghavan2009 with the metabolites in "
                    "plasma, urine and feces, the 25 µg solution of the microdose "
                    "cocktail of apixaban, rivaroxaban and edoxaban, intravenous "
                    "doses of 0.5 to 5 mg, and 10 and 50 mg once daily for 3 days "
                    "(Frost2015b, PK only); the studies with the fasting not "
                    "reported are simulated fasted and the oral doses with the "
                    "form not reported as tablets (NR in the coverage)"
                ),
            ),
            evidence=(
                Evidence(
                    "pharmacokinetics",
                    EvidenceRole.CALIBRATION,
                    metadata_filter(route={Route.PO, Route.IV}),
                    "the fitted apixaban and metabolites in plasma, urine and feces",
                    fit="PK",
                ),
                Evidence(
                    "pharmacodynamics",
                    EvidenceRole.CALIBRATION,
                    metadata_filter(route={Route.PO, Route.IV}),
                    "the fitted clotting times and anti-factor Xa activity",
                    fit="PD",
                ),
            ),
            rationale=(
                "Every figure of an apixaban study shows the fitted plasma, urine, "
                "feces and clotting times over their data, so the description is "
                "read together with the data it describes (influence low); it "
                "fixes no regimen of apixaban, and each context of a regimen, a "
                "population or an interaction stands on validation studies of "
                "its own (consequence low). "
                "The PK fit "
                "describes 82 % of its training points within 2-fold (GMFE 1.56) "
                "with a bias: the plasma after an oral dose is underpredicted (80 "
                "% within 2-fold, AFE 0.70; Song2015 0.42, Wang2016 0.49, "
                "Shaikh2021 0.53), after an intravenous dose it is not (AFE 0.97), "
                "consistent with the onset of the absorption and the late phase "
                "of the oral profile (TODO.md P1); the urine and the feces have a "
                "GMFE of at most 1.5. The PD fit describes 94 % within 2-fold "
                "(GMFE 1.22): the INR, PT, mPT and aPTT with a GMFE of at most "
                "1.07, the relative change of the INR worst (74 %, AFE 0.75), and "
                "the anti-factor Xa "
                "activity in IU/ml is underpredicted (81 %, AFE 0.58; its fitted "
                "slope is below the slope of the data, TODO.md P2, "
                "Pharmacodynamics). The acceptance is met (86 % within 2-fold), "
                "yet the COU is `insufficient_evidence`: two of its quantities "
                "have no calibration point inside the claimed domain, the PT, "
                "fitted on Wang2016 alone, whose fasting is not reported, and "
                "the relative change of the mPT, fitted on Frost2018 alone, whose "
                "application form is not reported (its relative changes after "
                "2.5 mg are outliers). Both studies are NR in the coverage, "
                "outside the claimed fasted state and forms, so the PT and the "
                "mPT change are uncovered quantities, although every claimed "
                "value of the metadata is calibrated by the points of the other "
                "quantities."
            ),
        ),
        ContextOfUse(
            id="dose",
            title="Repeated oral doses in healthy adults",
            question=(
                "Which plasma concentration of apixaban follows from repeated oral "
                "doses of 2.5 to 25 mg once or twice daily in fasted healthy "
                "adults?"
            ),
            level=CouLevel.C2,
            influence=Level.MEDIUM,
            consequence=Level.LOW,
            quantities=(_PLASMA,),
            domain=Domain(
                metadata={
                    **_HEALTHY_PO,
                    "dosing": (Dosing.MULTIPLE,),
                    "fasting": (Fasting.FASTED,),
                },
                statement=(
                    "repeated tablets of 2.5 to 25 mg twice daily and 10 and 25 "
                    "mg once daily for 4 to 7 days, within the single doses of "
                    "the training (0.5 to 50 mg), fasted; validated on the six "
                    "regimens of Frost2013a (fasted men, 7 days), 10 mg twice "
                    "daily of Cui2013 and 2.5 mg twice daily of Frost2014 (its "
                    "fasting not reported, NR in the coverage, simulated "
                    "fasted); 5 mg twice daily with the meals of Kreutz2017 is "
                    "fed, simulated fed and kept as validation evidence outside "
                    "the claim (FED in the coverage); 10 and 50 mg once daily "
                    "for 3 days (Frost2015b) are calibration"
                ),
            ),
            evidence=(
                Evidence(
                    "repeated doses",
                    EvidenceRole.VALIDATION,
                    named_filter(DOSE_VALIDATION),
                    "the repeated doses of Cui2013, Frost2013a, Frost2014 and "
                    "Kreutz2017, which the single doses of the training predict",
                    fit="PK",
                ),
                Evidence(
                    "fitted",
                    EvidenceRole.CALIBRATION,
                    metadata_filter(
                        route={Route.PO},
                        health={Health.HEALTHY},
                        coadministration={Coadministration.NONE},
                        dosing={Dosing.MULTIPLE},
                    ),
                    "the repeated doses of the training (Frost2015b), shown "
                    "beside the validation",
                    fit="PK",
                ),
            ),
            rationale=(
                "C2: 2.5 to 25 mg lie inside the fitted 0.5 to 50 mg, and a "
                "repeated regimen is the superposition of fitted single doses. The "
                "profile of a regimen which no study measured comes from the "
                "model, with the nine studied regimens as the check (influence "
                "medium); the indication fixes the regimen of the label, so a "
                "simulated profile of a healthy adult changes no regimen and "
                "serves the design of a trial or of a simulation (consequence "
                "low). Kreutz2017 is the one fed regimen: it is kept as "
                "validation evidence and not moved to the limitations, the "
                "conservative direction, since its points count in the "
                "acceptance although the fed state is not claimed. The fed arms "
                "of the single dose food studies are limitations instead, "
                "because their AUC change against the fasted arm is no process "
                "of the model, while the AUC over a dosing interval at steady "
                "state does not depend on the rate of the absorption, which is "
                "what the fed state of the model changes. The verdict rests on "
                "nine regimens of four studies (217 points) and carries the bias "
                "of the oral plasma of the training (AFE 0.78 against 0.70): the "
                "low doses are unbiased (2.5 and 5 mg twice daily of Frost2013a, "
                "AFE 1.01), the higher doses and the troughs are underpredicted, "
                "most 10 mg twice daily of Cui2013 (60 % within 2-fold, AFE "
                "0.46), whose troughs are a quarter of the data (TODO.md P1, "
                "terminal half-life and late phase)."
            ),
        ),
        ContextOfUse(
            id="renal",
            title="Renal function, age and body weight",
            question=(
                "Which plasma concentration and urinary excretion of apixaban "
                "follow from a single oral dose in adults with impaired renal "
                "function, in the elderly and at a low or high body weight?"
            ),
            level=CouLevel.C3,
            influence=Level.MEDIUM,
            consequence=Level.MEDIUM,
            quantities=(
                _PLASMA,
                _URINE,
                QuantityOfInterest(
                    "api_auc_ratio",
                    "the AUC of apixaban in the population over the AUC of a "
                    "healthy adult of normal renal function and body weight",
                    ratio=True,
                ),
            ),
            domain=Domain(
                metadata={
                    "route": (Route.PO,),
                    "dosing": (Dosing.SINGLE,),
                    "health": (Health.HEALTHY, Health.RENAL_IMPAIRMENT),
                },
                statement=(
                    "a single oral tablet of 5 to 20 mg, simulated with the "
                    "creatinine clearance, the body weight and the height of the "
                    "group; renal function: creatinine clearance 24.5 to 106.7 "
                    "ml/min (the four groups of Chang2016, 10 mg) and the first "
                    "dose of 5 mg in 20 elderly patients with atrial "
                    "fibrillation (Metze2021, age 72 yr, creatinine clearance 66 "
                    "ml/min, the individual profiles against the simulation of "
                    "the mean); age: the healthy elderly of Frost2015 (70 yr, "
                    "creatinine clearance 79.1 ml/min, 20 mg), the age acts "
                    "through the renal function and the body size; body weight: "
                    "47 and 137 kg (Upreti2013, 10 mg; the reference group of 75 "
                    "kg is training data); end-stage renal disease on dialysis "
                    "is a limitation and not claimed"
                ),
            ),
            evidence=(
                Evidence(
                    "renal impairment",
                    EvidenceRole.VALIDATION,
                    named_filter(_RENAL_IMPAIRMENT),
                    "the renal function groups of Chang2016 and the patients of "
                    "Metze2021 at the creatinine clearance each study measured, "
                    "held out of both fits",
                    fit="PK",
                ),
                Evidence(
                    "elderly",
                    EvidenceRole.VALIDATION,
                    named_filter(_ELDERLY),
                    "the healthy elderly men and women of Frost2015, whose young "
                    "groups are training data",
                    fit="PK",
                ),
                Evidence(
                    "body weight",
                    EvidenceRole.VALIDATION,
                    named_filter(_BODY_WEIGHT),
                    "the groups of low and high body weight of Upreti2013, whose "
                    "reference group is training data",
                    fit="PK",
                ),
            ),
            rationale=(
                "C3: the model describes the populations by its physiology, the "
                "renal function by the measured creatinine clearance (the "
                "filtration of apixaban and the chronic kidney disease profile of "
                "its albumin binding) and the body size by the body weight and "
                "the height, and the studies are the data of apixaban in these "
                "populations. A creatinine clearance, an age or a body weight "
                "between the groups of the four studies is simulated by the "
                "physiology of the model, the groups are the check (influence "
                "medium); the label halves the dose in atrial fibrillation with "
                "two of an age of at least 80 yr, a body weight of at most 60 kg "
                "and a serum creatinine of at least 1.5 mg/dl, and a simulated "
                "exposure of such a patient informs that reduction (consequence "
                "medium). The AUC ratio of a population over the healthy "
                "reference (`api_auc_ratio`) is the number of the reduction, "
                "left to step 3. The acceptance "
                "is not met (76 % within 2-fold, GMFE 1.82; 219 points of four "
                "studies): the plasma is underpredicted in every study, as the "
                "oral plasma of the training (AFE 0.70), most in Chang2016 (AFE "
                "0.43), whose normal group has an exposure a third above the "
                "other studies (AFE 0.54), and the bias grows with the "
                "impairment (mild 0.45, moderate 0.35, severe 0.41), so the "
                "model predicts a smaller rise of the exposure than observed; "
                "the elderly of Frost2015 (AFE 0.51, the young of the training "
                "0.66) and the body weights of Upreti2013 (0.65 and 0.58, the "
                "reference of the training 0.63, the AUC rises more at a low "
                "body weight than observed, TODO.md P1, Body weight) carry the "
                "bias of their study. The urine is within 1.5-fold in every "
                "group, and the patients of Metze2021 are unbiased (82 % within "
                "2-fold, AFE 0.92)."
            ),
        ),
        ContextOfUse(
            id="interaction",
            title="Coadministered drugs",
            question=(
                "Does the model predict the pharmacokinetics of apixaban with "
                "coadministered inhibitors and inducers of CYP3A4 and of the "
                "intestinal efflux, simulated with factors of their activity from "
                "the literature, and with drugs without an interaction?"
            ),
            level=CouLevel.C3,
            influence=Level.MEDIUM,
            consequence=Level.MEDIUM,
            quantities=(
                _PLASMA,
                _URINE,
                QuantityOfInterest(
                    "api_auc_ratio",
                    "the AUC of apixaban with the coadministered drug over the "
                    "AUC without it",
                    ratio=True,
                ),
            ),
            domain=Domain(
                metadata={
                    "route": (Route.PO, Route.IV),
                    "health": (Health.HEALTHY,),
                    "coadministration": _COADMINISTRATIONS,
                },
                statement=(
                    "single doses of apixaban (the 25 µg microdose to 10 mg "
                    "orally, 5 mg intravenously) in healthy adults with the "
                    "regimens of the perpetrators of the arms: inhibitors of "
                    "CYP3A4 and of the efflux (ketoconazole, clarithromycin, "
                    "ritonavir, diltiazem, lapatinib), of the efflux "
                    "(cyclosporine), inducers (rifampicin with oral and intravenous "
                    "apixaban, carbamazepine) and drugs without an interaction in "
                    "the model (atenolol, famotidine, gabapentin, pregabalin, "
                    "rosuvastatin, tacrolimus); the factors of CYP3A4 "
                    "(`LI__f_cyp3a4`) and of the efflux (`GU__f_abcb1`) are set "
                    "per drug in the studies, a drug without them is not claimed"
                ),
            ),
            evidence=(
                Evidence(
                    "interactions",
                    EvidenceRole.VALIDATION,
                    named_filter(INTERACTION_VALIDATION),
                    "the coadministration arms of Bashir2018, Frost2015a, "
                    "Frost2017, Garonzik2019, Jeong2019, Lenard2024, Lenard2025, "
                    "Mikus2019, Rohr2024, Tirona2018, Upreti2013a and "
                    "Vakkalagadda2016, which no fit sees",
                    fit="PK",
                ),
            ),
            rationale=(
                "C3: the interactions are factors of the activity of CYP3A4 in "
                "the liver and of the efflux of the intestine, set per drug from "
                "the literature and not fitted, and the arms are the data of "
                "apixaban with these drugs. A perpetrator or a regimen of no "
                "study is simulated with factors of the literature, the twelve "
                "studies of the arms are the check (influence medium); the label "
                "halves the dose of apixaban with a combined strong inhibitor of "
                "CYP3A4 and P-gp and avoids a combined strong inducer, so a "
                "simulated exposure with such a drug informs a prescription "
                "(consequence medium). The AUC ratios of the arms "
                "(`api_auc_ratio`) are left to step 3; the factors reproduce the "
                "AUC ratios "
                "of the arms but not their Cmax ratios (TODO.md P1, interactions "
                "by mouth). The arms carry the bias of their control arms rather "
                "than of the interaction: the worst are lapatinib and "
                "rosuvastatin of Jeong2019 (13 % and 38 % within 2-fold, AFE "
                "0.41 and 0.50), whose control arm is a limitation with an "
                "exposure about twice the one of the other studies, and "
                "diltiazem of Frost2015a (AFE 0.55) and famotidine of "
                "Upreti2013a (AFE 0.56), whose control arms are training data "
                "with an AFE of 0.62 and 0.60; the microdose arms of Lenard2024, "
                "Lenard2025, Mikus2019 and Rohr2024 are within 2-fold at 99 % of "
                "the points."
            ),
        ),
        ContextOfUse(
            id="coagulation",
            title="Clotting times in healthy adults",
            question=(
                "Which INR, modified prothrombin time and aPTT and which ratios "
                "of the prothrombin time and the aPTT over their baseline follow "
                "from single and repeated oral doses of apixaban in fasted "
                "healthy adults?"
            ),
            level=CouLevel.C5,
            influence=Level.MEDIUM,
            consequence=Level.LOW,
            quantities=_CLOTTING,
            domain=Domain(
                metadata=_PD_DOMAIN,
                statement=(
                    "fasted single oral doses of 0.5 to 50 mg and repeated "
                    "doses of 2.5 to 25 mg once or twice daily; validated on the "
                    "INR, aPTT and mPT of the repeated doses of Frost2013a and "
                    "the INR and mPT of a single dose of 20 mg in the healthy "
                    "elderly of Frost2015 (the only single dose of the "
                    "validation), and on the PT and aPTT ratios of 5 mg twice "
                    "daily with the meals of Kreutz2017, which are fed, "
                    "simulated fed and outside the claim (FED in the coverage), "
                    "so the two ratios are uncovered quantities; the PT and the "
                    "relative changes over the baseline have no "
                    "validation data and are not claimed (`describe`); renal "
                    "and hepatic impairment are limitations and not claimed"
                ),
            ),
            evidence=(
                Evidence(
                    "repeated doses",
                    EvidenceRole.VALIDATION,
                    named_filter(DOSE_VALIDATION),
                    "the clotting times of the repeated doses of Frost2013a and "
                    "the ratios of the fed regimen of Kreutz2017",
                    fit="PD",
                ),
                Evidence(
                    "elderly",
                    EvidenceRole.VALIDATION,
                    named_filter(_ELDERLY),
                    "the INR and mPT of the healthy elderly of Frost2015 (its "
                    "young groups are fitted)",
                    fit="PD",
                ),
                Evidence(
                    "fitted",
                    EvidenceRole.CALIBRATION,
                    _HEALTHY_PO_FILTER,
                    "the fitted clotting times of the healthy oral doses, shown "
                    "beside the validation",
                    fit="PD",
                ),
            ),
            rationale=(
                "C5: the clotting times of the coagulation model, driven by the "
                "simulated plasma apixaban. The clotting times of a regimen "
                "without PD data are read from the model, the repeated doses of "
                "Frost2013a are the check (influence medium); apixaban needs no "
                "monitoring of the coagulation, a simulated clotting time "
                "explains the result of an assay and sets no dose (consequence "
                "low). The "
                "fold criteria test the clotting times weakly: they are dominated "
                "by their baseline, the INR of the validation rises at most to "
                "1.9 and the aPTT 1.5-fold, the PT and aPTT ratios of Kreutz2017 "
                "to 1.11, so a 2-fold criterion is met by a model without an "
                "effect; the mPT rises about 4-fold (Frost2013a, 25 mg twice "
                "daily) and is the quantity which tests the effect (within "
                "2-fold at every point, GMFE 1.11). The acceptance is met on 352 "
                "points (100 % within 2-fold), mostly the repeated doses of "
                "Frost2013a and Kreutz2017 (320 of 352 points); the single dose "
                "has the 32 points of the elderly of Frost2015 only. The COU is "
                "nevertheless `insufficient_evidence`: the PT and aPTT ratios "
                "are validated only by the fed Kreutz2017, outside the claimed "
                "fasted state, so no decisive point of the two ratios lies "
                "inside the claim and both are uncovered quantities. They are "
                "claimed to state what the fed data of the ratios validates and "
                "are kept, the claim is not narrowed for a verdict: whether the "
                "ratios are an extrapolation to the fasted state or leave the "
                "claim is a decision of the modeller. The ratios of Kreutz2017 "
                "stay validation evidence outside the claim, the conservative "
                "direction (see `dose`). The relative changes over the baseline, "
                "which would test the effect directly, and the PT, fitted on "
                "Wang2016 alone, have no validation data and are claimed only by "
                "`describe` (the INR change of the training 74 % within 2-fold, "
                "AFE 0.75)."
            ),
        ),
        ContextOfUse(
            id="antixa",
            title="Anti-factor Xa activity in healthy adults",
            question=(
                "Which anti-factor Xa activity follows from single and repeated "
                "oral doses of apixaban in fasted healthy adults?"
            ),
            level=CouLevel.C5,
            influence=Level.MEDIUM,
            consequence=Level.LOW,
            quantities=_ANTIXA,
            domain=Domain(
                metadata=_PD_DOMAIN,
                statement=(
                    "the activity of the chromogenic assays in IU/ml and, "
                    "calibrated with apixaban, in ng/ml, after fasted single oral "
                    "doses of 0.5 to 50 mg and repeated doses of 2.5 to 10 mg "
                    "twice daily; validated on 10 mg twice daily of Cui2013, 2.5 "
                    "mg twice daily of Frost2014 (its fasting not reported, NR "
                    "in the coverage) and on a single dose of 20 mg in the "
                    "healthy elderly of Frost2015 (the only single dose of the "
                    "validation), and on the two points in ng/ml of 5 mg twice "
                    "daily with the meals of Kreutz2017, which are fed, "
                    "simulated fed and outside the claim (FED in the coverage)"
                ),
            ),
            evidence=(
                Evidence(
                    "repeated doses",
                    EvidenceRole.VALIDATION,
                    named_filter(DOSE_VALIDATION),
                    "the activity of the repeated doses of Cui2013, Frost2014 "
                    "and Kreutz2017",
                    fit="PD",
                ),
                Evidence(
                    "elderly",
                    EvidenceRole.VALIDATION,
                    named_filter(_ELDERLY),
                    "the activity of the healthy elderly of Frost2015, the young "
                    "of the study fitted",
                    fit="PD",
                ),
                Evidence(
                    "fitted",
                    EvidenceRole.CALIBRATION,
                    _HEALTHY_PO_FILTER,
                    "the fitted activity of the healthy oral doses, not deciding",
                    fit="PD",
                ),
            ),
            rationale=(
                "C5: the activity is proportional to the simulated plasma "
                "apixaban (a fitted slope per unit of the assay). The activity "
                "of a regimen without an assay follows from the simulated "
                "plasma and the slope, Cui2013, Frost2014, Frost2015 and "
                "Kreutz2017 are the check (influence medium); a measured "
                "activity estimates the exposure, e.g. before an urgent "
                "intervention, a simulated one explains such a measurement and "
                "replaces none (consequence low). The fed points of Kreutz2017 "
                "are kept outside the claim, as in `dose`. The "
                "activity carries the underprediction of the oral plasma and of "
                "the fitted slope in IU/ml, which is 0.69 to 0.84 times the slope "
                "of the data (TODO.md P2, Pharmacodynamics; the training of the "
                "domain 76 % within 2-fold, AFE 0.57). The acceptance is not met "
                "(63 % within 2-fold, GMFE 2.0, AFE 0.50; 65 points of four "
                "studies): Cui2013 is predicted at a third of the data (30 % "
                "within 2-fold, AFE 0.30, the troughs of its plasma are a "
                "quarter of the data), the elderly of Frost2015 at half (AFE "
                "0.53 in IU/ml and 0.49 in ng/ml), Frost2014 closer (76 %, AFE "
                "0.62). The bias is the one of the plasma and of the slope, "
                "not of the domain: the activity of the training is "
                "underpredicted alike."
            ),
        ),
    ),
    limitations=(
        Evidence(
            "limitations",
            EvidenceRole.LIMITATION,
            named_filter(LIMITATION_VALIDATION),
            "apixaban data which the model does not describe: hepatic impairment of "
            "Frost2021a (the Child-Pugh severity of the library lowers the hepatic "
            "clearance more than observed, the AUC of Child-Pugh B 1.28 times the "
            "control against 1.09), end-stage renal disease on hemodialysis of "
            "VandenBosch2021 and Wang2016 (no dialysis), the exposures about twice "
            "the ones of the other studies of the dose of Leong2024 and of the "
            "control arm of Jeong2019, the obese patients with a fatty liver of "
            "Tirona2018, the fed arms of the single dose food studies Frost2013 "
            "and Song2016 (their AUC change against the fasted arm, +4 % and -20 "
            "%, is no process of the model, whose fed state only slows the gastric "
            "emptying), the crushed tablet, the applesauce and the nasogastric "
            "tube of Song2015 and Song2016 (no process of the model), and the "
            "feces of the drained bile of Raghavan2009",
        ),
    ),
    notes=(
        "Not claimed: hepatic impairment (the data of Frost2021a, Child-Pugh A "
        "and B, is a limitation, so neither a description nor an extrapolation "
        "to Child-Pugh C is claimed), end-stage renal disease and dialysis, the "
        "fed state and the food effect (the fed regimen of Kreutz2017 is "
        "validation evidence of `dose`, `coagulation` and `antixa` outside "
        "their claim, the fed arms of Frost2013 and Song2016 are limitations), "
        "the alternative administrations, the plasma M7 (no "
        "data), the metabolites in renal impairment (no data, TODO.md P2), the "
        "pharmacodynamics in renal and hepatic impairment and with a "
        "coadministered drug, and the naproxen arm of Frost2014a (plotted, not "
        "mapped). The outliers are the placebo arms of Frost2013a, Frost2018 and "
        "Frost2021 and the relative changes after 2.5 mg of Frost2018. The "
        "TODO.md of apixaban has the open points."
    ),
    variability=VARIABILITY,
)
