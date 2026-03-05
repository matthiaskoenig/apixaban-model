"""FitParameters."""

from sbmlsim.fit import FitParameter


parameters_pharmacokinetics = [
    # tissue distribution
    FitParameter(
        pid="ftissue_api",
        lower_bound=0.01,
        start_value=0.1,
        upper_bound=10,
        unit="l/min",
    ),
    FitParameter(
        pid="Kp_api",
        lower_bound=0.01,
        start_value=0.2,
        upper_bound=1,
        unit="dimensionless",
    ),

    # gut absorption
    # F_api_abs
    # Ka_dis_api
    FitParameter(
        pid="GU__APIABS_k",
        lower_bound=1E-3,
        start_value=0.05,
        upper_bound=0.1,
        unit="1/min",
    ),
    # FitParameter(
    #     pid="GU__MXEXC_k",
    #     lower_bound=1E-6,
    #     start_value=1E-4,
    #     upper_bound=1E-2,
    #     unit="1/min",
    # ),


    # liver metabolism
    FitParameter(
        pid="LI__API2M2_k",
        lower_bound=1E-3,
        start_value=0.1,
        upper_bound=1E2,
        unit="1/min",
    ),
    FitParameter(
        pid="LI__API2M7_k",
        lower_bound=1E-3,
        start_value=0.1,
        upper_bound=1E2,
        unit="1/min",
    ),
    FitParameter(
        pid="LI__M22M1_k",
        lower_bound=1E-3,
        start_value=0.1,
        upper_bound=1E2,
        unit="1/min",
    ),
    # FitParameter(
    #     pid="LI__MXEXBI_k",
    #     lower_bound=1E-7,
    #     start_value=1E-5,
    #     upper_bound=1E-3,
    #     unit="1/min",
    # ),


    # kidney excretion
    FitParameter(
        pid="KI__APIEX_k",
        lower_bound=1E-3,
        start_value=0.1,
        upper_bound=1E2,
        unit="1/min",
    ),
    # FitParameter(
    #     pid="KI__M1EX_k",
    #     lower_bound=1E-3,
    #     start_value=0.1,
    #     upper_bound=1E2,
    #     unit="1/min",
    # ),
    # FitParameter(
    #     pid="KI__M7IEX_k",
    #     lower_bound=1E-3,
    #     start_value=0.1,
    #     upper_bound=1E2,
    #     unit="1/min",
    # ),
]

parameters_pharmacodynamics = [

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
        lower_bound=1E-7,
        start_value=0.00034,
        upper_bound=1E-2,
        unit="mM",
    ),
    # PT
    # FitParameter(
    #     pid="Emax_PT",
    #     lower_bound=0.1,
    #     start_value=1,
    #     upper_bound=10,
    #     unit="dimensionless",
    # ),
    # FitParameter(
    #     pid="EC50_api_PT",
    #     lower_bound=1E-7,
    #     start_value=0.00034,
    #     upper_bound=1E-2,
    #     unit="mM",
    # ),
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
        lower_bound=1E-7,
        start_value=0.00034,
        upper_bound=1E-2,
        unit="mM",
    ),
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
        lower_bound=1E-7,
        start_value=0.00034,
        upper_bound=1E-2,
        unit="mM",
    ),
    # Xa
    # FitParameter(
    #     pid="Emax_Xa",
    #     lower_bound=0.5,
    #     start_value=0.7,
    #     upper_bound=1.0,
    #     unit="IU_per_ml",
    # ),
    # FitParameter(
    #     pid="EC50_api_Xa",
    #     lower_bound=1E-7,
    #     start_value=0.00034,
    #     upper_bound=1E-2,
    #     unit="mM",
    # ),
    # FitParameter(
    #     pid="Emax_Xa_gram",
    #     lower_bound=0.5,
    #     start_value=0.7,
    #     upper_bound=1.0,
    #     unit="ng_per_ml",
    # ),
    # FitParameter(
    #     pid="EC50_api_Xa_gram",
    #     lower_bound=1E-7,
    #     start_value=0.00034,
    #     upper_bound=1E-2,
    #     unit="mM",
    # ),
]


parameters_all = parameters_pharmacokinetics + parameters_pharmacodynamics