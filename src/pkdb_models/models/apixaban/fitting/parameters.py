"""Fit parameters of the apixaban model.

The parameters of the model on the PBPK library (`models/definition.py`,
`models/model_coagulation.py`). The start values are the bootstrap of the
adopted fits of the hand-written model (PK_20261017_103232__85dfa,
PD_20261017_121913__2536d), converted to the physiology and the conventions
of the library so that the systemic clearances of the hand-written model are
kept: the per-litre liver constants times the old liver over the liver of the
library (1.575 l / 2.33 l), the renal factors of the metabolites times the old
GFR over the GFR of the library (101/125) as their fractions unbound (the
renal clearance of the library is `fu*GFR`), the biliary rates of the
metabolites over their fraction unbound (the rates of the library act on the
unbound metabolite), the tissue distribution of apixaban to the total plasma
concentration (`Kp_api` times fu 0.131, `ftissue_api` times the old Kp), and
the absorption `ka_api` and the intestinal efflux `GU__APISEC_k` calibrated
to the net fecal clearance of an iv dose and the bioavailability of the
solution of the hand-written model. The bounds are those of the hand-written
model, converted alike; the bounds of `ka_api` and `GU__APISEC_k` lie around
their calibrated values with the width of the converted bounds of the old
model, and the upper bound of `ftissue_api` is ten times the converted one
(the old estimate sat at its bound).

Not fitted: the physiology, the fraction unbound of apixaban (`fu_ref_api`),
the exchange of apixaban, M1 and M7 between the liver and its plasma
(`LI__kps_*`, fast), the split of the CYP3A4 metabolism into M2 and M7
(Raghavan2009), the dissolution of the solution (`Ka_sol_api`, the default of
the library), the regional absorption of the lower ileum and the colon (`f_ka_ile2_api`,
`f_ka_colon_api`, derived from Byon2018, `models/definition.py`), the
factors which the experiments set (`LI__f_cyp3a4`,
`GU__f_abcb1`, `f_renal_function`, `CP_severity`, `FED`) and the baselines of
the clotting times (`COAG__<marker>_ref`, set by the experiments). The
biliary excretion of M2 is not fitted: its profile likelihood was open upwards
in a fit with all 15 parameters (cost 105.215, the record is not kept), so it
is fixed at the rate of M1 (`models/definition.py`), the rule of the fit
table.

The segmented intestine absorbs the fraction `fabs_api` of the absorbed flux;
its start value comes from a fit on a hand-edited flat model before the
library had it (cost 105.215).
"""

from pkpdsim.pbpk import Organ, Sex, reference_individual
from sbmlsim.fit import FitParameter

#: the old liver over the liver of the reference individual of the library
_F_VLI = 1.575 / reference_individual(Sex.MALE).volumes[Organ.LIVER]

#: the fractions unbound of M1 and M7 of the bootstrap: the renal factors of
#: the hand-written model (PK_20261017_103232__85dfa) times its GFR, 101
#: ml/min, over the healthy GFR of the male reference individual of the
#: library, 125 ml/min (`healthy_gfr`, at the conversion of 2026-10-26); a
#: historical conversion of the start values, which the fits do not start
#: from (they sample the bounds)
_FU_M1 = 0.045980136023462854 * 101 / 125
_FU_M7 = 0.014186605666188744 * 101 / 125

#: the tissue distribution of apixaban, informed by the early phase after iv
#: (Frost2021, Vakkalagadda2016)
parameters_pk_distribution: list[FitParameter] = [
    FitParameter(
        pid="ftissue_api",
        start_value=6.85044313915785,
        lower_bound=0.028,
        upper_bound=70,
        unit="l/min",
    ),
    FitParameter(
        pid="Kp_api",
        start_value=0.183319747979395,
        lower_bound=0.039,
        upper_bound=1.97,
        unit="dimensionless",
    ),
]

#: the elimination of apixaban: the CYP3A4 metabolism (per litre of liver) and
#: the efflux of the mucosa into the intestinal lumen (per litre of small
#: intestine); the renal excretion is the filtration `fu*GFR`
parameters_pk_elimination: list[FitParameter] = [
    FitParameter(
        pid="LI__API2M_k",
        start_value=0.0592072297277776,
        lower_bound=0.005,
        upper_bound=1,
        unit="1/min",
    ),
    FitParameter(
        pid="GU__APISEC_k",
        start_value=0.41024897948848216,
        lower_bound=0.41024897948848216 * 1e-3 / 0.4269,
        upper_bound=0.41024897948848216 * 10 / 0.4269,
        unit="1/min",
    ),
]

