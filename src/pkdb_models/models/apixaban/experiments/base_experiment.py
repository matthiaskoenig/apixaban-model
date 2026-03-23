"""
Reusable functionality for multiple simulation experiments.
"""
import pandas as pd
from collections import namedtuple
from typing import Dict
from pkdb_models.models.apixaban import MODEL_PATH
from sbmlsim.experiment import SimulationExperiment
from sbmlsim.model import AbstractModel
from sbmlsim.task import Task

from pkdb_models.models.apixaban.apixaban_pk import calculate_apixaban_pk, calculate_apixaban_pd

# Constants for conversion
MolecularWeights = namedtuple("MolecularWeights", "api m1 m2 m7 riv")


class ApixabanSimulationExperiment(SimulationExperiment):
    """Base class for all SimulationExperiments."""

    font = {"weight": "bold", "size": 22}
    scan_font = {"weight": "bold", "size": 15}
    tick_font_size = 15
    legend_font_size = 9
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

    labels: Dict[str, str] = {
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

        "GU__APIEXC": "GU__APIEXC",

        "INR": "INR",
        "INR_change": "INR change",
        "INR_ratio": "INR ratio",
        "INR_relchange": "INR relative change",

        "PT": "PT",  # "prothrombin time",
        "PT_change": "PT change", # "prothrombin time change",
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

        "Xa_inhibition": "Xa inhibition",
        "antiXa_activity": "anti-FXa activity",
        "antiXa_activity_gram": "anti-FXa activity",
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

    units: Dict[str, str] = {
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

        "GU__APIEXC": "mmole/min",

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

        "Xa_inhibition": "dimensionless",
        "antiXa_activity": "IU/ml",
        "antiXa_activity_gram": "ng/ml"
    }

    # ----------- Multiple dosing -----
    admin_colors = {
        "single": "black",
        "multiple": "tab:olive"
    }

    # ----------- Fasting/food -----
    # food changes the fraction absorbed
    fasting_map = {  # GU__F_api_abs
        "not reported": 0.66,  # assuming fasted state if nothing is reported
        "fasted": 0.66, # Frost2021
        "fed": 1.0,
    }
    fasting_colors = {
        "fasted": "black",
        "fed": "tab:purple",
    }

    # ----------- Renal map --------------
    renal_map = {
        "Normal renal function": 101.0 / 101.0,  # 1.0,
        "Mild renal impairment": 50.0 / 101.0,  # 0.5
        "Moderate renal impairment": 35.0 / 101.0,  # 0.35
        "Severe renal impairment": 20.0 / 101.0,  # 0.20
        "End stage renal impairment": 10.5 / 101.0,  # 0.1
    }
    renal_colors = {
        "Normal renal function": "black",
        "Mild renal impairment": "#66c2a4",
        "Moderate renal impairment": "#2ca25f",
        "Severe renal impairment": "#006d2c",
        "End stage renal impairment": "#006d5e"
    }

    # ----------- Cirrhosis map --------------
    cirrhosis_map = {
        "Control": 0,
        "Mild cirrhosis": 0.3994897959183674,  # CPT A
        "Moderate cirrhosis": 0.6979591836734694,  # CPT B
        "Severe cirrhosis": 0.8127551020408164,  # CPT C
    }
    cirrhosis_colors = {
        "Control": "black",
        "Mild cirrhosis": "#74a9cf",  # CPT A
        "Moderate cirrhosis": "#2b8cbe",  # CPT B
        "Severe cirrhosis": "#045a8d",  # CPT C
    }

    def models(self) -> Dict[str, AbstractModel]:
        Q_ = self.Q_
        return {
            "model": AbstractModel(
                source=MODEL_PATH,
                language_type=AbstractModel.LanguageType.SBML,
                changes={},
            )
        }

    @staticmethod
    def _default_changes(Q_):
        """Default changes to simulations."""

        changes = {
            # pharmacokinetics
            #         >>> !Optimal parameter 'ftissue_api' within 5% of upper bound! <<<
            #         >>> !Optimal parameter 'GU__APIABS_k' within 5% of upper bound! <<<
                'ftissue_api': Q_(9.999362175489635, 'l/min'),  # [0.01 - 10]
                'Kp_api': Q_(0.033548549714271736, 'dimensionless'),  # [0.01 - 1]
                'GU__APIABS_k': Q_(0.09999949917572021, '1/min'),  # [0.001 - 0.1]
                'LI__API2M2_k': Q_(0.01570094528592168, '1/min'),  # [0.001 - 100.0]
                'LI__API2M7_k': Q_(0.020189792087538537, '1/min'),  # [0.001 - 100.0]
                'LI__M22M1_k': Q_(0.11061496092925446, '1/min'),  # [0.001 - 100.0]
                'KI__APIEX_k': Q_(0.044556517937263916, '1/min'),  # [0.001 - 100.0]

            # pharmacodynamics
            'Emax_INR': Q_(1.034912223511749, 'dimensionless'),  # [0.1 - 10]
            'EC50_api_INR': Q_(0.0011792528732025547, 'mM'),  # [1e-07 - 0.01]
            'Emax_mPT': Q_(1.9946311340457776, 'dimensionless'),  # [0.1 - 10]
            'EC50_api_mPT': Q_(0.00032191356203984284, 'mM'),  # [1e-07 - 0.01]
            'Emax_aPTT': Q_(0.4606822559153521, 'dimensionless'),  # [0.1 - 10]
            'EC50_api_aPTT': Q_(0.0005858154549784874, 'mM'),  # [1e-07 - 0.01]
            'Emax_Xa': Q_(4.581056537417629, 'per_mM'),  # [1e-06 - 1000000.0]
            'Emax_antiXa': Q_(6332.859524334975, 'IU_per_ml_mM'),  # [1e-06 - 1000000.0]
            'Emax_antiXa_gram': Q_(452775.1008926358, 'ng_per_ml_mM'),  # [1e-06 - 1000000.0]

        }

        return changes

    def default_changes(self: SimulationExperiment) -> Dict:
        """Default changes to simulations."""
        return ApixabanSimulationExperiment._default_changes(Q_=self.Q_)

    def tasks(self) -> Dict[str, Task]:
        if self.simulations():
            return {
                f"task_{key}": Task(model="model", simulation=key)
                for key in self.simulations()
            }
        return {}

    def data(self) -> Dict:
        self.add_selections_data(
            selections=[
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

                "GU__APIEXC",

                # cases
                'KI__f_renal_function',
                'f_cirrhosis',

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

                "Xa_inhibition",
                "antiXa_activity",
                "antiXa_activity_gram",

                "PODOSE_api",
                "GU__F_api_abs",
                "BW",
            ]
        )
        return {}

    @property
    def Mr(self):
        return MolecularWeights(
            api=self.Q_(459.5, "g/mole"),
            m1=self.Q_(525.5, "g/mole"),
            m2=self.Q_(445.5, "g/mole"),
            m7=self.Q_(459.5 + 16, "g/mole"),
            riv=self.Q_(435.88, "g/mole"),
        )

    # --- Pharmacokinetic parameters ---
    pk_labels = {
        "auc": "AUCend",
        "aucinf": "AUC",
        "aucend_12": "AUCend 12h",
        "aucend_24": "AUCend 24h",
        "aucend_48": "AUCend 48h",
        "aucend_72": "AUCend 72h",
        "aucend_96": "AUCend 96h",
        "cl": "Total clearance",
        "cl_renal": "Renal clearance",
        "cl_hepatic": "Hepatic clearance",
        "cmax": "Cmax",
        "tmax": "Max. time",
        "thalf": "Half-life",
        "kel": "kel",
        "vd": "vd",
        # "inrmax": "INRmax",
        # "ptmax": "PTmax",
        # "apttmax": "aPTTmax",
    }

    pk_units = {
        "auc": "µmole/l*hr",
        "aucinf": "µmole/l*hr",
        "aucend_12": "µmole/l*hr",
        "aucend_24": "µmole/l*hr",
        "aucend_48": "µmole/l*hr",
        "aucend_72": "µmole/l*hr",
        "aucend_96": "µmole/l*hr",
        "cl": "ml/min",
        "cl_renal": "ml/min",
        "cl_hepatic": "ml/min",
        "cmax": "µmole/l",
        "tmax": "hr",
        "thalf": "hr",
        "kel": "1/hr",
        "vd": "l",
        # "inrmax": "dimensionless",
        # "ptmax": "sec",
        # "apttmax": "sec",
    }

    def calculate_apixaban_pk(self, scans: list = []) -> Dict[str, pd.DataFrame]:
       """Calculate pk parameters for simulations (scans)"""
       pk_dfs = {}
       if scans:
           for sim_key in scans:
               xres = self.results[f"task_{sim_key}"]
               df = calculate_apixaban_pk(experiment=self, xres=xres)
               pk_dfs[sim_key] = df
       else:
           for sim_key in self._simulations.keys():
               xres = self.results[f"task_{sim_key}"]
               df = calculate_apixaban_pk(experiment=self, xres=xres)
               pk_dfs[sim_key] = df
       return pk_dfs

    def calculate_apixaban_pd(self, scans: list = []) -> Dict[str, pd.DataFrame]:
       """Calculate pd parameters for simulations (scans)"""
       pd_dfs = {}
       if scans:
           for sim_key in scans:
               xres = self.results[f"task_{sim_key}"]
               df = calculate_apixaban_pd(experiment=self, xres=xres)
               pd_dfs[sim_key] = df
       else:
           for sim_key in self._simulations.keys():
               xres = self.results[f"task_{sim_key}"]
               df = calculate_apixaban_pd(experiment=self, xres=xres)
               pd_dfs[sim_key] = df
       return pd_dfs