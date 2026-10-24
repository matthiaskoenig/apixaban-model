"""Base class of the apixaban simulation experiments."""

from collections.abc import Mapping, Sequence
from types import MappingProxyType
from typing import ClassVar, NamedTuple, override

import pandas as pd
from pkpdsim.experiment import PKPDSimulationExperiment
from pkpdsim.impairment import RENAL_COLORS_END_STAGE, RENAL_FUNCTION_GFR
from sbmlsim import Q
from sbmlsim.units import Quantity

from pkdb_models.models.apixaban import MODEL
from pkdb_models.models.apixaban.apixaban_pk import (
    calculate_apixaban_pd,
    calculate_apixaban_pk,
)


class MolecularWeights(NamedTuple):
    """Molecular weights for the conversion of the data."""

    api: Quantity
    m1: Quantity
    m2: Quantity
    m7: Quantity
    riv: Quantity


class ApixabanSimulationExperiment(PKPDSimulationExperiment):
    """Base class of the apixaban simulation experiments."""

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
        "[Cve_api]",
        "[Cve_m1]",
        "[Cve_m7]",
        "Aurine_api",
        "Aurine_m1",
        "Aurine_m7",
        "Afeces_api",
        "Afeces_m1",
        "Afeces_m2",
        "Afeces_m7",
        "GU__APIABS",
        "GU__APISEC",
        "GU__APIEXC",
        "KI__GFR",
        # cases
        "KI__f_renal_function",
        "f_cirrhosis",
        "LI__f_cyp3a4",
        "GU__f_pgp",
        # pharmacodynamics
        "INR",
        "INR_change",
        "INR_ratio",
        "INR_relchange",
        "PT",
        "PT_change",
        "PT_ratio",
        "PT_relchange",
        "mPT",
        "mPT_change",
        "mPT_ratio",
        "mPT_relchange",
        "aPTT",
        "aPTT_change",
        "aPTT_ratio",
        "aPTT_relchange",
        "antiXa_activity",
        "antiXa_activity_gram",
        "PODOSE_api",
        "SOLDOSE_api",
        "GU__F_api_abs",
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
        "[Cve_api]": label_api_plasma,
        "[Cve_m1]": label_m1_plasma,
        "[Cve_m7]": label_m7_plasma,
        "Aurine_api": label_api_urine,
        "Aurine_m1": label_m1_urine,
        "Aurine_m7": label_m7_urine,
        "Afeces_api": label_api_feces,
        "Afeces_m1": label_m1_feces,
        "Afeces_m2": label_m2_feces,
        "Afeces_m7": label_m7_feces,
        "GU__APIABS": "apixaban\nabsorption",
        "GU__APISEC": "apixaban intestinal\nsecretion",
        "GU__APIEXC": "apixaban fecal\nexcretion",
        "KI__GFR": "GFR",
        "INR": "INR",
        "INR_change": "INR change",
        "INR_ratio": "INR ratio",
        "INR_relchange": "INR relative change",
        "PT": "PT",  # "prothrombin time",
        "PT_change": "PT change",  # "prothrombin time change",
        "PT_ratio": "PT ratio",  # "prothrombin time ratio",
        "PT_relchange": "PT relative change",
        "aPTT": "aPTT",
        "aPTT_change": "aPTT change",
        "aPTT_ratio": "aPTT ratio",
        "aPTT_relchange": "aPTT relative change",
        "mPT": "mPT",  # "modified prothrombin time",
        "mPT_change": "mPT change",  # "modified prothrombin time change",
        "mPT_ratio": "mPT ratio",  # "modified prothrombin time ratio",
        "mPT_relchange": "mPT relative change",
        "antiXa_activity": "anti-Xa (IU)",
        "antiXa_activity_gram": "anti-Xa",
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
        "[Cve_api]": unit_api,
        "[Cve_m1]": unit_m1,
        "[Cve_m7]": unit_m7,
        "Aurine_api": unit_api_urine,
        "Aurine_m1": unit_m1_urine,
        "Aurine_m7": unit_m7_urine,
        "Afeces_api": unit_api_feces,
        "Afeces_m1": unit_m1_feces,
        "Afeces_m2": unit_m2_feces,
        "Afeces_m7": unit_m7_feces,
        "GU__APIABS": "µmole/min",
        "GU__APISEC": "µmole/min",
        "GU__APIEXC": "µmole/min",
        "KI__GFR": "ml/min",
        "INR": "dimensionless",
        "INR_change": "dimensionless",
        "INR_ratio": "dimensionless",
        "INR_relchange": "%",
        "PT": "s",
        "PT_change": "s",
        "PT_ratio": "dimensionless",
        "PT_relchange": "%",
        "mPT": "s",
        "mPT_change": "s",
        "mPT_ratio": "dimensionless",
        "mPT_relchange": "%",
        "aPTT": "s",
        "aPTT_change": "s",
        "aPTT_ratio": "dimensionless",
        "aPTT_relchange": "%",
        "antiXa_activity": "1/ml",  # IU/ml, see `data_units`
        "antiXa_activity_gram": "ng/ml",
    }

    # ----------- Multiple dosing -----
    admin_colors: ClassVar[dict[str, str]] = {
        "single": "black",
        "multiple": "tab:olive",
    }

    # ----------- Fasting/food -----
    # the model has no effect of food (Frost2013: AUC +4 %, Song2016: -20 %),
    # the fasting state is part of the metadata of the fit mappings only
    fasting_colors: ClassVar[dict[str, str]] = {
        "fasted": "black",
        "fed": "tab:purple",
    }

    # ----------- Renal map --------------
    # the renal function relative to the GFR of 101 ml/min (`KI__GFR_base`)
    renal_map = RENAL_FUNCTION_GFR
    renal_colors = RENAL_COLORS_END_STAGE

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

    # molecular weights of apixaban, its metabolites and rivaroxaban
    Mr: ClassVar[MolecularWeights] = MolecularWeights(
        api=Q(459.5, "g/mole"),
        m1=Q(525.5, "g/mole"),
        m2=Q(445.5, "g/mole"),
        m7=Q(459.5 + 16, "g/mole"),
        riv=Q(435.88, "g/mole"),
    )

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
        "antixa_activitymax": "anti-FXa activity max (IU)",
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
                experiment=self, res=self.results[f"task_{key}"], across=self._across()
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
                res=self.results[f"task_{key}"], across=self._across()
            )
            for key in keys
        }

    def _across(self) -> str | None:
        """Get the dimension of the draws of the fitted parameters, `None` without."""
        return None if self.uncertainty is None else self.uncertainty.id
