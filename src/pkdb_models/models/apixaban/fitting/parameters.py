"""Parameters to optimize in the apixaban fits, with their bounds.

The start values are the values of the model. Not fitted are the physiology,
the fraction unbound `fu_api`, the healthy GFR `KI__GFR_base`, the split of the
CYP3A4 metabolism `LI__f_m2` (Raghavan2009), the fecal transit `GU__LUMEX_k`, the interaction factors `LI__f_cyp3a4` and `GU__f_pgp` (set by
the experiments of the coadministrations) and the baselines of the clotting
times (`<marker>_ref`, set by the experiments).
"""

from sbmlsim.fit import FitParameter

#: the tissue distribution of apixaban, informed by the early phase after IV
#: (Frost2021, Vakkalagadda2016) and the volume of distribution (21.6 l)
parameters_pk_distribution: list[FitParameter] = [
    FitParameter(
        pid="ftissue_api",
        start_value=0.85,
        lower_bound=0.02,
        upper_bound=5,
        unit="l/min",
    ),
    FitParameter(
        pid="Kp_api",
        start_value=2.43,
        lower_bound=0.3,
        upper_bound=15,
        unit="dimensionless",
    ),
]

#: the elimination of apixaban: the CYP3A4 metabolism, the renal excretion and
#: the intestinal secretion. Without fecal data after IV the split between the
#: metabolism and the secretion rests on the recovery of the metabolites
#: (Raghavan2009)
parameters_pk_elimination: list[FitParameter] = [
    FitParameter(
        pid="LI__API2M_k",
        start_value=0.094,
        lower_bound=0.005,
        upper_bound=1,
        unit="1/min",
    ),
    FitParameter(
        pid="KI__APIEX_f",
        start_value=1.04,
        lower_bound=0.3,
        upper_bound=3,
        unit="dimensionless",
    ),
    FitParameter(
        pid="GU__APISEC_k",
        start_value=0.55,
        lower_bound=1e-3,
        upper_bound=10,
        unit="l/min",
    ),
]

#: the absorption in the small intestine: the fraction absorbed is
#: `APIABS_k/(APIABS_k + SITRANS_k)`, the small intestinal transit time is
#: between 1 and 8 hr
parameters_pk_absorption: list[FitParameter] = [
    FitParameter(
        pid="GU__APIABS_k",
        start_value=0.0139,
        lower_bound=1e-4,
        upper_bound=1,
        unit="1/min",
    ),
    FitParameter(
        pid="GU__SITRANS_k",
        start_value=1 / (3.5 * 60),
        lower_bound=1 / (8 * 60),
        upper_bound=1 / 60,
        unit="1/min",
    ),
    FitParameter(
        pid="GU__Ka_dis_api",
        start_value=1.0,
        lower_bound=0.05,
        upper_bound=10,
        unit="1/hr",
    ),
    FitParameter(
        pid="GU__Ka_sol_api",
        start_value=2.0,
        lower_bound=0.1,
        upper_bound=20,
        unit="1/hr",
    ),
    FitParameter(
        pid="GU__PODOSE_50",
        start_value=50,
        lower_bound=1,
        upper_bound=500,
        unit="mg",
    ),
]

#: the metabolites: their renal excretion relative to the GFR, the biliary
#: excretion and the sulfation of M2 to M1 (Raghavan2009 urine and feces)
parameters_pk_metabolites: list[FitParameter] = [
    FitParameter(
        pid="KI__M1EX_f",
        start_value=0.21,
        lower_bound=0.01,
        upper_bound=10,
        unit="dimensionless",
    ),
    FitParameter(
        pid="KI__M7EX_f",
        start_value=0.064,
        lower_bound=0.01,
        upper_bound=10,
        unit="dimensionless",
    ),
    FitParameter(
        pid="LI__MXEXBI_k",
        start_value=0.0107,
        lower_bound=1e-4,
        upper_bound=1,
        unit="1/min",
    ),
    FitParameter(
        pid="LI__M22M1_k",
        start_value=0.002,
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

#: the Emax models of the clotting times on the total concentration of
#: apixaban, the half-maximal concentrations are total concentrations
parameters_pd_clotting: list[FitParameter] = [
    FitParameter(
        pid=f"Emax_{sid}",
        start_value=emax,
        lower_bound=lb,
        upper_bound=ub,
        unit="dimensionless",
    )
    for sid, emax, lb, ub in [
        ("INR", 1.04, 0.1, 10),
        ("PT", 1.66, 0.1, 10),
        ("mPT", 2.02, 0.1, 10),
        ("aPTT", 0.58, 0.05, 5),
    ]
] + [
    FitParameter(
        pid=f"EC50_api_{sid}",
        start_value=ec50,
        lower_bound=lb,
        upper_bound=1e-2,
        unit="mM",
    )
    for sid, ec50, lb in [
        ("INR", 1.48e-3, 1e-4),
        ("PT", 1.41e-3, 1e-4),
        ("mPT", 4.27e-4, 1e-5),
        ("aPTT", 1.17e-3, 1e-4),
    ]
]

#: the anti-factor Xa activity, linear in the total concentration of apixaban
parameters_pd_antixa: list[FitParameter] = [
    FitParameter(
        pid="antiXa_slope",
        start_value=5341,
        lower_bound=500,
        upper_bound=5e4,
        unit="1/ml/mM",  # IU/ml per mM, the IU are counts in the model
    ),
    FitParameter(
        pid="antiXa_gram_slope",
        start_value=3.398e5,
        lower_bound=2e5,
        upper_bound=1e6,
        unit="ng/ml/mM",
    ),
]

#: the pharmacodynamics, fitted on the adopted values of the pharmacokinetics
parameters_pd: list[FitParameter] = parameters_pd_clotting + parameters_pd_antixa
