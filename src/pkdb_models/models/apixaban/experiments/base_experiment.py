"""Base class of the apixaban simulation experiments."""

from collections.abc import Mapping, Sequence
from types import MappingProxyType
from typing import ClassVar, override

import pandas as pd
from pkpdsim import impairment
from pkpdsim.pbpk import REFERENCE_GFR, PBPKSimulationExperiment, molecular_weights
from sbmlsim.units import Quantity

from pkdb_models.models.apixaban import MODEL
from pkdb_models.models.apixaban.apixaban_pk import (
    calculate_apixaban_pd,
    calculate_apixaban_pk,
)
from pkdb_models.models.apixaban.models.definition import DEFINITION


class ApixabanSimulationExperiment(PBPKSimulationExperiment):
    """Base class of the apixaban simulation experiments.

    The plasma of the studies is drawn from an arm vein (`Carm_<id>`), which
    the coagulation model reads as well (`COAG__<id>`). The food effect is the
    slower gastric emptying of the fed state of the library (`FED`), which
    the fed arms set. The coadministered drugs are factors of the activity of
    CYP3A4 in the liver (`LI__f_cyp3a4`) and of the efflux of the intestine
    (`GU__f_abcb1`, P-gp and BCRP lumped). The renal function is
    `f_renal_function` (a measured creatinine clearance is `renal_function`,
    the classes of renal impairment `renal_map`), cirrhosis the Child-Pugh
    severity `CP_severity` (`cirrhosis_map`).
    """

    pkpd_model = MODEL
    #: the model counts the international units (IU) of the anti-factor Xa
    #: activity (`IU_per_ml` is `1/ml`), so an IU of the data is a count and the
    #: values stay as they are, e.g. `IU/ml` is `IU_apixaban_antixa/ml`, `1/ml`
    data_units: ClassVar[Mapping[str, str]] = MappingProxyType(
        {"IU": "IU_apixaban_antixa = count"}
    )
    #: the tables whose time is not reported (`NR`), the scatter plots against
    #: the concentration: (study, figure or table)
    tables_without_time: ClassVar[frozenset[tuple[str, str]]] = frozenset(
        {
            ("Chang2016", "Fig4"),
            ("Frost2013", "Fig4"),
            ("Frost2015", "Fig4"),
            ("Frost2021", "Fig3"),
            ("Frost2021a", "Fig2a"),
            ("Upreti2013", "Fig4"),
            ("Wang2016", "Fig3"),
        }
    )
    selections = (
        "time",
        # dosing
        "PODOSE_api",
        "SOLDOSE_api",
        # arm vein plasma
        "Carm_api",
        "Carm_api_m1",
        "Carm_api_m7",
        # urine
        "Aurine_api",
        "Aurine_api_m1",
        "Aurine_api_m7",
        # feces
        "Afeces_api",
        "Afeces_api_m1",
        "Afeces_api_m2",
        "Afeces_api_m7",
        # intestine: the summed fluxes of the absorption, the efflux into the
        # lumen and the loss to the feces
        "Rabs_api",
        "Reff_api",
        "Rfeces_api",
        # the gross absorbed fraction of the oral dose
        "Fa_api",
        # kidney
        "GFR",  # glomerular filtration rate
        # cases
        "f_renal_function",
        "CP_severity",
        "LI__f_cyp3a4",
        "GU__f_abcb1",
        # pharmacodynamics
        "COAG__INR",
        "COAG__INR_change",
        "COAG__INR_ratio",
        "COAG__INR_relchange",
        "COAG__PT",
        "COAG__PT_change",
        "COAG__PT_ratio",
        "COAG__PT_relchange",
        "COAG__mPT",
        "COAG__mPT_change",
        "COAG__mPT_ratio",
        "COAG__mPT_relchange",
        "COAG__aPTT",
        "COAG__aPTT_change",
        "COAG__aPTT_ratio",
        "COAG__aPTT_relchange",
        "COAG__antiXa_activity",
        "COAG__antiXa_activity_gram",
        # covariates
        "BW",
        "BSA",
    )

    font: ClassVar[dict[str, str | int]] = {"weight": "bold", "size": 22}
    scan_font: ClassVar[dict[str, str | int]] = {"weight": "bold", "size": 15}
    tick_font_size = 15
    suptitle_font_size = 25

    panel_width = 7.7
    panel_height = 5.7

    # labels
    label_time = "time"
    label_api = "apixaban"
    label_m1 = "M1"
    label_m2 = "M2"
    label_m7 = "M7"

    label_api_plasma = label_api + " plasma"
    label_m1_plasma = label_m1 + " plasma"
    label_m2_plasma = label_m2 + " plasma"
    label_m7_plasma = label_m7 + " plasma"

    label_api_urine = label_api + " urine"
    label_m1_urine = label_m1 + " urine"
    label_m7_urine = label_m7 + " urine"

    label_api_feces = label_api + " feces"
    label_m1_feces = label_m1 + " feces"
    label_m2_feces = label_m2 + " feces"
    label_m7_feces = label_m7 + " feces"

    labels: ClassVar[Mapping[str, str]] = {
        "time": "time",
        "Carm_api": label_api_plasma,
        "Carm_api_m1": label_m1_plasma,
        "Carm_api_m7": label_m7_plasma,
        "Aurine_api": label_api_urine,
        "Aurine_api_m1": label_m1_urine,
        "Aurine_api_m7": label_m7_urine,
        "Afeces_api": label_api_feces,
        "Afeces_api_m1": label_m1_feces,
        "Afeces_api_m2": label_m2_feces,
        "Afeces_api_m7": label_m7_feces,
        "Rabs_api": label_api + " absorption",
        "Reff_api": label_api + " efflux",
        "Rfeces_api": label_api + " to feces",
        # the gross absorbed fraction of the oral dose
        "Fa_api": label_api + " absorbed fraction",
        "GFR": "GFR",
        "COAG__INR": "INR",
        "COAG__INR_change": "INR change",
        "COAG__INR_ratio": "INR ratio",
        "COAG__INR_relchange": "INR relative change",
        "COAG__PT": "PT",  # "prothrombin time",
        "COAG__PT_change": "PT change",  # "prothrombin time change",
        "COAG__PT_ratio": "PT ratio",  # "prothrombin time ratio",
        "COAG__PT_relchange": "PT relative change",
        "COAG__aPTT": "aPTT",
        "COAG__aPTT_change": "aPTT change",
        "COAG__aPTT_ratio": "aPTT ratio",
        "COAG__aPTT_relchange": "aPTT relative change",
        "COAG__mPT": "mPT",  # "modified prothrombin time",
        "COAG__mPT_change": "mPT change",  # "modified prothrombin time change",
        "COAG__mPT_ratio": "mPT ratio",  # "modified prothrombin time ratio",
        "COAG__mPT_relchange": "mPT relative change",
        "COAG__antiXa_activity": "anti-Xa (IU)",
        "COAG__antiXa_activity_gram": "anti-Xa",
    }

    # units
    unit_time = "hr"
    unit_metabolite = "µM"
    unit_metabolite_urine = "µmole"
    unit_metabolite_feces = "µmole"

    unit_api = unit_metabolite
    unit_m1 = unit_metabolite
    unit_m2 = unit_metabolite
    unit_m7 = unit_metabolite

    unit_api_urine = unit_metabolite_urine
    unit_m1_urine = unit_metabolite_urine
    unit_m7_urine = unit_metabolite_urine

    unit_api_feces = unit_metabolite_feces
    unit_m1_feces = unit_metabolite_feces
    unit_m2_feces = unit_metabolite_feces
    unit_m7_feces = unit_metabolite_feces

    units: ClassVar[Mapping[str, str]] = {
        "time": unit_time,
        "Carm_api": unit_api,
        "Carm_api_m1": unit_m1,
        "Carm_api_m7": unit_m7,
        "Aurine_api": unit_api_urine,
        "Aurine_api_m1": unit_m1_urine,
        "Aurine_api_m7": unit_m7_urine,
        "Afeces_api": unit_api_feces,
        "Afeces_api_m1": unit_m1_feces,
        "Afeces_api_m2": unit_m2_feces,
        "Afeces_api_m7": unit_m7_feces,
        "Rabs_api": "µmole/min",
        "Reff_api": "µmole/min",
        "Rfeces_api": "µmole/min",
        "Fa_api": "dimensionless",
        "GFR": "ml/min",
        "COAG__INR": "dimensionless",
        "COAG__INR_change": "dimensionless",
        "COAG__INR_ratio": "dimensionless",
        "COAG__INR_relchange": "%",
        "COAG__PT": "s",
        "COAG__PT_change": "s",
        "COAG__PT_ratio": "dimensionless",
        "COAG__PT_relchange": "%",
        "COAG__mPT": "s",
        "COAG__mPT_change": "s",
        "COAG__mPT_ratio": "dimensionless",
        "COAG__mPT_relchange": "%",
        "COAG__aPTT": "s",
        "COAG__aPTT_change": "s",
        "COAG__aPTT_ratio": "dimensionless",
        "COAG__aPTT_relchange": "%",
        "COAG__antiXa_activity": "1/ml",  # IU/ml, see `data_units`
        "COAG__antiXa_activity_gram": "ng/ml",
    }

    # ----------- Multiple dosing -----
    admin_colors: ClassVar[dict[str, str]] = {
        "single": "black",
        "multiple": "tab:olive",
    }

    # ----------- Fasting/food -----
    # the food effect is the slower gastric emptying of the fed state of the
    # library (`FED`), which the fed arms set; the measured effects of food
    # (Frost2013: AUC +4 %, Song2016: -20 %) are validation data of the
    # limitations (`fitting/mapping_collections.py`)
    fasting_colors: ClassVar[dict[str, str]] = {
        "fasted": "black",
        "fed": "tab:purple",
    }

    @override
    def initialize(self) -> None:
        """Initialize the experiment and label an axis in percent with `%`.

        sbmlsim writes the unit of an axis in the short form of pint, which is
        `percent` for `%`; the relative changes of the clotting times are in
        `%`.
        """
        super().initialize()
        # A workaround of sbmlsim: its unit registry defines
        # `percent = 0.01*count` without a symbol, so an axis in `%` reads
        # "[percent]" (in every model). Remove it once sbmlsim gives percent
        # the symbol `%` (`percent = 0.01*count = %`).
        for figure in self._figures.values():
            for plot in figure.get_plots():
                for axis in (plot.xaxis, plot.yaxis):
                    if axis is not None and axis.unit == "%":
                        axis.name = axis.name.replace("[percent]", "[%]")

    # ----------- Renal function --------------
    #: the GFR of the classes of renal impairment by the limits of their GFR
    #: and of the end stage renal disease [ml/min]
    #: (`impairment.RENAL_FUNCTION_GFR` relative to `REFERENCE_GFR`, 101 ml/min)
    renal_class_gfr: ClassVar[Mapping[str, float]] = MappingProxyType(
        {key: REFERENCE_GFR * v for key, v in impairment.RENAL_FUNCTION_GFR.items()}
    )

    @override
    def load_dataframe(
        self,
        fig_id: str,
        study: str | None = None,
        *,
        na_values: Sequence[str] | Mapping[str, Sequence[str]] | None = None,
    ) -> pd.DataFrame:
        """Load the digitized data of a figure or table of a study.

        The time and the time unit of a table of `tables_without_time` are not
        reported (`NR`), they are read as missing values.

        Args:
            fig_id: the id of the figure or table in the study, e.g. `Fig1`.
            study: the study, the id of the experiment by default.
            na_values: additional strings of missing values, for every column or
                by column, see `pandas.read_csv`.

        Raises:
            ValueError: if the experiment has no `data_path` or a definition of
                `data_units` is refused.
        """
        table = (self.sid if study is None else study, fig_id)
        if na_values is None and table in self.tables_without_time:
            na_values = {"time": ["NR"], "time_unit": ["NR"]}
        return super().load_dataframe(fig_id, study, na_values=na_values)

    #: the molecular weights of apixaban and its metabolites, by substance
    #: (`api`, `api_m1`, ...), those of the definition
    Mr: ClassVar[Mapping[str, Quantity]] = molecular_weights(DEFINITION)

    # --- Pharmacokinetic parameters ---
    # keys are the parameters of the non-compartmental analysis of pkpdutils
    # and the additional parameters of `apixaban_pk`
    pk_labels: ClassVar[Mapping[str, str]] = {
        "auc_last": "AUCend",
        "auc_inf_obs": "AUC",
        "aucend_12": "AUCend 12h",
        "aucend_24": "AUCend 24h",
        "aucend_48": "AUCend 48h",
        "aucend_72": "AUCend 72h",
        "aucend_96": "AUCend 96h",
        "cl_f": "Apparent clearance",
        "cl_renal": "Renal clearance",
        "cmax": "Cmax",
        "tmax": "Max. time",
        "thalf": "Half-life",
        "lambda_z": "Elimination rate",
        "vz_f": "Apparent volume",
    }

    pk_units: ClassVar[Mapping[str, str]] = {
        "auc_last": "µmole/l*hr",
        "auc_inf_obs": "µmole/l*hr",
        "aucend_12": "µmole/l*hr",
        "aucend_24": "µmole/l*hr",
        "aucend_48": "µmole/l*hr",
        "aucend_72": "µmole/l*hr",
        "aucend_96": "µmole/l*hr",
        "cl_f": "ml/min",
        "cl_renal": "ml/min",
        "cmax": "µmole/l",
        "tmax": "hr",
        "thalf": "hr",
        "lambda_z": "1/hr",
        "vz_f": "l",
    }

    pd_labels: ClassVar[dict[str, str]] = {
        "inrmax": "INRmax",
        "ptmax": "PTmax",
        "apttmax": "aPTTmax",
        "inr_ratiomax": "INRmax ratio",
        "pt_ratiomax": "PTmax ratio",
        "aptt_ratiomax": "aPTTmax ratio",
        "antixa_activitymax": "anti-Xa max (IU)",
    }

    pd_units: ClassVar[dict[str, str]] = {
        "inrmax": "dimensionless",
        "ptmax": "s",
        "apttmax": "s",
        "inr_ratiomax": "dimensionless",
        "pt_ratiomax": "dimensionless",
        "aptt_ratiomax": "dimensionless",
        "antixa_activitymax": "1/ml",  # IU/ml, see `data_units`
    }

    def calculate_apixaban_pk(
        self, scans: Sequence[str] | None = None
    ) -> dict[str, pd.DataFrame]:
        """Calculate the pharmacokinetic parameters of the scans.

        Args:
            scans: keys of the simulations, all simulations by default.

        Returns:
            The parameters of every scan by simulation key, per draw of the
            fitted parameters in a run over them (`uncertainty`).
        """
        keys = scans if scans else self._simulations
        return {
            key: calculate_apixaban_pk(
                experiment=self, res=self.results[f"task_{key}"], across=self.across()
            )
            for key in keys
        }

    def calculate_apixaban_pd(
        self, scans: Sequence[str] | None = None
    ) -> dict[str, dict[str, pd.DataFrame]]:
        """Calculate the extremes of the pharmacodynamic outputs of the scans.

        Args:
            scans: keys of the simulations, all simulations by default.

        Returns:
            The tables of the outputs of every scan by simulation key, per draw
            of the fitted parameters in a run over them (`uncertainty`).
        """
        keys = scans if scans else self._simulations
        return {
            key: calculate_apixaban_pd(
                res=self.results[f"task_{key}"], across=self.across()
            )
            for key in keys
        }