#: the absorption from the segmented intestine (the fraction of the absorbed
#: flux which enters the body, start value of a fit on a hand-edited flat
#: model) and the dose dependent dissolution of the tablet
parameters_pk_absorption: list[FitParameter] = [
    FitParameter(
        pid="ka_api",
        start_value=0.3320736355271903,
        lower_bound=0.3320736355271903 * 6e-3 / 1.111,
        upper_bound=0.3320736355271903 * 60 / 1.111,
        unit="1/hr",
    ),
    FitParameter(
        pid="fabs_api",
        start_value=0.729,
        lower_bound=0.01,
        upper_bound=1,
        unit="dimensionless",
    ),
    FitParameter(
        pid="Ka_dis_api",
        start_value=1.6298976674156418,
        lower_bound=0.05,
        upper_bound=10,
        unit="1/hr",
    ),
    FitParameter(
        pid="D50_dis_api",
        start_value=5.740959364533365,
        lower_bound=1,
        upper_bound=500,
        unit="mg",
    ),
]

#: the metabolites: their renal excretion (the fraction unbound is the renal
#: clearance relative to the GFR), the biliary excretion (per litre of liver)
#: and the sulfation of M2 to M1 (Raghavan2009 urine and feces)
parameters_pk_metabolites: list[FitParameter] = [
    FitParameter(
        pid="fu_ref_api_m1",
        start_value=_FU_M1,
        lower_bound=1e-3,
        upper_bound=1,
        unit="dimensionless",
    ),
    FitParameter(
        pid="fu_ref_api_m7",
        start_value=_FU_M7,
        lower_bound=1e-3,
        upper_bound=1,
        unit="dimensionless",
    ),
    FitParameter(
        pid="LI__M1EXBI_k",
        start_value=0.0024510033010617873 * _F_VLI / _FU_M1,
        lower_bound=1e-4 * _F_VLI / _FU_M1,
        upper_bound=1 * _F_VLI / _FU_M1,
        unit="1/min",
    ),
    FitParameter(
        pid="LI__M7EXBI_k",
        start_value=0.0024510033010617873 * _F_VLI / _FU_M7,
        lower_bound=1e-4 * _F_VLI / _FU_M7,
        upper_bound=1 * _F_VLI / _FU_M7,
        unit="1/min",
    ),
    FitParameter(
        pid="LI__M22M1_k",
        start_value=0.0004931944695645101 * _F_VLI,
        lower_bound=1e-4,
        upper_bound=0.1,
        unit="1/min",
    ),
]

#: the pharmacokinetics of apixaban and its metabolites
parameters_pk: list[FitParameter] = (
    parameters_pk_distribution
    + parameters_pk_elimination
    + parameters_pk_absorption
    + parameters_pk_metabolites
)

#: the clotting times relative to their baseline on the total concentration of
#: apixaban in the arm vein plasma: the INR and the PT linear (the slopes start
#: at Emax/EC50 of the Emax model of the INR of PD_20261031_140250__b09b7 and at
#: the increase of the PT of Wang2016 at its peak concentration), the mPT and the
#: aPTT Emax models whose half-maximal concentrations are total concentrations
parameters_pd_clotting: list[FitParameter] = [
    FitParameter(
        pid=f"COAG__slope_api_{sid}",
        start_value=slope,
        lower_bound=10,
        upper_bound=1e5,
        unit="1/mM",
    )
    for sid, slope in [("INR", 600.9), ("PT", 1360.0)]
] + [
    parameter
    for sid, emax, emax_lb, emax_ub, ec50, ec50_lb in [
        ("mPT", 6.053704513422128, 0.1, 10, 0.0019122026019966877, 1e-5),
        ("aPTT", 0.3596591786589533, 0.05, 5, 0.000720649921655501, 1e-4),
    ]
    for parameter in (
        FitParameter(
            pid=f"COAG__Emax_{sid}",
            start_value=emax,
            lower_bound=emax_lb,
            upper_bound=emax_ub,
            unit="dimensionless",
        ),
        FitParameter(
            pid=f"COAG__EC50_api_{sid}",
            start_value=ec50,
            lower_bound=ec50_lb,
            upper_bound=1e-2,
            unit="mM",
        ),
    )
]

#: the anti-factor Xa activity, linear in the total concentration of apixaban
parameters_pd_antixa: list[FitParameter] = [
    FitParameter(
        pid="COAG__antiXa_slope",
        start_value=5728.15077902583,
        lower_bound=500,
        upper_bound=5e4,
        unit="1/ml/mM",  # IU/ml per mM, the IU are counts in the model
    ),
    FitParameter(
        pid="COAG__antiXa_gram_slope",
        start_value=420605.75939786324,
        lower_bound=2e5,
        upper_bound=1e6,
        unit="ng/ml/mM",
    ),
]

#: the pharmacodynamics, fitted on the adopted values of the pharmacokinetics
parameters_pd: list[FitParameter] = parameters_pd_clotting + parameters_pd_antixa
