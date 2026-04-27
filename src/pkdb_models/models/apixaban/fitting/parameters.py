"""FitParameters."""

from sbmlsim.fit import FitParameter


parameters_pharmacokinetics = [
    # # tissue distribution
    # FitParameter(
    #     pid="ftissue_api",
    #     lower_bound=0.05,
    #     start_value=0.15984968256016194,
    #     upper_bound=10,
    #     unit="l/min",
    # ),
    # FitParameter(
    #     pid="Kp_api",
    #     lower_bound=0.1,
    #     start_value=0.75,
    #     upper_bound=2.0,
    #     unit="dimensionless",
    # ), # Xu2024
    #
    # gut absorption
    # F_api_abs
    # FitParameter(
    #     pid="GU__Ka_dis_api",
    #     lower_bound=0.1,
    #     start_value=0.15,
    #     upper_bound=0.9,
    #     unit="1/hr",
    # ),
    # FitParameter(
    #     pid="GU__Ksol_dis_api",
    #     lower_bound=0.1,
    #     start_value=0.15,
    #     upper_bound=0.9,
    #     unit="1/hr",
    # ),
    # FitParameter(
    #     pid="GU__APIABS_k",
    #     lower_bound=1E-1,
    #     start_value=0.17163083053357975,
    #     upper_bound=1.5,
    #     unit="1/min",
    # ),
    # FitParameter(
    #     pid="GU__APIABS_Vmax",
    #     lower_bound=1E-1,
    #     start_value=0.3668065430195214,
    #     upper_bound=2.0,
    #     unit="mmole/min",
    # ),
    FitParameter(
        pid="GU__APIABS_50",
        lower_bound=20,
        start_value=25,
        upper_bound=40,
        unit="mg",
    ),
    # FitParameter(
    #     pid="GU__MXEXC_k",
    #     lower_bound=1E-6,
    #     start_value=1E-4,
    #     upper_bound=1E-2,
    #     unit="1/min",
    # ),
    #
    # # liver metabolism
    # FitParameter(
    #     pid="LI__API2M2_k",
    #     lower_bound=1E-2/4,
    #     start_value=19.4/227/4,
    #     upper_bound=1.5E-0/4,
    #     unit="1/min", # appr. 4 times lower than M7
    # ),
    # FitParameter(
    #     pid="LI__API2M7_k",
    #     lower_bound=1E-3,
    #     start_value=19.4/227,
    #     upper_bound=1.5E-0,
    #     unit="1/min", # Vmax = 19.4 or 5.1 pmol/min/pmol, Km = 227 or 106.8 uM Wang2010
    # ),
    # FitParameter(
    #     pid="LI__M22M1_Vmax", # "LI__M22M1_k"
    #     lower_bound=1E-3,
    #     start_value=1E-2,
    #     upper_bound=1E-1,
    #     unit="mmole/min", # assumes as M2
    # ),
    # FitParameter(
    #     pid="LI__M22M1_Km",
    #     lower_bound=100/ 5,
    #     start_value=150/5,
    #     upper_bound=200 / 5,
    #     unit="mmole",
    # ),
    # FitParameter(
    #     pid="LI__MXEXBI_k",
    #     lower_bound=1E-3,
    #     start_value=1E-2,
    #     upper_bound=1E-1,
    #     unit="1/min",
    # ),
    #
    #
    # # # kidney excretion
    # FitParameter(
    #     pid="KI__APIEX_k",
    #     lower_bound=1E-3,
    #     start_value=0.2268201772171981,
    #     upper_bound=1E2,
    #     unit="1/min",
    # ),
    # FitParameter(
    #     pid="KI__M1EX_k",
    #     lower_bound=1E-3,
    #     start_value=0.1,
    #     upper_bound=1E0,
    #     unit="1/min",
    # ),
    # FitParameter(
    #     pid="KI__M7EX_k",
    #     lower_bound=1E-3,
    #     start_value=0.1,
    #     upper_bound=1E2,
    #     unit="1/min",
    # ),
]

parameters_food = [
    FitParameter(
        pid="GU__f_absorption",
        lower_bound=0.1,
        start_value=1,
        upper_bound=1.5,
        unit="dimensionless",
    ),
]

parameters_inr = [
    # INR
    FitParameter(
        pid="Emax_INR",
        lower_bound=0.1,
        start_value=1,
        upper_bound=10,
        unit="dimensionless",
    ),
    FitParameter(
        pid="EC50_api_INR",
        lower_bound=1E-4,
        start_value=1E-2,
        upper_bound=1E-3,
        unit="mM",
    ),
]
parameters_mpt = [
    # mPT
    FitParameter(
        pid="Emax_mPT",
        lower_bound=0.1,
        start_value=1,
        upper_bound=10,
        unit="dimensionless",
    ),
    FitParameter(
        pid="EC50_api_mPT",
        lower_bound=1E-5,
        start_value=0.00034,
        upper_bound=1E-4,
        unit="mM",
    ),
    # PT
    FitParameter(
        pid="Emax_PT",
        lower_bound=1,
        start_value=25,
        upper_bound=50,
        unit="dimensionless",
    ),
    FitParameter(
        pid="EC50_api_PT",
        lower_bound=1E-4,
        start_value=5E-4,
        upper_bound=1E-3,
        unit="mM",
    ),
]
parameters_aptt = [
    # aPTT
    FitParameter(
        pid="Emax_aPTT",
        lower_bound=0.1,
        start_value=1,
        upper_bound=10,
        unit="dimensionless",
    ),
    FitParameter(
        pid="EC50_api_aPTT",
        lower_bound=1E-4,
        start_value=1E-2,
        upper_bound=1E-3,
        unit="mM",
    ),
]

parameters_xa = [
    # Xa
    FitParameter(
        pid="Emax_antiXa",
        lower_bound=1E4,
        start_value=2.5E4,
        upper_bound=5E4,
        unit="IU_per_ml_mM",
    ),
    FitParameter(
        pid="Emax_antiXa_gram",
        lower_bound=2E6,
        start_value=2.5E6,
        upper_bound=3E6,
        unit="ng_per_ml_mM",
    ),
]
parameters_pharmacodynamics = parameters_inr + parameters_mpt + parameters_aptt + parameters_xa
parameters_all = parameters_pharmacokinetics + parameters_pharmacodynamics