# Apixaban body model (female)

Model `apixaban_body_female`, SBML Level 3 Version 2, read from apixaban\_body\_female\_flat.xml, written by sbmlode 0.3.2.

Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model apixaban (body model)

Whole-body physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model of apixaban, built with the PBPK library pkpdsim.pbpk: the dissolution of the tablet and the incomplete absorption of apixaban in the intestine, its efflux into the intestinal lumen (P-gp, BCRP), the distribution into the tissues, the metabolism by CYP3A4 in the liver to O-demethyl apixaban (M2), hydroxy apixaban (M7) and O-demethyl apixaban sulfate (M1), the renal excretion of apixaban, M1 and M7 and the biliary excretion of the metabolites, and the anticoagulant effects (anti-factor Xa activity, INR, PT, mPT, aPTT) of the total apixaban concentration of the plasma, with the effects of impaired renal and hepatic function, of the body weight and of the interactions of CYP3A4 and P-gp.

The content of this model has been carefully created in a manual research effort.

Terms of use

Copyright © 2026 Matthias König.

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

Redistribution and use of any part of this model, with or without modification, are permitted provided that the following conditions are met:

Redistributions of this SBML file must retain the above copyright notice, this list of conditions and the following disclaimer.

Redistributions in a different form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

This model is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

## Units

| Time | Substance | Extent | Volume | Area | Length |
| --- | --- | --- | --- | --- | --- |
| min | mmol | mmol | l | m<sup>2</sup> | m |

## Compartments

| Symbol | Id | Name | Size | Unit | Constant |
| --- | --- | --- | --- | --- | :---: |
| $\mathrm{Var}_{\mathrm{pl}}$ | `Var_pl` | arterial plasma | $1$ | l | ✓ |
| $\mathrm{Var}_{\mathrm{bc}}$ | `Var_bc` | arterial blood cells | $1$ | l | ✓ |
| $\mathrm{Vve}_{\mathrm{pl}}$ | `Vve_pl` | venous plasma | $1$ | l | ✓ |
| $\mathrm{Vve}_{\mathrm{bc}}$ | `Vve_bc` | venous blood cells | $1$ | l | ✓ |
| $\mathrm{Vpo}_{\mathrm{pl}}$ | `Vpo_pl` | portal plasma | $1$ | l | ✓ |
| $\mathrm{Vpo}_{\mathrm{bc}}$ | `Vpo_bc` | portal blood cells | $1$ | l | ✓ |
| $\mathrm{Vurine}$ | `Vurine` | urine | $1$ | l | ✓ |
| $\mathrm{Vfeces}$ | `Vfeces` | feces | $1$ | l | ✓ |
| $\mathrm{Vbile}$ | `Vbile` | bile | $0.058$ | l | ✓ |
| $\mathrm{LU}_{\mathrm{\_Vpl}}$ | `LU__Vpl` | plasma lung | $1$ | l | ✓ |
| $\mathrm{LU}_{\mathrm{\_Vti}}$ | `LU__Vti` | tissue lung | $1$ | l | ✓ |
| $\mathrm{HE}_{\mathrm{\_Vpl}}$ | `HE__Vpl` | plasma heart | $1$ | l | ✓ |
| $\mathrm{HE}_{\mathrm{\_Vti}}$ | `HE__Vti` | tissue heart | $1$ | l | ✓ |
| $\mathrm{BR}_{\mathrm{\_Vpl}}$ | `BR__Vpl` | plasma brain | $1$ | l | ✓ |
| $\mathrm{BR}_{\mathrm{\_Vti}}$ | `BR__Vti` | tissue brain | $1$ | l | ✓ |
| $\mathrm{LI}_{\mathrm{\_Vpl}}$ | `LI__Vpl` | plasma liver | $1$ | l | ✓ |
| $\mathrm{LI}_{\mathrm{\_Vis}}$ | `LI__Vis` | interstitium liver | $1$ | l | ✓ |
| $\mathrm{LI}_{\mathrm{\_Vic}}$ | `LI__Vic` | intracellular space liver | $1$ | l | ✓ |
| $\mathrm{LI}_{\mathrm{\_Vti}}$ | `LI__Vti` | tissue liver | $1$ | l | ✓ |
| $\mathrm{KI}_{\mathrm{\_Vpl}}$ | `KI__Vpl` | plasma kidney | $1$ | l | ✓ |
| $\mathrm{KI}_{\mathrm{\_Vti}}$ | `KI__Vti` | tissue kidney | $1$ | l | ✓ |
| $\mathrm{ST}_{\mathrm{\_Vpl}}$ | `ST__Vpl` | plasma stomach | $1$ | l | ✓ |
| $\mathrm{ST}_{\mathrm{\_Vti}}$ | `ST__Vti` | tissue stomach | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vpl}}$ | `GU__Vpl` | plasma small intestine | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vti}}$ | `GU__Vti` | tissue small intestine | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vti\_wall}}$ | `GU__Vti_wall` | tissue without the mucosa small intestine | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vlumen\_st}}$ | `GU__Vlumen_st` | lumen stomach | $0.028$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vlumen\_du}}$ | `GU__Vlumen_du` | lumen duodenum | $0.007819$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vlumen\_jej1}}$ | `GU__Vlumen_jej1` | lumen upper jejunum | $0.01955$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vlumen\_jej2}}$ | `GU__Vlumen_jej2` | lumen lower jejunum | $0.01955$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vlumen\_ile1}}$ | `GU__Vlumen_ile1` | lumen upper ileum | $0.02904$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vlumen\_ile2}}$ | `GU__Vlumen_ile2` | lumen lower ileum | $0.02904$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vlumen\_cae}}$ | `GU__Vlumen_cae` | lumen caecum | $0.002093$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vlumen\_asc}}$ | `GU__Vlumen_asc` | lumen colon ascendens | $0.002093$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vlumen\_tra}}$ | `GU__Vlumen_tra` | lumen colon transversum | $0.002111$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vlumen\_des}}$ | `GU__Vlumen_des` | lumen colon descendens | $0.002111$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vlumen\_sig}}$ | `GU__Vlumen_sig` | lumen colon sigmoid | $0.002296$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vlumen\_rec}}$ | `GU__Vlumen_rec` | lumen rectum | $0.002296$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vmu\_du}}$ | `GU__Vmu_du` | mucosa duodenum small intestine | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vmu\_jej1}}$ | `GU__Vmu_jej1` | mucosa upper jejunum small intestine | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vmu\_jej2}}$ | `GU__Vmu_jej2` | mucosa lower jejunum small intestine | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vmu\_ile1}}$ | `GU__Vmu_ile1` | mucosa upper ileum small intestine | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vmu\_ile2}}$ | `GU__Vmu_ile2` | mucosa lower ileum small intestine | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vmu\_cae}}$ | `GU__Vmu_cae` | mucosa caecum small intestine | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vmu\_asc}}$ | `GU__Vmu_asc` | mucosa colon ascendens small intestine | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vmu\_tra}}$ | `GU__Vmu_tra` | mucosa colon transversum small intestine | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vmu\_des}}$ | `GU__Vmu_des` | mucosa colon descendens small intestine | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vmu\_sig}}$ | `GU__Vmu_sig` | mucosa colon sigmoid small intestine | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vmu\_rec}}$ | `GU__Vmu_rec` | mucosa rectum small intestine | $1$ | l | ✓ |
| $\mathrm{SP}_{\mathrm{\_Vpl}}$ | `SP__Vpl` | plasma spleen | $1$ | l | ✓ |
| $\mathrm{SP}_{\mathrm{\_Vti}}$ | `SP__Vti` | tissue spleen | $1$ | l | ✓ |
| $\mathrm{PA}_{\mathrm{\_Vpl}}$ | `PA__Vpl` | plasma pancreas | $1$ | l | ✓ |
| $\mathrm{PA}_{\mathrm{\_Vti}}$ | `PA__Vti` | tissue pancreas | $1$ | l | ✓ |
| $\mathrm{MU}_{\mathrm{\_Vpl}}$ | `MU__Vpl` | plasma muscle | $1$ | l | ✓ |
| $\mathrm{MU}_{\mathrm{\_Vti}}$ | `MU__Vti` | tissue muscle | $1$ | l | ✓ |
| $\mathrm{SK}_{\mathrm{\_Vpl}}$ | `SK__Vpl` | plasma skin | $1$ | l | ✓ |
| $\mathrm{SK}_{\mathrm{\_Vti}}$ | `SK__Vti` | tissue skin | $1$ | l | ✓ |
| $\mathrm{AD}_{\mathrm{\_Vpl}}$ | `AD__Vpl` | plasma adipose | $1$ | l | ✓ |
| $\mathrm{AD}_{\mathrm{\_Vti}}$ | `AD__Vti` | tissue adipose | $1$ | l | ✓ |
| $\mathrm{BO}_{\mathrm{\_Vpl}}$ | `BO__Vpl` | plasma bone | $1$ | l | ✓ |
| $\mathrm{BO}_{\mathrm{\_Vti}}$ | `BO__Vti` | tissue bone | $1$ | l | ✓ |
| $\mathrm{GO}_{\mathrm{\_Vpl}}$ | `GO__Vpl` | plasma gonads | $1$ | l | ✓ |
| $\mathrm{GO}_{\mathrm{\_Vti}}$ | `GO__Vti` | tissue gonads | $1$ | l | ✓ |

## Species

| Symbol | Id | Name | Compartment | Value | Unit | Properties |
| --- | --- | --- | --- | --- | --- | --- |
| $\mathrm{Car}_{\mathrm{api}}$ | `Car_api` | apixaban (arterial plasma) | $\mathrm{Var}_{\mathrm{pl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Car}_{\mathrm{api\_m1}}$ | `Car_api_m1` | O-demethyl apixaban sulfate (M1) (arterial plasma) | $\mathrm{Var}_{\mathrm{pl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Car}_{\mathrm{api\_m2}}$ | `Car_api_m2` | O-demethyl apixaban (M2) (arterial plasma) | $\mathrm{Var}_{\mathrm{pl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Car}_{\mathrm{api\_m7}}$ | `Car_api_m7` | hydroxy apixaban (M7) (arterial plasma) | $\mathrm{Var}_{\mathrm{pl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{api}}$ | `Cve_api` | apixaban (venous plasma) | $\mathrm{Vve}_{\mathrm{pl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{api\_m1}}$ | `Cve_api_m1` | O-demethyl apixaban sulfate (M1) (venous plasma) | $\mathrm{Vve}_{\mathrm{pl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{api\_m2}}$ | `Cve_api_m2` | O-demethyl apixaban (M2) (venous plasma) | $\mathrm{Vve}_{\mathrm{pl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{api\_m7}}$ | `Cve_api_m7` | hydroxy apixaban (M7) (venous plasma) | $\mathrm{Vve}_{\mathrm{pl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpo}_{\mathrm{api}}$ | `Cpo_api` | apixaban (portal plasma) | $\mathrm{Vpo}_{\mathrm{pl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpo}_{\mathrm{api\_m1}}$ | `Cpo_api_m1` | O-demethyl apixaban sulfate (M1) (portal plasma) | $\mathrm{Vpo}_{\mathrm{pl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpo}_{\mathrm{api\_m2}}$ | `Cpo_api_m2` | O-demethyl apixaban (M2) (portal plasma) | $\mathrm{Vpo}_{\mathrm{pl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpo}_{\mathrm{api\_m7}}$ | `Cpo_api_m7` | hydroxy apixaban (M7) (portal plasma) | $\mathrm{Vpo}_{\mathrm{pl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Aurine}_{\mathrm{api}}$ | `Aurine_api` | apixaban (urine) | $\mathrm{Vurine}$ | $0$ | mmol | amount |
| $\mathrm{Afeces}_{\mathrm{api}}$ | `Afeces_api` | apixaban (feces) | $\mathrm{Vfeces}$ | $0$ | mmol | amount |
| $\mathrm{Cbile}_{\mathrm{api}}$ | `Cbile_api` | apixaban (bile) | $\mathrm{Vbile}$ | $0$ | mmol/l | concentration |
| $\mathrm{Aurine}_{\mathrm{api\_m1}}$ | `Aurine_api_m1` | O-demethyl apixaban sulfate (M1) (urine) | $\mathrm{Vurine}$ | $0$ | mmol | amount |
| $\mathrm{Afeces}_{\mathrm{api\_m1}}$ | `Afeces_api_m1` | O-demethyl apixaban sulfate (M1) (feces) | $\mathrm{Vfeces}$ | $0$ | mmol | amount |
| $\mathrm{Cbile}_{\mathrm{api\_m1}}$ | `Cbile_api_m1` | O-demethyl apixaban sulfate (M1) (bile) | $\mathrm{Vbile}$ | $0$ | mmol/l | concentration |
| $\mathrm{Aurine}_{\mathrm{api\_m2}}$ | `Aurine_api_m2` | O-demethyl apixaban (M2) (urine) | $\mathrm{Vurine}$ | $0$ | mmol | amount |
| $\mathrm{Afeces}_{\mathrm{api\_m2}}$ | `Afeces_api_m2` | O-demethyl apixaban (M2) (feces) | $\mathrm{Vfeces}$ | $0$ | mmol | amount |
| $\mathrm{Cbile}_{\mathrm{api\_m2}}$ | `Cbile_api_m2` | O-demethyl apixaban (M2) (bile) | $\mathrm{Vbile}$ | $0$ | mmol/l | concentration |
| $\mathrm{Aurine}_{\mathrm{api\_m7}}$ | `Aurine_api_m7` | hydroxy apixaban (M7) (urine) | $\mathrm{Vurine}$ | $0$ | mmol | amount |
| $\mathrm{Afeces}_{\mathrm{api\_m7}}$ | `Afeces_api_m7` | hydroxy apixaban (M7) (feces) | $\mathrm{Vfeces}$ | $0$ | mmol | amount |
| $\mathrm{Cbile}_{\mathrm{api\_m7}}$ | `Cbile_api_m7` | hydroxy apixaban (M7) (bile) | $\mathrm{Vbile}$ | $0$ | mmol/l | concentration |
| $\mathrm{LU}_{\mathrm{\_Cpl\_api}}$ | `LU__Cpl_api` | apixaban (plasma, lung) | $\mathrm{LU}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LU}_{\mathrm{\_Cti\_api}}$ | `LU__Cti_api` | apixaban (tissue, lung) | $\mathrm{LU}_{\mathrm{\_Vti}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LU}_{\mathrm{\_Cpl\_api\_m1}}$ | `LU__Cpl_api_m1` | O-demethyl apixaban sulfate (M1) (plasma, lung) | $\mathrm{LU}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LU}_{\mathrm{\_Cpl\_api\_m2}}$ | `LU__Cpl_api_m2` | O-demethyl apixaban (M2) (plasma, lung) | $\mathrm{LU}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LU}_{\mathrm{\_Cpl\_api\_m7}}$ | `LU__Cpl_api_m7` | hydroxy apixaban (M7) (plasma, lung) | $\mathrm{LU}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{HE}_{\mathrm{\_Cpl\_api}}$ | `HE__Cpl_api` | apixaban (plasma, heart) | $\mathrm{HE}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{HE}_{\mathrm{\_Cti\_api}}$ | `HE__Cti_api` | apixaban (tissue, heart) | $\mathrm{HE}_{\mathrm{\_Vti}}$ | $0$ | mmol/l | concentration |
| $\mathrm{HE}_{\mathrm{\_Cpl\_api\_m1}}$ | `HE__Cpl_api_m1` | O-demethyl apixaban sulfate (M1) (plasma, heart) | $\mathrm{HE}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{HE}_{\mathrm{\_Cpl\_api\_m2}}$ | `HE__Cpl_api_m2` | O-demethyl apixaban (M2) (plasma, heart) | $\mathrm{HE}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{HE}_{\mathrm{\_Cpl\_api\_m7}}$ | `HE__Cpl_api_m7` | hydroxy apixaban (M7) (plasma, heart) | $\mathrm{HE}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{BR}_{\mathrm{\_Cpl\_api}}$ | `BR__Cpl_api` | apixaban (plasma, brain) | $\mathrm{BR}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{BR}_{\mathrm{\_Cti\_api}}$ | `BR__Cti_api` | apixaban (tissue, brain) | $\mathrm{BR}_{\mathrm{\_Vti}}$ | $0$ | mmol/l | concentration |
| $\mathrm{BR}_{\mathrm{\_Cpl\_api\_m1}}$ | `BR__Cpl_api_m1` | O-demethyl apixaban sulfate (M1) (plasma, brain) | $\mathrm{BR}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{BR}_{\mathrm{\_Cpl\_api\_m2}}$ | `BR__Cpl_api_m2` | O-demethyl apixaban (M2) (plasma, brain) | $\mathrm{BR}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{BR}_{\mathrm{\_Cpl\_api\_m7}}$ | `BR__Cpl_api_m7` | hydroxy apixaban (M7) (plasma, brain) | $\mathrm{BR}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_Cpl\_api}}$ | `LI__Cpl_api` | apixaban (plasma, liver) | $\mathrm{LI}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_Cti\_api}}$ | `LI__Cti_api` | apixaban (tissue, liver) | $\mathrm{LI}_{\mathrm{\_Vti}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_Cpl\_api\_m1}}$ | `LI__Cpl_api_m1` | O-demethyl apixaban sulfate (M1) (plasma, liver) | $\mathrm{LI}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_Cis\_api\_m1}}$ | `LI__Cis_api_m1` | O-demethyl apixaban sulfate (M1) (interstitial, liver) | $\mathrm{LI}_{\mathrm{\_Vis}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_Cic\_api\_m1}}$ | `LI__Cic_api_m1` | O-demethyl apixaban sulfate (M1) (intracellular, liver) | $\mathrm{LI}_{\mathrm{\_Vic}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_Cpl\_api\_m2}}$ | `LI__Cpl_api_m2` | O-demethyl apixaban (M2) (plasma, liver) | $\mathrm{LI}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_Cis\_api\_m2}}$ | `LI__Cis_api_m2` | O-demethyl apixaban (M2) (interstitial, liver) | $\mathrm{LI}_{\mathrm{\_Vis}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_Cic\_api\_m2}}$ | `LI__Cic_api_m2` | O-demethyl apixaban (M2) (intracellular, liver) | $\mathrm{LI}_{\mathrm{\_Vic}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_Cpl\_api\_m7}}$ | `LI__Cpl_api_m7` | hydroxy apixaban (M7) (plasma, liver) | $\mathrm{LI}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_Cis\_api\_m7}}$ | `LI__Cis_api_m7` | hydroxy apixaban (M7) (interstitial, liver) | $\mathrm{LI}_{\mathrm{\_Vis}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_Cic\_api\_m7}}$ | `LI__Cic_api_m7` | hydroxy apixaban (M7) (intracellular, liver) | $\mathrm{LI}_{\mathrm{\_Vic}}$ | $0$ | mmol/l | concentration |
| $\mathrm{KI}_{\mathrm{\_Cpl\_api}}$ | `KI__Cpl_api` | apixaban (plasma, kidney) | $\mathrm{KI}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{KI}_{\mathrm{\_Cti\_api}}$ | `KI__Cti_api` | apixaban (tissue, kidney) | $\mathrm{KI}_{\mathrm{\_Vti}}$ | $0$ | mmol/l | concentration |
| $\mathrm{KI}_{\mathrm{\_Cpl\_api\_m1}}$ | `KI__Cpl_api_m1` | O-demethyl apixaban sulfate (M1) (plasma, kidney) | $\mathrm{KI}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{KI}_{\mathrm{\_Cpl\_api\_m2}}$ | `KI__Cpl_api_m2` | O-demethyl apixaban (M2) (plasma, kidney) | $\mathrm{KI}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{KI}_{\mathrm{\_Cpl\_api\_m7}}$ | `KI__Cpl_api_m7` | hydroxy apixaban (M7) (plasma, kidney) | $\mathrm{KI}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{ST}_{\mathrm{\_Cpl\_api}}$ | `ST__Cpl_api` | apixaban (plasma, stomach) | $\mathrm{ST}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{ST}_{\mathrm{\_Cti\_api}}$ | `ST__Cti_api` | apixaban (tissue, stomach) | $\mathrm{ST}_{\mathrm{\_Vti}}$ | $0$ | mmol/l | concentration |
| $\mathrm{ST}_{\mathrm{\_Cpl\_api\_m1}}$ | `ST__Cpl_api_m1` | O-demethyl apixaban sulfate (M1) (plasma, stomach) | $\mathrm{ST}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{ST}_{\mathrm{\_Cpl\_api\_m2}}$ | `ST__Cpl_api_m2` | O-demethyl apixaban (M2) (plasma, stomach) | $\mathrm{ST}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{ST}_{\mathrm{\_Cpl\_api\_m7}}$ | `ST__Cpl_api_m7` | hydroxy apixaban (M7) (plasma, stomach) | $\mathrm{ST}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Cpl\_api}}$ | `GU__Cpl_api` | apixaban (plasma, small intestine) | $\mathrm{GU}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Cti\_api}}$ | `GU__Cti_api` | apixaban (tissue, small intestine) | $\mathrm{GU}_{\mathrm{\_Vti\_wall}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Cmu\_du\_api}}$ | `GU__Cmu_du_api` | apixaban (mucosa duodenum) | $\mathrm{GU}_{\mathrm{\_Vmu\_du}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Cmu\_jej1\_api}}$ | `GU__Cmu_jej1_api` | apixaban (mucosa upper jejunum) | $\mathrm{GU}_{\mathrm{\_Vmu\_jej1}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Cmu\_jej2\_api}}$ | `GU__Cmu_jej2_api` | apixaban (mucosa lower jejunum) | $\mathrm{GU}_{\mathrm{\_Vmu\_jej2}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Cmu\_ile1\_api}}$ | `GU__Cmu_ile1_api` | apixaban (mucosa upper ileum) | $\mathrm{GU}_{\mathrm{\_Vmu\_ile1}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Cmu\_ile2\_api}}$ | `GU__Cmu_ile2_api` | apixaban (mucosa lower ileum) | $\mathrm{GU}_{\mathrm{\_Vmu\_ile2}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Cmu\_cae\_api}}$ | `GU__Cmu_cae_api` | apixaban (mucosa caecum) | $\mathrm{GU}_{\mathrm{\_Vmu\_cae}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Cmu\_asc\_api}}$ | `GU__Cmu_asc_api` | apixaban (mucosa colon ascendens) | $\mathrm{GU}_{\mathrm{\_Vmu\_asc}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Cmu\_tra\_api}}$ | `GU__Cmu_tra_api` | apixaban (mucosa colon transversum) | $\mathrm{GU}_{\mathrm{\_Vmu\_tra}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Cmu\_des\_api}}$ | `GU__Cmu_des_api` | apixaban (mucosa colon descendens) | $\mathrm{GU}_{\mathrm{\_Vmu\_des}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Cmu\_sig\_api}}$ | `GU__Cmu_sig_api` | apixaban (mucosa colon sigmoid) | $\mathrm{GU}_{\mathrm{\_Vmu\_sig}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Cmu\_rec\_api}}$ | `GU__Cmu_rec_api` | apixaban (mucosa rectum) | $\mathrm{GU}_{\mathrm{\_Vmu\_rec}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_st\_api}}$ | `GU__Clumen_st_api` | apixaban (lumen stomach) | $\mathrm{GU}_{\mathrm{\_Vlumen\_st}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_du\_api}}$ | `GU__Clumen_du_api` | apixaban (lumen duodenum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_du}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api}}$ | `GU__Clumen_jej1_api` | apixaban (lumen upper jejunum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_jej1}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api}}$ | `GU__Clumen_jej2_api` | apixaban (lumen lower jejunum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_jej2}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api}}$ | `GU__Clumen_ile1_api` | apixaban (lumen upper ileum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_ile1}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api}}$ | `GU__Clumen_ile2_api` | apixaban (lumen lower ileum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_ile2}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api}}$ | `GU__Clumen_cae_api` | apixaban (lumen caecum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_cae}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api}}$ | `GU__Clumen_asc_api` | apixaban (lumen colon ascendens) | $\mathrm{GU}_{\mathrm{\_Vlumen\_asc}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api}}$ | `GU__Clumen_tra_api` | apixaban (lumen colon transversum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_tra}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_des\_api}}$ | `GU__Clumen_des_api` | apixaban (lumen colon descendens) | $\mathrm{GU}_{\mathrm{\_Vlumen\_des}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api}}$ | `GU__Clumen_sig_api` | apixaban (lumen colon sigmoid) | $\mathrm{GU}_{\mathrm{\_Vlumen\_sig}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api}}$ | `GU__Clumen_rec_api` | apixaban (lumen rectum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_rec}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Asolid\_du\_api}}$ | `GU__Asolid_du_api` | apixaban (undissolved, lumen duodenum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_du}}$ | $0$ | mmol | amount |
| $\mathrm{GU}_{\mathrm{\_Asolid\_jej1\_api}}$ | `GU__Asolid_jej1_api` | apixaban (undissolved, lumen upper jejunum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_jej1}}$ | $0$ | mmol | amount |
| $\mathrm{GU}_{\mathrm{\_Asolid\_jej2\_api}}$ | `GU__Asolid_jej2_api` | apixaban (undissolved, lumen lower jejunum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_jej2}}$ | $0$ | mmol | amount |
| $\mathrm{GU}_{\mathrm{\_Asolid\_ile1\_api}}$ | `GU__Asolid_ile1_api` | apixaban (undissolved, lumen upper ileum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_ile1}}$ | $0$ | mmol | amount |
| $\mathrm{GU}_{\mathrm{\_Asolid\_ile2\_api}}$ | `GU__Asolid_ile2_api` | apixaban (undissolved, lumen lower ileum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_ile2}}$ | $0$ | mmol | amount |
| $\mathrm{GU}_{\mathrm{\_Asolid\_cae\_api}}$ | `GU__Asolid_cae_api` | apixaban (undissolved, lumen caecum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_cae}}$ | $0$ | mmol | amount |
| $\mathrm{GU}_{\mathrm{\_Asolid\_asc\_api}}$ | `GU__Asolid_asc_api` | apixaban (undissolved, lumen colon ascendens) | $\mathrm{GU}_{\mathrm{\_Vlumen\_asc}}$ | $0$ | mmol | amount |
| $\mathrm{GU}_{\mathrm{\_Asolid\_tra\_api}}$ | `GU__Asolid_tra_api` | apixaban (undissolved, lumen colon transversum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_tra}}$ | $0$ | mmol | amount |
| $\mathrm{GU}_{\mathrm{\_Asolid\_des\_api}}$ | `GU__Asolid_des_api` | apixaban (undissolved, lumen colon descendens) | $\mathrm{GU}_{\mathrm{\_Vlumen\_des}}$ | $0$ | mmol | amount |
| $\mathrm{GU}_{\mathrm{\_Asolid\_sig\_api}}$ | `GU__Asolid_sig_api` | apixaban (undissolved, lumen colon sigmoid) | $\mathrm{GU}_{\mathrm{\_Vlumen\_sig}}$ | $0$ | mmol | amount |
| $\mathrm{GU}_{\mathrm{\_Asolid\_rec\_api}}$ | `GU__Asolid_rec_api` | apixaban (undissolved, lumen rectum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_rec}}$ | $0$ | mmol | amount |
| $\mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}}$ | `GU__Cpl_api_m1` | O-demethyl apixaban sulfate (M1) (plasma, small intestine) | $\mathrm{GU}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_st\_api\_m1}}$ | `GU__Clumen_st_api_m1` | O-demethyl apixaban sulfate (M1) (lumen stomach) | $\mathrm{GU}_{\mathrm{\_Vlumen\_st}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m1}}$ | `GU__Clumen_du_api_m1` | O-demethyl apixaban sulfate (M1) (lumen duodenum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_du}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m1}}$ | `GU__Clumen_jej1_api_m1` | O-demethyl apixaban sulfate (M1) (lumen upper jejunum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_jej1}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m1}}$ | `GU__Clumen_jej2_api_m1` | O-demethyl apixaban sulfate (M1) (lumen lower jejunum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_jej2}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m1}}$ | `GU__Clumen_ile1_api_m1` | O-demethyl apixaban sulfate (M1) (lumen upper ileum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_ile1}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m1}}$ | `GU__Clumen_ile2_api_m1` | O-demethyl apixaban sulfate (M1) (lumen lower ileum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_ile2}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m1}}$ | `GU__Clumen_cae_api_m1` | O-demethyl apixaban sulfate (M1) (lumen caecum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_cae}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m1}}$ | `GU__Clumen_asc_api_m1` | O-demethyl apixaban sulfate (M1) (lumen colon ascendens) | $\mathrm{GU}_{\mathrm{\_Vlumen\_asc}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m1}}$ | `GU__Clumen_tra_api_m1` | O-demethyl apixaban sulfate (M1) (lumen colon transversum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_tra}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m1}}$ | `GU__Clumen_des_api_m1` | O-demethyl apixaban sulfate (M1) (lumen colon descendens) | $\mathrm{GU}_{\mathrm{\_Vlumen\_des}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m1}}$ | `GU__Clumen_sig_api_m1` | O-demethyl apixaban sulfate (M1) (lumen colon sigmoid) | $\mathrm{GU}_{\mathrm{\_Vlumen\_sig}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m1}}$ | `GU__Clumen_rec_api_m1` | O-demethyl apixaban sulfate (M1) (lumen rectum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_rec}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}}$ | `GU__Cpl_api_m2` | O-demethyl apixaban (M2) (plasma, small intestine) | $\mathrm{GU}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_st\_api\_m2}}$ | `GU__Clumen_st_api_m2` | O-demethyl apixaban (M2) (lumen stomach) | $\mathrm{GU}_{\mathrm{\_Vlumen\_st}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m2}}$ | `GU__Clumen_du_api_m2` | O-demethyl apixaban (M2) (lumen duodenum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_du}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m2}}$ | `GU__Clumen_jej1_api_m2` | O-demethyl apixaban (M2) (lumen upper jejunum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_jej1}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m2}}$ | `GU__Clumen_jej2_api_m2` | O-demethyl apixaban (M2) (lumen lower jejunum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_jej2}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m2}}$ | `GU__Clumen_ile1_api_m2` | O-demethyl apixaban (M2) (lumen upper ileum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_ile1}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m2}}$ | `GU__Clumen_ile2_api_m2` | O-demethyl apixaban (M2) (lumen lower ileum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_ile2}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m2}}$ | `GU__Clumen_cae_api_m2` | O-demethyl apixaban (M2) (lumen caecum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_cae}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m2}}$ | `GU__Clumen_asc_api_m2` | O-demethyl apixaban (M2) (lumen colon ascendens) | $\mathrm{GU}_{\mathrm{\_Vlumen\_asc}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m2}}$ | `GU__Clumen_tra_api_m2` | O-demethyl apixaban (M2) (lumen colon transversum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_tra}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m2}}$ | `GU__Clumen_des_api_m2` | O-demethyl apixaban (M2) (lumen colon descendens) | $\mathrm{GU}_{\mathrm{\_Vlumen\_des}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m2}}$ | `GU__Clumen_sig_api_m2` | O-demethyl apixaban (M2) (lumen colon sigmoid) | $\mathrm{GU}_{\mathrm{\_Vlumen\_sig}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m2}}$ | `GU__Clumen_rec_api_m2` | O-demethyl apixaban (M2) (lumen rectum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_rec}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}}$ | `GU__Cpl_api_m7` | hydroxy apixaban (M7) (plasma, small intestine) | $\mathrm{GU}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_st\_api\_m7}}$ | `GU__Clumen_st_api_m7` | hydroxy apixaban (M7) (lumen stomach) | $\mathrm{GU}_{\mathrm{\_Vlumen\_st}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m7}}$ | `GU__Clumen_du_api_m7` | hydroxy apixaban (M7) (lumen duodenum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_du}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m7}}$ | `GU__Clumen_jej1_api_m7` | hydroxy apixaban (M7) (lumen upper jejunum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_jej1}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m7}}$ | `GU__Clumen_jej2_api_m7` | hydroxy apixaban (M7) (lumen lower jejunum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_jej2}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m7}}$ | `GU__Clumen_ile1_api_m7` | hydroxy apixaban (M7) (lumen upper ileum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_ile1}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m7}}$ | `GU__Clumen_ile2_api_m7` | hydroxy apixaban (M7) (lumen lower ileum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_ile2}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m7}}$ | `GU__Clumen_cae_api_m7` | hydroxy apixaban (M7) (lumen caecum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_cae}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m7}}$ | `GU__Clumen_asc_api_m7` | hydroxy apixaban (M7) (lumen colon ascendens) | $\mathrm{GU}_{\mathrm{\_Vlumen\_asc}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m7}}$ | `GU__Clumen_tra_api_m7` | hydroxy apixaban (M7) (lumen colon transversum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_tra}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m7}}$ | `GU__Clumen_des_api_m7` | hydroxy apixaban (M7) (lumen colon descendens) | $\mathrm{GU}_{\mathrm{\_Vlumen\_des}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m7}}$ | `GU__Clumen_sig_api_m7` | hydroxy apixaban (M7) (lumen colon sigmoid) | $\mathrm{GU}_{\mathrm{\_Vlumen\_sig}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m7}}$ | `GU__Clumen_rec_api_m7` | hydroxy apixaban (M7) (lumen rectum) | $\mathrm{GU}_{\mathrm{\_Vlumen\_rec}}$ | $0$ | mmol/l | concentration |
| $\mathrm{SP}_{\mathrm{\_Cpl\_api}}$ | `SP__Cpl_api` | apixaban (plasma, spleen) | $\mathrm{SP}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{SP}_{\mathrm{\_Cti\_api}}$ | `SP__Cti_api` | apixaban (tissue, spleen) | $\mathrm{SP}_{\mathrm{\_Vti}}$ | $0$ | mmol/l | concentration |
| $\mathrm{SP}_{\mathrm{\_Cpl\_api\_m1}}$ | `SP__Cpl_api_m1` | O-demethyl apixaban sulfate (M1) (plasma, spleen) | $\mathrm{SP}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{SP}_{\mathrm{\_Cpl\_api\_m2}}$ | `SP__Cpl_api_m2` | O-demethyl apixaban (M2) (plasma, spleen) | $\mathrm{SP}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{SP}_{\mathrm{\_Cpl\_api\_m7}}$ | `SP__Cpl_api_m7` | hydroxy apixaban (M7) (plasma, spleen) | $\mathrm{SP}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{PA}_{\mathrm{\_Cpl\_api}}$ | `PA__Cpl_api` | apixaban (plasma, pancreas) | $\mathrm{PA}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{PA}_{\mathrm{\_Cti\_api}}$ | `PA__Cti_api` | apixaban (tissue, pancreas) | $\mathrm{PA}_{\mathrm{\_Vti}}$ | $0$ | mmol/l | concentration |
| $\mathrm{PA}_{\mathrm{\_Cpl\_api\_m1}}$ | `PA__Cpl_api_m1` | O-demethyl apixaban sulfate (M1) (plasma, pancreas) | $\mathrm{PA}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{PA}_{\mathrm{\_Cpl\_api\_m2}}$ | `PA__Cpl_api_m2` | O-demethyl apixaban (M2) (plasma, pancreas) | $\mathrm{PA}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{PA}_{\mathrm{\_Cpl\_api\_m7}}$ | `PA__Cpl_api_m7` | hydroxy apixaban (M7) (plasma, pancreas) | $\mathrm{PA}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{MU}_{\mathrm{\_Cpl\_api}}$ | `MU__Cpl_api` | apixaban (plasma, muscle) | $\mathrm{MU}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{MU}_{\mathrm{\_Cti\_api}}$ | `MU__Cti_api` | apixaban (tissue, muscle) | $\mathrm{MU}_{\mathrm{\_Vti}}$ | $0$ | mmol/l | concentration |
| $\mathrm{MU}_{\mathrm{\_Cpl\_api\_m1}}$ | `MU__Cpl_api_m1` | O-demethyl apixaban sulfate (M1) (plasma, muscle) | $\mathrm{MU}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{MU}_{\mathrm{\_Cpl\_api\_m2}}$ | `MU__Cpl_api_m2` | O-demethyl apixaban (M2) (plasma, muscle) | $\mathrm{MU}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{MU}_{\mathrm{\_Cpl\_api\_m7}}$ | `MU__Cpl_api_m7` | hydroxy apixaban (M7) (plasma, muscle) | $\mathrm{MU}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{SK}_{\mathrm{\_Cpl\_api}}$ | `SK__Cpl_api` | apixaban (plasma, skin) | $\mathrm{SK}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{SK}_{\mathrm{\_Cti\_api}}$ | `SK__Cti_api` | apixaban (tissue, skin) | $\mathrm{SK}_{\mathrm{\_Vti}}$ | $0$ | mmol/l | concentration |
| $\mathrm{SK}_{\mathrm{\_Cpl\_api\_m1}}$ | `SK__Cpl_api_m1` | O-demethyl apixaban sulfate (M1) (plasma, skin) | $\mathrm{SK}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{SK}_{\mathrm{\_Cpl\_api\_m2}}$ | `SK__Cpl_api_m2` | O-demethyl apixaban (M2) (plasma, skin) | $\mathrm{SK}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{SK}_{\mathrm{\_Cpl\_api\_m7}}$ | `SK__Cpl_api_m7` | hydroxy apixaban (M7) (plasma, skin) | $\mathrm{SK}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{AD}_{\mathrm{\_Cpl\_api}}$ | `AD__Cpl_api` | apixaban (plasma, adipose) | $\mathrm{AD}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{AD}_{\mathrm{\_Cti\_api}}$ | `AD__Cti_api` | apixaban (tissue, adipose) | $\mathrm{AD}_{\mathrm{\_Vti}}$ | $0$ | mmol/l | concentration |
| $\mathrm{AD}_{\mathrm{\_Cpl\_api\_m1}}$ | `AD__Cpl_api_m1` | O-demethyl apixaban sulfate (M1) (plasma, adipose) | $\mathrm{AD}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{AD}_{\mathrm{\_Cpl\_api\_m2}}$ | `AD__Cpl_api_m2` | O-demethyl apixaban (M2) (plasma, adipose) | $\mathrm{AD}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{AD}_{\mathrm{\_Cpl\_api\_m7}}$ | `AD__Cpl_api_m7` | hydroxy apixaban (M7) (plasma, adipose) | $\mathrm{AD}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{BO}_{\mathrm{\_Cpl\_api}}$ | `BO__Cpl_api` | apixaban (plasma, bone) | $\mathrm{BO}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{BO}_{\mathrm{\_Cti\_api}}$ | `BO__Cti_api` | apixaban (tissue, bone) | $\mathrm{BO}_{\mathrm{\_Vti}}$ | $0$ | mmol/l | concentration |
| $\mathrm{BO}_{\mathrm{\_Cpl\_api\_m1}}$ | `BO__Cpl_api_m1` | O-demethyl apixaban sulfate (M1) (plasma, bone) | $\mathrm{BO}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{BO}_{\mathrm{\_Cpl\_api\_m2}}$ | `BO__Cpl_api_m2` | O-demethyl apixaban (M2) (plasma, bone) | $\mathrm{BO}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{BO}_{\mathrm{\_Cpl\_api\_m7}}$ | `BO__Cpl_api_m7` | hydroxy apixaban (M7) (plasma, bone) | $\mathrm{BO}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GO}_{\mathrm{\_Cpl\_api}}$ | `GO__Cpl_api` | apixaban (plasma, gonads) | $\mathrm{GO}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GO}_{\mathrm{\_Cti\_api}}$ | `GO__Cti_api` | apixaban (tissue, gonads) | $\mathrm{GO}_{\mathrm{\_Vti}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GO}_{\mathrm{\_Cpl\_api\_m1}}$ | `GO__Cpl_api_m1` | O-demethyl apixaban sulfate (M1) (plasma, gonads) | $\mathrm{GO}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GO}_{\mathrm{\_Cpl\_api\_m2}}$ | `GO__Cpl_api_m2` | O-demethyl apixaban (M2) (plasma, gonads) | $\mathrm{GO}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GO}_{\mathrm{\_Cpl\_api\_m7}}$ | `GO__Cpl_api_m7` | hydroxy apixaban (M7) (plasma, gonads) | $\mathrm{GO}_{\mathrm{\_Vpl}}$ | $0$ | mmol/l | concentration |

## Parameters

| Symbol | Id | Name | Value | Unit | Constant |
| --- | --- | --- | --- | --- | :---: |
| $\mathrm{BW}$ | `BW` | body weight \[kg\] | $60$ | kg | ✓ |
| $\mathrm{HEIGHT}$ | `HEIGHT` | height \[cm\] | $163$ | cm | ✓ |
| $f_{\mathrm{renal\_function}}$ | `f_renal_function` | renal function | $1$ | \- | ✓ |
| $f_{\mathrm{cardiac\_function}}$ | `f_cardiac_function` | cardiac function | $1$ | \- | ✓ |
| $f_{\mathrm{shunt}}$ | `f_shunt` | portosystemic shunt | $0$ | \- | ✓ |
| $f_{\mathrm{functional}}$ | `f_functional` | functional liver fraction | $1$ | \- | ✓ |
| $\mathrm{BW}_{\mathrm{ref}}$ | `BW_ref` | reference body weight \[kg\] | $60$ | kg | ✓ |
| $\mathrm{HEIGHT}_{\mathrm{ref}}$ | `HEIGHT_ref` | reference height \[cm\] | $163$ | cm | ✓ |
| $\mathrm{BSA}_{\mathrm{ref}}$ | `BSA_ref` | reference body surface area \[m2\] |  | m<sup>2</sup> | ✓ |
| $\mathrm{fage}_{\mathrm{FFM}}$ | `fage_FFM` | age factor fat-free mass | $1$ | \- | ✓ |
| $\mathrm{FFM}_{\mathrm{ref}}$ | `FFM_ref` | reference fat-free mass \[kg\] |  | kg | ✓ |
| $\mathrm{CO}_{\mathrm{ref}}$ | `CO_ref` | reference cardiac output \[l/min\] | $5.9$ | l/min | ✓ |
| $\mathrm{GFR}_{\mathrm{ref}}$ | `GFR_ref` | reference glomerular filtration rate \[l/min\] | $0.109$ | l/min | ✓ |
| $\mathrm{Vblood}_{\mathrm{ref}}$ | `Vblood_ref` | reference blood volume \[l\] | $3.9$ | l | ✓ |
| $\mathrm{fage}_{\mathrm{HCT}}$ | `fage_HCT` | age factor hematocrit | $1$ | \- | ✓ |
| $\mathrm{HCT}_{\mathrm{ref}}$ | `HCT_ref` | reference hematocrit |  | \- | ✓ |
| $\mathrm{HCT}$ | `HCT` | hematocrit |  | \- | ✓ |
| $\mathrm{Mlu}_{\mathrm{ref}}$ | `Mlu_ref` | reference tissue mass lung \[kg\] | $0.42$ | kg | ✓ |
| $\mathrm{Mhe}_{\mathrm{ref}}$ | `Mhe_ref` | reference tissue mass heart \[kg\] | $0.25$ | kg | ✓ |
| $\mathrm{Mbr}_{\mathrm{ref}}$ | `Mbr_ref` | reference tissue mass brain \[kg\] | $1.3$ | kg | ✓ |
| $\mathrm{Mli}_{\mathrm{ref}}$ | `Mli_ref` | reference tissue mass liver \[kg\] | $1.4$ | kg | ✓ |
| $\mathrm{Mki}_{\mathrm{ref}}$ | `Mki_ref` | reference tissue mass kidney \[kg\] | $0.275$ | kg | ✓ |
| $\mathrm{Mst}_{\mathrm{ref}}$ | `Mst_ref` | reference tissue mass stomach \[kg\] | $0.14$ | kg | ✓ |
| $\mathrm{Msi}_{\mathrm{ref}}$ | `Msi_ref` | reference tissue mass small intestine \[kg\] | $0.6$ | kg | ✓ |
| $\mathrm{Mla}_{\mathrm{ref}}$ | `Mla_ref` | reference tissue mass large intestine \[kg\] | $0.36$ | kg | ✓ |
| $\mathrm{Msp}_{\mathrm{ref}}$ | `Msp_ref` | reference tissue mass spleen \[kg\] | $0.13$ | kg | ✓ |
| $\mathrm{Mpa}_{\mathrm{ref}}$ | `Mpa_ref` | reference tissue mass pancreas \[kg\] | $0.12$ | kg | ✓ |
| $\mathrm{Mmu}_{\mathrm{ref}}$ | `Mmu_ref` | reference tissue mass muscle \[kg\] | $17.5$ | kg | ✓ |
| $\mathrm{Msk}_{\mathrm{ref}}$ | `Msk_ref` | reference tissue mass skin \[kg\] | $2.3$ | kg | ✓ |
| $\mathrm{Mbo}_{\mathrm{ref}}$ | `Mbo_ref` | reference tissue mass bone \[kg\] | $7.8$ | kg | ✓ |
| $\mathrm{Mgo}_{\mathrm{ref}}$ | `Mgo_ref` | reference tissue mass gonads \[kg\] | $0.011$ | kg | ✓ |
| $\mathrm{fage}_{\mathrm{Qbr}}$ | `fage_Qbr` | age factor brain flow | $1$ | \- | ✓ |
| $\mathrm{fage}_{\mathrm{Qli}}$ | `fage_Qli` | age factor liver flow | $1$ | \- | ✓ |
| $\mathrm{fage}_{\mathrm{Qki}}$ | `fage_Qki` | age factor kidney flow | $1$ | \- | ✓ |
| $\mathrm{fage}_{\mathrm{Qrest}}$ | `fage_Qrest` | age factor of the organs besides the brain |  | \- | ✓ |
| $\mathrm{fage}_{\mathrm{Qother}}$ | `fage_Qother` | age factor of the organs without a factor of their own |  | \- | ✓ |
| $\mathrm{fQhe}$ | `fQhe` | blood flow fraction heart |  | \- | ✓ |
| $\mathrm{fQbr}$ | `fQbr` | blood flow fraction brain |  | \- | ✓ |
| $\mathrm{fQli}$ | `fQli` | blood flow fraction liver |  | \- | ✓ |
| $\mathrm{fQki}$ | `fQki` | blood flow fraction kidney |  | \- | ✓ |
| $\mathrm{fQst}$ | `fQst` | blood flow fraction stomach |  | \- | ✓ |
| $\mathrm{fQsi}$ | `fQsi` | blood flow fraction small intestine |  | \- | ✓ |
| $\mathrm{fQla}$ | `fQla` | blood flow fraction large intestine |  | \- | ✓ |
| $\mathrm{fQsp}$ | `fQsp` | blood flow fraction spleen |  | \- | ✓ |
| $\mathrm{fQpa}$ | `fQpa` | blood flow fraction pancreas |  | \- | ✓ |
| $\mathrm{fQmu}$ | `fQmu` | blood flow fraction muscle |  | \- | ✓ |
| $\mathrm{fQsk}$ | `fQsk` | blood flow fraction skin |  | \- | ✓ |
| $\mathrm{fQad}$ | `fQad` | blood flow fraction adipose |  | \- | ✓ |
| $\mathrm{fQbo}$ | `fQbo` | blood flow fraction bone |  | \- | ✓ |
| $\mathrm{fQgo}$ | `fQgo` | blood flow fraction gonads |  | \- | ✓ |
| $\mathrm{fVar}$ | `fVar` | blood fraction arterial pool | $0.105$ | \- | ✓ |
| $\mathrm{fVve}$ | `fVve` | blood fraction venous pool | $0.24667$ | \- | ✓ |
| $\mathrm{fVpo}$ | `fVpo` | blood fraction portal pool | $0.00113$ | \- | ✓ |
| $\mathrm{fsex}_{\mathrm{CO}}$ | `fsex_CO` | sex factor cardiac output | $0.913735556072023$ | \- | ✓ |
| $\mathrm{fsex}_{\mathrm{Qbr}}$ | `fsex_Qbr` | sex factor brain fraction of the cardiac output | $1.257$ | \- | ✓ |
| $\mathrm{fsex}_{\mathrm{t\_stomach\_fed}}$ | `fsex_t_stomach_fed` | sex factor transit time of the stomach in the fed state | $1.2$ | \- | ✓ |
| $\mathrm{fsex}_{\mathrm{t\_colon}}$ | `fsex_t_colon` | sex factor transit times of the large intestine | $1.333$ | \- | ✓ |
| $\mathrm{BMI}$ | `BMI` | body mass index \[kg/m2\] |  | kg/m<sup>2</sup> | ✓ |
| $\mathrm{BSA}$ | `BSA` | body surface area \[m2\] |  | m<sup>2</sup> | ✓ |
| $\mathrm{FFM}$ | `FFM` | fat-free mass \[kg\] |  | kg | ✓ |
| $\mathrm{SV}_{\mathrm{tis}}$ | `SV_tis` | scaling factor of the lean tissues |  | \- | ✓ |
| $\mathrm{Vblood}$ | `Vblood` | blood volume \[l\] |  | l | ✓ |
| $\mathrm{Mlu}$ | `Mlu` | tissue mass lung \[kg\] |  | kg | ✓ |
| $\mathrm{Mhe}$ | `Mhe` | tissue mass heart \[kg\] |  | kg | ✓ |
| $\mathrm{Mbr}$ | `Mbr` | tissue mass brain \[kg\] |  | kg | ✓ |
| $\mathrm{Mli}$ | `Mli` | tissue mass liver \[kg\] |  | kg | ✓ |
| $\mathrm{Mki}$ | `Mki` | tissue mass kidney \[kg\] |  | kg | ✓ |
| $\mathrm{Mst}$ | `Mst` | tissue mass stomach \[kg\] |  | kg | ✓ |
| $\mathrm{Msi}$ | `Msi` | tissue mass small intestine \[kg\] |  | kg | ✓ |
| $\mathrm{Mla}$ | `Mla` | tissue mass large intestine \[kg\] |  | kg | ✓ |
| $\mathrm{Msp}$ | `Msp` | tissue mass spleen \[kg\] |  | kg | ✓ |
| $\mathrm{Mpa}$ | `Mpa` | tissue mass pancreas \[kg\] |  | kg | ✓ |
| $\mathrm{Mmu}$ | `Mmu` | tissue mass muscle \[kg\] |  | kg | ✓ |
| $\mathrm{Msk}$ | `Msk` | tissue mass skin \[kg\] |  | kg | ✓ |
| $\mathrm{Mbo}$ | `Mbo` | tissue mass bone \[kg\] |  | kg | ✓ |
| $\mathrm{Mgo}$ | `Mgo` | tissue mass gonads \[kg\] |  | kg | ✓ |
| $\mathrm{Mlean}$ | `Mlean` | mass of the lean organ tissues \[kg\] |  | kg | ✓ |
| $\mathrm{Mad}$ | `Mad` | tissue mass adipose \[kg\] |  | kg | ✓ |
| $\mathrm{Vlu}$ | `Vlu` | volume lung \[l\] |  | l | ✓ |
| $\mathrm{Vhe}$ | `Vhe` | volume heart \[l\] |  | l | ✓ |
| $\mathrm{Vbr}$ | `Vbr` | volume brain \[l\] |  | l | ✓ |
| $\mathrm{Vli}$ | `Vli` | volume liver \[l\] |  | l | ✓ |
| $\mathrm{Vki}$ | `Vki` | volume kidney \[l\] |  | l | ✓ |
| $\mathrm{Vst}$ | `Vst` | volume stomach \[l\] |  | l | ✓ |
| $\mathrm{Vsi}$ | `Vsi` | volume small intestine \[l\] |  | l | ✓ |
| $\mathrm{Vla}$ | `Vla` | volume large intestine \[l\] |  | l | ✓ |
| $\mathrm{Vsp}$ | `Vsp` | volume spleen \[l\] |  | l | ✓ |
| $\mathrm{Vpa}$ | `Vpa` | volume pancreas \[l\] |  | l | ✓ |
| $\mathrm{Vmu}$ | `Vmu` | volume muscle \[l\] |  | l | ✓ |
| $\mathrm{Vsk}$ | `Vsk` | volume skin \[l\] |  | l | ✓ |
| $\mathrm{Vad}$ | `Vad` | volume adipose \[l\] |  | l | ✓ |
| $\mathrm{Vbo}$ | `Vbo` | volume bone \[l\] |  | l | ✓ |
| $\mathrm{Vgo}$ | `Vgo` | volume gonads \[l\] |  | l | ✓ |
| $\mathrm{Var}$ | `Var` | volume arterial blood \[l\] |  | l | ✓ |
| $\mathrm{Vve}$ | `Vve` | volume venous blood \[l\] |  | l | ✓ |
| $\mathrm{Vpo}$ | `Vpo` | volume portal blood \[l\] |  | l | ✓ |
| $f_{\mathrm{vas\_lu}}$ | `f_vas_lu` | vascular fraction lung |  | \- | ✓ |
| $f_{\mathrm{int\_lu}}$ | `f_int_lu` | interstitial fraction lung |  | \- | ✓ |
| $f_{\mathrm{vas\_he}}$ | `f_vas_he` | vascular fraction heart |  | \- | ✓ |
| $f_{\mathrm{int\_he}}$ | `f_int_he` | interstitial fraction heart |  | \- | ✓ |
| $f_{\mathrm{vas\_br}}$ | `f_vas_br` | vascular fraction brain |  | \- | ✓ |
| $f_{\mathrm{int\_br}}$ | `f_int_br` | interstitial fraction brain |  | \- | ✓ |
| $f_{\mathrm{vas\_li}}$ | `f_vas_li` | vascular fraction liver |  | \- | ✓ |
| $f_{\mathrm{int\_li}}$ | `f_int_li` | interstitial fraction liver |  | \- | ✓ |
| $f_{\mathrm{vas\_ki}}$ | `f_vas_ki` | vascular fraction kidney |  | \- | ✓ |
| $f_{\mathrm{int\_ki}}$ | `f_int_ki` | interstitial fraction kidney |  | \- | ✓ |
| $f_{\mathrm{vas\_st}}$ | `f_vas_st` | vascular fraction stomach |  | \- | ✓ |
| $f_{\mathrm{int\_st}}$ | `f_int_st` | interstitial fraction stomach |  | \- | ✓ |
| $f_{\mathrm{vas\_si}}$ | `f_vas_si` | vascular fraction small intestine |  | \- | ✓ |
| $f_{\mathrm{int\_si}}$ | `f_int_si` | interstitial fraction small intestine |  | \- | ✓ |
| $f_{\mathrm{vas\_la}}$ | `f_vas_la` | vascular fraction large intestine |  | \- | ✓ |
| $f_{\mathrm{int\_la}}$ | `f_int_la` | interstitial fraction large intestine |  | \- | ✓ |
| $f_{\mathrm{vas\_sp}}$ | `f_vas_sp` | vascular fraction spleen |  | \- | ✓ |
| $f_{\mathrm{int\_sp}}$ | `f_int_sp` | interstitial fraction spleen |  | \- | ✓ |
| $f_{\mathrm{vas\_pa}}$ | `f_vas_pa` | vascular fraction pancreas |  | \- | ✓ |
| $f_{\mathrm{int\_pa}}$ | `f_int_pa` | interstitial fraction pancreas |  | \- | ✓ |
| $f_{\mathrm{vas\_mu}}$ | `f_vas_mu` | vascular fraction muscle |  | \- | ✓ |
| $f_{\mathrm{int\_mu}}$ | `f_int_mu` | interstitial fraction muscle |  | \- | ✓ |
| $f_{\mathrm{vas\_sk}}$ | `f_vas_sk` | vascular fraction skin |  | \- | ✓ |
| $f_{\mathrm{int\_sk}}$ | `f_int_sk` | interstitial fraction skin |  | \- | ✓ |
| $f_{\mathrm{vas\_ad}}$ | `f_vas_ad` | vascular fraction adipose |  | \- | ✓ |
| $f_{\mathrm{int\_ad}}$ | `f_int_ad` | interstitial fraction adipose |  | \- | ✓ |
| $f_{\mathrm{vas\_bo}}$ | `f_vas_bo` | vascular fraction bone |  | \- | ✓ |
| $f_{\mathrm{int\_bo}}$ | `f_int_bo` | interstitial fraction bone |  | \- | ✓ |
| $f_{\mathrm{vas\_go}}$ | `f_vas_go` | vascular fraction gonads |  | \- | ✓ |
| $f_{\mathrm{int\_go}}$ | `f_int_go` | interstitial fraction gonads |  | \- | ✓ |
| $\mathrm{CO}_{\mathrm{base}}$ | `CO_base` | cardiac output without impairment \[l/min\] |  | l/min | ✓ |
| $\mathrm{CO}$ | `CO` | cardiac output \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qlu}$ | `Qlu` | blood flow lung \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qhe}$ | `Qhe` | blood flow heart \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qbr}$ | `Qbr` | blood flow brain \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qli}$ | `Qli` | blood flow liver \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qki}$ | `Qki` | blood flow kidney \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qst}$ | `Qst` | blood flow stomach \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qsi}$ | `Qsi` | blood flow small intestine \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qla}$ | `Qla` | blood flow large intestine \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qsp}$ | `Qsp` | blood flow spleen \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qpa}$ | `Qpa` | blood flow pancreas \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qmu}$ | `Qmu` | blood flow muscle \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qsk}$ | `Qsk` | blood flow skin \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qad}$ | `Qad` | blood flow adipose \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qbo}$ | `Qbo` | blood flow bone \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qgo}$ | `Qgo` | blood flow gonads \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qha}$ | `Qha` | hepatic arterial blood flow \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qpo}$ | `Qpo` | portal venous blood flow \[l/min\] |  | l/min | ✓ |
| $\mathrm{Qh}$ | `Qh` | liver blood flow \[l/min\] |  | l/min | ✓ |
| $\mathrm{fage}_{\mathrm{GFR}}$ | `fage_GFR` | age factor GFR | $1$ | \- | ✓ |
| $\mathrm{GFR}_{\mathrm{base}}$ | `GFR_base` | glomerular filtration rate at renal function 1 \[l/min\] |  | l/min | ✓ |
| $\mathrm{GFR}$ | `GFR` | glomerular filtration rate \[l/min\] |  | l/min | ✓ |
| $\mathrm{CP}_{\mathrm{severity}}$ | `CP_severity` | severity of liver cirrhosis | $0$ | \- | ✓ |
| $\mathrm{HF}_{\mathrm{severity}}$ | `HF_severity` | severity of heart failure | $0$ | \- | ✓ |
| $\mathrm{CKD}_{\mathrm{hepatic}}$ | `CKD_hepatic` | hepatic changes of chronic kidney disease | $0$ | \- | ✓ |
| $\mathrm{fcp}_{\mathrm{functional\_liver}}$ | `fcp_functional_liver` | cirrhosis factor functional\_liver |  | \- | ✓ |
| $\mathrm{fcp}_{\mathrm{hepatic\_artery\_flow}}$ | `fcp_hepatic_artery_flow` | cirrhosis factor hepatic\_artery\_flow |  | \- | ✓ |
| $\mathrm{fcp}_{\mathrm{kidney\_flow}}$ | `fcp_kidney_flow` | cirrhosis factor kidney\_flow |  | \- | ✓ |
| $\mathrm{fcp}_{\mathrm{cardiac\_index}}$ | `fcp_cardiac_index` | cirrhosis factor cardiac\_index |  | \- | ✓ |
| $\mathrm{fcp}_{\mathrm{gfr}}$ | `fcp_gfr` | cirrhosis factor gfr |  | \- | ✓ |
| $\mathrm{fcp}_{\mathrm{albumin}}$ | `fcp_albumin` | cirrhosis factor albumin |  | \- | ✓ |
| $\mathrm{fcp}_{\mathrm{agp}}$ | `fcp_agp` | cirrhosis factor agp |  | \- | ✓ |
| $\mathrm{fcp}_{\mathrm{hematocrit}}$ | `fcp_hematocrit` | cirrhosis factor hematocrit |  | \- | ✓ |
| $\mathrm{fcp}_{\mathrm{shunt}}$ | `fcp_shunt` | cirrhosis factor shunt |  | \- | ✓ |
| $\mathrm{fcp}_{\mathrm{cyp3a4}}$ | `fcp_cyp3a4` | cirrhosis factor CYP3A4 |  | \- | ✓ |
| $\mathrm{fcp}_{\mathrm{rest\_flow}}$ | `fcp_rest_flow` | cirrhosis factor flow of the other organs |  | \- | ✓ |
| $\mathrm{eGFR}$ | `eGFR` | GFR per 1.73 m2 of the renal function \[l/min\] |  | l/min | ✓ |
| $\mathrm{fckd}_{\mathrm{plasma\_protein}}$ | `fckd_plasma_protein` | CKD factor plasma\_protein |  | \- | ✓ |
| $\mathrm{fckd}_{\mathrm{hematocrit}}$ | `fckd_hematocrit` | CKD factor hematocrit |  | \- | ✓ |
| $\mathrm{fckd}_{\mathrm{kidney\_volume}}$ | `fckd_kidney_volume` | CKD factor kidney\_volume |  | \- | ✓ |
| $\mathrm{fckd}_{\mathrm{kidney\_flow}}$ | `fckd_kidney_flow` | CKD factor kidney\_flow |  | \- | ✓ |
| $\mathrm{fckd}_{\mathrm{gastric\_emptying\_time}}$ | `fckd_gastric_emptying_time` | CKD factor gastric\_emptying\_time |  | \- | ✓ |
| $\mathrm{fckd}_{\mathrm{si\_transit\_time}}$ | `fckd_si_transit_time` | CKD factor si\_transit\_time |  | \- | ✓ |
| $\mathrm{fckd}_{\mathrm{cyp3a4}}$ | `fckd_cyp3a4` | CKD factor CYP3A4 |  | \- | ✓ |
| $\mathrm{fhf}_{\mathrm{liver\_flow}}$ | `fhf_liver_flow` | heart failure factor liver flow |  | \- | ✓ |
| $\mathrm{fhf}_{\mathrm{kidney\_flow}}$ | `fhf_kidney_flow` | heart failure factor kidney flow |  | \- | ✓ |
| $\mathrm{fhf}_{\mathrm{peripheral\_flow}}$ | `fhf_peripheral_flow` | heart failure factor peripheral flow |  | \- | ✓ |
| $\mathrm{fsex}_{\mathrm{albumin}}$ | `fsex_albumin` | sex factor albumin |  | \- | ✓ |
| $\mathrm{fsex}_{\mathrm{li\_cyp3a4}}$ | `fsex_li_cyp3a4` | sex factor CYP3A4 liver |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{Qhe}}$ | `fimp_Qhe` | impairment factor Qhe |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{Qbr}}$ | `fimp_Qbr` | impairment factor Qbr |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{Qli}}$ | `fimp_Qli` | impairment factor Qli |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{Qki}}$ | `fimp_Qki` | impairment factor Qki |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{Qst}}$ | `fimp_Qst` | impairment factor Qst |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{Qsi}}$ | `fimp_Qsi` | impairment factor Qsi |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{Qla}}$ | `fimp_Qla` | impairment factor Qla |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{Qsp}}$ | `fimp_Qsp` | impairment factor Qsp |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{Qpa}}$ | `fimp_Qpa` | impairment factor Qpa |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{Qmu}}$ | `fimp_Qmu` | impairment factor Qmu |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{Qsk}}$ | `fimp_Qsk` | impairment factor Qsk |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{Qad}}$ | `fimp_Qad` | impairment factor Qad |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{Qbo}}$ | `fimp_Qbo` | impairment factor Qbo |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{Qgo}}$ | `fimp_Qgo` | impairment factor Qgo |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{CO}}$ | `fimp_CO` | impairment factor cardiac output |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{GFR}}$ | `fimp_GFR` | impairment factor GFR |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{HCT}}$ | `fimp_HCT` | impairment factor HCT |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{Mki}}$ | `fimp_Mki` | impairment factor Mki |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{albumin}}$ | `fimp_albumin` | impairment factor albumin |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{agp}}$ | `fimp_agp` | impairment factor agp |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{plasma\_protein}}$ | `fimp_plasma_protein` | impairment factor plasma\_protein |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{t\_stomach}}$ | `fimp_t_stomach` | impairment factor t\_stomach |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{t\_si}}$ | `fimp_t_si` | impairment factor t\_si |  | \- | ✓ |
| $\mathrm{fimp}_{\mathrm{li\_cyp3a4}}$ | `fimp_li_cyp3a4` | individual factor activity CYP3A4 liver |  | \- | ✓ |
| $\mathrm{Mr}_{\mathrm{api}}$ | `Mr_api` | molecular weight api \[g/mole\] | $459.5$ | g/mol | ✓ |
| $\mathrm{fu}_{\mathrm{ref\_api}}$ | `fu_ref_api` | reference fraction unbound api | $0.131$ | \- | ✓ |
| $\mathrm{fu}_{\mathrm{api}}$ | `fu_api` | fraction unbound api |  | \- | ✓ |
| $f_{\mathrm{reabsorbed\_api}}$ | `f_reabsorbed_api` | fraction reabsorbed api | $0$ | \- | ✓ |
| $\mathrm{Kp}_{\mathrm{api}}$ | `Kp_api` | tissue to plasma coefficient api | $0.226161223801224$ | \- | ✓ |
| $\mathrm{ftissue}_{\mathrm{api}}$ | `ftissue_api` | whole-body exchange api \[l/min\] | $12.9388974695916$ | l/min | ✓ |
| $\mathrm{Vti}_{\mathrm{total\_ref\_api}}$ | `Vti_total_ref_api` | reference tissue volume of the organs api enters \[l\] | $52.3385631316714$ | l | ✓ |
| $\mathrm{BP}_{\mathrm{api}}$ | `BP_api` | blood to plasma ratio api |  | \- | ✓ |
| $\mathrm{Mr}_{\mathrm{api\_m1}}$ | `Mr_api_m1` | molecular weight api\_m1 \[g/mole\] | $525.5$ | g/mol | ✓ |
| $\mathrm{fu}_{\mathrm{ref\_api\_m1}}$ | `fu_ref_api_m1` | reference fraction unbound api\_m1 | $0.0417291817985422$ | \- | ✓ |
| $\mathrm{fu}_{\mathrm{api\_m1}}$ | `fu_api_m1` | fraction unbound api\_m1 |  | \- | ✓ |
| $f_{\mathrm{reabsorbed\_api\_m1}}$ | `f_reabsorbed_api_m1` | fraction reabsorbed api\_m1 | $0$ | \- | ✓ |
| $\mathrm{Kp}_{\mathrm{api\_m1}}$ | `Kp_api_m1` | tissue to plasma coefficient api\_m1 | $1$ | \- | ✓ |
| $\mathrm{BP}_{\mathrm{api\_m1}}$ | `BP_api_m1` | blood to plasma ratio api\_m1 |  | \- | ✓ |
| $\mathrm{Mr}_{\mathrm{api\_m2}}$ | `Mr_api_m2` | molecular weight api\_m2 \[g/mole\] | $445.5$ | g/mol | ✓ |
| $\mathrm{fu}_{\mathrm{ref\_api\_m2}}$ | `fu_ref_api_m2` | reference fraction unbound api\_m2 | $1$ | \- | ✓ |
| $\mathrm{fu}_{\mathrm{api\_m2}}$ | `fu_api_m2` | fraction unbound api\_m2 |  | \- | ✓ |
| $\mathrm{BP}_{\mathrm{api\_m2}}$ | `BP_api_m2` | blood to plasma ratio api\_m2 |  | \- | ✓ |
| $\mathrm{Mr}_{\mathrm{api\_m7}}$ | `Mr_api_m7` | molecular weight api\_m7 \[g/mole\] | $475.5$ | g/mol | ✓ |
| $\mathrm{fu}_{\mathrm{ref\_api\_m7}}$ | `fu_ref_api_m7` | reference fraction unbound api\_m7 | $0.001284996162871$ | \- | ✓ |
| $\mathrm{fu}_{\mathrm{api\_m7}}$ | `fu_api_m7` | fraction unbound api\_m7 |  | \- | ✓ |
| $f_{\mathrm{reabsorbed\_api\_m7}}$ | `f_reabsorbed_api_m7` | fraction reabsorbed api\_m7 | $0$ | \- | ✓ |
| $\mathrm{Kp}_{\mathrm{api\_m7}}$ | `Kp_api_m7` | tissue to plasma coefficient api\_m7 | $1$ | \- | ✓ |
| $\mathrm{BP}_{\mathrm{api\_m7}}$ | `BP_api_m7` | blood to plasma ratio api\_m7 |  | \- | ✓ |
| $k_{\mathrm{bile}}$ | `k_bile` | transit bile to intestinal lumen \[1/min\] | $0.01$ | 1/min | ✓ |
| $\mathrm{ka}_{\mathrm{api}}$ | `ka_api` | absorption api \[1/hr\] | $2.77585725524381$ | 1/hr | ✓ |
| $\mathrm{ka}_{\mathrm{api\_m1}}$ | `ka_api_m1` | absorption api\_m1 \[1/hr\] | $0$ | 1/hr | ✓ |
| $\mathrm{ka}_{\mathrm{api\_m2}}$ | `ka_api_m2` | absorption api\_m2 \[1/hr\] | $0$ | 1/hr | ✓ |
| $\mathrm{ka}_{\mathrm{api\_m7}}$ | `ka_api_m7` | absorption api\_m7 \[1/hr\] | $0$ | 1/hr | ✓ |
| $\mathrm{fabs}_{\mathrm{api}}$ | `fabs_api` | fraction absorbed api | $0.682971030762384$ | \- | ✓ |
| $f_{\mathrm{ka\_colon\_api}}$ | `f_ka_colon_api` | absorption factor large intestine api | $0.0567$ | \- | ✓ |
| $f_{\mathrm{ka\_ile2\_api}}$ | `f_ka_ile2_api` | absorption factor lower ileum api | $0.149$ | \- | ✓ |
| $\mathrm{FED}$ | `FED` | fed state (0 fasted, 1 fed) | $0$ | \- | ✓ |
| $\mathrm{IVDOSE}_{\mathrm{api}}$ | `IVDOSE_api` | intravenous dose api \[mg\] | $0$ | mg |  |
| $\mathrm{ti}_{\mathrm{api}}$ | `ti_api` | injection time api \[s\] | $10$ | s | ✓ |
| $\mathrm{Kiv}_{\mathrm{api}}$ | `Kiv_api` | injection rate api \[1/min\] |  | 1/min |  |
| $\mathrm{Ri}_{\mathrm{api}}$ | `Ri_api` | infusion rate api \[mg/min\] | $0$ | mg/min | ✓ |
| $\mathrm{PODOSE}_{\mathrm{api}}$ | `PODOSE_api` | oral dose api (tablet) \[mg\] | $0$ | mg |  |
| $\mathrm{Ka}_{\mathrm{dis\_api}}$ | `Ka_dis_api` | dissolution rate api \[1/hr\] | $1.08228543237278$ | 1/hr | ✓ |
| $\mathrm{D50}_{\mathrm{dis\_api}}$ | `D50_dis_api` | undissolved amount of half the dissolution rate api \[mg\] | $9.09559808800995$ | mg | ✓ |
| $\mathrm{SOLDOSE}_{\mathrm{api}}$ | `SOLDOSE_api` | oral dose api (solution) \[mg\] | $0$ | mg |  |
| $\mathrm{Ka}_{\mathrm{sol\_api}}$ | `Ka_sol_api` | application rate api (solution) \[1/hr\] | $60$ | 1/hr | ✓ |
| $w_{\mathrm{arm\_sk}}$ | `w_arm_sk` | weight of venous outflow of the skin in the arm vein | $0.7$ | \- | ✓ |
| $w_{\mathrm{arm\_mu}}$ | `w_arm_mu` | weight of venous outflow of the muscle in the arm vein | $0.3$ | \- | ✓ |
| $\mathrm{Car}_{\mathrm{free\_api}}$ | `Car_free_api` | unbound plasma concentration api arterial \[mM\] |  | mmol/l |  |
| $\mathrm{Car}_{\mathrm{blood\_api}}$ | `Car_blood_api` | blood concentration api arterial \[mM\] |  | mmol/l |  |
| $\mathrm{Cve}_{\mathrm{free\_api}}$ | `Cve_free_api` | unbound plasma concentration api venous \[mM\] |  | mmol/l |  |
| $\mathrm{Cve}_{\mathrm{blood\_api}}$ | `Cve_blood_api` | blood concentration api venous \[mM\] |  | mmol/l |  |
| $\mathrm{Cpo}_{\mathrm{free\_api}}$ | `Cpo_free_api` | unbound plasma concentration api portal \[mM\] |  | mmol/l |  |
| $\mathrm{Cpo}_{\mathrm{blood\_api}}$ | `Cpo_blood_api` | blood concentration api portal \[mM\] |  | mmol/l |  |
| $\mathrm{Chv}_{\mathrm{api}}$ | `Chv_api` | hepatic vein plasma concentration api \[mM\] |  | mmol/l |  |
| $\mathrm{Chv}_{\mathrm{free\_api}}$ | `Chv_free_api` | hepatic vein unbound plasma concentration api \[mM\] |  | mmol/l |  |
| $\mathrm{Chv}_{\mathrm{blood\_api}}$ | `Chv_blood_api` | hepatic vein blood concentration api \[mM\] |  | mmol/l |  |
| $\mathrm{Carm}_{\mathrm{api}}$ | `Carm_api` | arm vein plasma concentration api \[mM\] |  | mmol/l |  |
| $\mathrm{Carm}_{\mathrm{free\_api}}$ | `Carm_free_api` | arm vein unbound plasma concentration api \[mM\] |  | mmol/l |  |
| $\mathrm{Carm}_{\mathrm{blood\_api}}$ | `Carm_blood_api` | arm vein blood concentration api \[mM\] |  | mmol/l |  |
| $\mathrm{Car}_{\mathrm{free\_api\_m1}}$ | `Car_free_api_m1` | unbound plasma concentration api\_m1 arterial \[mM\] |  | mmol/l |  |
| $\mathrm{Car}_{\mathrm{blood\_api\_m1}}$ | `Car_blood_api_m1` | blood concentration api\_m1 arterial \[mM\] |  | mmol/l |  |
| $\mathrm{Cve}_{\mathrm{free\_api\_m1}}$ | `Cve_free_api_m1` | unbound plasma concentration api\_m1 venous \[mM\] |  | mmol/l |  |
| $\mathrm{Cve}_{\mathrm{blood\_api\_m1}}$ | `Cve_blood_api_m1` | blood concentration api\_m1 venous \[mM\] |  | mmol/l |  |
| $\mathrm{Cpo}_{\mathrm{free\_api\_m1}}$ | `Cpo_free_api_m1` | unbound plasma concentration api\_m1 portal \[mM\] |  | mmol/l |  |
| $\mathrm{Cpo}_{\mathrm{blood\_api\_m1}}$ | `Cpo_blood_api_m1` | blood concentration api\_m1 portal \[mM\] |  | mmol/l |  |
| $\mathrm{Chv}_{\mathrm{api\_m1}}$ | `Chv_api_m1` | hepatic vein plasma concentration api\_m1 \[mM\] |  | mmol/l |  |
| $\mathrm{Chv}_{\mathrm{free\_api\_m1}}$ | `Chv_free_api_m1` | hepatic vein unbound plasma concentration api\_m1 \[mM\] |  | mmol/l |  |
| $\mathrm{Chv}_{\mathrm{blood\_api\_m1}}$ | `Chv_blood_api_m1` | hepatic vein blood concentration api\_m1 \[mM\] |  | mmol/l |  |
| $\mathrm{Carm}_{\mathrm{api\_m1}}$ | `Carm_api_m1` | arm vein plasma concentration api\_m1 \[mM\] |  | mmol/l |  |
| $\mathrm{Carm}_{\mathrm{free\_api\_m1}}$ | `Carm_free_api_m1` | arm vein unbound plasma concentration api\_m1 \[mM\] |  | mmol/l |  |
| $\mathrm{Carm}_{\mathrm{blood\_api\_m1}}$ | `Carm_blood_api_m1` | arm vein blood concentration api\_m1 \[mM\] |  | mmol/l |  |
| $\mathrm{Car}_{\mathrm{free\_api\_m2}}$ | `Car_free_api_m2` | unbound plasma concentration api\_m2 arterial \[mM\] |  | mmol/l |  |
| $\mathrm{Car}_{\mathrm{blood\_api\_m2}}$ | `Car_blood_api_m2` | blood concentration api\_m2 arterial \[mM\] |  | mmol/l |  |
| $\mathrm{Cve}_{\mathrm{free\_api\_m2}}$ | `Cve_free_api_m2` | unbound plasma concentration api\_m2 venous \[mM\] |  | mmol/l |  |
| $\mathrm{Cve}_{\mathrm{blood\_api\_m2}}$ | `Cve_blood_api_m2` | blood concentration api\_m2 venous \[mM\] |  | mmol/l |  |
| $\mathrm{Cpo}_{\mathrm{free\_api\_m2}}$ | `Cpo_free_api_m2` | unbound plasma concentration api\_m2 portal \[mM\] |  | mmol/l |  |
| $\mathrm{Cpo}_{\mathrm{blood\_api\_m2}}$ | `Cpo_blood_api_m2` | blood concentration api\_m2 portal \[mM\] |  | mmol/l |  |
| $\mathrm{Chv}_{\mathrm{api\_m2}}$ | `Chv_api_m2` | hepatic vein plasma concentration api\_m2 \[mM\] |  | mmol/l |  |
| $\mathrm{Chv}_{\mathrm{free\_api\_m2}}$ | `Chv_free_api_m2` | hepatic vein unbound plasma concentration api\_m2 \[mM\] |  | mmol/l |  |
| $\mathrm{Chv}_{\mathrm{blood\_api\_m2}}$ | `Chv_blood_api_m2` | hepatic vein blood concentration api\_m2 \[mM\] |  | mmol/l |  |
| $\mathrm{Carm}_{\mathrm{api\_m2}}$ | `Carm_api_m2` | arm vein plasma concentration api\_m2 \[mM\] |  | mmol/l |  |
| $\mathrm{Carm}_{\mathrm{free\_api\_m2}}$ | `Carm_free_api_m2` | arm vein unbound plasma concentration api\_m2 \[mM\] |  | mmol/l |  |
| $\mathrm{Carm}_{\mathrm{blood\_api\_m2}}$ | `Carm_blood_api_m2` | arm vein blood concentration api\_m2 \[mM\] |  | mmol/l |  |
| $\mathrm{Car}_{\mathrm{free\_api\_m7}}$ | `Car_free_api_m7` | unbound plasma concentration api\_m7 arterial \[mM\] |  | mmol/l |  |
| $\mathrm{Car}_{\mathrm{blood\_api\_m7}}$ | `Car_blood_api_m7` | blood concentration api\_m7 arterial \[mM\] |  | mmol/l |  |
| $\mathrm{Cve}_{\mathrm{free\_api\_m7}}$ | `Cve_free_api_m7` | unbound plasma concentration api\_m7 venous \[mM\] |  | mmol/l |  |
| $\mathrm{Cve}_{\mathrm{blood\_api\_m7}}$ | `Cve_blood_api_m7` | blood concentration api\_m7 venous \[mM\] |  | mmol/l |  |
| $\mathrm{Cpo}_{\mathrm{free\_api\_m7}}$ | `Cpo_free_api_m7` | unbound plasma concentration api\_m7 portal \[mM\] |  | mmol/l |  |
| $\mathrm{Cpo}_{\mathrm{blood\_api\_m7}}$ | `Cpo_blood_api_m7` | blood concentration api\_m7 portal \[mM\] |  | mmol/l |  |
| $\mathrm{Chv}_{\mathrm{api\_m7}}$ | `Chv_api_m7` | hepatic vein plasma concentration api\_m7 \[mM\] |  | mmol/l |  |
| $\mathrm{Chv}_{\mathrm{free\_api\_m7}}$ | `Chv_free_api_m7` | hepatic vein unbound plasma concentration api\_m7 \[mM\] |  | mmol/l |  |
| $\mathrm{Chv}_{\mathrm{blood\_api\_m7}}$ | `Chv_blood_api_m7` | hepatic vein blood concentration api\_m7 \[mM\] |  | mmol/l |  |
| $\mathrm{Carm}_{\mathrm{api\_m7}}$ | `Carm_api_m7` | arm vein plasma concentration api\_m7 \[mM\] |  | mmol/l |  |
| $\mathrm{Carm}_{\mathrm{free\_api\_m7}}$ | `Carm_free_api_m7` | arm vein unbound plasma concentration api\_m7 \[mM\] |  | mmol/l |  |
| $\mathrm{Carm}_{\mathrm{blood\_api\_m7}}$ | `Carm_blood_api_m7` | arm vein blood concentration api\_m7 \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{lu\_api}}$ | `Cout_lu_api` | outflow plasma concentration api lung \[mM\] |  | mmol/l |  |
| $\mathrm{LU}_{\mathrm{\_PS\_api}}$ | `LU__PS_api` | exchange plasma and tissue api \[l/min\] |  | l/min | ✓ |
| $\mathrm{LU}_{\mathrm{\_Cu\_ti\_api}}$ | `LU__Cu_ti_api` | unbound concentration api tissue lung \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{lu\_api\_m1}}$ | `Cout_lu_api_m1` | outflow plasma concentration api\_m1 lung \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{lu\_api\_m2}}$ | `Cout_lu_api_m2` | outflow plasma concentration api\_m2 lung \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{lu\_api\_m7}}$ | `Cout_lu_api_m7` | outflow plasma concentration api\_m7 lung \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{he\_api}}$ | `Cout_he_api` | outflow plasma concentration api heart \[mM\] |  | mmol/l |  |
| $\mathrm{HE}_{\mathrm{\_PS\_api}}$ | `HE__PS_api` | exchange plasma and tissue api \[l/min\] |  | l/min | ✓ |
| $\mathrm{HE}_{\mathrm{\_Cu\_ti\_api}}$ | `HE__Cu_ti_api` | unbound concentration api tissue heart \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{he\_api\_m1}}$ | `Cout_he_api_m1` | outflow plasma concentration api\_m1 heart \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{he\_api\_m2}}$ | `Cout_he_api_m2` | outflow plasma concentration api\_m2 heart \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{he\_api\_m7}}$ | `Cout_he_api_m7` | outflow plasma concentration api\_m7 heart \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{br\_api}}$ | `Cout_br_api` | outflow plasma concentration api brain \[mM\] |  | mmol/l |  |
| $\mathrm{BR}_{\mathrm{\_PS\_api}}$ | `BR__PS_api` | exchange plasma and tissue api \[l/min\] |  | l/min | ✓ |
| $\mathrm{BR}_{\mathrm{\_Cu\_ti\_api}}$ | `BR__Cu_ti_api` | unbound concentration api tissue brain \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{br\_api\_m1}}$ | `Cout_br_api_m1` | outflow plasma concentration api\_m1 brain \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{br\_api\_m2}}$ | `Cout_br_api_m2` | outflow plasma concentration api\_m2 brain \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{br\_api\_m7}}$ | `Cout_br_api_m7` | outflow plasma concentration api\_m7 brain \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{li\_api}}$ | `Cout_li_api` | outflow plasma concentration api liver \[mM\] |  | mmol/l |  |
| $\mathrm{LI}_{\mathrm{\_kps\_api}}$ | `LI__kps_api` | exchange per volume plasma and tissue api \[1/min\] | $42.9184549356223$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_PS\_api}}$ | `LI__PS_api` | exchange plasma and tissue api \[l/min\] |  | l/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_Cu\_ti\_api}}$ | `LI__Cu_ti_api` | unbound concentration api tissue liver \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{li\_api\_m1}}$ | `Cout_li_api_m1` | outflow plasma concentration api\_m1 liver \[mM\] |  | mmol/l |  |
| $\mathrm{LI}_{\mathrm{\_f\_water\_int}}$ | `LI__f_water_int` | water fraction interstitial fluid | $0.93049$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_f\_water\_pls}}$ | `LI__f_water_pls` | water fraction plasma | $0.93049$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_r\_protein\_int\_pls}}$ | `LI__r_protein_int_pls` | protein of the interstitial fluid relative to plasma | $0.37$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m1}}$ | `LI__K_int_pls_api_m1` | interstitial to plasma coefficient api\_m1 |  | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m1}}$ | `LI__K_cell_pls_api_m1` | intracellular to plasma coefficient api\_m1 |  | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_k\_vas}}$ | `LI__k_vas` | exchange plasma and interstitium per organ volume \[1/min\] | $1000$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_PS\_vas}}$ | `LI__PS_vas` | exchange plasma and interstitium \[l/min\] |  | l/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_kps\_api\_m1}}$ | `LI__kps_api_m1` | exchange per volume plasma and tissue api\_m1 \[1/min\] | $42.9184549356223$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_PS\_api\_m1}}$ | `LI__PS_api_m1` | exchange plasma and tissue api\_m1 \[l/min\] |  | l/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_Cu\_is\_api\_m1}}$ | `LI__Cu_is_api_m1` | unbound concentration api\_m1 interstitium liver \[mM\] |  | mmol/l |  |
| $\mathrm{LI}_{\mathrm{\_Cu\_ic\_api\_m1}}$ | `LI__Cu_ic_api_m1` | unbound concentration api\_m1 intracellular space liver \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{li\_api\_m2}}$ | `Cout_li_api_m2` | outflow plasma concentration api\_m2 liver \[mM\] |  | mmol/l |  |
| $\mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m2}}$ | `LI__K_int_pls_api_m2` | interstitial to plasma coefficient api\_m2 |  | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m2}}$ | `LI__K_cell_pls_api_m2` | intracellular to plasma coefficient api\_m2 |  | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_PS\_api\_m2}}$ | `LI__PS_api_m2` | exchange plasma and tissue api\_m2 \[l/min\] | $0$ | l/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_Cu\_is\_api\_m2}}$ | `LI__Cu_is_api_m2` | unbound concentration api\_m2 interstitium liver \[mM\] |  | mmol/l |  |
| $\mathrm{LI}_{\mathrm{\_Cu\_ic\_api\_m2}}$ | `LI__Cu_ic_api_m2` | unbound concentration api\_m2 intracellular space liver \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{li\_api\_m7}}$ | `Cout_li_api_m7` | outflow plasma concentration api\_m7 liver \[mM\] |  | mmol/l |  |
| $\mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m7}}$ | `LI__K_int_pls_api_m7` | interstitial to plasma coefficient api\_m7 |  | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m7}}$ | `LI__K_cell_pls_api_m7` | intracellular to plasma coefficient api\_m7 |  | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_kps\_api\_m7}}$ | `LI__kps_api_m7` | exchange per volume plasma and tissue api\_m7 \[1/min\] | $42.9184549356223$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_PS\_api\_m7}}$ | `LI__PS_api_m7` | exchange plasma and tissue api\_m7 \[l/min\] |  | l/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_Cu\_is\_api\_m7}}$ | `LI__Cu_is_api_m7` | unbound concentration api\_m7 interstitium liver \[mM\] |  | mmol/l |  |
| $\mathrm{LI}_{\mathrm{\_Cu\_ic\_api\_m7}}$ | `LI__Cu_ic_api_m7` | unbound concentration api\_m7 intracellular space liver \[mM\] |  | mmol/l |  |
| $\mathrm{LI}_{\mathrm{\_f\_cyp3a4}}$ | `LI__f_cyp3a4` | activity CYP3A4 | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_f\_sult1a1}}$ | `LI__f_sult1a1` | activity SULT1A1 | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_API2M\_k}}$ | `LI__API2M_k` | clearance per volume API2M \[1/min\] | $0.0787734166916452$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_M22M1\_k}}$ | `LI__M22M1_k` | clearance per volume M22M1 \[1/min\] | $0.00568318344918954$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_M1EXBI\_k}}$ | `LI__M1EXBI_k` | clearance per volume M1EXBI \[1/min\] | $0.0372352214739955$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_M2EXBI\_k}}$ | `LI__M2EXBI_k` | clearance per volume M2EXBI \[1/min\] | $0.0369505577062053$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_M7EXBI\_k}}$ | `LI__M7EXBI_k` | clearance per volume M7EXBI \[1/min\] | $0.132283842466316$ | 1/min | ✓ |
| $\mathrm{Cout}_{\mathrm{ki\_api}}$ | `Cout_ki_api` | outflow plasma concentration api kidney \[mM\] |  | mmol/l |  |
| $\mathrm{KI}_{\mathrm{\_PS\_api}}$ | `KI__PS_api` | exchange plasma and tissue api \[l/min\] |  | l/min | ✓ |
| $\mathrm{KI}_{\mathrm{\_Cu\_ti\_api}}$ | `KI__Cu_ti_api` | unbound concentration api tissue kidney \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{ki\_api\_m1}}$ | `Cout_ki_api_m1` | outflow plasma concentration api\_m1 kidney \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{ki\_api\_m2}}$ | `Cout_ki_api_m2` | outflow plasma concentration api\_m2 kidney \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{ki\_api\_m7}}$ | `Cout_ki_api_m7` | outflow plasma concentration api\_m7 kidney \[mM\] |  | mmol/l |  |
| $\mathrm{Rurine}_{\mathrm{api}}$ | `Rurine_api` | urinary excretion rate api \[mmole/min\] |  | mmol/min |  |
| $\mathrm{Rurine}_{\mathrm{api\_m1}}$ | `Rurine_api_m1` | urinary excretion rate api\_m1 \[mmole/min\] |  | mmol/min |  |
| $\mathrm{Rurine}_{\mathrm{api\_m7}}$ | `Rurine_api_m7` | urinary excretion rate api\_m7 \[mmole/min\] |  | mmol/min |  |
| $\mathrm{Cout}_{\mathrm{st\_api}}$ | `Cout_st_api` | outflow plasma concentration api stomach \[mM\] |  | mmol/l |  |
| $\mathrm{ST}_{\mathrm{\_PS\_api}}$ | `ST__PS_api` | exchange plasma and tissue api \[l/min\] |  | l/min | ✓ |
| $\mathrm{ST}_{\mathrm{\_Cu\_ti\_api}}$ | `ST__Cu_ti_api` | unbound concentration api tissue stomach \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{st\_api\_m1}}$ | `Cout_st_api_m1` | outflow plasma concentration api\_m1 stomach \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{st\_api\_m2}}$ | `Cout_st_api_m2` | outflow plasma concentration api\_m2 stomach \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{st\_api\_m7}}$ | `Cout_st_api_m7` | outflow plasma concentration api\_m7 stomach \[mM\] |  | mmol/l |  |
| $\mathrm{GU}_{\mathrm{\_Vgu}}$ | `GU__Vgu` | volume intestine \[l\] |  | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_vas\_gu}}$ | `GU__f_vas_gu` | vascular fraction intestine |  | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_wall}}$ | `GU__f_wall` | fraction of the intestinal tissue without the mucosa |  | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_T\_st}}$ | `GU__T_st` | transit time stomach \[min\] | $22.79$ | min | ✓ |
| $\mathrm{GU}_{\mathrm{\_T\_du}}$ | `GU__T_du` | transit time duodenum \[min\] | $14.3$ | min | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_area\_du}}$ | `GU__f_area_du` | absorption area factor duodenum | $1$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_T\_jej1}}$ | `GU__T_jej1` | transit time upper jejunum \[min\] | $35.74$ | min | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_area\_jej1}}$ | `GU__f_area_jej1` | absorption area factor upper jejunum | $1$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_T\_jej2}}$ | `GU__T_jej2` | transit time lower jejunum \[min\] | $35.74$ | min | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_area\_jej2}}$ | `GU__f_area_jej2` | absorption area factor lower jejunum | $1$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_T\_ile1}}$ | `GU__T_ile1` | transit time upper ileum \[min\] | $53.11$ | min | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_area\_ile1}}$ | `GU__f_area_ile1` | absorption area factor upper ileum | $1$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_T\_ile2}}$ | `GU__T_ile2` | transit time lower ileum \[min\] | $53.11$ | min | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_area\_ile2}}$ | `GU__f_area_ile2` | absorption area factor lower ileum | $1$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_T\_cae}}$ | `GU__T_cae` | transit time caecum \[min\] | $339$ | min | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_area\_cae}}$ | `GU__f_area_cae` | absorption area factor caecum | $0.0362$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_T\_asc}}$ | `GU__T_asc` | transit time colon ascendens \[min\] | $339$ | min | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_area\_asc}}$ | `GU__f_area_asc` | absorption area factor colon ascendens | $0.0362$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_T\_tra}}$ | `GU__T_tra` | transit time colon transversum \[min\] | $342$ | min | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_area\_tra}}$ | `GU__f_area_tra` | absorption area factor colon transversum | $0.0362$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_T\_des}}$ | `GU__T_des` | transit time colon descendens \[min\] | $342$ | min | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_area\_des}}$ | `GU__f_area_des` | absorption area factor colon descendens | $0.0362$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_T\_sig}}$ | `GU__T_sig` | transit time colon sigmoid \[min\] | $372$ | min | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_area\_sig}}$ | `GU__f_area_sig` | absorption area factor colon sigmoid | $0.0362$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_T\_rec}}$ | `GU__T_rec` | transit time rectum \[min\] | $372$ | min | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_area\_rec}}$ | `GU__f_area_rec` | absorption area factor rectum | $0.0362$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_T\_st\_fed}}$ | `GU__T_st_fed` | transit time stomach fed \[min\] | $63.48$ | min | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_mucosa\_volume}}$ | `GU__f_mucosa_volume` | mucosa fraction of the intestinal tissue | $0.1$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_mucosa\_flow}}$ | `GU__f_mucosa_flow` | mucosa fraction of the intestinal blood flow | $0.7$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_Qmu\_du}}$ | `GU__Qmu_du` | blood flow mucosa duodenum \[l/min\] |  | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_Qmu\_jej1}}$ | `GU__Qmu_jej1` | blood flow mucosa upper jejunum \[l/min\] |  | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_Qmu\_jej2}}$ | `GU__Qmu_jej2` | blood flow mucosa lower jejunum \[l/min\] |  | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_Qmu\_ile1}}$ | `GU__Qmu_ile1` | blood flow mucosa upper ileum \[l/min\] |  | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_Qmu\_ile2}}$ | `GU__Qmu_ile2` | blood flow mucosa lower ileum \[l/min\] |  | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_Qmu\_cae}}$ | `GU__Qmu_cae` | blood flow mucosa caecum \[l/min\] |  | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_Qmu\_asc}}$ | `GU__Qmu_asc` | blood flow mucosa colon ascendens \[l/min\] |  | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_Qmu\_tra}}$ | `GU__Qmu_tra` | blood flow mucosa colon transversum \[l/min\] |  | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_Qmu\_des}}$ | `GU__Qmu_des` | blood flow mucosa colon descendens \[l/min\] |  | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_Qmu\_sig}}$ | `GU__Qmu_sig` | blood flow mucosa colon sigmoid \[l/min\] |  | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_Qmu\_rec}}$ | `GU__Qmu_rec` | blood flow mucosa rectum \[l/min\] |  | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vmu\_total}}$ | `GU__Vmu_total` | volume mucosa \[l\] |  | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Qmu\_total}}$ | `GU__Qmu_total` | blood flow mucosa \[l/min\] |  | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_Qgu}}$ | `GU__Qgu` | blood flow intestine \[l/min\] |  | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_Qgu\_wall}}$ | `GU__Qgu_wall` | blood flow intestinal wall \[l/min\] |  | l/min | ✓ |
| $\mathrm{Cout}_{\mathrm{si\_api}}$ | `Cout_si_api` | outflow plasma concentration api small intestine \[mM\] |  | mmol/l |  |
| $\mathrm{GU}_{\mathrm{\_PS\_api}}$ | `GU__PS_api` | exchange plasma and tissue api \[l/min\] |  | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_Cu\_ti\_api}}$ | `GU__Cu_ti_api` | unbound concentration api tissue small intestine \[mM\] |  | mmol/l |  |
| $\mathrm{GU}_{\mathrm{\_K\_mu\_api}}$ | `GU__K_mu_api` | mucosa to plasma coefficient api |  | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_Cu\_mu\_du\_api}}$ | `GU__Cu_mu_du_api` | unbound concentration api mucosa duodenum \[mM\] |  | mmol/l |  |
| $\mathrm{GU}_{\mathrm{\_Cu\_mu\_jej1\_api}}$ | `GU__Cu_mu_jej1_api` | unbound concentration api mucosa upper jejunum \[mM\] |  | mmol/l |  |
| $\mathrm{GU}_{\mathrm{\_Cu\_mu\_jej2\_api}}$ | `GU__Cu_mu_jej2_api` | unbound concentration api mucosa lower jejunum \[mM\] |  | mmol/l |  |
| $\mathrm{GU}_{\mathrm{\_Cu\_mu\_ile1\_api}}$ | `GU__Cu_mu_ile1_api` | unbound concentration api mucosa upper ileum \[mM\] |  | mmol/l |  |
| $\mathrm{GU}_{\mathrm{\_Cu\_mu\_ile2\_api}}$ | `GU__Cu_mu_ile2_api` | unbound concentration api mucosa lower ileum \[mM\] |  | mmol/l |  |
| $\mathrm{GU}_{\mathrm{\_Cu\_mu\_cae\_api}}$ | `GU__Cu_mu_cae_api` | unbound concentration api mucosa caecum \[mM\] |  | mmol/l |  |
| $\mathrm{GU}_{\mathrm{\_Cu\_mu\_asc\_api}}$ | `GU__Cu_mu_asc_api` | unbound concentration api mucosa colon ascendens \[mM\] |  | mmol/l |  |
| $\mathrm{GU}_{\mathrm{\_Cu\_mu\_tra\_api}}$ | `GU__Cu_mu_tra_api` | unbound concentration api mucosa colon transversum \[mM\] |  | mmol/l |  |
| $\mathrm{GU}_{\mathrm{\_Cu\_mu\_des\_api}}$ | `GU__Cu_mu_des_api` | unbound concentration api mucosa colon descendens \[mM\] |  | mmol/l |  |
| $\mathrm{GU}_{\mathrm{\_Cu\_mu\_sig\_api}}$ | `GU__Cu_mu_sig_api` | unbound concentration api mucosa colon sigmoid \[mM\] |  | mmol/l |  |
| $\mathrm{GU}_{\mathrm{\_Cu\_mu\_rec\_api}}$ | `GU__Cu_mu_rec_api` | unbound concentration api mucosa rectum \[mM\] |  | mmol/l |  |
| $\mathrm{GU}_{\mathrm{\_kdis\_api}}$ | `GU__kdis_api` | dissolution rate api \[1/min\] |  | 1/min |  |
| $\mathrm{Cout}_{\mathrm{si\_api\_m1}}$ | `Cout_si_api_m1` | outflow plasma concentration api\_m1 small intestine \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{si\_api\_m2}}$ | `Cout_si_api_m2` | outflow plasma concentration api\_m2 small intestine \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{si\_api\_m7}}$ | `Cout_si_api_m7` | outflow plasma concentration api\_m7 small intestine \[mM\] |  | mmol/l |  |
| $\mathrm{GU}_{\mathrm{\_f\_abcb1}}$ | `GU__f_abcb1` | activity ABCB1 | $1$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_w\_uniform\_du}}$ | `GU__w_uniform_du` | share uniform mucosa duodenum |  | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_APISEC\_k}}$ | `GU__APISEC_k` | clearance per volume APISEC \[1/min\] | $0.269457165189852$ | 1/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_w\_uniform\_jej1}}$ | `GU__w_uniform_jej1` | share uniform mucosa upper jejunum |  | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_w\_uniform\_jej2}}$ | `GU__w_uniform_jej2` | share uniform mucosa lower jejunum |  | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_w\_uniform\_ile1}}$ | `GU__w_uniform_ile1` | share uniform mucosa upper ileum |  | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_w\_uniform\_ile2}}$ | `GU__w_uniform_ile2` | share uniform mucosa lower ileum |  | \- | ✓ |
| $T_{\mathrm{st\_eff}}$ | `T_st_eff` | transit time stomach \[min\] |  | min | ✓ |
| $\mathrm{Rabs}_{\mathrm{api}}$ | `Rabs_api` | rate of the absorption api \[mmole/min\] |  | mmol/min |  |
| $\mathrm{Reff}_{\mathrm{api}}$ | `Reff_api` | rate of the efflux into the intestinal lumen api \[mmole/min\] |  | mmol/min |  |
| $\mathrm{Rfeces}_{\mathrm{api}}$ | `Rfeces_api` | rate of the fecal excretion api \[mmole/min\] |  | mmol/min |  |
| $\mathrm{GU}_{\mathrm{\_Aabs\_api}}$ | `GU__Aabs_api` | amount absorbed api \[mmole\] | $0$ | mmol |  |
| $\mathrm{GU}_{\mathrm{\_Aapp\_api}}$ | `GU__Aapp_api` | oral dose applied api \[mmole\] | $0$ | mmol |  |
| $\mathrm{Fa}_{\mathrm{api}}$ | `Fa_api` | absorbed fraction of the oral dose api (gross) |  | \- |  |
| $\mathrm{Cout}_{\mathrm{sp\_api}}$ | `Cout_sp_api` | outflow plasma concentration api spleen \[mM\] |  | mmol/l |  |
| $\mathrm{SP}_{\mathrm{\_PS\_api}}$ | `SP__PS_api` | exchange plasma and tissue api \[l/min\] |  | l/min | ✓ |
| $\mathrm{SP}_{\mathrm{\_Cu\_ti\_api}}$ | `SP__Cu_ti_api` | unbound concentration api tissue spleen \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{sp\_api\_m1}}$ | `Cout_sp_api_m1` | outflow plasma concentration api\_m1 spleen \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{sp\_api\_m2}}$ | `Cout_sp_api_m2` | outflow plasma concentration api\_m2 spleen \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{sp\_api\_m7}}$ | `Cout_sp_api_m7` | outflow plasma concentration api\_m7 spleen \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{pa\_api}}$ | `Cout_pa_api` | outflow plasma concentration api pancreas \[mM\] |  | mmol/l |  |
| $\mathrm{PA}_{\mathrm{\_PS\_api}}$ | `PA__PS_api` | exchange plasma and tissue api \[l/min\] |  | l/min | ✓ |
| $\mathrm{PA}_{\mathrm{\_Cu\_ti\_api}}$ | `PA__Cu_ti_api` | unbound concentration api tissue pancreas \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{pa\_api\_m1}}$ | `Cout_pa_api_m1` | outflow plasma concentration api\_m1 pancreas \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{pa\_api\_m2}}$ | `Cout_pa_api_m2` | outflow plasma concentration api\_m2 pancreas \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{pa\_api\_m7}}$ | `Cout_pa_api_m7` | outflow plasma concentration api\_m7 pancreas \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{mu\_api}}$ | `Cout_mu_api` | outflow plasma concentration api muscle \[mM\] |  | mmol/l |  |
| $\mathrm{MU}_{\mathrm{\_PS\_api}}$ | `MU__PS_api` | exchange plasma and tissue api \[l/min\] |  | l/min | ✓ |
| $\mathrm{MU}_{\mathrm{\_Cu\_ti\_api}}$ | `MU__Cu_ti_api` | unbound concentration api tissue muscle \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{mu\_api\_m1}}$ | `Cout_mu_api_m1` | outflow plasma concentration api\_m1 muscle \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{mu\_api\_m2}}$ | `Cout_mu_api_m2` | outflow plasma concentration api\_m2 muscle \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{mu\_api\_m7}}$ | `Cout_mu_api_m7` | outflow plasma concentration api\_m7 muscle \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{sk\_api}}$ | `Cout_sk_api` | outflow plasma concentration api skin \[mM\] |  | mmol/l |  |
| $\mathrm{SK}_{\mathrm{\_PS\_api}}$ | `SK__PS_api` | exchange plasma and tissue api \[l/min\] |  | l/min | ✓ |
| $\mathrm{SK}_{\mathrm{\_Cu\_ti\_api}}$ | `SK__Cu_ti_api` | unbound concentration api tissue skin \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{sk\_api\_m1}}$ | `Cout_sk_api_m1` | outflow plasma concentration api\_m1 skin \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{sk\_api\_m2}}$ | `Cout_sk_api_m2` | outflow plasma concentration api\_m2 skin \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{sk\_api\_m7}}$ | `Cout_sk_api_m7` | outflow plasma concentration api\_m7 skin \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{ad\_api}}$ | `Cout_ad_api` | outflow plasma concentration api adipose \[mM\] |  | mmol/l |  |
| $\mathrm{AD}_{\mathrm{\_PS\_api}}$ | `AD__PS_api` | exchange plasma and tissue api \[l/min\] |  | l/min | ✓ |
| $\mathrm{AD}_{\mathrm{\_Cu\_ti\_api}}$ | `AD__Cu_ti_api` | unbound concentration api tissue adipose \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{ad\_api\_m1}}$ | `Cout_ad_api_m1` | outflow plasma concentration api\_m1 adipose \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{ad\_api\_m2}}$ | `Cout_ad_api_m2` | outflow plasma concentration api\_m2 adipose \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{ad\_api\_m7}}$ | `Cout_ad_api_m7` | outflow plasma concentration api\_m7 adipose \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{bo\_api}}$ | `Cout_bo_api` | outflow plasma concentration api bone \[mM\] |  | mmol/l |  |
| $\mathrm{BO}_{\mathrm{\_PS\_api}}$ | `BO__PS_api` | exchange plasma and tissue api \[l/min\] |  | l/min | ✓ |
| $\mathrm{BO}_{\mathrm{\_Cu\_ti\_api}}$ | `BO__Cu_ti_api` | unbound concentration api tissue bone \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{bo\_api\_m1}}$ | `Cout_bo_api_m1` | outflow plasma concentration api\_m1 bone \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{bo\_api\_m2}}$ | `Cout_bo_api_m2` | outflow plasma concentration api\_m2 bone \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{bo\_api\_m7}}$ | `Cout_bo_api_m7` | outflow plasma concentration api\_m7 bone \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{go\_api}}$ | `Cout_go_api` | outflow plasma concentration api gonads \[mM\] |  | mmol/l |  |
| $\mathrm{GO}_{\mathrm{\_PS\_api}}$ | `GO__PS_api` | exchange plasma and tissue api \[l/min\] |  | l/min | ✓ |
| $\mathrm{GO}_{\mathrm{\_Cu\_ti\_api}}$ | `GO__Cu_ti_api` | unbound concentration api tissue gonads \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{go\_api\_m1}}$ | `Cout_go_api_m1` | outflow plasma concentration api\_m1 gonads \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{go\_api\_m2}}$ | `Cout_go_api_m2` | outflow plasma concentration api\_m2 gonads \[mM\] |  | mmol/l |  |
| $\mathrm{Cout}_{\mathrm{go\_api\_m7}}$ | `Cout_go_api_m7` | outflow plasma concentration api\_m7 gonads \[mM\] |  | mmol/l |  |
| $\mathrm{COAG}_{\mathrm{\_INR\_ref}}$ | `COAG__INR_ref` | INR reference | $1$ | \- | ✓ |
| $\mathrm{COAG}_{\mathrm{\_PT\_ref}}$ | `COAG__PT_ref` | prothrombin time reference | $12.5$ | s | ✓ |
| $\mathrm{COAG}_{\mathrm{\_aPTT\_ref}}$ | `COAG__aPTT_ref` | activated partial thromboplastin reference | $28.4$ | s | ✓ |
| $\mathrm{COAG}_{\mathrm{\_mPT\_ref}}$ | `COAG__mPT_ref` | modified prothrombin time reference | $53.4$ | s | ✓ |
| $\mathrm{COAG}_{\mathrm{\_INR}}$ | `COAG__INR` | INR |  | \- |  |
| $\mathrm{COAG}_{\mathrm{\_PT}}$ | `COAG__PT` | prothrombin time |  | s |  |
| $\mathrm{COAG}_{\mathrm{\_aPTT}}$ | `COAG__aPTT` | activated partial thromboplastin |  | s |  |
| $\mathrm{COAG}_{\mathrm{\_mPT}}$ | `COAG__mPT` | modified prothrombin time |  | s |  |
| $\mathrm{COAG}_{\mathrm{\_antiXa\_activity}}$ | `COAG__antiXa_activity` | anti-FXa activity |  | 1/ml |  |
| $\mathrm{COAG}_{\mathrm{\_antiXa\_activity\_gram}}$ | `COAG__antiXa_activity_gram` | anti-FXa activity (apixaban calibrated) |  | ng/ml |  |
| $\mathrm{COAG}_{\mathrm{\_INR\_change}}$ | `COAG__INR_change` | INR change |  | \- |  |
| $\mathrm{COAG}_{\mathrm{\_INR\_ratio}}$ | `COAG__INR_ratio` | INR ratio |  | \- |  |
| $\mathrm{COAG}_{\mathrm{\_INR\_relchange}}$ | `COAG__INR_relchange` | INR relative change |  | \- |  |
| $\mathrm{COAG}_{\mathrm{\_PT\_change}}$ | `COAG__PT_change` | prothrombin time change |  | s |  |
| $\mathrm{COAG}_{\mathrm{\_PT\_ratio}}$ | `COAG__PT_ratio` | prothrombin time ratio |  | \- |  |
| $\mathrm{COAG}_{\mathrm{\_PT\_relchange}}$ | `COAG__PT_relchange` | prothrombin time relative change |  | \- |  |
| $\mathrm{COAG}_{\mathrm{\_aPTT\_change}}$ | `COAG__aPTT_change` | activated partial thromboplastin change |  | s |  |
| $\mathrm{COAG}_{\mathrm{\_aPTT\_ratio}}$ | `COAG__aPTT_ratio` | activated partial thromboplastin ratio |  | \- |  |
| $\mathrm{COAG}_{\mathrm{\_aPTT\_relchange}}$ | `COAG__aPTT_relchange` | activated partial thromboplastin relative change |  | \- |  |
| $\mathrm{COAG}_{\mathrm{\_mPT\_change}}$ | `COAG__mPT_change` | modified prothrombin time change |  | s |  |
| $\mathrm{COAG}_{\mathrm{\_mPT\_ratio}}$ | `COAG__mPT_ratio` | modified prothrombin time ratio |  | \- |  |
| $\mathrm{COAG}_{\mathrm{\_mPT\_relchange}}$ | `COAG__mPT_relchange` | modified prothrombin time relative change |  | \- |  |
| $\mathrm{COAG}_{\mathrm{\_slope\_api\_INR}}$ | `COAG__slope_api_INR` | relative increase of the INR per apixaban concentration | $485.385979198431$ | l/mmol | ✓ |
| $\mathrm{COAG}_{\mathrm{\_slope\_api\_PT}}$ | `COAG__slope_api_PT` | relative increase of the prothrombin time per apixaban concentration | $974.831512812244$ | l/mmol | ✓ |
| $\mathrm{COAG}_{\mathrm{\_Emax\_mPT}}$ | `COAG__Emax_mPT` | maximal relative increase of the modified prothrombin time | $6.05368718520111$ | \- | ✓ |
| $\mathrm{COAG}_{\mathrm{\_EC50\_api\_mPT}}$ | `COAG__EC50_api_mPT` | apixaban concentration of the half-maximal effect on the modified prothrombin time | $0.00191219547173888$ | mmol/l | ✓ |
| $\mathrm{COAG}_{\mathrm{\_Emax\_aPTT}}$ | `COAG__Emax_aPTT` | maximal relative increase of the activated partial thromboplastin | $0.359659187476217$ | \- | ✓ |
| $\mathrm{COAG}_{\mathrm{\_EC50\_api\_aPTT}}$ | `COAG__EC50_api_aPTT` | apixaban concentration of the half-maximal effect on the activated partial thromboplastin | $0.000720649954915313$ | mmol/l | ✓ |
| $\mathrm{COAG}_{\mathrm{\_antiXa\_slope}}$ | `COAG__antiXa_slope` | anti-FXa activity per apixaban concentration | $5429.38716208968$ | l/ml/mmol | ✓ |
| $\mathrm{COAG}_{\mathrm{\_antiXa\_gram\_slope}}$ | `COAG__antiXa_gram_slope` | anti-FXa activity (apixaban calibrated) per apixaban concentration | $430016.929599535$ | ng·l/ml/mmol | ✓ |

## Initial assignments and assignment rules

The initial assignments set the values at $t = 0$:

$$
\begin{aligned}
\mathrm{BSA}_{\mathrm{ref}} &= 0.007184 \cdot \mathopen{}\left(\frac{\mathrm{BW}_{\mathrm{ref}}}{1}\right)^{0.425} \cdot \mathopen{}\left(\frac{\mathrm{HEIGHT}_{\mathrm{ref}}}{1}\right)^{0.725} \\[1ex]
\mathrm{FFM}_{\mathrm{ref}} &= \frac{\mathrm{BW}_{\mathrm{ref}} \cdot 9270}{8780 + \frac{244 \cdot \frac{\mathrm{BW}_{\mathrm{ref}}}{1}}{\mathopen{}\left(\frac{\mathrm{HEIGHT}_{\mathrm{ref}}}{100}\right)^{2}}} \cdot \mathrm{fage}_{\mathrm{FFM}} \\[1ex]
\mathrm{HCT}_{\mathrm{ref}} &= 0.38 \cdot \mathrm{fage}_{\mathrm{HCT}} \\[1ex]
\mathrm{fage}_{\mathrm{Qrest}} &= \frac{1 - 0.130406433384047 \cdot \mathrm{fage}_{\mathrm{Qbr}} \cdot \mathrm{fsex}_{\mathrm{Qbr}}}{0.869593566615953} \\[1ex]
\mathrm{fage}_{\mathrm{Qother}} &= \frac{1 - 0.130406433384047 - 0.0706368180830254 \cdot \mathrm{fage}_{\mathrm{Qli}} - 0.0543360139100196 \cdot \mathrm{fage}_{\mathrm{Qli}} - 0.0108672027820039 \cdot \mathrm{fage}_{\mathrm{Qli}} - 0.119539230602043 \cdot \mathrm{fage}_{\mathrm{Qli}} - 0.0326016083460117 \cdot \mathrm{fage}_{\mathrm{Qli}} - 0.0108672027820039 \cdot \mathrm{fage}_{\mathrm{Qli}} - 0.184742447294067 \cdot \mathrm{fage}_{\mathrm{Qki}}}{0.386003042816779} \\[1ex]
\mathrm{fQhe} &= 0.0543360139100196 \cdot \mathrm{fage}_{\mathrm{Qrest}} \cdot \mathrm{fage}_{\mathrm{Qother}} \\[1ex]
\mathrm{fQbr} &= 0.130406433384047 \cdot \mathrm{fage}_{\mathrm{Qbr}} \cdot \mathrm{fsex}_{\mathrm{Qbr}} \\[1ex]
\mathrm{fQli} &= 0.0706368180830254 \cdot \mathrm{fage}_{\mathrm{Qrest}} \cdot \mathrm{fage}_{\mathrm{Qli}} \\[1ex]
\mathrm{fQki} &= 0.184742447294067 \cdot \mathrm{fage}_{\mathrm{Qrest}} \cdot \mathrm{fage}_{\mathrm{Qki}} \\[1ex]
\mathrm{fQst} &= 0.0108672027820039 \cdot \mathrm{fage}_{\mathrm{Qrest}} \cdot \mathrm{fage}_{\mathrm{Qli}} \\[1ex]
\mathrm{fQsi} &= 0.119539230602043 \cdot \mathrm{fage}_{\mathrm{Qrest}} \cdot \mathrm{fage}_{\mathrm{Qli}} \\[1ex]
\mathrm{fQla} &= 0.0543360139100196 \cdot \mathrm{fage}_{\mathrm{Qrest}} \cdot \mathrm{fage}_{\mathrm{Qli}} \\[1ex]
\mathrm{fQsp} &= 0.0326016083460117 \cdot \mathrm{fage}_{\mathrm{Qrest}} \cdot \mathrm{fage}_{\mathrm{Qli}} \\[1ex]
\mathrm{fQpa} &= 0.0108672027820039 \cdot \mathrm{fage}_{\mathrm{Qrest}} \cdot \mathrm{fage}_{\mathrm{Qli}} \\[1ex]
\mathrm{fQmu} &= 0.130406433384047 \cdot \mathrm{fage}_{\mathrm{Qrest}} \cdot \mathrm{fage}_{\mathrm{Qother}} \\[1ex]
\mathrm{fQsk} &= 0.0543360139100196 \cdot \mathrm{fage}_{\mathrm{Qrest}} \cdot \mathrm{fage}_{\mathrm{Qother}} \\[1ex]
\mathrm{fQad} &= 0.0923712236470333 \cdot \mathrm{fage}_{\mathrm{Qrest}} \cdot \mathrm{fage}_{\mathrm{Qother}} \\[1ex]
\mathrm{fQbo} &= 0.0543360139100196 \cdot \mathrm{fage}_{\mathrm{Qrest}} \cdot \mathrm{fage}_{\mathrm{Qother}} \\[1ex]
\mathrm{fQgo} &= 0.000217344055640078 \cdot \mathrm{fage}_{\mathrm{Qrest}} \cdot \mathrm{fage}_{\mathrm{Qother}} \\[1ex]
\mathrm{BMI} &= \frac{\frac{\mathrm{BW}}{1}}{\mathopen{}\left(\frac{\mathrm{HEIGHT}}{100}\right)^{2}} \cdot 1 \\[1ex]
\mathrm{BSA} &= 0.007184 \cdot \mathopen{}\left(\frac{\mathrm{BW}}{1}\right)^{0.425} \cdot \mathopen{}\left(\frac{\mathrm{HEIGHT}}{1}\right)^{0.725} \\[1ex]
\mathrm{FFM} &= \frac{\mathrm{BW} \cdot 9270}{8780 + \frac{244 \cdot \mathrm{BMI}}{1}} \cdot \mathrm{fage}_{\mathrm{FFM}} \\[1ex]
\mathrm{Mbr} &= \mathrm{Mbr}_{\mathrm{ref}} \\[1ex]
\mathrm{Msk} &= \frac{\mathrm{Msk}_{\mathrm{ref}} \cdot \mathrm{BSA}}{\mathrm{BSA}_{\mathrm{ref}}} \\[1ex]
\mathrm{SV}_{\mathrm{tis}} &= \frac{\mathrm{FFM} - \mathrm{Mbr} - \mathrm{Msk}}{\mathrm{FFM}_{\mathrm{ref}} - \mathrm{Mbr}_{\mathrm{ref}} - \mathrm{Msk}_{\mathrm{ref}}} \\[1ex]
\mathrm{Vblood} &= \mathrm{Vblood}_{\mathrm{ref}} \cdot \mathrm{SV}_{\mathrm{tis}} \\[1ex]
\mathrm{Mlu} &= \mathrm{Mlu}_{\mathrm{ref}} \cdot \mathrm{SV}_{\mathrm{tis}} \\[1ex]
\mathrm{Mhe} &= \mathrm{Mhe}_{\mathrm{ref}} \cdot \mathrm{SV}_{\mathrm{tis}} \\[1ex]
\mathrm{Mli} &= \mathrm{Mli}_{\mathrm{ref}} \cdot \mathrm{SV}_{\mathrm{tis}} \\[1ex]
\mathrm{Mst} &= \mathrm{Mst}_{\mathrm{ref}} \cdot \mathrm{SV}_{\mathrm{tis}} \\[1ex]
\mathrm{Msi} &= \mathrm{Msi}_{\mathrm{ref}} \cdot \mathrm{SV}_{\mathrm{tis}} \\[1ex]
\mathrm{Mla} &= \mathrm{Mla}_{\mathrm{ref}} \cdot \mathrm{SV}_{\mathrm{tis}} \\[1ex]
\mathrm{Msp} &= \mathrm{Msp}_{\mathrm{ref}} \cdot \mathrm{SV}_{\mathrm{tis}} \\[1ex]
\mathrm{Mpa} &= \mathrm{Mpa}_{\mathrm{ref}} \cdot \mathrm{SV}_{\mathrm{tis}} \\[1ex]
\mathrm{Mmu} &= \mathrm{Mmu}_{\mathrm{ref}} \cdot \mathrm{SV}_{\mathrm{tis}} \\[1ex]
\mathrm{Mbo} &= \mathrm{Mbo}_{\mathrm{ref}} \cdot \mathrm{SV}_{\mathrm{tis}} \\[1ex]
\mathrm{Mgo} &= \mathrm{Mgo}_{\mathrm{ref}} \cdot \mathrm{SV}_{\mathrm{tis}} \\[1ex]
\mathrm{Vlu} &= \frac{\mathrm{Mlu}}{1} + 0.125 \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Vhe} &= \frac{\mathrm{Mhe}}{1} + 0.01 \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Vbr} &= \frac{\mathrm{Mbr}}{1.04} + 0.012 \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Vli} &= \frac{\mathrm{Mli}}{1} + 0.1 \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Vst} &= \frac{\mathrm{Mst}}{1.045} + 0.01 \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Vsi} &= \frac{\mathrm{Msi}}{1.045} + 0.038 \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Vla} &= \frac{\mathrm{Mla}}{1.045} + 0.022 \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Vsp} &= \frac{\mathrm{Msp}}{1.06} + 0.014 \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Vpa} &= \frac{\mathrm{Mpa}}{1} + 0.006 \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Vmu} &= \frac{\mathrm{Mmu}}{1} + 0.105 \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Vsk} &= \frac{\mathrm{Msk}}{1.1} + 0.03 \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Vbo} &= \frac{\mathrm{Mbo}}{1.3} + 0.07 \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Vgo} &= \frac{\mathrm{Mgo}}{1.05} + 0.0002 \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Var} &= \mathrm{fVar} \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Vve} &= \mathrm{fVve} \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Vpo} &= \mathrm{fVpo} \cdot \mathrm{Vblood} \\[1ex]
f_{\mathrm{vas\_lu}} &= \frac{0.125 \cdot \mathrm{Vblood}}{\mathrm{Vlu}} \\[1ex]
\mathrm{LU}_{\mathrm{\_Vti}} &= \mathrm{Vlu} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_lu}}\right) \\[1ex]
f_{\mathrm{int\_lu}} &= 0.2 \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_lu}}\right) \\[1ex]
f_{\mathrm{vas\_he}} &= \frac{0.01 \cdot \mathrm{Vblood}}{\mathrm{Vhe}} \\[1ex]
\mathrm{HE}_{\mathrm{\_Vti}} &= \mathrm{Vhe} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_he}}\right) \\[1ex]
f_{\mathrm{int\_he}} &= 0.250028898393249 \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_he}}\right) \\[1ex]
f_{\mathrm{vas\_br}} &= \frac{0.012 \cdot \mathrm{Vblood}}{\mathrm{Vbr}} \\[1ex]
\mathrm{BR}_{\mathrm{\_Vti}} &= \mathrm{Vbr} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_br}}\right) \\[1ex]
f_{\mathrm{int\_br}} &= 0.0050004668485647 \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_br}}\right) \\[1ex]
f_{\mathrm{vas\_li}} &= \frac{0.1 \cdot \mathrm{Vblood}}{\mathrm{Vli}} \\[1ex]
f_{\mathrm{int\_li}} &= 0.23002173635085 \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_li}}\right) \\[1ex]
f_{\mathrm{vas\_st}} &= \frac{0.01 \cdot \mathrm{Vblood}}{\mathrm{Vst}} \\[1ex]
\mathrm{ST}_{\mathrm{\_Vti}} &= \mathrm{Vst} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_st}}\right) \\[1ex]
f_{\mathrm{int\_st}} &= 0.0959974176888315 \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_st}}\right) \\[1ex]
f_{\mathrm{vas\_si}} &= \frac{0.038 \cdot \mathrm{Vblood}}{\mathrm{Vsi}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Vmu\_du}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_volume}} \cdot \mathrm{Vsi} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_si}}\right) \cdot 0.0744792 \\[1ex]
\mathrm{GU}_{\mathrm{\_Vmu\_jej1}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_volume}} \cdot \mathrm{Vsi} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_si}}\right) \cdot 0.186146 \\[1ex]
\mathrm{GU}_{\mathrm{\_Vmu\_jej2}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_volume}} \cdot \mathrm{Vsi} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_si}}\right) \cdot 0.186146 \\[1ex]
\mathrm{GU}_{\mathrm{\_Vmu\_ile1}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_volume}} \cdot \mathrm{Vsi} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_si}}\right) \cdot 0.276615 \\[1ex]
\mathrm{GU}_{\mathrm{\_Vmu\_ile2}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_volume}} \cdot \mathrm{Vsi} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_si}}\right) \cdot 0.276615 \\[1ex]
f_{\mathrm{int\_si}} &= 0.0959989934574736 \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_si}}\right) \\[1ex]
f_{\mathrm{vas\_la}} &= \frac{0.022 \cdot \mathrm{Vblood}}{\mathrm{Vla}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Vmu\_cae}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_volume}} \cdot \mathrm{Vla} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_la}}\right) \cdot 0.160969 \\[1ex]
\mathrm{GU}_{\mathrm{\_Vmu\_asc}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_volume}} \cdot \mathrm{Vla} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_la}}\right) \cdot 0.160969 \\[1ex]
\mathrm{GU}_{\mathrm{\_Vmu\_tra}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_volume}} \cdot \mathrm{Vla} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_la}}\right) \cdot 0.162393 \\[1ex]
\mathrm{GU}_{\mathrm{\_Vmu\_des}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_volume}} \cdot \mathrm{Vla} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_la}}\right) \cdot 0.162393 \\[1ex]
\mathrm{GU}_{\mathrm{\_Vmu\_sig}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_volume}} \cdot \mathrm{Vla} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_la}}\right) \cdot 0.176638 \\[1ex]
\mathrm{GU}_{\mathrm{\_Vmu\_rec}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_volume}} \cdot \mathrm{Vla} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_la}}\right) \cdot 0.176638 \\[1ex]
f_{\mathrm{int\_la}} &= 0.0960029977516862 \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_la}}\right) \\[1ex]
f_{\mathrm{vas\_sp}} &= \frac{0.014 \cdot \mathrm{Vblood}}{\mathrm{Vsp}} \\[1ex]
\mathrm{SP}_{\mathrm{\_Vti}} &= \mathrm{Vsp} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_sp}}\right) \\[1ex]
f_{\mathrm{int\_sp}} &= 0.254950137303078 \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_sp}}\right) \\[1ex]
f_{\mathrm{vas\_pa}} &= \frac{0.006 \cdot \mathrm{Vblood}}{\mathrm{Vpa}} \\[1ex]
\mathrm{PA}_{\mathrm{\_Vti}} &= \mathrm{Vpa} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_pa}}\right) \\[1ex]
f_{\mathrm{int\_pa}} &= 0.0959966539196941 \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_pa}}\right) \\[1ex]
f_{\mathrm{vas\_mu}} &= \frac{0.105 \cdot \mathrm{Vblood}}{\mathrm{Vmu}} \\[1ex]
\mathrm{MU}_{\mathrm{\_Vti}} &= \mathrm{Vmu} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_mu}}\right) \\[1ex]
f_{\mathrm{int\_mu}} &= 0.150029678449352 \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_mu}}\right) \\[1ex]
f_{\mathrm{vas\_sk}} &= \frac{0.03 \cdot \mathrm{Vblood}}{\mathrm{Vsk}} \\[1ex]
\mathrm{SK}_{\mathrm{\_Vti}} &= \mathrm{Vsk} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_sk}}\right) \\[1ex]
f_{\mathrm{int\_sk}} &= 0.599993664269649 \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_sk}}\right) \\[1ex]
f_{\mathrm{vas\_bo}} &= \frac{0.07 \cdot \mathrm{Vblood}}{\mathrm{Vbo}} \\[1ex]
\mathrm{BO}_{\mathrm{\_Vti}} &= \mathrm{Vbo} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_bo}}\right) \\[1ex]
f_{\mathrm{int\_bo}} &= 0.100002091000335 \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_bo}}\right) \\[1ex]
f_{\mathrm{vas\_go}} &= \frac{0.0002 \cdot \mathrm{Vblood}}{\mathrm{Vgo}} \\[1ex]
\mathrm{GO}_{\mathrm{\_Vti}} &= \mathrm{Vgo} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_go}}\right) \\[1ex]
f_{\mathrm{int\_go}} &= 0.0960030084882347 \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_go}}\right) \\[1ex]
\mathrm{CO}_{\mathrm{base}} &= \mathrm{CO}_{\mathrm{ref}} \cdot \mathrm{SV}_{\mathrm{tis}} \cdot f_{\mathrm{cardiac\_function}} \cdot \mathrm{fsex}_{\mathrm{CO}} \\[1ex]
\mathrm{fcp}_{\mathrm{functional\_liver}} &= \begin{cases} 1 & \text{if } \mathrm{CP}_{\mathrm{severity}} \leq 0 \\ 1 - 0.1018 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 0\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 1 \\ 0.8982 - 0.1128 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 1\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 2 \\ 0.7854 - 0.1199 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 2\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 3 \\ 0.6655 & \text{otherwise} \end{cases} \\[1ex]
f_{\mathrm{functional}} &= \mathrm{fcp}_{\mathrm{functional\_liver}} \\[1ex]
\mathrm{LI}_{\mathrm{\_Vis}} &= \mathrm{Vli} \cdot f_{\mathrm{int\_li}} \cdot f_{\mathrm{functional}} \\[1ex]
\mathrm{LI}_{\mathrm{\_Vic}} &= \mathrm{Vli} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_li}} - f_{\mathrm{int\_li}}\right) \cdot f_{\mathrm{functional}} \\[1ex]
\mathrm{LI}_{\mathrm{\_Vti}} &= \mathrm{Vli} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_li}}\right) \cdot f_{\mathrm{functional}} \\[1ex]
\mathrm{fcp}_{\mathrm{hepatic\_artery\_flow}} &= \begin{cases} 1 & \text{if } \mathrm{CP}_{\mathrm{severity}} \leq 0 \\ 1 + 0.3 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 0\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 1 \\ 1.3 + 1 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 1\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 2 \\ 2.3 + 1.1 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 2\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 3 \\ 3.4 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fcp}_{\mathrm{kidney\_flow}} &= \begin{cases} 1 & \text{if } \mathrm{CP}_{\mathrm{severity}} \leq 0 \\ 1 - 0.12 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 0\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 1 \\ 0.88 - 0.23 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 1\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 2 \\ 0.65 - 0.17 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 2\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 3 \\ 0.48 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fcp}_{\mathrm{cardiac\_index}} &= \begin{cases} 1 & \text{if } \mathrm{CP}_{\mathrm{severity}} \leq 0 \\ 1 + 0.099 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 0\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 1 \\ 1.099 + 0.111 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 1\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 2 \\ 1.21 + 0.15 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 2\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 3 \\ 1.36 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fcp}_{\mathrm{gfr}} &= \begin{cases} 1 & \text{if } \mathrm{CP}_{\mathrm{severity}} \leq 0 \\ 1 + 0 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 0\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 1 \\ 1 - 0.3 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 1\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 2 \\ 0.7 - 0.34 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 2\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 3 \\ 0.36 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fcp}_{\mathrm{albumin}} &= \begin{cases} 1 & \text{if } \mathrm{CP}_{\mathrm{severity}} \leq 0 \\ 1 - 0.1355 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 0\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 1 \\ 0.8645 - 0.1847 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 1\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 2 \\ 0.6798 - 0.1906 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 2\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 3 \\ 0.4892 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fcp}_{\mathrm{agp}} &= \begin{cases} 1 & \text{if } \mathrm{CP}_{\mathrm{severity}} \leq 0 \\ 1 - 0.4 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 0\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 1 \\ 0.6 - 0.0399999999999999 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 1\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 2 \\ 0.56 - 0.26 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 2\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 3 \\ 0.3 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fcp}_{\mathrm{hematocrit}} &= \begin{cases} 1 & \text{if } \mathrm{CP}_{\mathrm{severity}} \leq 0 \\ 1 - 0.0768 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 0\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 1 \\ 0.9232 - 0.1821 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 1\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 2 \\ 0.7411 - 0.0179 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 2\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 3 \\ 0.7232 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fcp}_{\mathrm{shunt}} &= \begin{cases} 0 & \text{if } \mathrm{CP}_{\mathrm{severity}} \leq 0 \\ 0 + 0.399489795918367 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 0\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 1 \\ 0.399489795918367 + 0.298469387755102 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 1\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 2 \\ 0.697959183673469 + 0.114795918367347 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 2\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 3 \\ 0.812755102040816 & \text{otherwise} \end{cases} \\[1ex]
f_{\mathrm{shunt}} &= \mathrm{fcp}_{\mathrm{shunt}} \\[1ex]
\mathrm{fcp}_{\mathrm{cyp3a4}} &= \begin{cases} 1 & \text{if } \mathrm{CP}_{\mathrm{severity}} \leq 0 \\ 1 - 0.4019 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 0\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 1 \\ 0.5981 - 0.2532 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 1\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 2 \\ 0.3449 - 0.1499 \cdot \mathopen{}\left(\mathrm{CP}_{\mathrm{severity}} - 2\right) & \text{if } \mathrm{CP}_{\mathrm{severity}} < 3 \\ 0.195 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fcp}_{\mathrm{rest\_flow}} &= 1 + \frac{\mathrm{fcp}_{\mathrm{cardiac\_index}} - 1 - \mathrm{fQli} \cdot \mathopen{}\left(\mathrm{fcp}_{\mathrm{hepatic\_artery\_flow}} - 1\right) - \mathrm{fQki} \cdot \mathopen{}\left(\mathrm{fcp}_{\mathrm{kidney\_flow}} - 1\right)}{\mathrm{fQhe} + \mathrm{fQmu} + \mathrm{fQsk} + \mathrm{fQad} + \mathrm{fQbo} + \mathrm{fQgo}} \\[1ex]
\mathrm{eGFR} &= 0.114698036359284 \cdot f_{\mathrm{renal\_function}} \\[1ex]
\mathrm{fckd}_{\mathrm{plasma\_protein}} &= \begin{cases} 1 & \text{if } \mathrm{eGFR} \geq 0.09 \\ 1 & \text{if } \mathrm{eGFR} \geq 0.075 \\ 1 + \frac{0.45 \cdot \mathopen{}\left(0.075 - \mathrm{eGFR}\right)}{0.03} & \text{if } \mathrm{eGFR} \geq 0.045 \\ 1.45 + \frac{0.75 \cdot \mathopen{}\left(0.045 - \mathrm{eGFR}\right)}{0.0225} & \text{if } \mathrm{eGFR} \geq 0.0225 \\ 2.2 + \frac{0.3 \cdot \mathopen{}\left(0.0225 - \mathrm{eGFR}\right)}{0.015} & \text{if } \mathrm{eGFR} \geq 0.0075 \\ 2.5 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fckd}_{\mathrm{hematocrit}} &= \begin{cases} 1 & \text{if } \mathrm{eGFR} \geq 0.09 \\ 1 + \frac{-0.0651 \cdot \mathopen{}\left(0.09 - \mathrm{eGFR}\right)}{0.015} & \text{if } \mathrm{eGFR} \geq 0.075 \\ 0.9349 + \frac{-0.0491999999999999 \cdot \mathopen{}\left(0.075 - \mathrm{eGFR}\right)}{0.03} & \text{if } \mathrm{eGFR} \geq 0.045 \\ 0.8857 + \frac{-0.0948 \cdot \mathopen{}\left(0.045 - \mathrm{eGFR}\right)}{0.0225} & \text{if } \mathrm{eGFR} \geq 0.0225 \\ 0.7909 + \frac{-0.0803 \cdot \mathopen{}\left(0.0225 - \mathrm{eGFR}\right)}{0.015} & \text{if } \mathrm{eGFR} \geq 0.0075 \\ 0.7106 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fckd}_{\mathrm{kidney\_volume}} &= \begin{cases} 1 & \text{if } \mathrm{eGFR} \geq 0.09 \\ 1 & \text{if } \mathrm{eGFR} \geq 0.075 \\ 1 & \text{if } \mathrm{eGFR} \geq 0.045 \\ 1 & \text{if } \mathrm{eGFR} \geq 0.0225 \\ 1 & \text{if } \mathrm{eGFR} \geq 0.0075 \\ 1 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fckd}_{\mathrm{kidney\_flow}} &= \begin{cases} 1 & \text{if } \mathrm{eGFR} \geq 0.09 \\ 1 + \frac{-0.2288 \cdot \mathopen{}\left(0.09 - \mathrm{eGFR}\right)}{0.015} & \text{if } \mathrm{eGFR} \geq 0.075 \\ 0.7712 + \frac{-0.2145 \cdot \mathopen{}\left(0.075 - \mathrm{eGFR}\right)}{0.03} & \text{if } \mathrm{eGFR} \geq 0.045 \\ 0.5567 + \frac{-0.1384 \cdot \mathopen{}\left(0.045 - \mathrm{eGFR}\right)}{0.0225} & \text{if } \mathrm{eGFR} \geq 0.0225 \\ 0.4183 + \frac{-0.0839 \cdot \mathopen{}\left(0.0225 - \mathrm{eGFR}\right)}{0.015} & \text{if } \mathrm{eGFR} \geq 0.0075 \\ 0.3344 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fckd}_{\mathrm{gastric\_emptying\_time}} &= \begin{cases} 1 & \text{if } \mathrm{eGFR} \geq 0.09 \\ 1 & \text{if } \mathrm{eGFR} \geq 0.075 \\ 1 & \text{if } \mathrm{eGFR} \geq 0.045 \\ 1 + \frac{0.6 \cdot \mathopen{}\left(0.045 - \mathrm{eGFR}\right)}{0.0225} & \text{if } \mathrm{eGFR} \geq 0.0225 \\ 1.6 & \text{if } \mathrm{eGFR} \geq 0.0075 \\ 1.6 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fckd}_{\mathrm{si\_transit\_time}} &= \begin{cases} 1 & \text{if } \mathrm{eGFR} \geq 0.09 \\ 1 & \text{if } \mathrm{eGFR} \geq 0.075 \\ 1 & \text{if } \mathrm{eGFR} \geq 0.045 \\ 1 + \frac{0.4 \cdot \mathopen{}\left(0.045 - \mathrm{eGFR}\right)}{0.0225} & \text{if } \mathrm{eGFR} \geq 0.0225 \\ 1.4 & \text{if } \mathrm{eGFR} \geq 0.0075 \\ 1.4 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fckd}_{\mathrm{cyp3a4}} &= \begin{cases} 1 & \text{if } \mathrm{eGFR} \geq 0.09 \\ 1 & \text{if } \mathrm{eGFR} \geq 0.075 \\ 1 & \text{if } \mathrm{eGFR} \geq 0.045 \\ 1 & \text{if } \mathrm{eGFR} \geq 0.0225 \\ 1 & \text{if } \mathrm{eGFR} \geq 0.0075 \\ 1 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fhf}_{\mathrm{liver\_flow}} &= \begin{cases} 1 & \text{if } \mathrm{HF}_{\mathrm{severity}} \leq 0 \\ 1 - 0.1272 \cdot \mathopen{}\left(\mathrm{HF}_{\mathrm{severity}} - 0\right) & \text{if } \mathrm{HF}_{\mathrm{severity}} < 1 \\ 0.8728 - 0.1272 \cdot \mathopen{}\left(\mathrm{HF}_{\mathrm{severity}} - 1\right) & \text{if } \mathrm{HF}_{\mathrm{severity}} < 2 \\ 0.7456 - 0.2189 \cdot \mathopen{}\left(\mathrm{HF}_{\mathrm{severity}} - 2\right) & \text{if } \mathrm{HF}_{\mathrm{severity}} < 3 \\ 0.5267 - 0.0604999999999999 \cdot \mathopen{}\left(\mathrm{HF}_{\mathrm{severity}} - 3\right) & \text{if } \mathrm{HF}_{\mathrm{severity}} < 4 \\ 0.4662 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fhf}_{\mathrm{kidney\_flow}} &= \begin{cases} 1 & \text{if } \mathrm{HF}_{\mathrm{severity}} \leq 0 \\ 1 - 0.1208 \cdot \mathopen{}\left(\mathrm{HF}_{\mathrm{severity}} - 0\right) & \text{if } \mathrm{HF}_{\mathrm{severity}} < 1 \\ 0.8792 - 0.1208 \cdot \mathopen{}\left(\mathrm{HF}_{\mathrm{severity}} - 1\right) & \text{if } \mathrm{HF}_{\mathrm{severity}} < 2 \\ 0.7584 - 0.2092 \cdot \mathopen{}\left(\mathrm{HF}_{\mathrm{severity}} - 2\right) & \text{if } \mathrm{HF}_{\mathrm{severity}} < 3 \\ 0.5492 + 0.0806 \cdot \mathopen{}\left(\mathrm{HF}_{\mathrm{severity}} - 3\right) & \text{if } \mathrm{HF}_{\mathrm{severity}} < 4 \\ 0.6298 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fhf}_{\mathrm{peripheral\_flow}} &= \begin{cases} 1 & \text{if } \mathrm{HF}_{\mathrm{severity}} \leq 0 \\ 1 - 0.1756 \cdot \mathopen{}\left(\mathrm{HF}_{\mathrm{severity}} - 0\right) & \text{if } \mathrm{HF}_{\mathrm{severity}} < 1 \\ 0.8244 - 0.1756 \cdot \mathopen{}\left(\mathrm{HF}_{\mathrm{severity}} - 1\right) & \text{if } \mathrm{HF}_{\mathrm{severity}} < 2 \\ 0.6488 - 0.0779000000000001 \cdot \mathopen{}\left(\mathrm{HF}_{\mathrm{severity}} - 2\right) & \text{if } \mathrm{HF}_{\mathrm{severity}} < 3 \\ 0.5709 - 0.1055 \cdot \mathopen{}\left(\mathrm{HF}_{\mathrm{severity}} - 3\right) & \text{if } \mathrm{HF}_{\mathrm{severity}} < 4 \\ 0.4654 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{fsex}_{\mathrm{albumin}} &= 0.939819933659769 \\[1ex]
\mathrm{fsex}_{\mathrm{li\_cyp3a4}} &= 1.2 \\[1ex]
\mathrm{fimp}_{\mathrm{Qhe}} &= \mathrm{fcp}_{\mathrm{rest\_flow}} \\[1ex]
\mathrm{Qhe} &= \mathrm{fQhe} \cdot \mathrm{CO}_{\mathrm{base}} \cdot \mathrm{fimp}_{\mathrm{Qhe}} \\[1ex]
\mathrm{fimp}_{\mathrm{Qbr}} &= 1 \\[1ex]
\mathrm{Qbr} &= \mathrm{fQbr} \cdot \mathrm{CO}_{\mathrm{base}} \cdot \mathrm{fimp}_{\mathrm{Qbr}} \\[1ex]
\mathrm{fimp}_{\mathrm{Qli}} &= \mathrm{fcp}_{\mathrm{hepatic\_artery\_flow}} \cdot \mathrm{fhf}_{\mathrm{liver\_flow}} \\[1ex]
\mathrm{Qli} &= \mathrm{fQli} \cdot \mathrm{CO}_{\mathrm{base}} \cdot \mathrm{fimp}_{\mathrm{Qli}} \\[1ex]
\mathrm{Qha} &= \mathrm{Qli} \\[1ex]
\mathrm{fimp}_{\mathrm{Qki}} &= \mathrm{fcp}_{\mathrm{kidney\_flow}} \cdot \mathrm{fckd}_{\mathrm{kidney\_flow}} \cdot \mathrm{fhf}_{\mathrm{kidney\_flow}} \\[1ex]
\mathrm{Qki} &= \mathrm{fQki} \cdot \mathrm{CO}_{\mathrm{base}} \cdot \mathrm{fimp}_{\mathrm{Qki}} \\[1ex]
\mathrm{fimp}_{\mathrm{Qst}} &= \mathrm{fhf}_{\mathrm{liver\_flow}} \\[1ex]
\mathrm{Qst} &= \mathrm{fQst} \cdot \mathrm{CO}_{\mathrm{base}} \cdot \mathrm{fimp}_{\mathrm{Qst}} \\[1ex]
\mathrm{fimp}_{\mathrm{Qsi}} &= \mathrm{fhf}_{\mathrm{liver\_flow}} \\[1ex]
\mathrm{Qsi} &= \mathrm{fQsi} \cdot \mathrm{CO}_{\mathrm{base}} \cdot \mathrm{fimp}_{\mathrm{Qsi}} \\[1ex]
\mathrm{fimp}_{\mathrm{Qla}} &= \mathrm{fhf}_{\mathrm{liver\_flow}} \\[1ex]
\mathrm{Qla} &= \mathrm{fQla} \cdot \mathrm{CO}_{\mathrm{base}} \cdot \mathrm{fimp}_{\mathrm{Qla}} \\[1ex]
\mathrm{fimp}_{\mathrm{Qsp}} &= \mathrm{fhf}_{\mathrm{liver\_flow}} \\[1ex]
\mathrm{Qsp} &= \mathrm{fQsp} \cdot \mathrm{CO}_{\mathrm{base}} \cdot \mathrm{fimp}_{\mathrm{Qsp}} \\[1ex]
\mathrm{fimp}_{\mathrm{Qpa}} &= \mathrm{fhf}_{\mathrm{liver\_flow}} \\[1ex]
\mathrm{Qpa} &= \mathrm{fQpa} \cdot \mathrm{CO}_{\mathrm{base}} \cdot \mathrm{fimp}_{\mathrm{Qpa}} \\[1ex]
\mathrm{Qpo} &= \mathrm{Qst} + \mathrm{Qsi} + \mathrm{Qla} + \mathrm{Qsp} \\
&\quad {} + \mathrm{Qpa} \\[1ex]
\mathrm{Qh} &= \mathrm{Qha} + \mathrm{Qpo} \\[1ex]
\mathrm{fimp}_{\mathrm{Qmu}} &= \mathrm{fcp}_{\mathrm{rest\_flow}} \cdot \mathrm{fhf}_{\mathrm{peripheral\_flow}} \\[1ex]
\mathrm{Qmu} &= \mathrm{fQmu} \cdot \mathrm{CO}_{\mathrm{base}} \cdot \mathrm{fimp}_{\mathrm{Qmu}} \\[1ex]
\mathrm{fimp}_{\mathrm{Qsk}} &= \mathrm{fcp}_{\mathrm{rest\_flow}} \cdot \mathrm{fhf}_{\mathrm{peripheral\_flow}} \\[1ex]
\mathrm{Qsk} &= \mathrm{fQsk} \cdot \mathrm{CO}_{\mathrm{base}} \cdot \mathrm{fimp}_{\mathrm{Qsk}} \\[1ex]
\mathrm{fimp}_{\mathrm{Qad}} &= \mathrm{fcp}_{\mathrm{rest\_flow}} \cdot \mathrm{fhf}_{\mathrm{peripheral\_flow}} \\[1ex]
\mathrm{Qad} &= \mathrm{fQad} \cdot \mathrm{CO}_{\mathrm{base}} \cdot \mathrm{fimp}_{\mathrm{Qad}} \\[1ex]
\mathrm{fimp}_{\mathrm{Qbo}} &= \mathrm{fcp}_{\mathrm{rest\_flow}} \\[1ex]
\mathrm{Qbo} &= \mathrm{fQbo} \cdot \mathrm{CO}_{\mathrm{base}} \cdot \mathrm{fimp}_{\mathrm{Qbo}} \\[1ex]
\mathrm{fimp}_{\mathrm{Qgo}} &= \mathrm{fcp}_{\mathrm{rest\_flow}} \\[1ex]
\mathrm{Qgo} &= \mathrm{fQgo} \cdot \mathrm{CO}_{\mathrm{base}} \cdot \mathrm{fimp}_{\mathrm{Qgo}} \\[1ex]
\mathrm{fimp}_{\mathrm{CO}} &= 1 + \mathrm{fQbr} \cdot \mathopen{}\left(\mathrm{fimp}_{\mathrm{Qbr}} - 1\right) + \mathrm{fQli} \cdot \mathopen{}\left(\mathrm{fimp}_{\mathrm{Qli}} - 1\right) + \mathrm{fQki} \cdot \mathopen{}\left(\mathrm{fimp}_{\mathrm{Qki}} - 1\right) \\
&\quad {} + \mathrm{fQst} \cdot \mathopen{}\left(\mathrm{fimp}_{\mathrm{Qst}} - 1\right) + \mathrm{fQsi} \cdot \mathopen{}\left(\mathrm{fimp}_{\mathrm{Qsi}} - 1\right) + \mathrm{fQla} \cdot \mathopen{}\left(\mathrm{fimp}_{\mathrm{Qla}} - 1\right) + \mathrm{fQsp} \cdot \mathopen{}\left(\mathrm{fimp}_{\mathrm{Qsp}} - 1\right) \\
&\quad {} + \mathrm{fQpa} \cdot \mathopen{}\left(\mathrm{fimp}_{\mathrm{Qpa}} - 1\right) + \mathopen{}\left(\mathrm{fQhe} + \mathrm{fQbo} + \mathrm{fQgo}\right) \cdot \mathopen{}\left(\mathrm{fcp}_{\mathrm{rest\_flow}} - 1\right) + \mathopen{}\left(\mathrm{fQmu} + \mathrm{fQsk} + \mathrm{fQad}\right) \cdot \mathopen{}\left(\mathrm{fcp}_{\mathrm{rest\_flow}} \cdot \mathrm{fhf}_{\mathrm{peripheral\_flow}} - 1\right) \\[1ex]
\mathrm{CO} &= \mathrm{CO}_{\mathrm{base}} \cdot \mathrm{fimp}_{\mathrm{CO}} \\[1ex]
\mathrm{Qlu} &= \mathrm{CO} \\[1ex]
\mathrm{fimp}_{\mathrm{GFR}} &= \mathrm{fcp}_{\mathrm{gfr}} \cdot \mathrm{fhf}_{\mathrm{kidney\_flow}} \\[1ex]
\mathrm{GFR}_{\mathrm{base}} &= \frac{\mathrm{GFR}_{\mathrm{ref}} \cdot \mathrm{BSA}}{1.64405604477236} \cdot \mathrm{fage}_{\mathrm{GFR}} \cdot \mathrm{fimp}_{\mathrm{GFR}} \\[1ex]
\mathrm{GFR} &= \mathrm{GFR}_{\mathrm{base}} \cdot f_{\mathrm{renal\_function}} \\[1ex]
\mathrm{fimp}_{\mathrm{HCT}} &= \mathrm{fcp}_{\mathrm{hematocrit}} \cdot \mathrm{fckd}_{\mathrm{hematocrit}} \\[1ex]
\mathrm{HCT} &= \mathrm{HCT}_{\mathrm{ref}} \cdot \mathrm{fimp}_{\mathrm{HCT}} \\[1ex]
\mathrm{Var}_{\mathrm{pl}} &= \mathrm{Var} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{Var}_{\mathrm{bc}} &= \mathrm{Var} \cdot \mathrm{HCT} \\[1ex]
\mathrm{Vve}_{\mathrm{pl}} &= \mathrm{Vve} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{Vve}_{\mathrm{bc}} &= \mathrm{Vve} \cdot \mathrm{HCT} \\[1ex]
\mathrm{Vpo}_{\mathrm{pl}} &= \mathrm{Vpo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{Vpo}_{\mathrm{bc}} &= \mathrm{Vpo} \cdot \mathrm{HCT} \\[1ex]
\mathrm{LU}_{\mathrm{\_Vpl}} &= \mathrm{Vlu} \cdot f_{\mathrm{vas\_lu}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{HE}_{\mathrm{\_Vpl}} &= \mathrm{Vhe} \cdot f_{\mathrm{vas\_he}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{BR}_{\mathrm{\_Vpl}} &= \mathrm{Vbr} \cdot f_{\mathrm{vas\_br}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{LI}_{\mathrm{\_Vpl}} &= \mathrm{Vli} \cdot f_{\mathrm{vas\_li}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{ST}_{\mathrm{\_Vpl}} &= \mathrm{Vst} \cdot f_{\mathrm{vas\_st}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{SP}_{\mathrm{\_Vpl}} &= \mathrm{Vsp} \cdot f_{\mathrm{vas\_sp}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{PA}_{\mathrm{\_Vpl}} &= \mathrm{Vpa} \cdot f_{\mathrm{vas\_pa}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{MU}_{\mathrm{\_Vpl}} &= \mathrm{Vmu} \cdot f_{\mathrm{vas\_mu}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{SK}_{\mathrm{\_Vpl}} &= \mathrm{Vsk} \cdot f_{\mathrm{vas\_sk}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{BO}_{\mathrm{\_Vpl}} &= \mathrm{Vbo} \cdot f_{\mathrm{vas\_bo}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{GO}_{\mathrm{\_Vpl}} &= \mathrm{Vgo} \cdot f_{\mathrm{vas\_go}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{fimp}_{\mathrm{Mki}} &= \mathrm{fckd}_{\mathrm{kidney\_volume}} \\[1ex]
\mathrm{Mki} &= \mathrm{Mki}_{\mathrm{ref}} \cdot \mathrm{SV}_{\mathrm{tis}} \cdot \mathrm{fimp}_{\mathrm{Mki}} \\[1ex]
\mathrm{Mlean} &= \mathrm{Mlu} + \mathrm{Mhe} + \mathrm{Mbr} + \mathrm{Mli} \\
&\quad {} + \mathrm{Mki} + \mathrm{Mst} + \mathrm{Msi} + \mathrm{Mla} \\
&\quad {} + \mathrm{Msp} + \mathrm{Mpa} + \mathrm{Mmu} + \mathrm{Msk} \\
&\quad {} + \mathrm{Mbo} + \mathrm{Mgo} \\[1ex]
\mathrm{Mad} &= \mathrm{BW} - \mathrm{Mlean} - \mathrm{Vblood} \cdot 1.06 \\[1ex]
\mathrm{Vki} &= \frac{\mathrm{Mki}}{1.05} + 0.02 \cdot \mathrm{Vblood} \\[1ex]
\mathrm{Vad} &= \frac{\mathrm{Mad}}{1} + 0.085 \cdot \mathrm{Vblood} \\[1ex]
f_{\mathrm{vas\_ki}} &= \frac{0.02 \cdot \mathrm{Vblood}}{\mathrm{Vki}} \\[1ex]
\mathrm{KI}_{\mathrm{\_Vpl}} &= \mathrm{Vki} \cdot f_{\mathrm{vas\_ki}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{KI}_{\mathrm{\_Vti}} &= \mathrm{Vki} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_ki}}\right) \\[1ex]
f_{\mathrm{int\_ki}} &= 0.164957819597664 \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_ki}}\right) \\[1ex]
f_{\mathrm{vas\_ad}} &= \frac{0.085 \cdot \mathrm{Vblood}}{\mathrm{Vad}} \\[1ex]
\mathrm{AD}_{\mathrm{\_Vpl}} &= \mathrm{Vad} \cdot f_{\mathrm{vas\_ad}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{AD}_{\mathrm{\_Vti}} &= \mathrm{Vad} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_ad}}\right) \\[1ex]
f_{\mathrm{int\_ad}} &= 0.140001017449255 \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_ad}}\right) \\[1ex]
\mathrm{fimp}_{\mathrm{albumin}} &= \mathrm{fcp}_{\mathrm{albumin}} \cdot \mathrm{fsex}_{\mathrm{albumin}} \\[1ex]
\mathrm{fimp}_{\mathrm{agp}} &= \mathrm{fcp}_{\mathrm{agp}} \\[1ex]
\mathrm{fimp}_{\mathrm{plasma\_protein}} &= \mathrm{fckd}_{\mathrm{plasma\_protein}} \\[1ex]
\mathrm{fimp}_{\mathrm{t\_stomach}} &= \mathrm{fckd}_{\mathrm{gastric\_emptying\_time}} \\[1ex]
\mathrm{fimp}_{\mathrm{t\_si}} &= \mathrm{fckd}_{\mathrm{si\_transit\_time}} \\[1ex]
\mathrm{fimp}_{\mathrm{li\_cyp3a4}} &= \mathrm{fcp}_{\mathrm{cyp3a4}} \cdot \mathopen{}\left(1 + \mathrm{CKD}_{\mathrm{hepatic}} \cdot \mathopen{}\left(\mathrm{fckd}_{\mathrm{cyp3a4}} - 1\right)\right) \cdot \mathrm{fsex}_{\mathrm{li\_cyp3a4}} \\[1ex]
\mathrm{fu}_{\mathrm{api}} &= \frac{1}{1 + \frac{\mathrm{fimp}_{\mathrm{albumin}} \cdot \mathopen{}\left(1 - \mathrm{fu}_{\mathrm{ref\_api}}\right)}{\mathrm{fu}_{\mathrm{ref\_api}}}} \\[1ex]
\mathrm{BP}_{\mathrm{api}} &= 1 - \mathrm{HCT} \\[1ex]
\mathrm{fu}_{\mathrm{api\_m1}} &= \mathrm{fu}_{\mathrm{ref\_api\_m1}} \\[1ex]
\mathrm{BP}_{\mathrm{api\_m1}} &= 1 - \mathrm{HCT} \\[1ex]
\mathrm{fu}_{\mathrm{api\_m2}} &= \mathrm{fu}_{\mathrm{ref\_api\_m2}} \\[1ex]
\mathrm{BP}_{\mathrm{api\_m2}} &= 1 - \mathrm{HCT} \\[1ex]
\mathrm{fu}_{\mathrm{api\_m7}} &= \mathrm{fu}_{\mathrm{ref\_api\_m7}} \\[1ex]
\mathrm{BP}_{\mathrm{api\_m7}} &= 1 - \mathrm{HCT} \\[1ex]
\mathrm{LU}_{\mathrm{\_PS\_api}} &= \frac{\mathrm{ftissue}_{\mathrm{api}} \cdot \mathrm{Vlu} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_lu}}\right)}{\mathrm{Vti}_{\mathrm{total\_ref\_api}}} \\[1ex]
\mathrm{HE}_{\mathrm{\_PS\_api}} &= \frac{\mathrm{ftissue}_{\mathrm{api}} \cdot \mathrm{Vhe} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_he}}\right)}{\mathrm{Vti}_{\mathrm{total\_ref\_api}}} \\[1ex]
\mathrm{BR}_{\mathrm{\_PS\_api}} &= \frac{\mathrm{ftissue}_{\mathrm{api}} \cdot \mathrm{Vbr} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_br}}\right)}{\mathrm{Vti}_{\mathrm{total\_ref\_api}}} \\[1ex]
\mathrm{LI}_{\mathrm{\_PS\_api}} &= \mathrm{LI}_{\mathrm{\_kps\_api}} \cdot \mathrm{Vli} \cdot f_{\mathrm{functional}} \\[1ex]
\mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m1}} &= \mathopen{}\left(\mathrm{LI}_{\mathrm{\_f\_water\_int}} + \mathrm{LI}_{\mathrm{\_r\_protein\_int\_pls}} \cdot \mathopen{}\left(\frac{1}{\mathrm{fu}_{\mathrm{api\_m1}}} - \mathrm{LI}_{\mathrm{\_f\_water\_pls}}\right)\right) \cdot \mathrm{fu}_{\mathrm{api\_m1}} \\[1ex]
\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m1}} &= \begin{cases} \frac{\mathrm{Kp}_{\mathrm{api\_m1}} \cdot \mathopen{}\left(f_{\mathrm{int\_li}} + 1 - f_{\mathrm{vas\_li}} - f_{\mathrm{int\_li}}\right) - f_{\mathrm{int\_li}} \cdot \mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m1}}}{1 - f_{\mathrm{vas\_li}} - f_{\mathrm{int\_li}}} & \text{if } \frac{\mathrm{Kp}_{\mathrm{api\_m1}} \cdot \mathopen{}\left(f_{\mathrm{int\_li}} + 1 - f_{\mathrm{vas\_li}} - f_{\mathrm{int\_li}}\right) - f_{\mathrm{int\_li}} \cdot \mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m1}}}{1 - f_{\mathrm{vas\_li}} - f_{\mathrm{int\_li}}} > 10^{-6} \\ 10^{-6} & \text{otherwise} \end{cases} \\[1ex]
\mathrm{LI}_{\mathrm{\_PS\_vas}} &= \mathrm{LI}_{\mathrm{\_k\_vas}} \cdot \mathrm{Vli} \\[1ex]
\mathrm{LI}_{\mathrm{\_PS\_api\_m1}} &= \mathrm{LI}_{\mathrm{\_kps\_api\_m1}} \cdot \mathrm{Vli} \cdot f_{\mathrm{functional}} \\[1ex]
\mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m2}} &= \mathopen{}\left(\mathrm{LI}_{\mathrm{\_f\_water\_int}} + \mathrm{LI}_{\mathrm{\_r\_protein\_int\_pls}} \cdot \mathopen{}\left(\frac{1}{\mathrm{fu}_{\mathrm{api\_m2}}} - \mathrm{LI}_{\mathrm{\_f\_water\_pls}}\right)\right) \cdot \mathrm{fu}_{\mathrm{api\_m2}} \\[1ex]
\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m2}} &= \mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m2}} \\[1ex]
\mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m7}} &= \mathopen{}\left(\mathrm{LI}_{\mathrm{\_f\_water\_int}} + \mathrm{LI}_{\mathrm{\_r\_protein\_int\_pls}} \cdot \mathopen{}\left(\frac{1}{\mathrm{fu}_{\mathrm{api\_m7}}} - \mathrm{LI}_{\mathrm{\_f\_water\_pls}}\right)\right) \cdot \mathrm{fu}_{\mathrm{api\_m7}} \\[1ex]
\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m7}} &= \begin{cases} \frac{\mathrm{Kp}_{\mathrm{api\_m7}} \cdot \mathopen{}\left(f_{\mathrm{int\_li}} + 1 - f_{\mathrm{vas\_li}} - f_{\mathrm{int\_li}}\right) - f_{\mathrm{int\_li}} \cdot \mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m7}}}{1 - f_{\mathrm{vas\_li}} - f_{\mathrm{int\_li}}} & \text{if } \frac{\mathrm{Kp}_{\mathrm{api\_m7}} \cdot \mathopen{}\left(f_{\mathrm{int\_li}} + 1 - f_{\mathrm{vas\_li}} - f_{\mathrm{int\_li}}\right) - f_{\mathrm{int\_li}} \cdot \mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m7}}}{1 - f_{\mathrm{vas\_li}} - f_{\mathrm{int\_li}}} > 10^{-6} \\ 10^{-6} & \text{otherwise} \end{cases} \\[1ex]
\mathrm{LI}_{\mathrm{\_PS\_api\_m7}} &= \mathrm{LI}_{\mathrm{\_kps\_api\_m7}} \cdot \mathrm{Vli} \cdot f_{\mathrm{functional}} \\[1ex]
\mathrm{KI}_{\mathrm{\_PS\_api}} &= \frac{\mathrm{ftissue}_{\mathrm{api}} \cdot \mathrm{Vki} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_ki}}\right)}{\mathrm{Vti}_{\mathrm{total\_ref\_api}}} \\[1ex]
\mathrm{ST}_{\mathrm{\_PS\_api}} &= \frac{\mathrm{ftissue}_{\mathrm{api}} \cdot \mathrm{Vst} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_st}}\right)}{\mathrm{Vti}_{\mathrm{total\_ref\_api}}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Vgu}} &= \mathrm{Vsi} + \mathrm{Vla} \\[1ex]
\mathrm{GU}_{\mathrm{\_f\_vas\_gu}} &= \frac{\mathrm{Vsi} \cdot f_{\mathrm{vas\_si}} + \mathrm{Vla} \cdot f_{\mathrm{vas\_la}}}{\mathrm{GU}_{\mathrm{\_Vgu}}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Vpl}} &= \mathrm{GU}_{\mathrm{\_Vgu}} \cdot \mathrm{GU}_{\mathrm{\_f\_vas\_gu}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{GU}_{\mathrm{\_Vti}} &= \mathrm{GU}_{\mathrm{\_Vgu}} \cdot \mathopen{}\left(1 - \mathrm{GU}_{\mathrm{\_f\_vas\_gu}}\right) \\[1ex]
\mathrm{GU}_{\mathrm{\_Qmu\_du}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_flow}} \cdot \mathrm{Qsi} \cdot 0.0744792 \\[1ex]
\mathrm{GU}_{\mathrm{\_Qmu\_jej1}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_flow}} \cdot \mathrm{Qsi} \cdot 0.186146 \\[1ex]
\mathrm{GU}_{\mathrm{\_Qmu\_jej2}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_flow}} \cdot \mathrm{Qsi} \cdot 0.186146 \\[1ex]
\mathrm{GU}_{\mathrm{\_Qmu\_ile1}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_flow}} \cdot \mathrm{Qsi} \cdot 0.276615 \\[1ex]
\mathrm{GU}_{\mathrm{\_Qmu\_ile2}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_flow}} \cdot \mathrm{Qsi} \cdot 0.276615 \\[1ex]
\mathrm{GU}_{\mathrm{\_Qmu\_cae}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_flow}} \cdot \mathrm{Qla} \cdot 0.160969 \\[1ex]
\mathrm{GU}_{\mathrm{\_Qmu\_asc}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_flow}} \cdot \mathrm{Qla} \cdot 0.160969 \\[1ex]
\mathrm{GU}_{\mathrm{\_Qmu\_tra}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_flow}} \cdot \mathrm{Qla} \cdot 0.162393 \\[1ex]
\mathrm{GU}_{\mathrm{\_Qmu\_des}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_flow}} \cdot \mathrm{Qla} \cdot 0.162393 \\[1ex]
\mathrm{GU}_{\mathrm{\_Qmu\_sig}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_flow}} \cdot \mathrm{Qla} \cdot 0.176638 \\[1ex]
\mathrm{GU}_{\mathrm{\_Qmu\_rec}} &= \mathrm{GU}_{\mathrm{\_f\_mucosa\_flow}} \cdot \mathrm{Qla} \cdot 0.176638 \\[1ex]
\mathrm{GU}_{\mathrm{\_Vmu\_total}} &= \mathrm{GU}_{\mathrm{\_Vmu\_du}} + \mathrm{GU}_{\mathrm{\_Vmu\_jej1}} + \mathrm{GU}_{\mathrm{\_Vmu\_jej2}} + \mathrm{GU}_{\mathrm{\_Vmu\_ile1}} \\
&\quad {} + \mathrm{GU}_{\mathrm{\_Vmu\_ile2}} + \mathrm{GU}_{\mathrm{\_Vmu\_cae}} + \mathrm{GU}_{\mathrm{\_Vmu\_asc}} + \mathrm{GU}_{\mathrm{\_Vmu\_tra}} \\
&\quad {} + \mathrm{GU}_{\mathrm{\_Vmu\_des}} + \mathrm{GU}_{\mathrm{\_Vmu\_sig}} + \mathrm{GU}_{\mathrm{\_Vmu\_rec}} \\[1ex]
\mathrm{GU}_{\mathrm{\_f\_wall}} &= 1 - \frac{\mathrm{GU}_{\mathrm{\_Vmu\_total}}}{\mathrm{GU}_{\mathrm{\_Vgu}} \cdot \mathopen{}\left(1 - \mathrm{GU}_{\mathrm{\_f\_vas\_gu}}\right)} \\[1ex]
\mathrm{GU}_{\mathrm{\_Vti\_wall}} &= \mathrm{GU}_{\mathrm{\_Vti}} \cdot \mathrm{GU}_{\mathrm{\_f\_wall}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Qmu\_total}} &= \mathrm{GU}_{\mathrm{\_Qmu\_du}} + \mathrm{GU}_{\mathrm{\_Qmu\_jej1}} + \mathrm{GU}_{\mathrm{\_Qmu\_jej2}} + \mathrm{GU}_{\mathrm{\_Qmu\_ile1}} \\
&\quad {} + \mathrm{GU}_{\mathrm{\_Qmu\_ile2}} + \mathrm{GU}_{\mathrm{\_Qmu\_cae}} + \mathrm{GU}_{\mathrm{\_Qmu\_asc}} + \mathrm{GU}_{\mathrm{\_Qmu\_tra}} \\
&\quad {} + \mathrm{GU}_{\mathrm{\_Qmu\_des}} + \mathrm{GU}_{\mathrm{\_Qmu\_sig}} + \mathrm{GU}_{\mathrm{\_Qmu\_rec}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Qgu}} &= \mathrm{Qsi} + \mathrm{Qla} \\[1ex]
\mathrm{GU}_{\mathrm{\_Qgu\_wall}} &= \mathrm{GU}_{\mathrm{\_Qgu}} - \mathrm{GU}_{\mathrm{\_Qmu\_total}} \\[1ex]
\mathrm{GU}_{\mathrm{\_PS\_api}} &= \frac{\mathrm{ftissue}_{\mathrm{api}} \cdot \mathrm{GU}_{\mathrm{\_Vgu}} \cdot \mathopen{}\left(1 - \mathrm{GU}_{\mathrm{\_f\_vas\_gu}}\right)}{\mathrm{Vti}_{\mathrm{total\_ref\_api}}} \\[1ex]
\mathrm{GU}_{\mathrm{\_K\_mu\_api}} &= \mathrm{Kp}_{\mathrm{api}} \\[1ex]
\mathrm{GU}_{\mathrm{\_w\_uniform\_du}} &= \frac{\mathrm{GU}_{\mathrm{\_Vmu\_du}}}{\mathrm{GU}_{\mathrm{\_Vmu\_du}} + \mathrm{GU}_{\mathrm{\_Vmu\_jej1}} + \mathrm{GU}_{\mathrm{\_Vmu\_jej2}} + \mathrm{GU}_{\mathrm{\_Vmu\_ile1}} + \mathrm{GU}_{\mathrm{\_Vmu\_ile2}}} \\[1ex]
\mathrm{GU}_{\mathrm{\_w\_uniform\_jej1}} &= \frac{\mathrm{GU}_{\mathrm{\_Vmu\_jej1}}}{\mathrm{GU}_{\mathrm{\_Vmu\_du}} + \mathrm{GU}_{\mathrm{\_Vmu\_jej1}} + \mathrm{GU}_{\mathrm{\_Vmu\_jej2}} + \mathrm{GU}_{\mathrm{\_Vmu\_ile1}} + \mathrm{GU}_{\mathrm{\_Vmu\_ile2}}} \\[1ex]
\mathrm{GU}_{\mathrm{\_w\_uniform\_jej2}} &= \frac{\mathrm{GU}_{\mathrm{\_Vmu\_jej2}}}{\mathrm{GU}_{\mathrm{\_Vmu\_du}} + \mathrm{GU}_{\mathrm{\_Vmu\_jej1}} + \mathrm{GU}_{\mathrm{\_Vmu\_jej2}} + \mathrm{GU}_{\mathrm{\_Vmu\_ile1}} + \mathrm{GU}_{\mathrm{\_Vmu\_ile2}}} \\[1ex]
\mathrm{GU}_{\mathrm{\_w\_uniform\_ile1}} &= \frac{\mathrm{GU}_{\mathrm{\_Vmu\_ile1}}}{\mathrm{GU}_{\mathrm{\_Vmu\_du}} + \mathrm{GU}_{\mathrm{\_Vmu\_jej1}} + \mathrm{GU}_{\mathrm{\_Vmu\_jej2}} + \mathrm{GU}_{\mathrm{\_Vmu\_ile1}} + \mathrm{GU}_{\mathrm{\_Vmu\_ile2}}} \\[1ex]
\mathrm{GU}_{\mathrm{\_w\_uniform\_ile2}} &= \frac{\mathrm{GU}_{\mathrm{\_Vmu\_ile2}}}{\mathrm{GU}_{\mathrm{\_Vmu\_du}} + \mathrm{GU}_{\mathrm{\_Vmu\_jej1}} + \mathrm{GU}_{\mathrm{\_Vmu\_jej2}} + \mathrm{GU}_{\mathrm{\_Vmu\_ile1}} + \mathrm{GU}_{\mathrm{\_Vmu\_ile2}}} \\[1ex]
T_{\mathrm{st\_eff}} &= \mathopen{}\left(\mathrm{GU}_{\mathrm{\_T\_st}} + \mathrm{FED} \cdot \mathopen{}\left(\mathrm{GU}_{\mathrm{\_T\_st\_fed}} \cdot \mathrm{fsex}_{\mathrm{t\_stomach\_fed}} - \mathrm{GU}_{\mathrm{\_T\_st}}\right)\right) \cdot \mathrm{fimp}_{\mathrm{t\_stomach}} \\[1ex]
\mathrm{SP}_{\mathrm{\_PS\_api}} &= \frac{\mathrm{ftissue}_{\mathrm{api}} \cdot \mathrm{Vsp} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_sp}}\right)}{\mathrm{Vti}_{\mathrm{total\_ref\_api}}} \\[1ex]
\mathrm{PA}_{\mathrm{\_PS\_api}} &= \frac{\mathrm{ftissue}_{\mathrm{api}} \cdot \mathrm{Vpa} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_pa}}\right)}{\mathrm{Vti}_{\mathrm{total\_ref\_api}}} \\[1ex]
\mathrm{MU}_{\mathrm{\_PS\_api}} &= \frac{\mathrm{ftissue}_{\mathrm{api}} \cdot \mathrm{Vmu} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_mu}}\right)}{\mathrm{Vti}_{\mathrm{total\_ref\_api}}} \\[1ex]
\mathrm{SK}_{\mathrm{\_PS\_api}} &= \frac{\mathrm{ftissue}_{\mathrm{api}} \cdot \mathrm{Vsk} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_sk}}\right)}{\mathrm{Vti}_{\mathrm{total\_ref\_api}}} \\[1ex]
\mathrm{AD}_{\mathrm{\_PS\_api}} &= \frac{\mathrm{ftissue}_{\mathrm{api}} \cdot \mathrm{Vad} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_ad}}\right)}{\mathrm{Vti}_{\mathrm{total\_ref\_api}}} \\[1ex]
\mathrm{BO}_{\mathrm{\_PS\_api}} &= \frac{\mathrm{ftissue}_{\mathrm{api}} \cdot \mathrm{Vbo} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_bo}}\right)}{\mathrm{Vti}_{\mathrm{total\_ref\_api}}} \\[1ex]
\mathrm{GO}_{\mathrm{\_PS\_api}} &= \frac{\mathrm{ftissue}_{\mathrm{api}} \cdot \mathrm{Vgo} \cdot \mathopen{}\left(1 - f_{\mathrm{vas\_go}}\right)}{\mathrm{Vti}_{\mathrm{total\_ref\_api}}}
\end{aligned}
$$

The assignment rules hold at every time $t$:

$$
\begin{aligned}
\mathrm{Kiv}_{\mathrm{api}} &= \frac{\ln\mathopen{}\left(2\right)}{\mathrm{ti}_{\mathrm{api}}} \cdot 60 \\[1ex]
\mathrm{Car}_{\mathrm{free\_api}} &= \mathrm{fu}_{\mathrm{api}} \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
\mathrm{Car}_{\mathrm{blood\_api}} &= \mathrm{BP}_{\mathrm{api}} \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
\mathrm{Cve}_{\mathrm{free\_api}} &= \mathrm{fu}_{\mathrm{api}} \cdot \mathrm{Cve}_{\mathrm{api}} \\[1ex]
\mathrm{Cve}_{\mathrm{blood\_api}} &= \mathrm{BP}_{\mathrm{api}} \cdot \mathrm{Cve}_{\mathrm{api}} \\[1ex]
\mathrm{Cpo}_{\mathrm{free\_api}} &= \mathrm{fu}_{\mathrm{api}} \cdot \mathrm{Cpo}_{\mathrm{api}} \\[1ex]
\mathrm{Cpo}_{\mathrm{blood\_api}} &= \mathrm{BP}_{\mathrm{api}} \cdot \mathrm{Cpo}_{\mathrm{api}} \\[1ex]
\mathrm{Car}_{\mathrm{free\_api\_m1}} &= \mathrm{fu}_{\mathrm{api\_m1}} \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
\mathrm{Car}_{\mathrm{blood\_api\_m1}} &= \mathrm{BP}_{\mathrm{api\_m1}} \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
\mathrm{Cve}_{\mathrm{free\_api\_m1}} &= \mathrm{fu}_{\mathrm{api\_m1}} \cdot \mathrm{Cve}_{\mathrm{api\_m1}} \\[1ex]
\mathrm{Cve}_{\mathrm{blood\_api\_m1}} &= \mathrm{BP}_{\mathrm{api\_m1}} \cdot \mathrm{Cve}_{\mathrm{api\_m1}} \\[1ex]
\mathrm{Cpo}_{\mathrm{free\_api\_m1}} &= \mathrm{fu}_{\mathrm{api\_m1}} \cdot \mathrm{Cpo}_{\mathrm{api\_m1}} \\[1ex]
\mathrm{Cpo}_{\mathrm{blood\_api\_m1}} &= \mathrm{BP}_{\mathrm{api\_m1}} \cdot \mathrm{Cpo}_{\mathrm{api\_m1}} \\[1ex]
\mathrm{Car}_{\mathrm{free\_api\_m2}} &= \mathrm{fu}_{\mathrm{api\_m2}} \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
\mathrm{Car}_{\mathrm{blood\_api\_m2}} &= \mathrm{BP}_{\mathrm{api\_m2}} \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
\mathrm{Cve}_{\mathrm{free\_api\_m2}} &= \mathrm{fu}_{\mathrm{api\_m2}} \cdot \mathrm{Cve}_{\mathrm{api\_m2}} \\[1ex]
\mathrm{Cve}_{\mathrm{blood\_api\_m2}} &= \mathrm{BP}_{\mathrm{api\_m2}} \cdot \mathrm{Cve}_{\mathrm{api\_m2}} \\[1ex]
\mathrm{Cpo}_{\mathrm{free\_api\_m2}} &= \mathrm{fu}_{\mathrm{api\_m2}} \cdot \mathrm{Cpo}_{\mathrm{api\_m2}} \\[1ex]
\mathrm{Cpo}_{\mathrm{blood\_api\_m2}} &= \mathrm{BP}_{\mathrm{api\_m2}} \cdot \mathrm{Cpo}_{\mathrm{api\_m2}} \\[1ex]
\mathrm{Car}_{\mathrm{free\_api\_m7}} &= \mathrm{fu}_{\mathrm{api\_m7}} \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
\mathrm{Car}_{\mathrm{blood\_api\_m7}} &= \mathrm{BP}_{\mathrm{api\_m7}} \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
\mathrm{Cve}_{\mathrm{free\_api\_m7}} &= \mathrm{fu}_{\mathrm{api\_m7}} \cdot \mathrm{Cve}_{\mathrm{api\_m7}} \\[1ex]
\mathrm{Cve}_{\mathrm{blood\_api\_m7}} &= \mathrm{BP}_{\mathrm{api\_m7}} \cdot \mathrm{Cve}_{\mathrm{api\_m7}} \\[1ex]
\mathrm{Cpo}_{\mathrm{free\_api\_m7}} &= \mathrm{fu}_{\mathrm{api\_m7}} \cdot \mathrm{Cpo}_{\mathrm{api\_m7}} \\[1ex]
\mathrm{Cpo}_{\mathrm{blood\_api\_m7}} &= \mathrm{BP}_{\mathrm{api\_m7}} \cdot \mathrm{Cpo}_{\mathrm{api\_m7}} \\[1ex]
\mathrm{Cout}_{\mathrm{lu\_api}} &= \mathrm{LU}_{\mathrm{\_Cpl\_api}} \\[1ex]
\mathrm{LU}_{\mathrm{\_Cu\_ti\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{Kp}_{\mathrm{api}}} \cdot \mathrm{LU}_{\mathrm{\_Cti\_api}} \\[1ex]
\mathrm{Cout}_{\mathrm{lu\_api\_m1}} &= \mathrm{LU}_{\mathrm{\_Cpl\_api\_m1}} \\[1ex]
\mathrm{Cout}_{\mathrm{lu\_api\_m2}} &= \mathrm{LU}_{\mathrm{\_Cpl\_api\_m2}} \\[1ex]
\mathrm{Cout}_{\mathrm{lu\_api\_m7}} &= \mathrm{LU}_{\mathrm{\_Cpl\_api\_m7}} \\[1ex]
\mathrm{Cout}_{\mathrm{he\_api}} &= \mathrm{HE}_{\mathrm{\_Cpl\_api}} \\[1ex]
\mathrm{HE}_{\mathrm{\_Cu\_ti\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{Kp}_{\mathrm{api}}} \cdot \mathrm{HE}_{\mathrm{\_Cti\_api}} \\[1ex]
\mathrm{Cout}_{\mathrm{he\_api\_m1}} &= \mathrm{HE}_{\mathrm{\_Cpl\_api\_m1}} \\[1ex]
\mathrm{Cout}_{\mathrm{he\_api\_m2}} &= \mathrm{HE}_{\mathrm{\_Cpl\_api\_m2}} \\[1ex]
\mathrm{Cout}_{\mathrm{he\_api\_m7}} &= \mathrm{HE}_{\mathrm{\_Cpl\_api\_m7}} \\[1ex]
\mathrm{Cout}_{\mathrm{br\_api}} &= \mathrm{BR}_{\mathrm{\_Cpl\_api}} \\[1ex]
\mathrm{BR}_{\mathrm{\_Cu\_ti\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{Kp}_{\mathrm{api}}} \cdot \mathrm{BR}_{\mathrm{\_Cti\_api}} \\[1ex]
\mathrm{Cout}_{\mathrm{br\_api\_m1}} &= \mathrm{BR}_{\mathrm{\_Cpl\_api\_m1}} \\[1ex]
\mathrm{Cout}_{\mathrm{br\_api\_m2}} &= \mathrm{BR}_{\mathrm{\_Cpl\_api\_m2}} \\[1ex]
\mathrm{Cout}_{\mathrm{br\_api\_m7}} &= \mathrm{BR}_{\mathrm{\_Cpl\_api\_m7}} \\[1ex]
\mathrm{Cout}_{\mathrm{li\_api}} &= \mathrm{LI}_{\mathrm{\_Cpl\_api}} \\[1ex]
\mathrm{Chv}_{\mathrm{api}} &= \frac{\mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qh} \cdot \mathrm{Cout}_{\mathrm{li\_api}} + f_{\mathrm{shunt}} \cdot \mathopen{}\left(\mathrm{Qha} \cdot \mathrm{Car}_{\mathrm{api}} + \mathrm{Qpo} \cdot \mathrm{Cpo}_{\mathrm{api}}\right)}{\mathrm{Qh}} \\[1ex]
\mathrm{Chv}_{\mathrm{free\_api}} &= \mathrm{fu}_{\mathrm{api}} \cdot \mathrm{Chv}_{\mathrm{api}} \\[1ex]
\mathrm{Chv}_{\mathrm{blood\_api}} &= \mathrm{BP}_{\mathrm{api}} \cdot \mathrm{Chv}_{\mathrm{api}} \\[1ex]
\mathrm{LI}_{\mathrm{\_Cu\_ti\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{Kp}_{\mathrm{api}}} \cdot \mathrm{LI}_{\mathrm{\_Cti\_api}} \\[1ex]
\mathrm{Cout}_{\mathrm{li\_api\_m1}} &= \mathrm{LI}_{\mathrm{\_Cpl\_api\_m1}} \\[1ex]
\mathrm{Chv}_{\mathrm{api\_m1}} &= \frac{\mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qh} \cdot \mathrm{Cout}_{\mathrm{li\_api\_m1}} + f_{\mathrm{shunt}} \cdot \mathopen{}\left(\mathrm{Qha} \cdot \mathrm{Car}_{\mathrm{api\_m1}} + \mathrm{Qpo} \cdot \mathrm{Cpo}_{\mathrm{api\_m1}}\right)}{\mathrm{Qh}} \\[1ex]
\mathrm{Chv}_{\mathrm{free\_api\_m1}} &= \mathrm{fu}_{\mathrm{api\_m1}} \cdot \mathrm{Chv}_{\mathrm{api\_m1}} \\[1ex]
\mathrm{Chv}_{\mathrm{blood\_api\_m1}} &= \mathrm{BP}_{\mathrm{api\_m1}} \cdot \mathrm{Chv}_{\mathrm{api\_m1}} \\[1ex]
\mathrm{LI}_{\mathrm{\_Cu\_is\_api\_m1}} &= \frac{\mathrm{fu}_{\mathrm{api\_m1}}}{\mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m1}}} \cdot \mathrm{LI}_{\mathrm{\_Cis\_api\_m1}} \\[1ex]
\mathrm{LI}_{\mathrm{\_Cu\_ic\_api\_m1}} &= \frac{\mathrm{fu}_{\mathrm{api\_m1}}}{\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m1}}} \cdot \mathrm{LI}_{\mathrm{\_Cic\_api\_m1}} \\[1ex]
\mathrm{Cout}_{\mathrm{li\_api\_m2}} &= \mathrm{LI}_{\mathrm{\_Cpl\_api\_m2}} \\[1ex]
\mathrm{Chv}_{\mathrm{api\_m2}} &= \frac{\mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qh} \cdot \mathrm{Cout}_{\mathrm{li\_api\_m2}} + f_{\mathrm{shunt}} \cdot \mathopen{}\left(\mathrm{Qha} \cdot \mathrm{Car}_{\mathrm{api\_m2}} + \mathrm{Qpo} \cdot \mathrm{Cpo}_{\mathrm{api\_m2}}\right)}{\mathrm{Qh}} \\[1ex]
\mathrm{Chv}_{\mathrm{free\_api\_m2}} &= \mathrm{fu}_{\mathrm{api\_m2}} \cdot \mathrm{Chv}_{\mathrm{api\_m2}} \\[1ex]
\mathrm{Chv}_{\mathrm{blood\_api\_m2}} &= \mathrm{BP}_{\mathrm{api\_m2}} \cdot \mathrm{Chv}_{\mathrm{api\_m2}} \\[1ex]
\mathrm{LI}_{\mathrm{\_Cu\_is\_api\_m2}} &= \frac{\mathrm{fu}_{\mathrm{api\_m2}}}{\mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m2}}} \cdot \mathrm{LI}_{\mathrm{\_Cis\_api\_m2}} \\[1ex]
\mathrm{LI}_{\mathrm{\_Cu\_ic\_api\_m2}} &= \frac{\mathrm{fu}_{\mathrm{api\_m2}}}{\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m2}}} \cdot \mathrm{LI}_{\mathrm{\_Cic\_api\_m2}} \\[1ex]
\mathrm{Cout}_{\mathrm{li\_api\_m7}} &= \mathrm{LI}_{\mathrm{\_Cpl\_api\_m7}} \\[1ex]
\mathrm{Chv}_{\mathrm{api\_m7}} &= \frac{\mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qh} \cdot \mathrm{Cout}_{\mathrm{li\_api\_m7}} + f_{\mathrm{shunt}} \cdot \mathopen{}\left(\mathrm{Qha} \cdot \mathrm{Car}_{\mathrm{api\_m7}} + \mathrm{Qpo} \cdot \mathrm{Cpo}_{\mathrm{api\_m7}}\right)}{\mathrm{Qh}} \\[1ex]
\mathrm{Chv}_{\mathrm{free\_api\_m7}} &= \mathrm{fu}_{\mathrm{api\_m7}} \cdot \mathrm{Chv}_{\mathrm{api\_m7}} \\[1ex]
\mathrm{Chv}_{\mathrm{blood\_api\_m7}} &= \mathrm{BP}_{\mathrm{api\_m7}} \cdot \mathrm{Chv}_{\mathrm{api\_m7}} \\[1ex]
\mathrm{LI}_{\mathrm{\_Cu\_is\_api\_m7}} &= \frac{\mathrm{fu}_{\mathrm{api\_m7}}}{\mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m7}}} \cdot \mathrm{LI}_{\mathrm{\_Cis\_api\_m7}} \\[1ex]
\mathrm{LI}_{\mathrm{\_Cu\_ic\_api\_m7}} &= \frac{\mathrm{fu}_{\mathrm{api\_m7}}}{\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m7}}} \cdot \mathrm{LI}_{\mathrm{\_Cic\_api\_m7}} \\[1ex]
\mathrm{Cout}_{\mathrm{ki\_api}} &= \mathrm{KI}_{\mathrm{\_Cpl\_api}} \\[1ex]
\mathrm{KI}_{\mathrm{\_Cu\_ti\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{Kp}_{\mathrm{api}}} \cdot \mathrm{KI}_{\mathrm{\_Cti\_api}} \\[1ex]
\mathrm{Cout}_{\mathrm{ki\_api\_m1}} &= \mathrm{KI}_{\mathrm{\_Cpl\_api\_m1}} \\[1ex]
\mathrm{Cout}_{\mathrm{ki\_api\_m2}} &= \mathrm{KI}_{\mathrm{\_Cpl\_api\_m2}} \\[1ex]
\mathrm{Cout}_{\mathrm{ki\_api\_m7}} &= \mathrm{KI}_{\mathrm{\_Cpl\_api\_m7}} \\[1ex]
\mathrm{Cout}_{\mathrm{st\_api}} &= \mathrm{ST}_{\mathrm{\_Cpl\_api}} \\[1ex]
\mathrm{ST}_{\mathrm{\_Cu\_ti\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{Kp}_{\mathrm{api}}} \cdot \mathrm{ST}_{\mathrm{\_Cti\_api}} \\[1ex]
\mathrm{Cout}_{\mathrm{st\_api\_m1}} &= \mathrm{ST}_{\mathrm{\_Cpl\_api\_m1}} \\[1ex]
\mathrm{Cout}_{\mathrm{st\_api\_m2}} &= \mathrm{ST}_{\mathrm{\_Cpl\_api\_m2}} \\[1ex]
\mathrm{Cout}_{\mathrm{st\_api\_m7}} &= \mathrm{ST}_{\mathrm{\_Cpl\_api\_m7}} \\[1ex]
\mathrm{Cout}_{\mathrm{si\_api}} &= \mathrm{GU}_{\mathrm{\_Cpl\_api}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Cu\_ti\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{Kp}_{\mathrm{api}}} \cdot \mathrm{GU}_{\mathrm{\_Cti\_api}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Cu\_mu\_du\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_du\_api}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Cu\_mu\_jej1\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_jej1\_api}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Cu\_mu\_jej2\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_jej2\_api}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Cu\_mu\_ile1\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_ile1\_api}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Cu\_mu\_ile2\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_ile2\_api}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Cu\_mu\_cae\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_cae\_api}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Cu\_mu\_asc\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_asc\_api}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Cu\_mu\_tra\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_tra\_api}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Cu\_mu\_des\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_des\_api}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Cu\_mu\_sig\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_sig\_api}} \\[1ex]
\mathrm{GU}_{\mathrm{\_Cu\_mu\_rec\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_rec\_api}} \\[1ex]
\mathrm{GU}_{\mathrm{\_kdis\_api}} &= \frac{\frac{\mathrm{Ka}_{\mathrm{dis\_api}}}{60} \cdot \mathrm{D50}_{\mathrm{dis\_api}}}{\mathrm{D50}_{\mathrm{dis\_api}} + \mathrm{PODOSE}_{\mathrm{api}} + \mathrm{Mr}_{\mathrm{api}} \cdot \mathopen{}\left(\mathrm{GU}_{\mathrm{\_Asolid\_du\_api}} + \mathrm{GU}_{\mathrm{\_Asolid\_jej1\_api}} + \mathrm{GU}_{\mathrm{\_Asolid\_jej2\_api}} + \mathrm{GU}_{\mathrm{\_Asolid\_ile1\_api}} + \mathrm{GU}_{\mathrm{\_Asolid\_ile2\_api}} + \mathrm{GU}_{\mathrm{\_Asolid\_cae\_api}} + \mathrm{GU}_{\mathrm{\_Asolid\_asc\_api}} + \mathrm{GU}_{\mathrm{\_Asolid\_tra\_api}} + \mathrm{GU}_{\mathrm{\_Asolid\_des\_api}} + \mathrm{GU}_{\mathrm{\_Asolid\_sig\_api}} + \mathrm{GU}_{\mathrm{\_Asolid\_rec\_api}}\right)} \\[1ex]
\mathrm{Cout}_{\mathrm{si\_api\_m1}} &= \mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}} \\[1ex]
\mathrm{Cout}_{\mathrm{si\_api\_m2}} &= \mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}} \\[1ex]
\mathrm{Cout}_{\mathrm{si\_api\_m7}} &= \mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}} \\[1ex]
\mathrm{Fa}_{\mathrm{api}} &= \begin{cases} \frac{\mathrm{GU}_{\mathrm{\_Aabs\_api}}}{\frac{\mathrm{PODOSE}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}} + \frac{\mathrm{SOLDOSE}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}} + \mathrm{GU}_{\mathrm{\_Aapp\_api}}} & \text{if } \frac{\mathrm{PODOSE}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}} + \frac{\mathrm{SOLDOSE}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}} + \mathrm{GU}_{\mathrm{\_Aapp\_api}} > 0 \\ 0 & \text{otherwise} \end{cases} \\[1ex]
\mathrm{Cout}_{\mathrm{sp\_api}} &= \mathrm{SP}_{\mathrm{\_Cpl\_api}} \\[1ex]
\mathrm{SP}_{\mathrm{\_Cu\_ti\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{Kp}_{\mathrm{api}}} \cdot \mathrm{SP}_{\mathrm{\_Cti\_api}} \\[1ex]
\mathrm{Cout}_{\mathrm{sp\_api\_m1}} &= \mathrm{SP}_{\mathrm{\_Cpl\_api\_m1}} \\[1ex]
\mathrm{Cout}_{\mathrm{sp\_api\_m2}} &= \mathrm{SP}_{\mathrm{\_Cpl\_api\_m2}} \\[1ex]
\mathrm{Cout}_{\mathrm{sp\_api\_m7}} &= \mathrm{SP}_{\mathrm{\_Cpl\_api\_m7}} \\[1ex]
\mathrm{Cout}_{\mathrm{pa\_api}} &= \mathrm{PA}_{\mathrm{\_Cpl\_api}} \\[1ex]
\mathrm{PA}_{\mathrm{\_Cu\_ti\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{Kp}_{\mathrm{api}}} \cdot \mathrm{PA}_{\mathrm{\_Cti\_api}} \\[1ex]
\mathrm{Cout}_{\mathrm{pa\_api\_m1}} &= \mathrm{PA}_{\mathrm{\_Cpl\_api\_m1}} \\[1ex]
\mathrm{Cout}_{\mathrm{pa\_api\_m2}} &= \mathrm{PA}_{\mathrm{\_Cpl\_api\_m2}} \\[1ex]
\mathrm{Cout}_{\mathrm{pa\_api\_m7}} &= \mathrm{PA}_{\mathrm{\_Cpl\_api\_m7}} \\[1ex]
\mathrm{Cout}_{\mathrm{mu\_api}} &= \mathrm{MU}_{\mathrm{\_Cpl\_api}} \\[1ex]
\mathrm{MU}_{\mathrm{\_Cu\_ti\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{Kp}_{\mathrm{api}}} \cdot \mathrm{MU}_{\mathrm{\_Cti\_api}} \\[1ex]
\mathrm{Cout}_{\mathrm{mu\_api\_m1}} &= \mathrm{MU}_{\mathrm{\_Cpl\_api\_m1}} \\[1ex]
\mathrm{Cout}_{\mathrm{mu\_api\_m2}} &= \mathrm{MU}_{\mathrm{\_Cpl\_api\_m2}} \\[1ex]
\mathrm{Cout}_{\mathrm{mu\_api\_m7}} &= \mathrm{MU}_{\mathrm{\_Cpl\_api\_m7}} \\[1ex]
\mathrm{Cout}_{\mathrm{sk\_api}} &= \mathrm{SK}_{\mathrm{\_Cpl\_api}} \\[1ex]
\mathrm{Carm}_{\mathrm{api}} &= w_{\mathrm{arm\_sk}} \cdot \mathrm{Cout}_{\mathrm{sk\_api}} + w_{\mathrm{arm\_mu}} \cdot \mathrm{Cout}_{\mathrm{mu\_api}} \\[1ex]
\mathrm{Carm}_{\mathrm{free\_api}} &= \mathrm{fu}_{\mathrm{api}} \cdot \mathrm{Carm}_{\mathrm{api}} \\[1ex]
\mathrm{Carm}_{\mathrm{blood\_api}} &= \mathrm{BP}_{\mathrm{api}} \cdot \mathrm{Carm}_{\mathrm{api}} \\[1ex]
\mathrm{SK}_{\mathrm{\_Cu\_ti\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{Kp}_{\mathrm{api}}} \cdot \mathrm{SK}_{\mathrm{\_Cti\_api}} \\[1ex]
\mathrm{Cout}_{\mathrm{sk\_api\_m1}} &= \mathrm{SK}_{\mathrm{\_Cpl\_api\_m1}} \\[1ex]
\mathrm{Carm}_{\mathrm{api\_m1}} &= w_{\mathrm{arm\_sk}} \cdot \mathrm{Cout}_{\mathrm{sk\_api\_m1}} + w_{\mathrm{arm\_mu}} \cdot \mathrm{Cout}_{\mathrm{mu\_api\_m1}} \\[1ex]
\mathrm{Carm}_{\mathrm{free\_api\_m1}} &= \mathrm{fu}_{\mathrm{api\_m1}} \cdot \mathrm{Carm}_{\mathrm{api\_m1}} \\[1ex]
\mathrm{Carm}_{\mathrm{blood\_api\_m1}} &= \mathrm{BP}_{\mathrm{api\_m1}} \cdot \mathrm{Carm}_{\mathrm{api\_m1}} \\[1ex]
\mathrm{Cout}_{\mathrm{sk\_api\_m2}} &= \mathrm{SK}_{\mathrm{\_Cpl\_api\_m2}} \\[1ex]
\mathrm{Carm}_{\mathrm{api\_m2}} &= w_{\mathrm{arm\_sk}} \cdot \mathrm{Cout}_{\mathrm{sk\_api\_m2}} + w_{\mathrm{arm\_mu}} \cdot \mathrm{Cout}_{\mathrm{mu\_api\_m2}} \\[1ex]
\mathrm{Carm}_{\mathrm{free\_api\_m2}} &= \mathrm{fu}_{\mathrm{api\_m2}} \cdot \mathrm{Carm}_{\mathrm{api\_m2}} \\[1ex]
\mathrm{Carm}_{\mathrm{blood\_api\_m2}} &= \mathrm{BP}_{\mathrm{api\_m2}} \cdot \mathrm{Carm}_{\mathrm{api\_m2}} \\[1ex]
\mathrm{Cout}_{\mathrm{sk\_api\_m7}} &= \mathrm{SK}_{\mathrm{\_Cpl\_api\_m7}} \\[1ex]
\mathrm{Carm}_{\mathrm{api\_m7}} &= w_{\mathrm{arm\_sk}} \cdot \mathrm{Cout}_{\mathrm{sk\_api\_m7}} + w_{\mathrm{arm\_mu}} \cdot \mathrm{Cout}_{\mathrm{mu\_api\_m7}} \\[1ex]
\mathrm{Carm}_{\mathrm{free\_api\_m7}} &= \mathrm{fu}_{\mathrm{api\_m7}} \cdot \mathrm{Carm}_{\mathrm{api\_m7}} \\[1ex]
\mathrm{Carm}_{\mathrm{blood\_api\_m7}} &= \mathrm{BP}_{\mathrm{api\_m7}} \cdot \mathrm{Carm}_{\mathrm{api\_m7}} \\[1ex]
\mathrm{Cout}_{\mathrm{ad\_api}} &= \mathrm{AD}_{\mathrm{\_Cpl\_api}} \\[1ex]
\mathrm{AD}_{\mathrm{\_Cu\_ti\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{Kp}_{\mathrm{api}}} \cdot \mathrm{AD}_{\mathrm{\_Cti\_api}} \\[1ex]
\mathrm{Cout}_{\mathrm{ad\_api\_m1}} &= \mathrm{AD}_{\mathrm{\_Cpl\_api\_m1}} \\[1ex]
\mathrm{Cout}_{\mathrm{ad\_api\_m2}} &= \mathrm{AD}_{\mathrm{\_Cpl\_api\_m2}} \\[1ex]
\mathrm{Cout}_{\mathrm{ad\_api\_m7}} &= \mathrm{AD}_{\mathrm{\_Cpl\_api\_m7}} \\[1ex]
\mathrm{Cout}_{\mathrm{bo\_api}} &= \mathrm{BO}_{\mathrm{\_Cpl\_api}} \\[1ex]
\mathrm{BO}_{\mathrm{\_Cu\_ti\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{Kp}_{\mathrm{api}}} \cdot \mathrm{BO}_{\mathrm{\_Cti\_api}} \\[1ex]
\mathrm{Cout}_{\mathrm{bo\_api\_m1}} &= \mathrm{BO}_{\mathrm{\_Cpl\_api\_m1}} \\[1ex]
\mathrm{Cout}_{\mathrm{bo\_api\_m2}} &= \mathrm{BO}_{\mathrm{\_Cpl\_api\_m2}} \\[1ex]
\mathrm{Cout}_{\mathrm{bo\_api\_m7}} &= \mathrm{BO}_{\mathrm{\_Cpl\_api\_m7}} \\[1ex]
\mathrm{Cout}_{\mathrm{go\_api}} &= \mathrm{GO}_{\mathrm{\_Cpl\_api}} \\[1ex]
\mathrm{GO}_{\mathrm{\_Cu\_ti\_api}} &= \frac{\mathrm{fu}_{\mathrm{api}}}{\mathrm{Kp}_{\mathrm{api}}} \cdot \mathrm{GO}_{\mathrm{\_Cti\_api}} \\[1ex]
\mathrm{Cout}_{\mathrm{go\_api\_m1}} &= \mathrm{GO}_{\mathrm{\_Cpl\_api\_m1}} \\[1ex]
\mathrm{Cout}_{\mathrm{go\_api\_m2}} &= \mathrm{GO}_{\mathrm{\_Cpl\_api\_m2}} \\[1ex]
\mathrm{Cout}_{\mathrm{go\_api\_m7}} &= \mathrm{GO}_{\mathrm{\_Cpl\_api\_m7}} \\[1ex]
\mathrm{COAG}_{\mathrm{\_INR}} &= \mathrm{COAG}_{\mathrm{\_INR\_ref}} \cdot \mathopen{}\left(1 + \mathrm{COAG}_{\mathrm{\_slope\_api\_INR}} \cdot \mathrm{Carm}_{\mathrm{api}}\right) \\[1ex]
\mathrm{COAG}_{\mathrm{\_INR\_change}} &= \mathrm{COAG}_{\mathrm{\_INR}} - \mathrm{COAG}_{\mathrm{\_INR\_ref}} \\[1ex]
\mathrm{COAG}_{\mathrm{\_INR\_ratio}} &= \frac{\mathrm{COAG}_{\mathrm{\_INR}}}{\mathrm{COAG}_{\mathrm{\_INR\_ref}}} \\[1ex]
\mathrm{COAG}_{\mathrm{\_INR\_relchange}} &= \frac{\mathrm{COAG}_{\mathrm{\_INR}} - \mathrm{COAG}_{\mathrm{\_INR\_ref}}}{\mathrm{COAG}_{\mathrm{\_INR\_ref}}} \\[1ex]
\mathrm{COAG}_{\mathrm{\_PT}} &= \mathrm{COAG}_{\mathrm{\_PT\_ref}} \cdot \mathopen{}\left(1 + \mathrm{COAG}_{\mathrm{\_slope\_api\_PT}} \cdot \mathrm{Carm}_{\mathrm{api}}\right) \\[1ex]
\mathrm{COAG}_{\mathrm{\_PT\_change}} &= \mathrm{COAG}_{\mathrm{\_PT}} - \mathrm{COAG}_{\mathrm{\_PT\_ref}} \\[1ex]
\mathrm{COAG}_{\mathrm{\_PT\_ratio}} &= \frac{\mathrm{COAG}_{\mathrm{\_PT}}}{\mathrm{COAG}_{\mathrm{\_PT\_ref}}} \\[1ex]
\mathrm{COAG}_{\mathrm{\_PT\_relchange}} &= \frac{\mathrm{COAG}_{\mathrm{\_PT}} - \mathrm{COAG}_{\mathrm{\_PT\_ref}}}{\mathrm{COAG}_{\mathrm{\_PT\_ref}}} \\[1ex]
\mathrm{COAG}_{\mathrm{\_mPT}} &= \mathrm{COAG}_{\mathrm{\_mPT\_ref}} \cdot \mathopen{}\left(1 + \frac{\mathrm{COAG}_{\mathrm{\_Emax\_mPT}} \cdot \mathrm{Carm}_{\mathrm{api}}}{\mathrm{Carm}_{\mathrm{api}} + \mathrm{COAG}_{\mathrm{\_EC50\_api\_mPT}}}\right) \\[1ex]
\mathrm{COAG}_{\mathrm{\_mPT\_change}} &= \mathrm{COAG}_{\mathrm{\_mPT}} - \mathrm{COAG}_{\mathrm{\_mPT\_ref}} \\[1ex]
\mathrm{COAG}_{\mathrm{\_mPT\_ratio}} &= \frac{\mathrm{COAG}_{\mathrm{\_mPT}}}{\mathrm{COAG}_{\mathrm{\_mPT\_ref}}} \\[1ex]
\mathrm{COAG}_{\mathrm{\_mPT\_relchange}} &= \frac{\mathrm{COAG}_{\mathrm{\_mPT}} - \mathrm{COAG}_{\mathrm{\_mPT\_ref}}}{\mathrm{COAG}_{\mathrm{\_mPT\_ref}}} \\[1ex]
\mathrm{COAG}_{\mathrm{\_aPTT}} &= \mathrm{COAG}_{\mathrm{\_aPTT\_ref}} \cdot \mathopen{}\left(1 + \frac{\mathrm{COAG}_{\mathrm{\_Emax\_aPTT}} \cdot \mathrm{Carm}_{\mathrm{api}}}{\mathrm{Carm}_{\mathrm{api}} + \mathrm{COAG}_{\mathrm{\_EC50\_api\_aPTT}}}\right) \\[1ex]
\mathrm{COAG}_{\mathrm{\_aPTT\_change}} &= \mathrm{COAG}_{\mathrm{\_aPTT}} - \mathrm{COAG}_{\mathrm{\_aPTT\_ref}} \\[1ex]
\mathrm{COAG}_{\mathrm{\_aPTT\_ratio}} &= \frac{\mathrm{COAG}_{\mathrm{\_aPTT}}}{\mathrm{COAG}_{\mathrm{\_aPTT\_ref}}} \\[1ex]
\mathrm{COAG}_{\mathrm{\_aPTT\_relchange}} &= \frac{\mathrm{COAG}_{\mathrm{\_aPTT}} - \mathrm{COAG}_{\mathrm{\_aPTT\_ref}}}{\mathrm{COAG}_{\mathrm{\_aPTT\_ref}}} \\[1ex]
\mathrm{COAG}_{\mathrm{\_antiXa\_activity}} &= \mathrm{COAG}_{\mathrm{\_antiXa\_slope}} \cdot \mathrm{Carm}_{\mathrm{api}} \\[1ex]
\mathrm{COAG}_{\mathrm{\_antiXa\_activity\_gram}} &= \mathrm{COAG}_{\mathrm{\_antiXa\_gram\_slope}} \cdot \mathrm{Carm}_{\mathrm{api}} \\[1ex]
\mathrm{Rurine}_{\mathrm{api}} &= v_{\mathrm{KI\_\_J\_gfr\_api}} \\[1ex]
\mathrm{Rurine}_{\mathrm{api\_m1}} &= v_{\mathrm{KI\_\_J\_gfr\_api\_m1}} \\[1ex]
\mathrm{Rurine}_{\mathrm{api\_m7}} &= v_{\mathrm{KI\_\_J\_gfr\_api\_m7}} \\[1ex]
\mathrm{Rabs}_{\mathrm{api}} &= v_{\mathrm{GU\_\_J\_abs\_du\_api}} + v_{\mathrm{GU\_\_J\_abs\_jej1\_api}} + v_{\mathrm{GU\_\_J\_abs\_jej2\_api}} + v_{\mathrm{GU\_\_J\_abs\_ile1\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_abs\_ile2\_api}} + v_{\mathrm{GU\_\_J\_abs\_cae\_api}} + v_{\mathrm{GU\_\_J\_abs\_asc\_api}} + v_{\mathrm{GU\_\_J\_abs\_tra\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_abs\_des\_api}} + v_{\mathrm{GU\_\_J\_abs\_sig\_api}} + v_{\mathrm{GU\_\_J\_abs\_rec\_api}} \\[1ex]
\mathrm{Rfeces}_{\mathrm{api}} &= v_{\mathrm{GU\_\_J\_feces\_du\_api}} + v_{\mathrm{GU\_\_J\_feces\_jej1\_api}} + v_{\mathrm{GU\_\_J\_feces\_jej2\_api}} + v_{\mathrm{GU\_\_J\_feces\_ile1\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_feces\_ile2\_api}} + v_{\mathrm{GU\_\_J\_feces\_cae\_api}} + v_{\mathrm{GU\_\_J\_feces\_asc\_api}} + v_{\mathrm{GU\_\_J\_feces\_tra\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_feces\_des\_api}} + v_{\mathrm{GU\_\_J\_feces\_sig\_api}} + v_{\mathrm{GU\_\_J\_tr\_rec\_api}} + v_{\mathrm{GU\_\_J\_feces\_rec\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_trs\_rec\_api}} \\[1ex]
\mathrm{Reff}_{\mathrm{api}} &= v_{\mathrm{GU\_\_APISEC\_du}} + v_{\mathrm{GU\_\_APISEC\_jej1}} + v_{\mathrm{GU\_\_APISEC\_jej2}} + v_{\mathrm{GU\_\_APISEC\_ile1}} \\
&\quad {} + v_{\mathrm{GU\_\_APISEC\_ile2}}
\end{aligned}
$$

## Reactions

| Rate | Id | Name | Equation | Modifiers |
| --- | --- | --- | --- | --- |
| $v_{\mathrm{J\_iv\_api}}$ | `J_iv_api` | intravenous application api | $\varnothing \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |  |
| $v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api}}$ | `LU__J_in_ve_pl_api` | inflow api from venous pool | $\mathrm{Cve}_{\mathrm{api}} \longrightarrow \mathrm{LU}_{\mathrm{\_Cpl\_api}}$ |  |
| $v_{\mathrm{LU\_\_J\_out\_pl\_api}}$ | `LU__J_out_pl_api` | outflow api into arterial pool | $\mathrm{LU}_{\mathrm{\_Cpl\_api}} \longrightarrow \mathrm{Car}_{\mathrm{api}}$ |  |
| $v_{\mathrm{LU\_\_J\_ti\_api}}$ | `LU__J_ti_api` | exchange api plasma and tissue | $\mathrm{LU}_{\mathrm{\_Cpl\_api}} \rightleftharpoons \mathrm{LU}_{\mathrm{\_Cti\_api}}$ |  |
| $v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api\_m1}}$ | `LU__J_in_ve_pl_api_m1` | inflow api\_m1 from venous pool | $\mathrm{Cve}_{\mathrm{api\_m1}} \longrightarrow \mathrm{LU}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{LU\_\_J\_out\_pl\_api\_m1}}$ | `LU__J_out_pl_api_m1` | outflow api\_m1 into arterial pool | $\mathrm{LU}_{\mathrm{\_Cpl\_api\_m1}} \longrightarrow \mathrm{Car}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api\_m2}}$ | `LU__J_in_ve_pl_api_m2` | inflow api\_m2 from venous pool | $\mathrm{Cve}_{\mathrm{api\_m2}} \longrightarrow \mathrm{LU}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{LU\_\_J\_out\_pl\_api\_m2}}$ | `LU__J_out_pl_api_m2` | outflow api\_m2 into arterial pool | $\mathrm{LU}_{\mathrm{\_Cpl\_api\_m2}} \longrightarrow \mathrm{Car}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api\_m7}}$ | `LU__J_in_ve_pl_api_m7` | inflow api\_m7 from venous pool | $\mathrm{Cve}_{\mathrm{api\_m7}} \longrightarrow \mathrm{LU}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{LU\_\_J\_out\_pl\_api\_m7}}$ | `LU__J_out_pl_api_m7` | outflow api\_m7 into arterial pool | $\mathrm{LU}_{\mathrm{\_Cpl\_api\_m7}} \longrightarrow \mathrm{Car}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api}}$ | `HE__J_in_ar_pl_api` | inflow api from arterial pool | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{HE}_{\mathrm{\_Cpl\_api}}$ |  |
| $v_{\mathrm{HE\_\_J\_out\_pl\_api}}$ | `HE__J_out_pl_api` | outflow api into venous pool | $\mathrm{HE}_{\mathrm{\_Cpl\_api}} \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |  |
| $v_{\mathrm{HE\_\_J\_ti\_api}}$ | `HE__J_ti_api` | exchange api plasma and tissue | $\mathrm{HE}_{\mathrm{\_Cpl\_api}} \rightleftharpoons \mathrm{HE}_{\mathrm{\_Cti\_api}}$ |  |
| $v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api\_m1}}$ | `HE__J_in_ar_pl_api_m1` | inflow api\_m1 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m1}} \longrightarrow \mathrm{HE}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{HE\_\_J\_out\_pl\_api\_m1}}$ | `HE__J_out_pl_api_m1` | outflow api\_m1 into venous pool | $\mathrm{HE}_{\mathrm{\_Cpl\_api\_m1}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api\_m2}}$ | `HE__J_in_ar_pl_api_m2` | inflow api\_m2 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m2}} \longrightarrow \mathrm{HE}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{HE\_\_J\_out\_pl\_api\_m2}}$ | `HE__J_out_pl_api_m2` | outflow api\_m2 into venous pool | $\mathrm{HE}_{\mathrm{\_Cpl\_api\_m2}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api\_m7}}$ | `HE__J_in_ar_pl_api_m7` | inflow api\_m7 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m7}} \longrightarrow \mathrm{HE}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{HE\_\_J\_out\_pl\_api\_m7}}$ | `HE__J_out_pl_api_m7` | outflow api\_m7 into venous pool | $\mathrm{HE}_{\mathrm{\_Cpl\_api\_m7}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api}}$ | `BR__J_in_ar_pl_api` | inflow api from arterial pool | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{BR}_{\mathrm{\_Cpl\_api}}$ |  |
| $v_{\mathrm{BR\_\_J\_out\_pl\_api}}$ | `BR__J_out_pl_api` | outflow api into venous pool | $\mathrm{BR}_{\mathrm{\_Cpl\_api}} \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |  |
| $v_{\mathrm{BR\_\_J\_ti\_api}}$ | `BR__J_ti_api` | exchange api plasma and tissue | $\mathrm{BR}_{\mathrm{\_Cpl\_api}} \rightleftharpoons \mathrm{BR}_{\mathrm{\_Cti\_api}}$ |  |
| $v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api\_m1}}$ | `BR__J_in_ar_pl_api_m1` | inflow api\_m1 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m1}} \longrightarrow \mathrm{BR}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{BR\_\_J\_out\_pl\_api\_m1}}$ | `BR__J_out_pl_api_m1` | outflow api\_m1 into venous pool | $\mathrm{BR}_{\mathrm{\_Cpl\_api\_m1}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api\_m2}}$ | `BR__J_in_ar_pl_api_m2` | inflow api\_m2 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m2}} \longrightarrow \mathrm{BR}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{BR\_\_J\_out\_pl\_api\_m2}}$ | `BR__J_out_pl_api_m2` | outflow api\_m2 into venous pool | $\mathrm{BR}_{\mathrm{\_Cpl\_api\_m2}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api\_m7}}$ | `BR__J_in_ar_pl_api_m7` | inflow api\_m7 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m7}} \longrightarrow \mathrm{BR}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{BR\_\_J\_out\_pl\_api\_m7}}$ | `BR__J_out_pl_api_m7` | outflow api\_m7 into venous pool | $\mathrm{BR}_{\mathrm{\_Cpl\_api\_m7}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api}}$ | `LI__J_in_ar_pl_api` | inflow api from arterial pool | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{LI}_{\mathrm{\_Cpl\_api}}$ |  |
| $v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api}}$ | `LI__J_shunt_ar_pl_api` | shunt api from arterial pool past the liver into venous pool | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |  |
| $v_{\mathrm{LI\_\_J\_in\_po\_pl\_api}}$ | `LI__J_in_po_pl_api` | inflow api from portal pool | $\mathrm{Cpo}_{\mathrm{api}} \longrightarrow \mathrm{LI}_{\mathrm{\_Cpl\_api}}$ |  |
| $v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api}}$ | `LI__J_shunt_po_pl_api` | shunt api from portal pool past the liver into venous pool | $\mathrm{Cpo}_{\mathrm{api}} \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |  |
| $v_{\mathrm{LI\_\_J\_out\_pl\_api}}$ | `LI__J_out_pl_api` | outflow api into venous pool | $\mathrm{LI}_{\mathrm{\_Cpl\_api}} \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |  |
| $v_{\mathrm{LI\_\_J\_ti\_api}}$ | `LI__J_ti_api` | exchange api plasma and tissue | $\mathrm{LI}_{\mathrm{\_Cpl\_api}} \rightleftharpoons \mathrm{LI}_{\mathrm{\_Cti\_api}}$ |  |
| $v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api\_m1}}$ | `LI__J_in_ar_pl_api_m1` | inflow api\_m1 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m1}} \longrightarrow \mathrm{LI}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api\_m1}}$ | `LI__J_shunt_ar_pl_api_m1` | shunt api\_m1 from arterial pool past the liver into venous pool | $\mathrm{Car}_{\mathrm{api\_m1}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{LI\_\_J\_in\_po\_pl\_api\_m1}}$ | `LI__J_in_po_pl_api_m1` | inflow api\_m1 from portal pool | $\mathrm{Cpo}_{\mathrm{api\_m1}} \longrightarrow \mathrm{LI}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api\_m1}}$ | `LI__J_shunt_po_pl_api_m1` | shunt api\_m1 from portal pool past the liver into venous pool | $\mathrm{Cpo}_{\mathrm{api\_m1}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{LI\_\_J\_out\_pl\_api\_m1}}$ | `LI__J_out_pl_api_m1` | outflow api\_m1 into venous pool | $\mathrm{LI}_{\mathrm{\_Cpl\_api\_m1}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{LI\_\_J\_is\_api\_m1}}$ | `LI__J_is_api_m1` | exchange api\_m1 plasma and interstitium | $\mathrm{LI}_{\mathrm{\_Cpl\_api\_m1}} \rightleftharpoons \mathrm{LI}_{\mathrm{\_Cis\_api\_m1}}$ |  |
| $v_{\mathrm{LI\_\_J\_ic\_api\_m1}}$ | `LI__J_ic_api_m1` | passive exchange api\_m1 interstitium and cells | $\mathrm{LI}_{\mathrm{\_Cis\_api\_m1}} \rightleftharpoons \mathrm{LI}_{\mathrm{\_Cic\_api\_m1}}$ |  |
| $v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api\_m2}}$ | `LI__J_in_ar_pl_api_m2` | inflow api\_m2 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m2}} \longrightarrow \mathrm{LI}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api\_m2}}$ | `LI__J_shunt_ar_pl_api_m2` | shunt api\_m2 from arterial pool past the liver into venous pool | $\mathrm{Car}_{\mathrm{api\_m2}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{LI\_\_J\_in\_po\_pl\_api\_m2}}$ | `LI__J_in_po_pl_api_m2` | inflow api\_m2 from portal pool | $\mathrm{Cpo}_{\mathrm{api\_m2}} \longrightarrow \mathrm{LI}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api\_m2}}$ | `LI__J_shunt_po_pl_api_m2` | shunt api\_m2 from portal pool past the liver into venous pool | $\mathrm{Cpo}_{\mathrm{api\_m2}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{LI\_\_J\_out\_pl\_api\_m2}}$ | `LI__J_out_pl_api_m2` | outflow api\_m2 into venous pool | $\mathrm{LI}_{\mathrm{\_Cpl\_api\_m2}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{LI\_\_J\_is\_api\_m2}}$ | `LI__J_is_api_m2` | exchange api\_m2 plasma and interstitium | $\mathrm{LI}_{\mathrm{\_Cpl\_api\_m2}} \rightleftharpoons \mathrm{LI}_{\mathrm{\_Cis\_api\_m2}}$ |  |
| $v_{\mathrm{LI\_\_J\_ic\_api\_m2}}$ | `LI__J_ic_api_m2` | passive exchange api\_m2 interstitium and cells | $\mathrm{LI}_{\mathrm{\_Cis\_api\_m2}} \rightleftharpoons \mathrm{LI}_{\mathrm{\_Cic\_api\_m2}}$ |  |
| $v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api\_m7}}$ | `LI__J_in_ar_pl_api_m7` | inflow api\_m7 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m7}} \longrightarrow \mathrm{LI}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api\_m7}}$ | `LI__J_shunt_ar_pl_api_m7` | shunt api\_m7 from arterial pool past the liver into venous pool | $\mathrm{Car}_{\mathrm{api\_m7}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{LI\_\_J\_in\_po\_pl\_api\_m7}}$ | `LI__J_in_po_pl_api_m7` | inflow api\_m7 from portal pool | $\mathrm{Cpo}_{\mathrm{api\_m7}} \longrightarrow \mathrm{LI}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api\_m7}}$ | `LI__J_shunt_po_pl_api_m7` | shunt api\_m7 from portal pool past the liver into venous pool | $\mathrm{Cpo}_{\mathrm{api\_m7}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{LI\_\_J\_out\_pl\_api\_m7}}$ | `LI__J_out_pl_api_m7` | outflow api\_m7 into venous pool | $\mathrm{LI}_{\mathrm{\_Cpl\_api\_m7}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{LI\_\_J\_is\_api\_m7}}$ | `LI__J_is_api_m7` | exchange api\_m7 plasma and interstitium | $\mathrm{LI}_{\mathrm{\_Cpl\_api\_m7}} \rightleftharpoons \mathrm{LI}_{\mathrm{\_Cis\_api\_m7}}$ |  |
| $v_{\mathrm{LI\_\_J\_ic\_api\_m7}}$ | `LI__J_ic_api_m7` | passive exchange api\_m7 interstitium and cells | $\mathrm{LI}_{\mathrm{\_Cis\_api\_m7}} \rightleftharpoons \mathrm{LI}_{\mathrm{\_Cic\_api\_m7}}$ |  |
| $v_{\mathrm{LI\_\_API2M}}$ | `LI__API2M` | api -&gt; api\_m2, api\_m7 (CYP3A4) | $\mathrm{LI}_{\mathrm{\_Cti\_api}} \longrightarrow 0.78 \, \mathrm{LI}_{\mathrm{\_Cic\_api\_m2}} + 0.22 \, \mathrm{LI}_{\mathrm{\_Cic\_api\_m7}}$ |  |
| $v_{\mathrm{LI\_\_M22M1}}$ | `LI__M22M1` | api\_m2 -&gt; api\_m1 (SULT1A1) | $\mathrm{LI}_{\mathrm{\_Cic\_api\_m2}} \longrightarrow \mathrm{LI}_{\mathrm{\_Cic\_api\_m1}}$ |  |
| $v_{\mathrm{LI\_\_M1EXBI}}$ | `LI__M1EXBI` | efflux api\_m1 apical | $\mathrm{LI}_{\mathrm{\_Cic\_api\_m1}} \longrightarrow \mathrm{Cbile}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{LI\_\_M2EXBI}}$ | `LI__M2EXBI` | efflux api\_m2 apical | $\mathrm{LI}_{\mathrm{\_Cic\_api\_m2}} \longrightarrow \mathrm{Cbile}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{LI\_\_M7EXBI}}$ | `LI__M7EXBI` | efflux api\_m7 apical | $\mathrm{LI}_{\mathrm{\_Cic\_api\_m7}} \longrightarrow \mathrm{Cbile}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api}}$ | `KI__J_in_ar_pl_api` | inflow api from arterial pool | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{KI}_{\mathrm{\_Cpl\_api}}$ |  |
| $v_{\mathrm{KI\_\_J\_out\_pl\_api}}$ | `KI__J_out_pl_api` | outflow api into venous pool | $\mathrm{KI}_{\mathrm{\_Cpl\_api}} \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |  |
| $v_{\mathrm{KI\_\_J\_gfr\_api}}$ | `KI__J_gfr_api` | glomerular filtration api | $\mathrm{KI}_{\mathrm{\_Cpl\_api}} \longrightarrow \mathrm{Aurine}_{\mathrm{api}}$ | $\mathrm{Car}_{\mathrm{api}}$ |
| $v_{\mathrm{KI\_\_J\_ti\_api}}$ | `KI__J_ti_api` | exchange api plasma and tissue | $\mathrm{KI}_{\mathrm{\_Cpl\_api}} \rightleftharpoons \mathrm{KI}_{\mathrm{\_Cti\_api}}$ |  |
| $v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api\_m1}}$ | `KI__J_in_ar_pl_api_m1` | inflow api\_m1 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m1}} \longrightarrow \mathrm{KI}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{KI\_\_J\_out\_pl\_api\_m1}}$ | `KI__J_out_pl_api_m1` | outflow api\_m1 into venous pool | $\mathrm{KI}_{\mathrm{\_Cpl\_api\_m1}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{KI\_\_J\_gfr\_api\_m1}}$ | `KI__J_gfr_api_m1` | glomerular filtration api\_m1 | $\mathrm{KI}_{\mathrm{\_Cpl\_api\_m1}} \longrightarrow \mathrm{Aurine}_{\mathrm{api\_m1}}$ | $\mathrm{Car}_{\mathrm{api\_m1}}$ |
| $v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api\_m2}}$ | `KI__J_in_ar_pl_api_m2` | inflow api\_m2 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m2}} \longrightarrow \mathrm{KI}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{KI\_\_J\_out\_pl\_api\_m2}}$ | `KI__J_out_pl_api_m2` | outflow api\_m2 into venous pool | $\mathrm{KI}_{\mathrm{\_Cpl\_api\_m2}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api\_m7}}$ | `KI__J_in_ar_pl_api_m7` | inflow api\_m7 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m7}} \longrightarrow \mathrm{KI}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{KI\_\_J\_out\_pl\_api\_m7}}$ | `KI__J_out_pl_api_m7` | outflow api\_m7 into venous pool | $\mathrm{KI}_{\mathrm{\_Cpl\_api\_m7}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{KI\_\_J\_gfr\_api\_m7}}$ | `KI__J_gfr_api_m7` | glomerular filtration api\_m7 | $\mathrm{KI}_{\mathrm{\_Cpl\_api\_m7}} \longrightarrow \mathrm{Aurine}_{\mathrm{api\_m7}}$ | $\mathrm{Car}_{\mathrm{api\_m7}}$ |
| $v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api}}$ | `ST__J_in_ar_pl_api` | inflow api from arterial pool | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{ST}_{\mathrm{\_Cpl\_api}}$ |  |
| $v_{\mathrm{ST\_\_J\_out\_pl\_api}}$ | `ST__J_out_pl_api` | outflow api into portal pool | $\mathrm{ST}_{\mathrm{\_Cpl\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |  |
| $v_{\mathrm{ST\_\_J\_ti\_api}}$ | `ST__J_ti_api` | exchange api plasma and tissue | $\mathrm{ST}_{\mathrm{\_Cpl\_api}} \rightleftharpoons \mathrm{ST}_{\mathrm{\_Cti\_api}}$ |  |
| $v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api\_m1}}$ | `ST__J_in_ar_pl_api_m1` | inflow api\_m1 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m1}} \longrightarrow \mathrm{ST}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{ST\_\_J\_out\_pl\_api\_m1}}$ | `ST__J_out_pl_api_m1` | outflow api\_m1 into portal pool | $\mathrm{ST}_{\mathrm{\_Cpl\_api\_m1}} \longrightarrow \mathrm{Cpo}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api\_m2}}$ | `ST__J_in_ar_pl_api_m2` | inflow api\_m2 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m2}} \longrightarrow \mathrm{ST}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{ST\_\_J\_out\_pl\_api\_m2}}$ | `ST__J_out_pl_api_m2` | outflow api\_m2 into portal pool | $\mathrm{ST}_{\mathrm{\_Cpl\_api\_m2}} \longrightarrow \mathrm{Cpo}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api\_m7}}$ | `ST__J_in_ar_pl_api_m7` | inflow api\_m7 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m7}} \longrightarrow \mathrm{ST}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{ST\_\_J\_out\_pl\_api\_m7}}$ | `ST__J_out_pl_api_m7` | outflow api\_m7 into portal pool | $\mathrm{ST}_{\mathrm{\_Cpl\_api\_m7}} \longrightarrow \mathrm{Cpo}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api}}$ | `GU__J_in_ar_pl_api` | inflow api from arterial pool | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_out\_pl\_api}}$ | `GU__J_out_pl_api` | outflow api into portal pool | $\mathrm{GU}_{\mathrm{\_Cpl\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_ti\_api}}$ | `GU__J_ti_api` | exchange api plasma and tissue | $\mathrm{GU}_{\mathrm{\_Cpl\_api}} \rightleftharpoons \mathrm{GU}_{\mathrm{\_Cti\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_in\_du\_api}}$ | `GU__J_mu_in_du_api` | inflow api into mucosa duodenum | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_du\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_out\_du\_api}}$ | `GU__J_mu_out_du_api` | outflow api from mucosa duodenum | $\mathrm{GU}_{\mathrm{\_Cmu\_du\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_in\_jej1\_api}}$ | `GU__J_mu_in_jej1_api` | inflow api into mucosa upper jejunum | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_jej1\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_out\_jej1\_api}}$ | `GU__J_mu_out_jej1_api` | outflow api from mucosa upper jejunum | $\mathrm{GU}_{\mathrm{\_Cmu\_jej1\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_in\_jej2\_api}}$ | `GU__J_mu_in_jej2_api` | inflow api into mucosa lower jejunum | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_jej2\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_out\_jej2\_api}}$ | `GU__J_mu_out_jej2_api` | outflow api from mucosa lower jejunum | $\mathrm{GU}_{\mathrm{\_Cmu\_jej2\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_in\_ile1\_api}}$ | `GU__J_mu_in_ile1_api` | inflow api into mucosa upper ileum | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_ile1\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_out\_ile1\_api}}$ | `GU__J_mu_out_ile1_api` | outflow api from mucosa upper ileum | $\mathrm{GU}_{\mathrm{\_Cmu\_ile1\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_in\_ile2\_api}}$ | `GU__J_mu_in_ile2_api` | inflow api into mucosa lower ileum | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_ile2\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_out\_ile2\_api}}$ | `GU__J_mu_out_ile2_api` | outflow api from mucosa lower ileum | $\mathrm{GU}_{\mathrm{\_Cmu\_ile2\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_in\_cae\_api}}$ | `GU__J_mu_in_cae_api` | inflow api into mucosa caecum | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_cae\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_out\_cae\_api}}$ | `GU__J_mu_out_cae_api` | outflow api from mucosa caecum | $\mathrm{GU}_{\mathrm{\_Cmu\_cae\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_in\_asc\_api}}$ | `GU__J_mu_in_asc_api` | inflow api into mucosa colon ascendens | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_asc\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_out\_asc\_api}}$ | `GU__J_mu_out_asc_api` | outflow api from mucosa colon ascendens | $\mathrm{GU}_{\mathrm{\_Cmu\_asc\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_in\_tra\_api}}$ | `GU__J_mu_in_tra_api` | inflow api into mucosa colon transversum | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_tra\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_out\_tra\_api}}$ | `GU__J_mu_out_tra_api` | outflow api from mucosa colon transversum | $\mathrm{GU}_{\mathrm{\_Cmu\_tra\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_in\_des\_api}}$ | `GU__J_mu_in_des_api` | inflow api into mucosa colon descendens | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_des\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_out\_des\_api}}$ | `GU__J_mu_out_des_api` | outflow api from mucosa colon descendens | $\mathrm{GU}_{\mathrm{\_Cmu\_des\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_in\_sig\_api}}$ | `GU__J_mu_in_sig_api` | inflow api into mucosa colon sigmoid | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_sig\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_out\_sig\_api}}$ | `GU__J_mu_out_sig_api` | outflow api from mucosa colon sigmoid | $\mathrm{GU}_{\mathrm{\_Cmu\_sig\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_in\_rec\_api}}$ | `GU__J_mu_in_rec_api` | inflow api into mucosa rectum | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_rec\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_mu\_out\_rec\_api}}$ | `GU__J_mu_out_rec_api` | outflow api from mucosa rectum | $\mathrm{GU}_{\mathrm{\_Cmu\_rec\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_st\_api}}$ | `GU__J_tr_st_api` | transit api stomach | $\mathrm{GU}_{\mathrm{\_Clumen\_st\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_du\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_du\_api}}$ | `GU__J_tr_du_api` | transit api duodenum | $\mathrm{GU}_{\mathrm{\_Clumen\_du\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_du\_api}}$ | `GU__J_abs_du_api` | absorption api duodenum | $\mathrm{GU}_{\mathrm{\_Clumen\_du\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_du\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_feces\_du\_api}}$ | `GU__J_feces_du_api` | unabsorbed fraction api duodenum into the feces | $\mathrm{GU}_{\mathrm{\_Clumen\_du\_api}} \longrightarrow \mathrm{Afeces}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_jej1\_api}}$ | `GU__J_tr_jej1_api` | transit api upper jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_jej1\_api}}$ | `GU__J_abs_jej1_api` | absorption api upper jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_jej1\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_feces\_jej1\_api}}$ | `GU__J_feces_jej1_api` | unabsorbed fraction api upper jejunum into the feces | $\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api}} \longrightarrow \mathrm{Afeces}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_jej2\_api}}$ | `GU__J_tr_jej2_api` | transit api lower jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_jej2\_api}}$ | `GU__J_abs_jej2_api` | absorption api lower jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_jej2\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_feces\_jej2\_api}}$ | `GU__J_feces_jej2_api` | unabsorbed fraction api lower jejunum into the feces | $\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api}} \longrightarrow \mathrm{Afeces}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_ile1\_api}}$ | `GU__J_tr_ile1_api` | transit api upper ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_ile1\_api}}$ | `GU__J_abs_ile1_api` | absorption api upper ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_ile1\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_feces\_ile1\_api}}$ | `GU__J_feces_ile1_api` | unabsorbed fraction api upper ileum into the feces | $\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api}} \longrightarrow \mathrm{Afeces}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_ile2\_api}}$ | `GU__J_tr_ile2_api` | transit api lower ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_cae\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_ile2\_api}}$ | `GU__J_abs_ile2_api` | absorption api lower ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_ile2\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_feces\_ile2\_api}}$ | `GU__J_feces_ile2_api` | unabsorbed fraction api lower ileum into the feces | $\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api}} \longrightarrow \mathrm{Afeces}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_cae\_api}}$ | `GU__J_tr_cae_api` | transit api caecum | $\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_asc\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_cae\_api}}$ | `GU__J_abs_cae_api` | absorption api caecum | $\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_cae\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_feces\_cae\_api}}$ | `GU__J_feces_cae_api` | unabsorbed fraction api caecum into the feces | $\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api}} \longrightarrow \mathrm{Afeces}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_asc\_api}}$ | `GU__J_tr_asc_api` | transit api colon ascendens | $\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_tra\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_asc\_api}}$ | `GU__J_abs_asc_api` | absorption api colon ascendens | $\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_asc\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_feces\_asc\_api}}$ | `GU__J_feces_asc_api` | unabsorbed fraction api colon ascendens into the feces | $\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api}} \longrightarrow \mathrm{Afeces}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_tra\_api}}$ | `GU__J_tr_tra_api` | transit api colon transversum | $\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_des\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_tra\_api}}$ | `GU__J_abs_tra_api` | absorption api colon transversum | $\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_tra\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_feces\_tra\_api}}$ | `GU__J_feces_tra_api` | unabsorbed fraction api colon transversum into the feces | $\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api}} \longrightarrow \mathrm{Afeces}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_des\_api}}$ | `GU__J_tr_des_api` | transit api colon descendens | $\mathrm{GU}_{\mathrm{\_Clumen\_des\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_sig\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_des\_api}}$ | `GU__J_abs_des_api` | absorption api colon descendens | $\mathrm{GU}_{\mathrm{\_Clumen\_des\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_des\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_feces\_des\_api}}$ | `GU__J_feces_des_api` | unabsorbed fraction api colon descendens into the feces | $\mathrm{GU}_{\mathrm{\_Clumen\_des\_api}} \longrightarrow \mathrm{Afeces}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_sig\_api}}$ | `GU__J_tr_sig_api` | transit api colon sigmoid | $\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_rec\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_sig\_api}}$ | `GU__J_abs_sig_api` | absorption api colon sigmoid | $\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_sig\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_feces\_sig\_api}}$ | `GU__J_feces_sig_api` | unabsorbed fraction api colon sigmoid into the feces | $\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api}} \longrightarrow \mathrm{Afeces}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_rec\_api}}$ | `GU__J_tr_rec_api` | transit api rectum | $\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api}} \longrightarrow \mathrm{Afeces}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_rec\_api}}$ | `GU__J_abs_rec_api` | absorption api rectum | $\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cmu\_rec\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_feces\_rec\_api}}$ | `GU__J_feces_rec_api` | unabsorbed fraction api rectum into the feces | $\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api}} \longrightarrow \mathrm{Afeces}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_bile\_api}}$ | `GU__J_bile_api` | transit api bile to intestinal lumen | $\mathrm{Cbile}_{\mathrm{api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_du\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_po\_api}}$ | `GU__J_po_api` | dissolution api (tablet) stomach | $\varnothing \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_st\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_trs\_st\_api}}$ | `GU__J_trs_st_api` | transit api undissolved stomach | $\varnothing \longrightarrow \mathrm{GU}_{\mathrm{\_Asolid\_du\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_dis\_du\_api}}$ | `GU__J_dis_du_api` | dissolution api duodenum | $\mathrm{GU}_{\mathrm{\_Asolid\_du\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_du\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_trs\_du\_api}}$ | `GU__J_trs_du_api` | transit api undissolved duodenum | $\mathrm{GU}_{\mathrm{\_Asolid\_du\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Asolid\_jej1\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_dis\_jej1\_api}}$ | `GU__J_dis_jej1_api` | dissolution api upper jejunum | $\mathrm{GU}_{\mathrm{\_Asolid\_jej1\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_trs\_jej1\_api}}$ | `GU__J_trs_jej1_api` | transit api undissolved upper jejunum | $\mathrm{GU}_{\mathrm{\_Asolid\_jej1\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Asolid\_jej2\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_dis\_jej2\_api}}$ | `GU__J_dis_jej2_api` | dissolution api lower jejunum | $\mathrm{GU}_{\mathrm{\_Asolid\_jej2\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_trs\_jej2\_api}}$ | `GU__J_trs_jej2_api` | transit api undissolved lower jejunum | $\mathrm{GU}_{\mathrm{\_Asolid\_jej2\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Asolid\_ile1\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_dis\_ile1\_api}}$ | `GU__J_dis_ile1_api` | dissolution api upper ileum | $\mathrm{GU}_{\mathrm{\_Asolid\_ile1\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_trs\_ile1\_api}}$ | `GU__J_trs_ile1_api` | transit api undissolved upper ileum | $\mathrm{GU}_{\mathrm{\_Asolid\_ile1\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Asolid\_ile2\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_dis\_ile2\_api}}$ | `GU__J_dis_ile2_api` | dissolution api lower ileum | $\mathrm{GU}_{\mathrm{\_Asolid\_ile2\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_trs\_ile2\_api}}$ | `GU__J_trs_ile2_api` | transit api undissolved lower ileum | $\mathrm{GU}_{\mathrm{\_Asolid\_ile2\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Asolid\_cae\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_dis\_cae\_api}}$ | `GU__J_dis_cae_api` | dissolution api caecum | $\mathrm{GU}_{\mathrm{\_Asolid\_cae\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_cae\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_trs\_cae\_api}}$ | `GU__J_trs_cae_api` | transit api undissolved caecum | $\mathrm{GU}_{\mathrm{\_Asolid\_cae\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Asolid\_asc\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_dis\_asc\_api}}$ | `GU__J_dis_asc_api` | dissolution api colon ascendens | $\mathrm{GU}_{\mathrm{\_Asolid\_asc\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_asc\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_trs\_asc\_api}}$ | `GU__J_trs_asc_api` | transit api undissolved colon ascendens | $\mathrm{GU}_{\mathrm{\_Asolid\_asc\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Asolid\_tra\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_dis\_tra\_api}}$ | `GU__J_dis_tra_api` | dissolution api colon transversum | $\mathrm{GU}_{\mathrm{\_Asolid\_tra\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_tra\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_trs\_tra\_api}}$ | `GU__J_trs_tra_api` | transit api undissolved colon transversum | $\mathrm{GU}_{\mathrm{\_Asolid\_tra\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Asolid\_des\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_dis\_des\_api}}$ | `GU__J_dis_des_api` | dissolution api colon descendens | $\mathrm{GU}_{\mathrm{\_Asolid\_des\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_des\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_trs\_des\_api}}$ | `GU__J_trs_des_api` | transit api undissolved colon descendens | $\mathrm{GU}_{\mathrm{\_Asolid\_des\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Asolid\_sig\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_dis\_sig\_api}}$ | `GU__J_dis_sig_api` | dissolution api colon sigmoid | $\mathrm{GU}_{\mathrm{\_Asolid\_sig\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_sig\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_trs\_sig\_api}}$ | `GU__J_trs_sig_api` | transit api undissolved colon sigmoid | $\mathrm{GU}_{\mathrm{\_Asolid\_sig\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Asolid\_rec\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_dis\_rec\_api}}$ | `GU__J_dis_rec_api` | dissolution api rectum | $\mathrm{GU}_{\mathrm{\_Asolid\_rec\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_rec\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_trs\_rec\_api}}$ | `GU__J_trs_rec_api` | transit api undissolved rectum | $\mathrm{GU}_{\mathrm{\_Asolid\_rec\_api}} \longrightarrow \mathrm{Afeces}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GU\_\_J\_sol\_api}}$ | `GU__J_sol_api` | oral application api (solution) | $\varnothing \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_st\_api}}$ |  |
| $v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api\_m1}}$ | `GU__J_in_ar_pl_api_m1` | inflow api\_m1 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_out\_pl\_api\_m1}}$ | `GU__J_out_pl_api_m1` | outflow api\_m1 into portal pool | $\mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}} \longrightarrow \mathrm{Cpo}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_st\_api\_m1}}$ | `GU__J_tr_st_api_m1` | transit api\_m1 stomach | $\mathrm{GU}_{\mathrm{\_Clumen\_st\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_du\_api\_m1}}$ | `GU__J_tr_du_api_m1` | transit api\_m1 duodenum | $\mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_du\_api\_m1}}$ | `GU__J_abs_du_api_m1` | absorption api\_m1 duodenum | $\mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_jej1\_api\_m1}}$ | `GU__J_tr_jej1_api_m1` | transit api\_m1 upper jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_jej1\_api\_m1}}$ | `GU__J_abs_jej1_api_m1` | absorption api\_m1 upper jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_jej2\_api\_m1}}$ | `GU__J_tr_jej2_api_m1` | transit api\_m1 lower jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_jej2\_api\_m1}}$ | `GU__J_abs_jej2_api_m1` | absorption api\_m1 lower jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_ile1\_api\_m1}}$ | `GU__J_tr_ile1_api_m1` | transit api\_m1 upper ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_ile1\_api\_m1}}$ | `GU__J_abs_ile1_api_m1` | absorption api\_m1 upper ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_ile2\_api\_m1}}$ | `GU__J_tr_ile2_api_m1` | transit api\_m1 lower ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_ile2\_api\_m1}}$ | `GU__J_abs_ile2_api_m1` | absorption api\_m1 lower ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_cae\_api\_m1}}$ | `GU__J_tr_cae_api_m1` | transit api\_m1 caecum | $\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_cae\_api\_m1}}$ | `GU__J_abs_cae_api_m1` | absorption api\_m1 caecum | $\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_asc\_api\_m1}}$ | `GU__J_tr_asc_api_m1` | transit api\_m1 colon ascendens | $\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_asc\_api\_m1}}$ | `GU__J_abs_asc_api_m1` | absorption api\_m1 colon ascendens | $\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_tra\_api\_m1}}$ | `GU__J_tr_tra_api_m1` | transit api\_m1 colon transversum | $\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_tra\_api\_m1}}$ | `GU__J_abs_tra_api_m1` | absorption api\_m1 colon transversum | $\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_des\_api\_m1}}$ | `GU__J_tr_des_api_m1` | transit api\_m1 colon descendens | $\mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_des\_api\_m1}}$ | `GU__J_abs_des_api_m1` | absorption api\_m1 colon descendens | $\mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_sig\_api\_m1}}$ | `GU__J_tr_sig_api_m1` | transit api\_m1 colon sigmoid | $\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_sig\_api\_m1}}$ | `GU__J_abs_sig_api_m1` | absorption api\_m1 colon sigmoid | $\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_rec\_api\_m1}}$ | `GU__J_tr_rec_api_m1` | transit api\_m1 rectum | $\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m1}} \longrightarrow \mathrm{Afeces}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_rec\_api\_m1}}$ | `GU__J_abs_rec_api_m1` | absorption api\_m1 rectum | $\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_bile\_api\_m1}}$ | `GU__J_bile_api_m1` | transit api\_m1 bile to intestinal lumen | $\mathrm{Cbile}_{\mathrm{api\_m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m1}}$ |  |
| $v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api\_m2}}$ | `GU__J_in_ar_pl_api_m2` | inflow api\_m2 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_out\_pl\_api\_m2}}$ | `GU__J_out_pl_api_m2` | outflow api\_m2 into portal pool | $\mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}} \longrightarrow \mathrm{Cpo}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_st\_api\_m2}}$ | `GU__J_tr_st_api_m2` | transit api\_m2 stomach | $\mathrm{GU}_{\mathrm{\_Clumen\_st\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_du\_api\_m2}}$ | `GU__J_tr_du_api_m2` | transit api\_m2 duodenum | $\mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_du\_api\_m2}}$ | `GU__J_abs_du_api_m2` | absorption api\_m2 duodenum | $\mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_jej1\_api\_m2}}$ | `GU__J_tr_jej1_api_m2` | transit api\_m2 upper jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_jej1\_api\_m2}}$ | `GU__J_abs_jej1_api_m2` | absorption api\_m2 upper jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_jej2\_api\_m2}}$ | `GU__J_tr_jej2_api_m2` | transit api\_m2 lower jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_jej2\_api\_m2}}$ | `GU__J_abs_jej2_api_m2` | absorption api\_m2 lower jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_ile1\_api\_m2}}$ | `GU__J_tr_ile1_api_m2` | transit api\_m2 upper ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_ile1\_api\_m2}}$ | `GU__J_abs_ile1_api_m2` | absorption api\_m2 upper ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_ile2\_api\_m2}}$ | `GU__J_tr_ile2_api_m2` | transit api\_m2 lower ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_ile2\_api\_m2}}$ | `GU__J_abs_ile2_api_m2` | absorption api\_m2 lower ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_cae\_api\_m2}}$ | `GU__J_tr_cae_api_m2` | transit api\_m2 caecum | $\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_cae\_api\_m2}}$ | `GU__J_abs_cae_api_m2` | absorption api\_m2 caecum | $\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_asc\_api\_m2}}$ | `GU__J_tr_asc_api_m2` | transit api\_m2 colon ascendens | $\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_asc\_api\_m2}}$ | `GU__J_abs_asc_api_m2` | absorption api\_m2 colon ascendens | $\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_tra\_api\_m2}}$ | `GU__J_tr_tra_api_m2` | transit api\_m2 colon transversum | $\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_tra\_api\_m2}}$ | `GU__J_abs_tra_api_m2` | absorption api\_m2 colon transversum | $\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_des\_api\_m2}}$ | `GU__J_tr_des_api_m2` | transit api\_m2 colon descendens | $\mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_des\_api\_m2}}$ | `GU__J_abs_des_api_m2` | absorption api\_m2 colon descendens | $\mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_sig\_api\_m2}}$ | `GU__J_tr_sig_api_m2` | transit api\_m2 colon sigmoid | $\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_sig\_api\_m2}}$ | `GU__J_abs_sig_api_m2` | absorption api\_m2 colon sigmoid | $\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_rec\_api\_m2}}$ | `GU__J_tr_rec_api_m2` | transit api\_m2 rectum | $\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m2}} \longrightarrow \mathrm{Afeces}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_rec\_api\_m2}}$ | `GU__J_abs_rec_api_m2` | absorption api\_m2 rectum | $\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_bile\_api\_m2}}$ | `GU__J_bile_api_m2` | transit api\_m2 bile to intestinal lumen | $\mathrm{Cbile}_{\mathrm{api\_m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m2}}$ |  |
| $v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api\_m7}}$ | `GU__J_in_ar_pl_api_m7` | inflow api\_m7 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_out\_pl\_api\_m7}}$ | `GU__J_out_pl_api_m7` | outflow api\_m7 into portal pool | $\mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}} \longrightarrow \mathrm{Cpo}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_st\_api\_m7}}$ | `GU__J_tr_st_api_m7` | transit api\_m7 stomach | $\mathrm{GU}_{\mathrm{\_Clumen\_st\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_du\_api\_m7}}$ | `GU__J_tr_du_api_m7` | transit api\_m7 duodenum | $\mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_du\_api\_m7}}$ | `GU__J_abs_du_api_m7` | absorption api\_m7 duodenum | $\mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_jej1\_api\_m7}}$ | `GU__J_tr_jej1_api_m7` | transit api\_m7 upper jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_jej1\_api\_m7}}$ | `GU__J_abs_jej1_api_m7` | absorption api\_m7 upper jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_jej2\_api\_m7}}$ | `GU__J_tr_jej2_api_m7` | transit api\_m7 lower jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_jej2\_api\_m7}}$ | `GU__J_abs_jej2_api_m7` | absorption api\_m7 lower jejunum | $\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_ile1\_api\_m7}}$ | `GU__J_tr_ile1_api_m7` | transit api\_m7 upper ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_ile1\_api\_m7}}$ | `GU__J_abs_ile1_api_m7` | absorption api\_m7 upper ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_ile2\_api\_m7}}$ | `GU__J_tr_ile2_api_m7` | transit api\_m7 lower ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_ile2\_api\_m7}}$ | `GU__J_abs_ile2_api_m7` | absorption api\_m7 lower ileum | $\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_cae\_api\_m7}}$ | `GU__J_tr_cae_api_m7` | transit api\_m7 caecum | $\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_cae\_api\_m7}}$ | `GU__J_abs_cae_api_m7` | absorption api\_m7 caecum | $\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_asc\_api\_m7}}$ | `GU__J_tr_asc_api_m7` | transit api\_m7 colon ascendens | $\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_asc\_api\_m7}}$ | `GU__J_abs_asc_api_m7` | absorption api\_m7 colon ascendens | $\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_tra\_api\_m7}}$ | `GU__J_tr_tra_api_m7` | transit api\_m7 colon transversum | $\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_tra\_api\_m7}}$ | `GU__J_abs_tra_api_m7` | absorption api\_m7 colon transversum | $\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_des\_api\_m7}}$ | `GU__J_tr_des_api_m7` | transit api\_m7 colon descendens | $\mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_des\_api\_m7}}$ | `GU__J_abs_des_api_m7` | absorption api\_m7 colon descendens | $\mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_sig\_api\_m7}}$ | `GU__J_tr_sig_api_m7` | transit api\_m7 colon sigmoid | $\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_sig\_api\_m7}}$ | `GU__J_abs_sig_api_m7` | absorption api\_m7 colon sigmoid | $\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_tr\_rec\_api\_m7}}$ | `GU__J_tr_rec_api_m7` | transit api\_m7 rectum | $\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m7}} \longrightarrow \mathrm{Afeces}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_abs\_rec\_api\_m7}}$ | `GU__J_abs_rec_api_m7` | absorption api\_m7 rectum | $\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_J\_bile\_api\_m7}}$ | `GU__J_bile_api_m7` | transit api\_m7 bile to intestinal lumen | $\mathrm{Cbile}_{\mathrm{api\_m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m7}}$ |  |
| $v_{\mathrm{GU\_\_APISEC\_du}}$ | `GU__APISEC_du` | efflux api apical mucosa duodenum (ABCB1) | $\mathrm{GU}_{\mathrm{\_Cmu\_du\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_du\_api}}$ |  |
| $v_{\mathrm{GU\_\_APISEC\_jej1}}$ | `GU__APISEC_jej1` | efflux api apical mucosa upper jejunum (ABCB1) | $\mathrm{GU}_{\mathrm{\_Cmu\_jej1\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api}}$ |  |
| $v_{\mathrm{GU\_\_APISEC\_jej2}}$ | `GU__APISEC_jej2` | efflux api apical mucosa lower jejunum (ABCB1) | $\mathrm{GU}_{\mathrm{\_Cmu\_jej2\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api}}$ |  |
| $v_{\mathrm{GU\_\_APISEC\_ile1}}$ | `GU__APISEC_ile1` | efflux api apical mucosa upper ileum (ABCB1) | $\mathrm{GU}_{\mathrm{\_Cmu\_ile1\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api}}$ |  |
| $v_{\mathrm{GU\_\_APISEC\_ile2}}$ | `GU__APISEC_ile2` | efflux api apical mucosa lower ileum (ABCB1) | $\mathrm{GU}_{\mathrm{\_Cmu\_ile2\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api}}$ |  |
| $v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api}}$ | `SP__J_in_ar_pl_api` | inflow api from arterial pool | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{SP}_{\mathrm{\_Cpl\_api}}$ |  |
| $v_{\mathrm{SP\_\_J\_out\_pl\_api}}$ | `SP__J_out_pl_api` | outflow api into portal pool | $\mathrm{SP}_{\mathrm{\_Cpl\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |  |
| $v_{\mathrm{SP\_\_J\_ti\_api}}$ | `SP__J_ti_api` | exchange api plasma and tissue | $\mathrm{SP}_{\mathrm{\_Cpl\_api}} \rightleftharpoons \mathrm{SP}_{\mathrm{\_Cti\_api}}$ |  |
| $v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api\_m1}}$ | `SP__J_in_ar_pl_api_m1` | inflow api\_m1 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m1}} \longrightarrow \mathrm{SP}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{SP\_\_J\_out\_pl\_api\_m1}}$ | `SP__J_out_pl_api_m1` | outflow api\_m1 into portal pool | $\mathrm{SP}_{\mathrm{\_Cpl\_api\_m1}} \longrightarrow \mathrm{Cpo}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api\_m2}}$ | `SP__J_in_ar_pl_api_m2` | inflow api\_m2 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m2}} \longrightarrow \mathrm{SP}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{SP\_\_J\_out\_pl\_api\_m2}}$ | `SP__J_out_pl_api_m2` | outflow api\_m2 into portal pool | $\mathrm{SP}_{\mathrm{\_Cpl\_api\_m2}} \longrightarrow \mathrm{Cpo}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api\_m7}}$ | `SP__J_in_ar_pl_api_m7` | inflow api\_m7 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m7}} \longrightarrow \mathrm{SP}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{SP\_\_J\_out\_pl\_api\_m7}}$ | `SP__J_out_pl_api_m7` | outflow api\_m7 into portal pool | $\mathrm{SP}_{\mathrm{\_Cpl\_api\_m7}} \longrightarrow \mathrm{Cpo}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api}}$ | `PA__J_in_ar_pl_api` | inflow api from arterial pool | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{PA}_{\mathrm{\_Cpl\_api}}$ |  |
| $v_{\mathrm{PA\_\_J\_out\_pl\_api}}$ | `PA__J_out_pl_api` | outflow api into portal pool | $\mathrm{PA}_{\mathrm{\_Cpl\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |  |
| $v_{\mathrm{PA\_\_J\_ti\_api}}$ | `PA__J_ti_api` | exchange api plasma and tissue | $\mathrm{PA}_{\mathrm{\_Cpl\_api}} \rightleftharpoons \mathrm{PA}_{\mathrm{\_Cti\_api}}$ |  |
| $v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api\_m1}}$ | `PA__J_in_ar_pl_api_m1` | inflow api\_m1 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m1}} \longrightarrow \mathrm{PA}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{PA\_\_J\_out\_pl\_api\_m1}}$ | `PA__J_out_pl_api_m1` | outflow api\_m1 into portal pool | $\mathrm{PA}_{\mathrm{\_Cpl\_api\_m1}} \longrightarrow \mathrm{Cpo}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api\_m2}}$ | `PA__J_in_ar_pl_api_m2` | inflow api\_m2 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m2}} \longrightarrow \mathrm{PA}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{PA\_\_J\_out\_pl\_api\_m2}}$ | `PA__J_out_pl_api_m2` | outflow api\_m2 into portal pool | $\mathrm{PA}_{\mathrm{\_Cpl\_api\_m2}} \longrightarrow \mathrm{Cpo}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api\_m7}}$ | `PA__J_in_ar_pl_api_m7` | inflow api\_m7 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m7}} \longrightarrow \mathrm{PA}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{PA\_\_J\_out\_pl\_api\_m7}}$ | `PA__J_out_pl_api_m7` | outflow api\_m7 into portal pool | $\mathrm{PA}_{\mathrm{\_Cpl\_api\_m7}} \longrightarrow \mathrm{Cpo}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api}}$ | `MU__J_in_ar_pl_api` | inflow api from arterial pool | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{MU}_{\mathrm{\_Cpl\_api}}$ |  |
| $v_{\mathrm{MU\_\_J\_out\_pl\_api}}$ | `MU__J_out_pl_api` | outflow api into venous pool | $\mathrm{MU}_{\mathrm{\_Cpl\_api}} \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |  |
| $v_{\mathrm{MU\_\_J\_ti\_api}}$ | `MU__J_ti_api` | exchange api plasma and tissue | $\mathrm{MU}_{\mathrm{\_Cpl\_api}} \rightleftharpoons \mathrm{MU}_{\mathrm{\_Cti\_api}}$ |  |
| $v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api\_m1}}$ | `MU__J_in_ar_pl_api_m1` | inflow api\_m1 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m1}} \longrightarrow \mathrm{MU}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{MU\_\_J\_out\_pl\_api\_m1}}$ | `MU__J_out_pl_api_m1` | outflow api\_m1 into venous pool | $\mathrm{MU}_{\mathrm{\_Cpl\_api\_m1}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api\_m2}}$ | `MU__J_in_ar_pl_api_m2` | inflow api\_m2 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m2}} \longrightarrow \mathrm{MU}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{MU\_\_J\_out\_pl\_api\_m2}}$ | `MU__J_out_pl_api_m2` | outflow api\_m2 into venous pool | $\mathrm{MU}_{\mathrm{\_Cpl\_api\_m2}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api\_m7}}$ | `MU__J_in_ar_pl_api_m7` | inflow api\_m7 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m7}} \longrightarrow \mathrm{MU}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{MU\_\_J\_out\_pl\_api\_m7}}$ | `MU__J_out_pl_api_m7` | outflow api\_m7 into venous pool | $\mathrm{MU}_{\mathrm{\_Cpl\_api\_m7}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api}}$ | `SK__J_in_ar_pl_api` | inflow api from arterial pool | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{SK}_{\mathrm{\_Cpl\_api}}$ |  |
| $v_{\mathrm{SK\_\_J\_out\_pl\_api}}$ | `SK__J_out_pl_api` | outflow api into venous pool | $\mathrm{SK}_{\mathrm{\_Cpl\_api}} \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |  |
| $v_{\mathrm{SK\_\_J\_ti\_api}}$ | `SK__J_ti_api` | exchange api plasma and tissue | $\mathrm{SK}_{\mathrm{\_Cpl\_api}} \rightleftharpoons \mathrm{SK}_{\mathrm{\_Cti\_api}}$ |  |
| $v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api\_m1}}$ | `SK__J_in_ar_pl_api_m1` | inflow api\_m1 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m1}} \longrightarrow \mathrm{SK}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{SK\_\_J\_out\_pl\_api\_m1}}$ | `SK__J_out_pl_api_m1` | outflow api\_m1 into venous pool | $\mathrm{SK}_{\mathrm{\_Cpl\_api\_m1}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api\_m2}}$ | `SK__J_in_ar_pl_api_m2` | inflow api\_m2 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m2}} \longrightarrow \mathrm{SK}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{SK\_\_J\_out\_pl\_api\_m2}}$ | `SK__J_out_pl_api_m2` | outflow api\_m2 into venous pool | $\mathrm{SK}_{\mathrm{\_Cpl\_api\_m2}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api\_m7}}$ | `SK__J_in_ar_pl_api_m7` | inflow api\_m7 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m7}} \longrightarrow \mathrm{SK}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{SK\_\_J\_out\_pl\_api\_m7}}$ | `SK__J_out_pl_api_m7` | outflow api\_m7 into venous pool | $\mathrm{SK}_{\mathrm{\_Cpl\_api\_m7}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api}}$ | `AD__J_in_ar_pl_api` | inflow api from arterial pool | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{AD}_{\mathrm{\_Cpl\_api}}$ |  |
| $v_{\mathrm{AD\_\_J\_out\_pl\_api}}$ | `AD__J_out_pl_api` | outflow api into venous pool | $\mathrm{AD}_{\mathrm{\_Cpl\_api}} \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |  |
| $v_{\mathrm{AD\_\_J\_ti\_api}}$ | `AD__J_ti_api` | exchange api plasma and tissue | $\mathrm{AD}_{\mathrm{\_Cpl\_api}} \rightleftharpoons \mathrm{AD}_{\mathrm{\_Cti\_api}}$ |  |
| $v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api\_m1}}$ | `AD__J_in_ar_pl_api_m1` | inflow api\_m1 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m1}} \longrightarrow \mathrm{AD}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{AD\_\_J\_out\_pl\_api\_m1}}$ | `AD__J_out_pl_api_m1` | outflow api\_m1 into venous pool | $\mathrm{AD}_{\mathrm{\_Cpl\_api\_m1}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api\_m2}}$ | `AD__J_in_ar_pl_api_m2` | inflow api\_m2 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m2}} \longrightarrow \mathrm{AD}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{AD\_\_J\_out\_pl\_api\_m2}}$ | `AD__J_out_pl_api_m2` | outflow api\_m2 into venous pool | $\mathrm{AD}_{\mathrm{\_Cpl\_api\_m2}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api\_m7}}$ | `AD__J_in_ar_pl_api_m7` | inflow api\_m7 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m7}} \longrightarrow \mathrm{AD}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{AD\_\_J\_out\_pl\_api\_m7}}$ | `AD__J_out_pl_api_m7` | outflow api\_m7 into venous pool | $\mathrm{AD}_{\mathrm{\_Cpl\_api\_m7}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api}}$ | `BO__J_in_ar_pl_api` | inflow api from arterial pool | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{BO}_{\mathrm{\_Cpl\_api}}$ |  |
| $v_{\mathrm{BO\_\_J\_out\_pl\_api}}$ | `BO__J_out_pl_api` | outflow api into venous pool | $\mathrm{BO}_{\mathrm{\_Cpl\_api}} \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |  |
| $v_{\mathrm{BO\_\_J\_ti\_api}}$ | `BO__J_ti_api` | exchange api plasma and tissue | $\mathrm{BO}_{\mathrm{\_Cpl\_api}} \rightleftharpoons \mathrm{BO}_{\mathrm{\_Cti\_api}}$ |  |
| $v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api\_m1}}$ | `BO__J_in_ar_pl_api_m1` | inflow api\_m1 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m1}} \longrightarrow \mathrm{BO}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{BO\_\_J\_out\_pl\_api\_m1}}$ | `BO__J_out_pl_api_m1` | outflow api\_m1 into venous pool | $\mathrm{BO}_{\mathrm{\_Cpl\_api\_m1}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api\_m2}}$ | `BO__J_in_ar_pl_api_m2` | inflow api\_m2 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m2}} \longrightarrow \mathrm{BO}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{BO\_\_J\_out\_pl\_api\_m2}}$ | `BO__J_out_pl_api_m2` | outflow api\_m2 into venous pool | $\mathrm{BO}_{\mathrm{\_Cpl\_api\_m2}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api\_m7}}$ | `BO__J_in_ar_pl_api_m7` | inflow api\_m7 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m7}} \longrightarrow \mathrm{BO}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{BO\_\_J\_out\_pl\_api\_m7}}$ | `BO__J_out_pl_api_m7` | outflow api\_m7 into venous pool | $\mathrm{BO}_{\mathrm{\_Cpl\_api\_m7}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m7}}$ |  |
| $v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api}}$ | `GO__J_in_ar_pl_api` | inflow api from arterial pool | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{GO}_{\mathrm{\_Cpl\_api}}$ |  |
| $v_{\mathrm{GO\_\_J\_out\_pl\_api}}$ | `GO__J_out_pl_api` | outflow api into venous pool | $\mathrm{GO}_{\mathrm{\_Cpl\_api}} \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |  |
| $v_{\mathrm{GO\_\_J\_ti\_api}}$ | `GO__J_ti_api` | exchange api plasma and tissue | $\mathrm{GO}_{\mathrm{\_Cpl\_api}} \rightleftharpoons \mathrm{GO}_{\mathrm{\_Cti\_api}}$ |  |
| $v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api\_m1}}$ | `GO__J_in_ar_pl_api_m1` | inflow api\_m1 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m1}} \longrightarrow \mathrm{GO}_{\mathrm{\_Cpl\_api\_m1}}$ |  |
| $v_{\mathrm{GO\_\_J\_out\_pl\_api\_m1}}$ | `GO__J_out_pl_api_m1` | outflow api\_m1 into venous pool | $\mathrm{GO}_{\mathrm{\_Cpl\_api\_m1}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m1}}$ |  |
| $v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api\_m2}}$ | `GO__J_in_ar_pl_api_m2` | inflow api\_m2 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m2}} \longrightarrow \mathrm{GO}_{\mathrm{\_Cpl\_api\_m2}}$ |  |
| $v_{\mathrm{GO\_\_J\_out\_pl\_api\_m2}}$ | `GO__J_out_pl_api_m2` | outflow api\_m2 into venous pool | $\mathrm{GO}_{\mathrm{\_Cpl\_api\_m2}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m2}}$ |  |
| $v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api\_m7}}$ | `GO__J_in_ar_pl_api_m7` | inflow api\_m7 from arterial pool | $\mathrm{Car}_{\mathrm{api\_m7}} \longrightarrow \mathrm{GO}_{\mathrm{\_Cpl\_api\_m7}}$ |  |
| $v_{\mathrm{GO\_\_J\_out\_pl\_api\_m7}}$ | `GO__J_out_pl_api_m7` | outflow api\_m7 into venous pool | $\mathrm{GO}_{\mathrm{\_Cpl\_api\_m7}} \longrightarrow \mathrm{Cve}_{\mathrm{api\_m7}}$ |  |

The rates of the reactions are:

$$
\begin{aligned}
v_{\mathrm{J\_iv\_api}} &= \frac{\mathrm{Kiv}_{\mathrm{api}} \cdot \mathrm{IVDOSE}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}} \\[1ex]
v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api}} &= \mathrm{Qlu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cve}_{\mathrm{api}} \\[1ex]
v_{\mathrm{LU\_\_J\_out\_pl\_api}} &= \mathrm{Qlu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{lu\_api}} \\[1ex]
v_{\mathrm{LU\_\_J\_ti\_api}} &= \mathrm{LU}_{\mathrm{\_PS\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathopen{}\left(\mathrm{LU}_{\mathrm{\_Cpl\_api}} - \frac{\mathrm{LU}_{\mathrm{\_Cti\_api}}}{\mathrm{Kp}_{\mathrm{api}}}\right) \\[1ex]
v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api\_m1}} &= \mathrm{Qlu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cve}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{LU\_\_J\_out\_pl\_api\_m1}} &= \mathrm{Qlu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{lu\_api\_m1}} \\[1ex]
v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api\_m2}} &= \mathrm{Qlu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cve}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{LU\_\_J\_out\_pl\_api\_m2}} &= \mathrm{Qlu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{lu\_api\_m2}} \\[1ex]
v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api\_m7}} &= \mathrm{Qlu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cve}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{LU\_\_J\_out\_pl\_api\_m7}} &= \mathrm{Qlu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{lu\_api\_m7}} \\[1ex]
v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api}} &= \mathrm{Qhe} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{HE\_\_J\_out\_pl\_api}} &= \mathrm{Qhe} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{he\_api}} \\[1ex]
v_{\mathrm{HE\_\_J\_ti\_api}} &= \mathrm{HE}_{\mathrm{\_PS\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathopen{}\left(\mathrm{HE}_{\mathrm{\_Cpl\_api}} - \frac{\mathrm{HE}_{\mathrm{\_Cti\_api}}}{\mathrm{Kp}_{\mathrm{api}}}\right) \\[1ex]
v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api\_m1}} &= \mathrm{Qhe} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{HE\_\_J\_out\_pl\_api\_m1}} &= \mathrm{Qhe} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{he\_api\_m1}} \\[1ex]
v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api\_m2}} &= \mathrm{Qhe} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{HE\_\_J\_out\_pl\_api\_m2}} &= \mathrm{Qhe} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{he\_api\_m2}} \\[1ex]
v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api\_m7}} &= \mathrm{Qhe} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{HE\_\_J\_out\_pl\_api\_m7}} &= \mathrm{Qhe} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{he\_api\_m7}} \\[1ex]
v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api}} &= \mathrm{Qbr} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{BR\_\_J\_out\_pl\_api}} &= \mathrm{Qbr} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{br\_api}} \\[1ex]
v_{\mathrm{BR\_\_J\_ti\_api}} &= \mathrm{BR}_{\mathrm{\_PS\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathopen{}\left(\mathrm{BR}_{\mathrm{\_Cpl\_api}} - \frac{\mathrm{BR}_{\mathrm{\_Cti\_api}}}{\mathrm{Kp}_{\mathrm{api}}}\right) \\[1ex]
v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api\_m1}} &= \mathrm{Qbr} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{BR\_\_J\_out\_pl\_api\_m1}} &= \mathrm{Qbr} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{br\_api\_m1}} \\[1ex]
v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api\_m2}} &= \mathrm{Qbr} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{BR\_\_J\_out\_pl\_api\_m2}} &= \mathrm{Qbr} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{br\_api\_m2}} \\[1ex]
v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api\_m7}} &= \mathrm{Qbr} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{BR\_\_J\_out\_pl\_api\_m7}} &= \mathrm{Qbr} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{br\_api\_m7}} \\[1ex]
v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api}} &= \mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qha} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api}} &= f_{\mathrm{shunt}} \cdot \mathrm{Qha} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{LI\_\_J\_in\_po\_pl\_api}} &= \mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qpo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cpo}_{\mathrm{api}} \\[1ex]
v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api}} &= f_{\mathrm{shunt}} \cdot \mathrm{Qpo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cpo}_{\mathrm{api}} \\[1ex]
v_{\mathrm{LI\_\_J\_out\_pl\_api}} &= \mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qh} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{li\_api}} \\[1ex]
v_{\mathrm{LI\_\_J\_ti\_api}} &= \mathrm{LI}_{\mathrm{\_PS\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathopen{}\left(\mathrm{LI}_{\mathrm{\_Cpl\_api}} - \frac{\mathrm{LI}_{\mathrm{\_Cti\_api}}}{\mathrm{Kp}_{\mathrm{api}}}\right) \\[1ex]
v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api\_m1}} &= \mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qha} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api\_m1}} &= f_{\mathrm{shunt}} \cdot \mathrm{Qha} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{LI\_\_J\_in\_po\_pl\_api\_m1}} &= \mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qpo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cpo}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api\_m1}} &= f_{\mathrm{shunt}} \cdot \mathrm{Qpo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cpo}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{LI\_\_J\_out\_pl\_api\_m1}} &= \mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qh} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{li\_api\_m1}} \\[1ex]
v_{\mathrm{LI\_\_J\_is\_api\_m1}} &= \mathrm{LI}_{\mathrm{\_PS\_vas}} \cdot \mathrm{fu}_{\mathrm{api\_m1}} \cdot \mathopen{}\left(\mathrm{LI}_{\mathrm{\_Cpl\_api\_m1}} - \frac{\mathrm{LI}_{\mathrm{\_Cis\_api\_m1}}}{\mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m1}}}\right) \\[1ex]
v_{\mathrm{LI\_\_J\_ic\_api\_m1}} &= \mathrm{LI}_{\mathrm{\_PS\_api\_m1}} \cdot \mathopen{}\left(\frac{\mathrm{fu}_{\mathrm{api\_m1}}}{\mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m1}}} \cdot \mathrm{LI}_{\mathrm{\_Cis\_api\_m1}} - \frac{\mathrm{fu}_{\mathrm{api\_m1}}}{\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m1}}} \cdot \mathrm{LI}_{\mathrm{\_Cic\_api\_m1}}\right) \\[1ex]
v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api\_m2}} &= \mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qha} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api\_m2}} &= f_{\mathrm{shunt}} \cdot \mathrm{Qha} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{LI\_\_J\_in\_po\_pl\_api\_m2}} &= \mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qpo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cpo}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api\_m2}} &= f_{\mathrm{shunt}} \cdot \mathrm{Qpo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cpo}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{LI\_\_J\_out\_pl\_api\_m2}} &= \mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qh} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{li\_api\_m2}} \\[1ex]
v_{\mathrm{LI\_\_J\_is\_api\_m2}} &= \mathrm{LI}_{\mathrm{\_PS\_vas}} \cdot \mathrm{fu}_{\mathrm{api\_m2}} \cdot \mathopen{}\left(\mathrm{LI}_{\mathrm{\_Cpl\_api\_m2}} - \frac{\mathrm{LI}_{\mathrm{\_Cis\_api\_m2}}}{\mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m2}}}\right) \\[1ex]
v_{\mathrm{LI\_\_J\_ic\_api\_m2}} &= \mathrm{LI}_{\mathrm{\_PS\_api\_m2}} \cdot \mathopen{}\left(\frac{\mathrm{fu}_{\mathrm{api\_m2}}}{\mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m2}}} \cdot \mathrm{LI}_{\mathrm{\_Cis\_api\_m2}} - \frac{\mathrm{fu}_{\mathrm{api\_m2}}}{\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m2}}} \cdot \mathrm{LI}_{\mathrm{\_Cic\_api\_m2}}\right) \\[1ex]
v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api\_m7}} &= \mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qha} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api\_m7}} &= f_{\mathrm{shunt}} \cdot \mathrm{Qha} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{LI\_\_J\_in\_po\_pl\_api\_m7}} &= \mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qpo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cpo}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api\_m7}} &= f_{\mathrm{shunt}} \cdot \mathrm{Qpo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cpo}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{LI\_\_J\_out\_pl\_api\_m7}} &= \mathopen{}\left(1 - f_{\mathrm{shunt}}\right) \cdot \mathrm{Qh} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{li\_api\_m7}} \\[1ex]
v_{\mathrm{LI\_\_J\_is\_api\_m7}} &= \mathrm{LI}_{\mathrm{\_PS\_vas}} \cdot \mathrm{fu}_{\mathrm{api\_m7}} \cdot \mathopen{}\left(\mathrm{LI}_{\mathrm{\_Cpl\_api\_m7}} - \frac{\mathrm{LI}_{\mathrm{\_Cis\_api\_m7}}}{\mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m7}}}\right) \\[1ex]
v_{\mathrm{LI\_\_J\_ic\_api\_m7}} &= \mathrm{LI}_{\mathrm{\_PS\_api\_m7}} \cdot \mathopen{}\left(\frac{\mathrm{fu}_{\mathrm{api\_m7}}}{\mathrm{LI}_{\mathrm{\_K\_int\_pls\_api\_m7}}} \cdot \mathrm{LI}_{\mathrm{\_Cis\_api\_m7}} - \frac{\mathrm{fu}_{\mathrm{api\_m7}}}{\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m7}}} \cdot \mathrm{LI}_{\mathrm{\_Cic\_api\_m7}}\right) \\[1ex]
v_{\mathrm{LI\_\_API2M}} &= \frac{\mathrm{LI}_{\mathrm{\_f\_cyp3a4}} \cdot \mathrm{fimp}_{\mathrm{li\_cyp3a4}} \cdot f_{\mathrm{functional}} \cdot \mathrm{LI}_{\mathrm{\_API2M\_k}} \cdot \mathrm{Vli} \cdot \mathrm{fu}_{\mathrm{api}}}{\mathrm{Kp}_{\mathrm{api}}} \cdot \mathrm{LI}_{\mathrm{\_Cti\_api}} \\[1ex]
v_{\mathrm{LI\_\_M22M1}} &= \frac{\mathrm{LI}_{\mathrm{\_f\_sult1a1}} \cdot f_{\mathrm{functional}} \cdot \mathrm{LI}_{\mathrm{\_M22M1\_k}} \cdot \mathrm{Vli} \cdot \mathrm{fu}_{\mathrm{api\_m2}}}{\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m2}}} \cdot \mathrm{LI}_{\mathrm{\_Cic\_api\_m2}} \\[1ex]
v_{\mathrm{LI\_\_M1EXBI}} &= \frac{f_{\mathrm{functional}} \cdot \mathrm{LI}_{\mathrm{\_M1EXBI\_k}} \cdot \mathrm{Vli} \cdot \mathrm{fu}_{\mathrm{api\_m1}}}{\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m1}}} \cdot \mathrm{LI}_{\mathrm{\_Cic\_api\_m1}} \\[1ex]
v_{\mathrm{LI\_\_M2EXBI}} &= \frac{f_{\mathrm{functional}} \cdot \mathrm{LI}_{\mathrm{\_M2EXBI\_k}} \cdot \mathrm{Vli} \cdot \mathrm{fu}_{\mathrm{api\_m2}}}{\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m2}}} \cdot \mathrm{LI}_{\mathrm{\_Cic\_api\_m2}} \\[1ex]
v_{\mathrm{LI\_\_M7EXBI}} &= \frac{f_{\mathrm{functional}} \cdot \mathrm{LI}_{\mathrm{\_M7EXBI\_k}} \cdot \mathrm{Vli} \cdot \mathrm{fu}_{\mathrm{api\_m7}}}{\mathrm{LI}_{\mathrm{\_K\_cell\_pls\_api\_m7}}} \cdot \mathrm{LI}_{\mathrm{\_Cic\_api\_m7}} \\[1ex]
v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api}} &= \mathrm{Qki} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{KI\_\_J\_out\_pl\_api}} &= \mathrm{Qki} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{ki\_api}} - \mathrm{fu}_{\mathrm{api}} \cdot \mathrm{GFR} \cdot \mathrm{Cout}_{\mathrm{ki\_api}} \cdot \mathopen{}\left(1 - f_{\mathrm{reabsorbed\_api}}\right) \\[1ex]
v_{\mathrm{KI\_\_J\_gfr\_api}} &= \mathrm{fu}_{\mathrm{api}} \cdot \mathrm{GFR} \cdot \mathrm{Car}_{\mathrm{api}} \cdot \mathopen{}\left(1 - f_{\mathrm{reabsorbed\_api}}\right) \\[1ex]
v_{\mathrm{KI\_\_J\_ti\_api}} &= \mathrm{KI}_{\mathrm{\_PS\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathopen{}\left(\mathrm{KI}_{\mathrm{\_Cpl\_api}} - \frac{\mathrm{KI}_{\mathrm{\_Cti\_api}}}{\mathrm{Kp}_{\mathrm{api}}}\right) \\[1ex]
v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api\_m1}} &= \mathrm{Qki} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{KI\_\_J\_out\_pl\_api\_m1}} &= \mathrm{Qki} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{ki\_api\_m1}} - \mathrm{fu}_{\mathrm{api\_m1}} \cdot \mathrm{GFR} \cdot \mathrm{Cout}_{\mathrm{ki\_api\_m1}} \cdot \mathopen{}\left(1 - f_{\mathrm{reabsorbed\_api\_m1}}\right) \\[1ex]
v_{\mathrm{KI\_\_J\_gfr\_api\_m1}} &= \mathrm{fu}_{\mathrm{api\_m1}} \cdot \mathrm{GFR} \cdot \mathrm{Car}_{\mathrm{api\_m1}} \cdot \mathopen{}\left(1 - f_{\mathrm{reabsorbed\_api\_m1}}\right) \\[1ex]
v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api\_m2}} &= \mathrm{Qki} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{KI\_\_J\_out\_pl\_api\_m2}} &= \mathrm{Qki} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{ki\_api\_m2}} \\[1ex]
v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api\_m7}} &= \mathrm{Qki} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{KI\_\_J\_out\_pl\_api\_m7}} &= \mathrm{Qki} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{ki\_api\_m7}} - \mathrm{fu}_{\mathrm{api\_m7}} \cdot \mathrm{GFR} \cdot \mathrm{Cout}_{\mathrm{ki\_api\_m7}} \cdot \mathopen{}\left(1 - f_{\mathrm{reabsorbed\_api\_m7}}\right) \\[1ex]
v_{\mathrm{KI\_\_J\_gfr\_api\_m7}} &= \mathrm{fu}_{\mathrm{api\_m7}} \cdot \mathrm{GFR} \cdot \mathrm{Car}_{\mathrm{api\_m7}} \cdot \mathopen{}\left(1 - f_{\mathrm{reabsorbed\_api\_m7}}\right) \\[1ex]
v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api}} &= \mathrm{Qst} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{ST\_\_J\_out\_pl\_api}} &= \mathrm{Qst} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{st\_api}} \\[1ex]
v_{\mathrm{ST\_\_J\_ti\_api}} &= \mathrm{ST}_{\mathrm{\_PS\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathopen{}\left(\mathrm{ST}_{\mathrm{\_Cpl\_api}} - \frac{\mathrm{ST}_{\mathrm{\_Cti\_api}}}{\mathrm{Kp}_{\mathrm{api}}}\right) \\[1ex]
v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api\_m1}} &= \mathrm{Qst} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{ST\_\_J\_out\_pl\_api\_m1}} &= \mathrm{Qst} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{st\_api\_m1}} \\[1ex]
v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api\_m2}} &= \mathrm{Qst} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{ST\_\_J\_out\_pl\_api\_m2}} &= \mathrm{Qst} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{st\_api\_m2}} \\[1ex]
v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api\_m7}} &= \mathrm{Qst} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{ST\_\_J\_out\_pl\_api\_m7}} &= \mathrm{Qst} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{st\_api\_m7}} \\[1ex]
v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api}} &= \mathrm{GU}_{\mathrm{\_Qgu\_wall}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{GU\_\_J\_out\_pl\_api}} &= \mathrm{GU}_{\mathrm{\_Qgu\_wall}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{si\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_ti\_api}} &= \mathrm{GU}_{\mathrm{\_PS\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathopen{}\left(\mathrm{GU}_{\mathrm{\_Cpl\_api}} - \frac{\mathrm{GU}_{\mathrm{\_Cti\_api}}}{\mathrm{Kp}_{\mathrm{api}}}\right) \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_in\_du\_api}} &= \mathrm{GU}_{\mathrm{\_Qmu\_du}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_out\_du\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Qmu\_du}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{GU}_{\mathrm{\_Cmu\_du\_api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_in\_jej1\_api}} &= \mathrm{GU}_{\mathrm{\_Qmu\_jej1}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_out\_jej1\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Qmu\_jej1}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{GU}_{\mathrm{\_Cmu\_jej1\_api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_in\_jej2\_api}} &= \mathrm{GU}_{\mathrm{\_Qmu\_jej2}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_out\_jej2\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Qmu\_jej2}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{GU}_{\mathrm{\_Cmu\_jej2\_api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_in\_ile1\_api}} &= \mathrm{GU}_{\mathrm{\_Qmu\_ile1}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_out\_ile1\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Qmu\_ile1}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{GU}_{\mathrm{\_Cmu\_ile1\_api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_in\_ile2\_api}} &= \mathrm{GU}_{\mathrm{\_Qmu\_ile2}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_out\_ile2\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Qmu\_ile2}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{GU}_{\mathrm{\_Cmu\_ile2\_api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_in\_cae\_api}} &= \mathrm{GU}_{\mathrm{\_Qmu\_cae}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_out\_cae\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Qmu\_cae}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{GU}_{\mathrm{\_Cmu\_cae\_api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_in\_asc\_api}} &= \mathrm{GU}_{\mathrm{\_Qmu\_asc}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_out\_asc\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Qmu\_asc}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{GU}_{\mathrm{\_Cmu\_asc\_api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_in\_tra\_api}} &= \mathrm{GU}_{\mathrm{\_Qmu\_tra}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_out\_tra\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Qmu\_tra}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{GU}_{\mathrm{\_Cmu\_tra\_api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_in\_des\_api}} &= \mathrm{GU}_{\mathrm{\_Qmu\_des}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_out\_des\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Qmu\_des}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{GU}_{\mathrm{\_Cmu\_des\_api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_in\_sig\_api}} &= \mathrm{GU}_{\mathrm{\_Qmu\_sig}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_out\_sig\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Qmu\_sig}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{GU}_{\mathrm{\_Cmu\_sig\_api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_in\_rec\_api}} &= \mathrm{GU}_{\mathrm{\_Qmu\_rec}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{GU\_\_J\_mu\_out\_rec\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Qmu\_rec}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{GU}_{\mathrm{\_Cmu\_rec\_api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_st\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_st}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_st\_api}}}{\mathopen{}\left(\mathrm{GU}_{\mathrm{\_T\_st}} + \mathrm{FED} \cdot \mathopen{}\left(\mathrm{GU}_{\mathrm{\_T\_st\_fed}} \cdot \mathrm{fsex}_{\mathrm{t\_stomach\_fed}} - \mathrm{GU}_{\mathrm{\_T\_st}}\right)\right) \cdot \mathrm{fimp}_{\mathrm{t\_stomach}}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_du\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_du}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_du\_api}}}{\mathrm{GU}_{\mathrm{\_T\_du}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_du\_api}} &= \frac{\mathrm{fabs}_{\mathrm{api}} \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_du}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_du}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_du\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_feces\_du\_api}} &= \frac{\mathopen{}\left(1 - \mathrm{fabs}_{\mathrm{api}}\right) \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_du}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_du}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_du\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_jej1\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_jej1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api}}}{\mathrm{GU}_{\mathrm{\_T\_jej1}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_jej1\_api}} &= \frac{\mathrm{fabs}_{\mathrm{api}} \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_jej1}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_jej1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_feces\_jej1\_api}} &= \frac{\mathopen{}\left(1 - \mathrm{fabs}_{\mathrm{api}}\right) \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_jej1}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_jej1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_jej2\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_jej2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api}}}{\mathrm{GU}_{\mathrm{\_T\_jej2}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_jej2\_api}} &= \frac{\mathrm{fabs}_{\mathrm{api}} \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_jej2}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_jej2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_feces\_jej2\_api}} &= \frac{\mathopen{}\left(1 - \mathrm{fabs}_{\mathrm{api}}\right) \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_jej2}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_jej2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_ile1\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_ile1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api}}}{\mathrm{GU}_{\mathrm{\_T\_ile1}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_ile1\_api}} &= \frac{\mathrm{fabs}_{\mathrm{api}} \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_ile1}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_ile1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_feces\_ile1\_api}} &= \frac{\mathopen{}\left(1 - \mathrm{fabs}_{\mathrm{api}}\right) \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_ile1}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_ile1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_ile2\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_ile2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api}}}{\mathrm{GU}_{\mathrm{\_T\_ile2}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_ile2\_api}} &= \frac{\mathrm{fabs}_{\mathrm{api}} \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_ile2}} \cdot f_{\mathrm{ka\_ile2\_api}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_ile2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_feces\_ile2\_api}} &= \frac{\mathopen{}\left(1 - \mathrm{fabs}_{\mathrm{api}}\right) \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_ile2}} \cdot f_{\mathrm{ka\_ile2\_api}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_ile2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_cae\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_cae}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_cae\_api}}}{\mathrm{GU}_{\mathrm{\_T\_cae}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_cae\_api}} &= \frac{\mathrm{fabs}_{\mathrm{api}} \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_cae}} \cdot f_{\mathrm{ka\_colon\_api}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_cae}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_cae\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_feces\_cae\_api}} &= \frac{\mathopen{}\left(1 - \mathrm{fabs}_{\mathrm{api}}\right) \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_cae}} \cdot f_{\mathrm{ka\_colon\_api}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_cae}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_cae\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_asc\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_asc}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_asc\_api}}}{\mathrm{GU}_{\mathrm{\_T\_asc}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_asc\_api}} &= \frac{\mathrm{fabs}_{\mathrm{api}} \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_asc}} \cdot f_{\mathrm{ka\_colon\_api}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_asc}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_asc\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_feces\_asc\_api}} &= \frac{\mathopen{}\left(1 - \mathrm{fabs}_{\mathrm{api}}\right) \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_asc}} \cdot f_{\mathrm{ka\_colon\_api}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_asc}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_asc\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_tra\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_tra}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_tra\_api}}}{\mathrm{GU}_{\mathrm{\_T\_tra}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_tra\_api}} &= \frac{\mathrm{fabs}_{\mathrm{api}} \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_tra}} \cdot f_{\mathrm{ka\_colon\_api}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_tra}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_tra\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_feces\_tra\_api}} &= \frac{\mathopen{}\left(1 - \mathrm{fabs}_{\mathrm{api}}\right) \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_tra}} \cdot f_{\mathrm{ka\_colon\_api}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_tra}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_tra\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_des\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_des}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_des\_api}}}{\mathrm{GU}_{\mathrm{\_T\_des}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_des\_api}} &= \frac{\mathrm{fabs}_{\mathrm{api}} \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_des}} \cdot f_{\mathrm{ka\_colon\_api}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_des}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_des\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_feces\_des\_api}} &= \frac{\mathopen{}\left(1 - \mathrm{fabs}_{\mathrm{api}}\right) \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_des}} \cdot f_{\mathrm{ka\_colon\_api}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_des}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_des\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_sig\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_sig}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_sig\_api}}}{\mathrm{GU}_{\mathrm{\_T\_sig}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_sig\_api}} &= \frac{\mathrm{fabs}_{\mathrm{api}} \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_sig}} \cdot f_{\mathrm{ka\_colon\_api}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_sig}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_sig\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_feces\_sig\_api}} &= \frac{\mathopen{}\left(1 - \mathrm{fabs}_{\mathrm{api}}\right) \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_sig}} \cdot f_{\mathrm{ka\_colon\_api}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_sig}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_sig\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_rec\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_rec}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_rec\_api}}}{\mathrm{GU}_{\mathrm{\_T\_rec}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_rec\_api}} &= \frac{\mathrm{fabs}_{\mathrm{api}} \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_rec}} \cdot f_{\mathrm{ka\_colon\_api}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_rec}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_rec\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_feces\_rec\_api}} &= \frac{\mathopen{}\left(1 - \mathrm{fabs}_{\mathrm{api}}\right) \cdot \mathrm{ka}_{\mathrm{api}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_rec}} \cdot f_{\mathrm{ka\_colon\_api}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_rec}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_rec\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_bile\_api}} &= k_{\mathrm{bile}} \cdot \mathrm{Vbile} \cdot \mathrm{Cbile}_{\mathrm{api}} \\[1ex]
v_{\mathrm{GU\_\_J\_po\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_kdis\_api}} \cdot \mathrm{PODOSE}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}} \\[1ex]
v_{\mathrm{GU\_\_J\_trs\_st\_api}} &= \frac{\frac{\mathrm{PODOSE}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}}}{\mathopen{}\left(\mathrm{GU}_{\mathrm{\_T\_st}} + \mathrm{FED} \cdot \mathopen{}\left(\mathrm{GU}_{\mathrm{\_T\_st\_fed}} \cdot \mathrm{fsex}_{\mathrm{t\_stomach\_fed}} - \mathrm{GU}_{\mathrm{\_T\_st}}\right)\right) \cdot \mathrm{fimp}_{\mathrm{t\_stomach}}} \\[1ex]
v_{\mathrm{GU\_\_J\_dis\_du\_api}} &= \mathrm{GU}_{\mathrm{\_kdis\_api}} \cdot \mathrm{GU}_{\mathrm{\_Asolid\_du\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_trs\_du\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Asolid\_du\_api}}}{\mathrm{GU}_{\mathrm{\_T\_du}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_dis\_jej1\_api}} &= \mathrm{GU}_{\mathrm{\_kdis\_api}} \cdot \mathrm{GU}_{\mathrm{\_Asolid\_jej1\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_trs\_jej1\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Asolid\_jej1\_api}}}{\mathrm{GU}_{\mathrm{\_T\_jej1}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_dis\_jej2\_api}} &= \mathrm{GU}_{\mathrm{\_kdis\_api}} \cdot \mathrm{GU}_{\mathrm{\_Asolid\_jej2\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_trs\_jej2\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Asolid\_jej2\_api}}}{\mathrm{GU}_{\mathrm{\_T\_jej2}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_dis\_ile1\_api}} &= \mathrm{GU}_{\mathrm{\_kdis\_api}} \cdot \mathrm{GU}_{\mathrm{\_Asolid\_ile1\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_trs\_ile1\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Asolid\_ile1\_api}}}{\mathrm{GU}_{\mathrm{\_T\_ile1}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_dis\_ile2\_api}} &= \mathrm{GU}_{\mathrm{\_kdis\_api}} \cdot \mathrm{GU}_{\mathrm{\_Asolid\_ile2\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_trs\_ile2\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Asolid\_ile2\_api}}}{\mathrm{GU}_{\mathrm{\_T\_ile2}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_dis\_cae\_api}} &= \mathrm{GU}_{\mathrm{\_kdis\_api}} \cdot \mathrm{GU}_{\mathrm{\_Asolid\_cae\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_trs\_cae\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Asolid\_cae\_api}}}{\mathrm{GU}_{\mathrm{\_T\_cae}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_dis\_asc\_api}} &= \mathrm{GU}_{\mathrm{\_kdis\_api}} \cdot \mathrm{GU}_{\mathrm{\_Asolid\_asc\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_trs\_asc\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Asolid\_asc\_api}}}{\mathrm{GU}_{\mathrm{\_T\_asc}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_dis\_tra\_api}} &= \mathrm{GU}_{\mathrm{\_kdis\_api}} \cdot \mathrm{GU}_{\mathrm{\_Asolid\_tra\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_trs\_tra\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Asolid\_tra\_api}}}{\mathrm{GU}_{\mathrm{\_T\_tra}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_dis\_des\_api}} &= \mathrm{GU}_{\mathrm{\_kdis\_api}} \cdot \mathrm{GU}_{\mathrm{\_Asolid\_des\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_trs\_des\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Asolid\_des\_api}}}{\mathrm{GU}_{\mathrm{\_T\_des}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_dis\_sig\_api}} &= \mathrm{GU}_{\mathrm{\_kdis\_api}} \cdot \mathrm{GU}_{\mathrm{\_Asolid\_sig\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_trs\_sig\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Asolid\_sig\_api}}}{\mathrm{GU}_{\mathrm{\_T\_sig}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_dis\_rec\_api}} &= \mathrm{GU}_{\mathrm{\_kdis\_api}} \cdot \mathrm{GU}_{\mathrm{\_Asolid\_rec\_api}} \\[1ex]
v_{\mathrm{GU\_\_J\_trs\_rec\_api}} &= \frac{\mathrm{GU}_{\mathrm{\_Asolid\_rec\_api}}}{\mathrm{GU}_{\mathrm{\_T\_rec}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_sol\_api}} &= \frac{\frac{\mathrm{Ka}_{\mathrm{sol\_api}}}{60} \cdot \mathrm{SOLDOSE}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}} \\[1ex]
v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api\_m1}} &= \mathrm{GU}_{\mathrm{\_Qgu}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{GU\_\_J\_out\_pl\_api\_m1}} &= \mathrm{GU}_{\mathrm{\_Qgu}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{si\_api\_m1}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_st\_api\_m1}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_st}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_st\_api\_m1}}}{\mathopen{}\left(\mathrm{GU}_{\mathrm{\_T\_st}} + \mathrm{FED} \cdot \mathopen{}\left(\mathrm{GU}_{\mathrm{\_T\_st\_fed}} \cdot \mathrm{fsex}_{\mathrm{t\_stomach\_fed}} - \mathrm{GU}_{\mathrm{\_T\_st}}\right)\right) \cdot \mathrm{fimp}_{\mathrm{t\_stomach}}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_du\_api\_m1}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_du}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_T\_du}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_du\_api\_m1}} &= \frac{\mathrm{ka}_{\mathrm{api\_m1}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_du}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_du}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m1}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_jej1\_api\_m1}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_jej1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_T\_jej1}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_jej1\_api\_m1}} &= \frac{\mathrm{ka}_{\mathrm{api\_m1}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_jej1}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_jej1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m1}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_jej2\_api\_m1}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_jej2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_T\_jej2}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_jej2\_api\_m1}} &= \frac{\mathrm{ka}_{\mathrm{api\_m1}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_jej2}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_jej2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m1}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_ile1\_api\_m1}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_ile1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_T\_ile1}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_ile1\_api\_m1}} &= \frac{\mathrm{ka}_{\mathrm{api\_m1}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_ile1}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_ile1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m1}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_ile2\_api\_m1}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_ile2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_T\_ile2}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_ile2\_api\_m1}} &= \frac{\mathrm{ka}_{\mathrm{api\_m1}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_ile2}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_ile2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m1}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_cae\_api\_m1}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_cae}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_T\_cae}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_cae\_api\_m1}} &= \frac{\mathrm{ka}_{\mathrm{api\_m1}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_cae}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_cae}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m1}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_asc\_api\_m1}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_asc}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_T\_asc}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_asc\_api\_m1}} &= \frac{\mathrm{ka}_{\mathrm{api\_m1}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_asc}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_asc}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m1}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_tra\_api\_m1}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_tra}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_T\_tra}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_tra\_api\_m1}} &= \frac{\mathrm{ka}_{\mathrm{api\_m1}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_tra}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_tra}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m1}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_des\_api\_m1}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_des}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_T\_des}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_des\_api\_m1}} &= \frac{\mathrm{ka}_{\mathrm{api\_m1}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_des}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_des}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m1}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_sig\_api\_m1}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_sig}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_T\_sig}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_sig\_api\_m1}} &= \frac{\mathrm{ka}_{\mathrm{api\_m1}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_sig}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_sig}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m1}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_rec\_api\_m1}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_rec}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_T\_rec}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_rec\_api\_m1}} &= \frac{\mathrm{ka}_{\mathrm{api\_m1}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_rec}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_rec}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m1}} \\[1ex]
v_{\mathrm{GU\_\_J\_bile\_api\_m1}} &= k_{\mathrm{bile}} \cdot \mathrm{Vbile} \cdot \mathrm{Cbile}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api\_m2}} &= \mathrm{GU}_{\mathrm{\_Qgu}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{GU\_\_J\_out\_pl\_api\_m2}} &= \mathrm{GU}_{\mathrm{\_Qgu}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{si\_api\_m2}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_st\_api\_m2}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_st}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_st\_api\_m2}}}{\mathopen{}\left(\mathrm{GU}_{\mathrm{\_T\_st}} + \mathrm{FED} \cdot \mathopen{}\left(\mathrm{GU}_{\mathrm{\_T\_st\_fed}} \cdot \mathrm{fsex}_{\mathrm{t\_stomach\_fed}} - \mathrm{GU}_{\mathrm{\_T\_st}}\right)\right) \cdot \mathrm{fimp}_{\mathrm{t\_stomach}}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_du\_api\_m2}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_du}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_T\_du}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_du\_api\_m2}} &= \frac{\mathrm{ka}_{\mathrm{api\_m2}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_du}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_du}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m2}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_jej1\_api\_m2}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_jej1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_T\_jej1}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_jej1\_api\_m2}} &= \frac{\mathrm{ka}_{\mathrm{api\_m2}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_jej1}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_jej1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m2}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_jej2\_api\_m2}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_jej2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_T\_jej2}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_jej2\_api\_m2}} &= \frac{\mathrm{ka}_{\mathrm{api\_m2}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_jej2}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_jej2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m2}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_ile1\_api\_m2}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_ile1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_T\_ile1}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_ile1\_api\_m2}} &= \frac{\mathrm{ka}_{\mathrm{api\_m2}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_ile1}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_ile1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m2}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_ile2\_api\_m2}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_ile2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_T\_ile2}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_ile2\_api\_m2}} &= \frac{\mathrm{ka}_{\mathrm{api\_m2}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_ile2}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_ile2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m2}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_cae\_api\_m2}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_cae}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_T\_cae}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_cae\_api\_m2}} &= \frac{\mathrm{ka}_{\mathrm{api\_m2}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_cae}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_cae}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m2}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_asc\_api\_m2}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_asc}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_T\_asc}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_asc\_api\_m2}} &= \frac{\mathrm{ka}_{\mathrm{api\_m2}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_asc}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_asc}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m2}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_tra\_api\_m2}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_tra}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_T\_tra}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_tra\_api\_m2}} &= \frac{\mathrm{ka}_{\mathrm{api\_m2}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_tra}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_tra}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m2}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_des\_api\_m2}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_des}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_T\_des}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_des\_api\_m2}} &= \frac{\mathrm{ka}_{\mathrm{api\_m2}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_des}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_des}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m2}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_sig\_api\_m2}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_sig}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_T\_sig}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_sig\_api\_m2}} &= \frac{\mathrm{ka}_{\mathrm{api\_m2}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_sig}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_sig}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m2}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_rec\_api\_m2}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_rec}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_T\_rec}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_rec\_api\_m2}} &= \frac{\mathrm{ka}_{\mathrm{api\_m2}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_rec}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_rec}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m2}} \\[1ex]
v_{\mathrm{GU\_\_J\_bile\_api\_m2}} &= k_{\mathrm{bile}} \cdot \mathrm{Vbile} \cdot \mathrm{Cbile}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api\_m7}} &= \mathrm{GU}_{\mathrm{\_Qgu}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{GU\_\_J\_out\_pl\_api\_m7}} &= \mathrm{GU}_{\mathrm{\_Qgu}} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{si\_api\_m7}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_st\_api\_m7}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_st}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_st\_api\_m7}}}{\mathopen{}\left(\mathrm{GU}_{\mathrm{\_T\_st}} + \mathrm{FED} \cdot \mathopen{}\left(\mathrm{GU}_{\mathrm{\_T\_st\_fed}} \cdot \mathrm{fsex}_{\mathrm{t\_stomach\_fed}} - \mathrm{GU}_{\mathrm{\_T\_st}}\right)\right) \cdot \mathrm{fimp}_{\mathrm{t\_stomach}}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_du\_api\_m7}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_du}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_T\_du}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_du\_api\_m7}} &= \frac{\mathrm{ka}_{\mathrm{api\_m7}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_du}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_du}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m7}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_jej1\_api\_m7}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_jej1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_T\_jej1}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_jej1\_api\_m7}} &= \frac{\mathrm{ka}_{\mathrm{api\_m7}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_jej1}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_jej1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m7}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_jej2\_api\_m7}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_jej2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_T\_jej2}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_jej2\_api\_m7}} &= \frac{\mathrm{ka}_{\mathrm{api\_m7}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_jej2}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_jej2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m7}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_ile1\_api\_m7}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_ile1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_T\_ile1}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_ile1\_api\_m7}} &= \frac{\mathrm{ka}_{\mathrm{api\_m7}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_ile1}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_ile1}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m7}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_ile2\_api\_m7}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_ile2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_T\_ile2}} \cdot \mathrm{fimp}_{\mathrm{t\_si}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_ile2\_api\_m7}} &= \frac{\mathrm{ka}_{\mathrm{api\_m7}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_ile2}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_ile2}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m7}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_cae\_api\_m7}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_cae}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_T\_cae}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_cae\_api\_m7}} &= \frac{\mathrm{ka}_{\mathrm{api\_m7}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_cae}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_cae}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m7}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_asc\_api\_m7}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_asc}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_T\_asc}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_asc\_api\_m7}} &= \frac{\mathrm{ka}_{\mathrm{api\_m7}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_asc}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_asc}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m7}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_tra\_api\_m7}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_tra}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_T\_tra}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_tra\_api\_m7}} &= \frac{\mathrm{ka}_{\mathrm{api\_m7}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_tra}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_tra}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m7}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_des\_api\_m7}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_des}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_T\_des}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_des\_api\_m7}} &= \frac{\mathrm{ka}_{\mathrm{api\_m7}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_des}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_des}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m7}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_sig\_api\_m7}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_sig}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_T\_sig}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_sig\_api\_m7}} &= \frac{\mathrm{ka}_{\mathrm{api\_m7}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_sig}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_sig}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m7}} \\[1ex]
v_{\mathrm{GU\_\_J\_tr\_rec\_api\_m7}} &= \frac{\mathrm{GU}_{\mathrm{\_Vlumen\_rec}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_T\_rec}} \cdot \mathrm{fsex}_{\mathrm{t\_colon}}} \\[1ex]
v_{\mathrm{GU\_\_J\_abs\_rec\_api\_m7}} &= \frac{\mathrm{ka}_{\mathrm{api\_m7}}}{60} \cdot \mathrm{GU}_{\mathrm{\_f\_area\_rec}} \cdot \mathrm{GU}_{\mathrm{\_Vlumen\_rec}} \cdot \mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m7}} \\[1ex]
v_{\mathrm{GU\_\_J\_bile\_api\_m7}} &= k_{\mathrm{bile}} \cdot \mathrm{Vbile} \cdot \mathrm{Cbile}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{GU\_\_APISEC\_du}} &= \frac{\mathrm{GU}_{\mathrm{\_f\_abcb1}} \cdot \mathrm{GU}_{\mathrm{\_w\_uniform\_du}} \cdot \mathrm{GU}_{\mathrm{\_APISEC\_k}} \cdot \mathrm{Vsi} \cdot \mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_du\_api}} \\[1ex]
v_{\mathrm{GU\_\_APISEC\_jej1}} &= \frac{\mathrm{GU}_{\mathrm{\_f\_abcb1}} \cdot \mathrm{GU}_{\mathrm{\_w\_uniform\_jej1}} \cdot \mathrm{GU}_{\mathrm{\_APISEC\_k}} \cdot \mathrm{Vsi} \cdot \mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_jej1\_api}} \\[1ex]
v_{\mathrm{GU\_\_APISEC\_jej2}} &= \frac{\mathrm{GU}_{\mathrm{\_f\_abcb1}} \cdot \mathrm{GU}_{\mathrm{\_w\_uniform\_jej2}} \cdot \mathrm{GU}_{\mathrm{\_APISEC\_k}} \cdot \mathrm{Vsi} \cdot \mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_jej2\_api}} \\[1ex]
v_{\mathrm{GU\_\_APISEC\_ile1}} &= \frac{\mathrm{GU}_{\mathrm{\_f\_abcb1}} \cdot \mathrm{GU}_{\mathrm{\_w\_uniform\_ile1}} \cdot \mathrm{GU}_{\mathrm{\_APISEC\_k}} \cdot \mathrm{Vsi} \cdot \mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_ile1\_api}} \\[1ex]
v_{\mathrm{GU\_\_APISEC\_ile2}} &= \frac{\mathrm{GU}_{\mathrm{\_f\_abcb1}} \cdot \mathrm{GU}_{\mathrm{\_w\_uniform\_ile2}} \cdot \mathrm{GU}_{\mathrm{\_APISEC\_k}} \cdot \mathrm{Vsi} \cdot \mathrm{fu}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_K\_mu\_api}}} \cdot \mathrm{GU}_{\mathrm{\_Cmu\_ile2\_api}} \\[1ex]
v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api}} &= \mathrm{Qsp} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{SP\_\_J\_out\_pl\_api}} &= \mathrm{Qsp} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{sp\_api}} \\[1ex]
v_{\mathrm{SP\_\_J\_ti\_api}} &= \mathrm{SP}_{\mathrm{\_PS\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathopen{}\left(\mathrm{SP}_{\mathrm{\_Cpl\_api}} - \frac{\mathrm{SP}_{\mathrm{\_Cti\_api}}}{\mathrm{Kp}_{\mathrm{api}}}\right) \\[1ex]
v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api\_m1}} &= \mathrm{Qsp} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{SP\_\_J\_out\_pl\_api\_m1}} &= \mathrm{Qsp} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{sp\_api\_m1}} \\[1ex]
v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api\_m2}} &= \mathrm{Qsp} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{SP\_\_J\_out\_pl\_api\_m2}} &= \mathrm{Qsp} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{sp\_api\_m2}} \\[1ex]
v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api\_m7}} &= \mathrm{Qsp} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{SP\_\_J\_out\_pl\_api\_m7}} &= \mathrm{Qsp} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{sp\_api\_m7}} \\[1ex]
v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api}} &= \mathrm{Qpa} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{PA\_\_J\_out\_pl\_api}} &= \mathrm{Qpa} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{pa\_api}} \\[1ex]
v_{\mathrm{PA\_\_J\_ti\_api}} &= \mathrm{PA}_{\mathrm{\_PS\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathopen{}\left(\mathrm{PA}_{\mathrm{\_Cpl\_api}} - \frac{\mathrm{PA}_{\mathrm{\_Cti\_api}}}{\mathrm{Kp}_{\mathrm{api}}}\right) \\[1ex]
v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api\_m1}} &= \mathrm{Qpa} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{PA\_\_J\_out\_pl\_api\_m1}} &= \mathrm{Qpa} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{pa\_api\_m1}} \\[1ex]
v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api\_m2}} &= \mathrm{Qpa} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{PA\_\_J\_out\_pl\_api\_m2}} &= \mathrm{Qpa} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{pa\_api\_m2}} \\[1ex]
v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api\_m7}} &= \mathrm{Qpa} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{PA\_\_J\_out\_pl\_api\_m7}} &= \mathrm{Qpa} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{pa\_api\_m7}} \\[1ex]
v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api}} &= \mathrm{Qmu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{MU\_\_J\_out\_pl\_api}} &= \mathrm{Qmu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{mu\_api}} \\[1ex]
v_{\mathrm{MU\_\_J\_ti\_api}} &= \mathrm{MU}_{\mathrm{\_PS\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathopen{}\left(\mathrm{MU}_{\mathrm{\_Cpl\_api}} - \frac{\mathrm{MU}_{\mathrm{\_Cti\_api}}}{\mathrm{Kp}_{\mathrm{api}}}\right) \\[1ex]
v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api\_m1}} &= \mathrm{Qmu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{MU\_\_J\_out\_pl\_api\_m1}} &= \mathrm{Qmu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{mu\_api\_m1}} \\[1ex]
v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api\_m2}} &= \mathrm{Qmu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{MU\_\_J\_out\_pl\_api\_m2}} &= \mathrm{Qmu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{mu\_api\_m2}} \\[1ex]
v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api\_m7}} &= \mathrm{Qmu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{MU\_\_J\_out\_pl\_api\_m7}} &= \mathrm{Qmu} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{mu\_api\_m7}} \\[1ex]
v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api}} &= \mathrm{Qsk} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{SK\_\_J\_out\_pl\_api}} &= \mathrm{Qsk} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{sk\_api}} \\[1ex]
v_{\mathrm{SK\_\_J\_ti\_api}} &= \mathrm{SK}_{\mathrm{\_PS\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathopen{}\left(\mathrm{SK}_{\mathrm{\_Cpl\_api}} - \frac{\mathrm{SK}_{\mathrm{\_Cti\_api}}}{\mathrm{Kp}_{\mathrm{api}}}\right) \\[1ex]
v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api\_m1}} &= \mathrm{Qsk} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{SK\_\_J\_out\_pl\_api\_m1}} &= \mathrm{Qsk} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{sk\_api\_m1}} \\[1ex]
v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api\_m2}} &= \mathrm{Qsk} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{SK\_\_J\_out\_pl\_api\_m2}} &= \mathrm{Qsk} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{sk\_api\_m2}} \\[1ex]
v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api\_m7}} &= \mathrm{Qsk} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{SK\_\_J\_out\_pl\_api\_m7}} &= \mathrm{Qsk} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{sk\_api\_m7}} \\[1ex]
v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api}} &= \mathrm{Qad} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{AD\_\_J\_out\_pl\_api}} &= \mathrm{Qad} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{ad\_api}} \\[1ex]
v_{\mathrm{AD\_\_J\_ti\_api}} &= \mathrm{AD}_{\mathrm{\_PS\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathopen{}\left(\mathrm{AD}_{\mathrm{\_Cpl\_api}} - \frac{\mathrm{AD}_{\mathrm{\_Cti\_api}}}{\mathrm{Kp}_{\mathrm{api}}}\right) \\[1ex]
v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api\_m1}} &= \mathrm{Qad} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{AD\_\_J\_out\_pl\_api\_m1}} &= \mathrm{Qad} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{ad\_api\_m1}} \\[1ex]
v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api\_m2}} &= \mathrm{Qad} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{AD\_\_J\_out\_pl\_api\_m2}} &= \mathrm{Qad} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{ad\_api\_m2}} \\[1ex]
v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api\_m7}} &= \mathrm{Qad} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{AD\_\_J\_out\_pl\_api\_m7}} &= \mathrm{Qad} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{ad\_api\_m7}} \\[1ex]
v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api}} &= \mathrm{Qbo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{BO\_\_J\_out\_pl\_api}} &= \mathrm{Qbo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{bo\_api}} \\[1ex]
v_{\mathrm{BO\_\_J\_ti\_api}} &= \mathrm{BO}_{\mathrm{\_PS\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathopen{}\left(\mathrm{BO}_{\mathrm{\_Cpl\_api}} - \frac{\mathrm{BO}_{\mathrm{\_Cti\_api}}}{\mathrm{Kp}_{\mathrm{api}}}\right) \\[1ex]
v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api\_m1}} &= \mathrm{Qbo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{BO\_\_J\_out\_pl\_api\_m1}} &= \mathrm{Qbo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{bo\_api\_m1}} \\[1ex]
v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api\_m2}} &= \mathrm{Qbo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{BO\_\_J\_out\_pl\_api\_m2}} &= \mathrm{Qbo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{bo\_api\_m2}} \\[1ex]
v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api\_m7}} &= \mathrm{Qbo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{BO\_\_J\_out\_pl\_api\_m7}} &= \mathrm{Qbo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{bo\_api\_m7}} \\[1ex]
v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api}} &= \mathrm{Qgo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{GO\_\_J\_out\_pl\_api}} &= \mathrm{Qgo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{go\_api}} \\[1ex]
v_{\mathrm{GO\_\_J\_ti\_api}} &= \mathrm{GO}_{\mathrm{\_PS\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathopen{}\left(\mathrm{GO}_{\mathrm{\_Cpl\_api}} - \frac{\mathrm{GO}_{\mathrm{\_Cti\_api}}}{\mathrm{Kp}_{\mathrm{api}}}\right) \\[1ex]
v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api\_m1}} &= \mathrm{Qgo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m1}} \\[1ex]
v_{\mathrm{GO\_\_J\_out\_pl\_api\_m1}} &= \mathrm{Qgo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{go\_api\_m1}} \\[1ex]
v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api\_m2}} &= \mathrm{Qgo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m2}} \\[1ex]
v_{\mathrm{GO\_\_J\_out\_pl\_api\_m2}} &= \mathrm{Qgo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{go\_api\_m2}} \\[1ex]
v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api\_m7}} &= \mathrm{Qgo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Car}_{\mathrm{api\_m7}} \\[1ex]
v_{\mathrm{GO\_\_J\_out\_pl\_api\_m7}} &= \mathrm{Qgo} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathrm{Cout}_{\mathrm{go\_api\_m7}}
\end{aligned}
$$

## ODE system

The states change in time with the rates of the reactions and the rate rules:

$$
\begin{aligned}
\frac{\mathrm{d} \,\mathrm{Car}_{\mathrm{api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Var}_{\mathrm{pl}}} \Bigl( v_{\mathrm{LU\_\_J\_out\_pl\_api}} - v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api}} \\
&\quad {} - v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api}} - v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api}} \\
&\quad {} - v_{\mathrm{GU\_\_J\_mu\_in\_du\_api}} - v_{\mathrm{GU\_\_J\_mu\_in\_jej1\_api}} - v_{\mathrm{GU\_\_J\_mu\_in\_jej2\_api}} - v_{\mathrm{GU\_\_J\_mu\_in\_ile1\_api}} \\
&\quad {} - v_{\mathrm{GU\_\_J\_mu\_in\_ile2\_api}} - v_{\mathrm{GU\_\_J\_mu\_in\_cae\_api}} - v_{\mathrm{GU\_\_J\_mu\_in\_asc\_api}} - v_{\mathrm{GU\_\_J\_mu\_in\_tra\_api}} \\
&\quad {} - v_{\mathrm{GU\_\_J\_mu\_in\_des\_api}} - v_{\mathrm{GU\_\_J\_mu\_in\_sig\_api}} - v_{\mathrm{GU\_\_J\_mu\_in\_rec\_api}} - v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api}} \\
&\quad {} - v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api}} \\
&\quad {} - v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Car}_{\mathrm{api\_m1}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Var}_{\mathrm{pl}}} \Bigl( v_{\mathrm{LU\_\_J\_out\_pl\_api\_m1}} - v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api\_m1}} \\
&\quad {} - v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api\_m1}} - v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api\_m1}} \\
&\quad {} - v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api\_m1}} \\
&\quad {} - v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api\_m1}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Car}_{\mathrm{api\_m2}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Var}_{\mathrm{pl}}} \Bigl( v_{\mathrm{LU\_\_J\_out\_pl\_api\_m2}} - v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api\_m2}} \\
&\quad {} - v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api\_m2}} - v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api\_m2}} \\
&\quad {} - v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api\_m2}} \\
&\quad {} - v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api\_m2}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Car}_{\mathrm{api\_m7}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Var}_{\mathrm{pl}}} \Bigl( v_{\mathrm{LU\_\_J\_out\_pl\_api\_m7}} - v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api\_m7}} \\
&\quad {} - v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api\_m7}} - v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api\_m7}} \\
&\quad {} - v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api\_m7}} \\
&\quad {} - v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api\_m7}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cve}_{\mathrm{api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vve}_{\mathrm{pl}}} \Bigl( v_{\mathrm{J\_iv\_api}} - v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api}} + v_{\mathrm{HE\_\_J\_out\_pl\_api}} + v_{\mathrm{BR\_\_J\_out\_pl\_api}} \\
&\quad {} + v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api}} + v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api}} + v_{\mathrm{LI\_\_J\_out\_pl\_api}} + v_{\mathrm{KI\_\_J\_out\_pl\_api}} \\
&\quad {} + v_{\mathrm{MU\_\_J\_out\_pl\_api}} + v_{\mathrm{SK\_\_J\_out\_pl\_api}} + v_{\mathrm{AD\_\_J\_out\_pl\_api}} + v_{\mathrm{BO\_\_J\_out\_pl\_api}} \\
&\quad {} + v_{\mathrm{GO\_\_J\_out\_pl\_api}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cve}_{\mathrm{api\_m1}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vve}_{\mathrm{pl}}} \Bigl( -v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api\_m1}} + v_{\mathrm{HE\_\_J\_out\_pl\_api\_m1}} + v_{\mathrm{BR\_\_J\_out\_pl\_api\_m1}} + v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api\_m1}} \\
&\quad {} + v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api\_m1}} + v_{\mathrm{LI\_\_J\_out\_pl\_api\_m1}} + v_{\mathrm{KI\_\_J\_out\_pl\_api\_m1}} + v_{\mathrm{MU\_\_J\_out\_pl\_api\_m1}} \\
&\quad {} + v_{\mathrm{SK\_\_J\_out\_pl\_api\_m1}} + v_{\mathrm{AD\_\_J\_out\_pl\_api\_m1}} + v_{\mathrm{BO\_\_J\_out\_pl\_api\_m1}} + v_{\mathrm{GO\_\_J\_out\_pl\_api\_m1}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cve}_{\mathrm{api\_m2}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vve}_{\mathrm{pl}}} \Bigl( -v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api\_m2}} + v_{\mathrm{HE\_\_J\_out\_pl\_api\_m2}} + v_{\mathrm{BR\_\_J\_out\_pl\_api\_m2}} + v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api\_m2}} \\
&\quad {} + v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api\_m2}} + v_{\mathrm{LI\_\_J\_out\_pl\_api\_m2}} + v_{\mathrm{KI\_\_J\_out\_pl\_api\_m2}} + v_{\mathrm{MU\_\_J\_out\_pl\_api\_m2}} \\
&\quad {} + v_{\mathrm{SK\_\_J\_out\_pl\_api\_m2}} + v_{\mathrm{AD\_\_J\_out\_pl\_api\_m2}} + v_{\mathrm{BO\_\_J\_out\_pl\_api\_m2}} + v_{\mathrm{GO\_\_J\_out\_pl\_api\_m2}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cve}_{\mathrm{api\_m7}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vve}_{\mathrm{pl}}} \Bigl( -v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api\_m7}} + v_{\mathrm{HE\_\_J\_out\_pl\_api\_m7}} + v_{\mathrm{BR\_\_J\_out\_pl\_api\_m7}} + v_{\mathrm{LI\_\_J\_shunt\_ar\_pl\_api\_m7}} \\
&\quad {} + v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api\_m7}} + v_{\mathrm{LI\_\_J\_out\_pl\_api\_m7}} + v_{\mathrm{KI\_\_J\_out\_pl\_api\_m7}} + v_{\mathrm{MU\_\_J\_out\_pl\_api\_m7}} \\
&\quad {} + v_{\mathrm{SK\_\_J\_out\_pl\_api\_m7}} + v_{\mathrm{AD\_\_J\_out\_pl\_api\_m7}} + v_{\mathrm{BO\_\_J\_out\_pl\_api\_m7}} + v_{\mathrm{GO\_\_J\_out\_pl\_api\_m7}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpo}_{\mathrm{api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vpo}_{\mathrm{pl}}} \Bigl( -v_{\mathrm{LI\_\_J\_in\_po\_pl\_api}} - v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api}} + v_{\mathrm{ST\_\_J\_out\_pl\_api}} + v_{\mathrm{GU\_\_J\_out\_pl\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_mu\_out\_du\_api}} + v_{\mathrm{GU\_\_J\_mu\_out\_jej1\_api}} + v_{\mathrm{GU\_\_J\_mu\_out\_jej2\_api}} + v_{\mathrm{GU\_\_J\_mu\_out\_ile1\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_mu\_out\_ile2\_api}} + v_{\mathrm{GU\_\_J\_mu\_out\_cae\_api}} + v_{\mathrm{GU\_\_J\_mu\_out\_asc\_api}} + v_{\mathrm{GU\_\_J\_mu\_out\_tra\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_mu\_out\_des\_api}} + v_{\mathrm{GU\_\_J\_mu\_out\_sig\_api}} + v_{\mathrm{GU\_\_J\_mu\_out\_rec\_api}} + v_{\mathrm{SP\_\_J\_out\_pl\_api}} \\
&\quad {} + v_{\mathrm{PA\_\_J\_out\_pl\_api}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpo}_{\mathrm{api\_m1}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vpo}_{\mathrm{pl}}} \Bigl( -v_{\mathrm{LI\_\_J\_in\_po\_pl\_api\_m1}} - v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api\_m1}} + v_{\mathrm{ST\_\_J\_out\_pl\_api\_m1}} + v_{\mathrm{GU\_\_J\_out\_pl\_api\_m1}} \\
&\quad {} + v_{\mathrm{SP\_\_J\_out\_pl\_api\_m1}} + v_{\mathrm{PA\_\_J\_out\_pl\_api\_m1}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpo}_{\mathrm{api\_m2}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vpo}_{\mathrm{pl}}} \Bigl( -v_{\mathrm{LI\_\_J\_in\_po\_pl\_api\_m2}} - v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api\_m2}} + v_{\mathrm{ST\_\_J\_out\_pl\_api\_m2}} + v_{\mathrm{GU\_\_J\_out\_pl\_api\_m2}} \\
&\quad {} + v_{\mathrm{SP\_\_J\_out\_pl\_api\_m2}} + v_{\mathrm{PA\_\_J\_out\_pl\_api\_m2}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpo}_{\mathrm{api\_m7}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vpo}_{\mathrm{pl}}} \Bigl( -v_{\mathrm{LI\_\_J\_in\_po\_pl\_api\_m7}} - v_{\mathrm{LI\_\_J\_shunt\_po\_pl\_api\_m7}} + v_{\mathrm{ST\_\_J\_out\_pl\_api\_m7}} + v_{\mathrm{GU\_\_J\_out\_pl\_api\_m7}} \\
&\quad {} + v_{\mathrm{SP\_\_J\_out\_pl\_api\_m7}} + v_{\mathrm{PA\_\_J\_out\_pl\_api\_m7}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Aurine}_{\mathrm{api}}}{\mathrm{d} t} &= v_{\mathrm{KI\_\_J\_gfr\_api}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Afeces}_{\mathrm{api}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_feces\_du\_api}} + v_{\mathrm{GU\_\_J\_feces\_jej1\_api}} + v_{\mathrm{GU\_\_J\_feces\_jej2\_api}} + v_{\mathrm{GU\_\_J\_feces\_ile1\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_feces\_ile2\_api}} + v_{\mathrm{GU\_\_J\_feces\_cae\_api}} + v_{\mathrm{GU\_\_J\_feces\_asc\_api}} + v_{\mathrm{GU\_\_J\_feces\_tra\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_feces\_des\_api}} + v_{\mathrm{GU\_\_J\_feces\_sig\_api}} + v_{\mathrm{GU\_\_J\_tr\_rec\_api}} + v_{\mathrm{GU\_\_J\_feces\_rec\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_trs\_rec\_api}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cbile}_{\mathrm{api}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{GU\_\_J\_bile\_api}}}{\mathrm{Vbile}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Aurine}_{\mathrm{api\_m1}}}{\mathrm{d} t} &= v_{\mathrm{KI\_\_J\_gfr\_api\_m1}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Afeces}_{\mathrm{api\_m1}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_tr\_rec\_api\_m1}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cbile}_{\mathrm{api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_M1EXBI}} - v_{\mathrm{GU\_\_J\_bile\_api\_m1}}}{\mathrm{Vbile}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Afeces}_{\mathrm{api\_m2}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_tr\_rec\_api\_m2}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cbile}_{\mathrm{api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_M2EXBI}} - v_{\mathrm{GU\_\_J\_bile\_api\_m2}}}{\mathrm{Vbile}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Aurine}_{\mathrm{api\_m7}}}{\mathrm{d} t} &= v_{\mathrm{KI\_\_J\_gfr\_api\_m7}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Afeces}_{\mathrm{api\_m7}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_tr\_rec\_api\_m7}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cbile}_{\mathrm{api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_M7EXBI}} - v_{\mathrm{GU\_\_J\_bile\_api\_m7}}}{\mathrm{Vbile}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LU}_{\mathrm{\_Cpl\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api}} - v_{\mathrm{LU\_\_J\_out\_pl\_api}} - v_{\mathrm{LU\_\_J\_ti\_api}}}{\mathrm{LU}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LU}_{\mathrm{\_Cti\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LU\_\_J\_ti\_api}}}{\mathrm{LU}_{\mathrm{\_Vti}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LU}_{\mathrm{\_Cpl\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api\_m1}} - v_{\mathrm{LU\_\_J\_out\_pl\_api\_m1}}}{\mathrm{LU}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LU}_{\mathrm{\_Cpl\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api\_m2}} - v_{\mathrm{LU\_\_J\_out\_pl\_api\_m2}}}{\mathrm{LU}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LU}_{\mathrm{\_Cpl\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LU\_\_J\_in\_ve\_pl\_api\_m7}} - v_{\mathrm{LU\_\_J\_out\_pl\_api\_m7}}}{\mathrm{LU}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{HE}_{\mathrm{\_Cpl\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{HE\_\_J\_out\_pl\_api}} - v_{\mathrm{HE\_\_J\_ti\_api}}}{\mathrm{HE}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{HE}_{\mathrm{\_Cti\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{HE\_\_J\_ti\_api}}}{\mathrm{HE}_{\mathrm{\_Vti}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{HE}_{\mathrm{\_Cpl\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{HE\_\_J\_out\_pl\_api\_m1}}}{\mathrm{HE}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{HE}_{\mathrm{\_Cpl\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{HE\_\_J\_out\_pl\_api\_m2}}}{\mathrm{HE}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{HE}_{\mathrm{\_Cpl\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{HE\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{HE\_\_J\_out\_pl\_api\_m7}}}{\mathrm{HE}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{BR}_{\mathrm{\_Cpl\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{BR\_\_J\_out\_pl\_api}} - v_{\mathrm{BR\_\_J\_ti\_api}}}{\mathrm{BR}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{BR}_{\mathrm{\_Cti\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{BR\_\_J\_ti\_api}}}{\mathrm{BR}_{\mathrm{\_Vti}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{BR}_{\mathrm{\_Cpl\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{BR\_\_J\_out\_pl\_api\_m1}}}{\mathrm{BR}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{BR}_{\mathrm{\_Cpl\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{BR\_\_J\_out\_pl\_api\_m2}}}{\mathrm{BR}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{BR}_{\mathrm{\_Cpl\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{BR\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{BR\_\_J\_out\_pl\_api\_m7}}}{\mathrm{BR}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_Cpl\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api}} + v_{\mathrm{LI\_\_J\_in\_po\_pl\_api}} - v_{\mathrm{LI\_\_J\_out\_pl\_api}} - v_{\mathrm{LI\_\_J\_ti\_api}}}{\mathrm{LI}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_Cti\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_J\_ti\_api}} - v_{\mathrm{LI\_\_API2M}}}{\mathrm{LI}_{\mathrm{\_Vti}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_Cpl\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api\_m1}} + v_{\mathrm{LI\_\_J\_in\_po\_pl\_api\_m1}} - v_{\mathrm{LI\_\_J\_out\_pl\_api\_m1}} - v_{\mathrm{LI\_\_J\_is\_api\_m1}}}{\mathrm{LI}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_Cis\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_J\_is\_api\_m1}} - v_{\mathrm{LI\_\_J\_ic\_api\_m1}}}{\mathrm{LI}_{\mathrm{\_Vis}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_Cic\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_J\_ic\_api\_m1}} + v_{\mathrm{LI\_\_M22M1}} - v_{\mathrm{LI\_\_M1EXBI}}}{\mathrm{LI}_{\mathrm{\_Vic}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_Cpl\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api\_m2}} + v_{\mathrm{LI\_\_J\_in\_po\_pl\_api\_m2}} - v_{\mathrm{LI\_\_J\_out\_pl\_api\_m2}} - v_{\mathrm{LI\_\_J\_is\_api\_m2}}}{\mathrm{LI}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_Cis\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_J\_is\_api\_m2}} - v_{\mathrm{LI\_\_J\_ic\_api\_m2}}}{\mathrm{LI}_{\mathrm{\_Vis}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_Cic\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_J\_ic\_api\_m2}} + 0.78 \cdot v_{\mathrm{LI\_\_API2M}} - v_{\mathrm{LI\_\_M22M1}} - v_{\mathrm{LI\_\_M2EXBI}}}{\mathrm{LI}_{\mathrm{\_Vic}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_Cpl\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_J\_in\_ar\_pl\_api\_m7}} + v_{\mathrm{LI\_\_J\_in\_po\_pl\_api\_m7}} - v_{\mathrm{LI\_\_J\_out\_pl\_api\_m7}} - v_{\mathrm{LI\_\_J\_is\_api\_m7}}}{\mathrm{LI}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_Cis\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_J\_is\_api\_m7}} - v_{\mathrm{LI\_\_J\_ic\_api\_m7}}}{\mathrm{LI}_{\mathrm{\_Vis}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_Cic\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_J\_ic\_api\_m7}} + 0.22 \cdot v_{\mathrm{LI\_\_API2M}} - v_{\mathrm{LI\_\_M7EXBI}}}{\mathrm{LI}_{\mathrm{\_Vic}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{KI}_{\mathrm{\_Cpl\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{KI\_\_J\_out\_pl\_api}} - v_{\mathrm{KI\_\_J\_gfr\_api}} - v_{\mathrm{KI\_\_J\_ti\_api}}}{\mathrm{KI}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{KI}_{\mathrm{\_Cti\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{KI\_\_J\_ti\_api}}}{\mathrm{KI}_{\mathrm{\_Vti}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{KI}_{\mathrm{\_Cpl\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{KI\_\_J\_out\_pl\_api\_m1}} - v_{\mathrm{KI\_\_J\_gfr\_api\_m1}}}{\mathrm{KI}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{KI}_{\mathrm{\_Cpl\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{KI\_\_J\_out\_pl\_api\_m2}}}{\mathrm{KI}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{KI}_{\mathrm{\_Cpl\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{KI\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{KI\_\_J\_out\_pl\_api\_m7}} - v_{\mathrm{KI\_\_J\_gfr\_api\_m7}}}{\mathrm{KI}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{ST}_{\mathrm{\_Cpl\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{ST\_\_J\_out\_pl\_api}} - v_{\mathrm{ST\_\_J\_ti\_api}}}{\mathrm{ST}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{ST}_{\mathrm{\_Cti\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{ST\_\_J\_ti\_api}}}{\mathrm{ST}_{\mathrm{\_Vti}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{ST}_{\mathrm{\_Cpl\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{ST\_\_J\_out\_pl\_api\_m1}}}{\mathrm{ST}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{ST}_{\mathrm{\_Cpl\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{ST\_\_J\_out\_pl\_api\_m2}}}{\mathrm{ST}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{ST}_{\mathrm{\_Cpl\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{ST\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{ST\_\_J\_out\_pl\_api\_m7}}}{\mathrm{ST}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cpl\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{GU\_\_J\_out\_pl\_api}} - v_{\mathrm{GU\_\_J\_ti\_api}}}{\mathrm{GU}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cti\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_ti\_api}}}{\mathrm{GU}_{\mathrm{\_Vti\_wall}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cmu\_du\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_mu\_in\_du\_api}} - v_{\mathrm{GU\_\_J\_mu\_out\_du\_api}} + v_{\mathrm{GU\_\_J\_abs\_du\_api}} - v_{\mathrm{GU\_\_APISEC\_du}}}{\mathrm{GU}_{\mathrm{\_Vmu\_du}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cmu\_jej1\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_mu\_in\_jej1\_api}} - v_{\mathrm{GU\_\_J\_mu\_out\_jej1\_api}} + v_{\mathrm{GU\_\_J\_abs\_jej1\_api}} - v_{\mathrm{GU\_\_APISEC\_jej1}}}{\mathrm{GU}_{\mathrm{\_Vmu\_jej1}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cmu\_jej2\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_mu\_in\_jej2\_api}} - v_{\mathrm{GU\_\_J\_mu\_out\_jej2\_api}} + v_{\mathrm{GU\_\_J\_abs\_jej2\_api}} - v_{\mathrm{GU\_\_APISEC\_jej2}}}{\mathrm{GU}_{\mathrm{\_Vmu\_jej2}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cmu\_ile1\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_mu\_in\_ile1\_api}} - v_{\mathrm{GU\_\_J\_mu\_out\_ile1\_api}} + v_{\mathrm{GU\_\_J\_abs\_ile1\_api}} - v_{\mathrm{GU\_\_APISEC\_ile1}}}{\mathrm{GU}_{\mathrm{\_Vmu\_ile1}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cmu\_ile2\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_mu\_in\_ile2\_api}} - v_{\mathrm{GU\_\_J\_mu\_out\_ile2\_api}} + v_{\mathrm{GU\_\_J\_abs\_ile2\_api}} - v_{\mathrm{GU\_\_APISEC\_ile2}}}{\mathrm{GU}_{\mathrm{\_Vmu\_ile2}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cmu\_cae\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_mu\_in\_cae\_api}} - v_{\mathrm{GU\_\_J\_mu\_out\_cae\_api}} + v_{\mathrm{GU\_\_J\_abs\_cae\_api}}}{\mathrm{GU}_{\mathrm{\_Vmu\_cae}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cmu\_asc\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_mu\_in\_asc\_api}} - v_{\mathrm{GU\_\_J\_mu\_out\_asc\_api}} + v_{\mathrm{GU\_\_J\_abs\_asc\_api}}}{\mathrm{GU}_{\mathrm{\_Vmu\_asc}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cmu\_tra\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_mu\_in\_tra\_api}} - v_{\mathrm{GU\_\_J\_mu\_out\_tra\_api}} + v_{\mathrm{GU\_\_J\_abs\_tra\_api}}}{\mathrm{GU}_{\mathrm{\_Vmu\_tra}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cmu\_des\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_mu\_in\_des\_api}} - v_{\mathrm{GU\_\_J\_mu\_out\_des\_api}} + v_{\mathrm{GU\_\_J\_abs\_des\_api}}}{\mathrm{GU}_{\mathrm{\_Vmu\_des}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cmu\_sig\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_mu\_in\_sig\_api}} - v_{\mathrm{GU\_\_J\_mu\_out\_sig\_api}} + v_{\mathrm{GU\_\_J\_abs\_sig\_api}}}{\mathrm{GU}_{\mathrm{\_Vmu\_sig}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cmu\_rec\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_mu\_in\_rec\_api}} - v_{\mathrm{GU\_\_J\_mu\_out\_rec\_api}} + v_{\mathrm{GU\_\_J\_abs\_rec\_api}}}{\mathrm{GU}_{\mathrm{\_Vmu\_rec}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_st\_api}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{GU\_\_J\_tr\_st\_api}} + v_{\mathrm{GU\_\_J\_po\_api}} + v_{\mathrm{GU\_\_J\_sol\_api}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_st}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_du\_api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{GU}_{\mathrm{\_Vlumen\_du}}} \Bigl( v_{\mathrm{GU\_\_J\_tr\_st\_api}} - v_{\mathrm{GU\_\_J\_tr\_du\_api}} - v_{\mathrm{GU\_\_J\_abs\_du\_api}} - v_{\mathrm{GU\_\_J\_feces\_du\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_bile\_api}} + v_{\mathrm{GU\_\_J\_dis\_du\_api}} + v_{\mathrm{GU\_\_APISEC\_du}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{GU}_{\mathrm{\_Vlumen\_jej1}}} \Bigl( v_{\mathrm{GU\_\_J\_tr\_du\_api}} - v_{\mathrm{GU\_\_J\_tr\_jej1\_api}} - v_{\mathrm{GU\_\_J\_abs\_jej1\_api}} - v_{\mathrm{GU\_\_J\_feces\_jej1\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_dis\_jej1\_api}} + v_{\mathrm{GU\_\_APISEC\_jej1}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{GU}_{\mathrm{\_Vlumen\_jej2}}} \Bigl( v_{\mathrm{GU\_\_J\_tr\_jej1\_api}} - v_{\mathrm{GU\_\_J\_tr\_jej2\_api}} - v_{\mathrm{GU\_\_J\_abs\_jej2\_api}} - v_{\mathrm{GU\_\_J\_feces\_jej2\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_dis\_jej2\_api}} + v_{\mathrm{GU\_\_APISEC\_jej2}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{GU}_{\mathrm{\_Vlumen\_ile1}}} \Bigl( v_{\mathrm{GU\_\_J\_tr\_jej2\_api}} - v_{\mathrm{GU\_\_J\_tr\_ile1\_api}} - v_{\mathrm{GU\_\_J\_abs\_ile1\_api}} - v_{\mathrm{GU\_\_J\_feces\_ile1\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_dis\_ile1\_api}} + v_{\mathrm{GU\_\_APISEC\_ile1}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{GU}_{\mathrm{\_Vlumen\_ile2}}} \Bigl( v_{\mathrm{GU\_\_J\_tr\_ile1\_api}} - v_{\mathrm{GU\_\_J\_tr\_ile2\_api}} - v_{\mathrm{GU\_\_J\_abs\_ile2\_api}} - v_{\mathrm{GU\_\_J\_feces\_ile2\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_dis\_ile2\_api}} + v_{\mathrm{GU\_\_APISEC\_ile2}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{GU}_{\mathrm{\_Vlumen\_cae}}} \Bigl( v_{\mathrm{GU\_\_J\_tr\_ile2\_api}} - v_{\mathrm{GU\_\_J\_tr\_cae\_api}} - v_{\mathrm{GU\_\_J\_abs\_cae\_api}} - v_{\mathrm{GU\_\_J\_feces\_cae\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_dis\_cae\_api}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{GU}_{\mathrm{\_Vlumen\_asc}}} \Bigl( v_{\mathrm{GU\_\_J\_tr\_cae\_api}} - v_{\mathrm{GU\_\_J\_tr\_asc\_api}} - v_{\mathrm{GU\_\_J\_abs\_asc\_api}} - v_{\mathrm{GU\_\_J\_feces\_asc\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_dis\_asc\_api}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{GU}_{\mathrm{\_Vlumen\_tra}}} \Bigl( v_{\mathrm{GU\_\_J\_tr\_asc\_api}} - v_{\mathrm{GU\_\_J\_tr\_tra\_api}} - v_{\mathrm{GU\_\_J\_abs\_tra\_api}} - v_{\mathrm{GU\_\_J\_feces\_tra\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_dis\_tra\_api}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_des\_api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{GU}_{\mathrm{\_Vlumen\_des}}} \Bigl( v_{\mathrm{GU\_\_J\_tr\_tra\_api}} - v_{\mathrm{GU\_\_J\_tr\_des\_api}} - v_{\mathrm{GU\_\_J\_abs\_des\_api}} - v_{\mathrm{GU\_\_J\_feces\_des\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_dis\_des\_api}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{GU}_{\mathrm{\_Vlumen\_sig}}} \Bigl( v_{\mathrm{GU\_\_J\_tr\_des\_api}} - v_{\mathrm{GU\_\_J\_tr\_sig\_api}} - v_{\mathrm{GU\_\_J\_abs\_sig\_api}} - v_{\mathrm{GU\_\_J\_feces\_sig\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_dis\_sig\_api}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{GU}_{\mathrm{\_Vlumen\_rec}}} \Bigl( v_{\mathrm{GU\_\_J\_tr\_sig\_api}} - v_{\mathrm{GU\_\_J\_tr\_rec\_api}} - v_{\mathrm{GU\_\_J\_abs\_rec\_api}} - v_{\mathrm{GU\_\_J\_feces\_rec\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_dis\_rec\_api}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Asolid\_du\_api}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_trs\_st\_api}} - v_{\mathrm{GU\_\_J\_dis\_du\_api}} - v_{\mathrm{GU\_\_J\_trs\_du\_api}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Asolid\_jej1\_api}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_trs\_du\_api}} - v_{\mathrm{GU\_\_J\_dis\_jej1\_api}} - v_{\mathrm{GU\_\_J\_trs\_jej1\_api}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Asolid\_jej2\_api}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_trs\_jej1\_api}} - v_{\mathrm{GU\_\_J\_dis\_jej2\_api}} - v_{\mathrm{GU\_\_J\_trs\_jej2\_api}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Asolid\_ile1\_api}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_trs\_jej2\_api}} - v_{\mathrm{GU\_\_J\_dis\_ile1\_api}} - v_{\mathrm{GU\_\_J\_trs\_ile1\_api}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Asolid\_ile2\_api}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_trs\_ile1\_api}} - v_{\mathrm{GU\_\_J\_dis\_ile2\_api}} - v_{\mathrm{GU\_\_J\_trs\_ile2\_api}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Asolid\_cae\_api}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_trs\_ile2\_api}} - v_{\mathrm{GU\_\_J\_dis\_cae\_api}} - v_{\mathrm{GU\_\_J\_trs\_cae\_api}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Asolid\_asc\_api}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_trs\_cae\_api}} - v_{\mathrm{GU\_\_J\_dis\_asc\_api}} - v_{\mathrm{GU\_\_J\_trs\_asc\_api}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Asolid\_tra\_api}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_trs\_asc\_api}} - v_{\mathrm{GU\_\_J\_dis\_tra\_api}} - v_{\mathrm{GU\_\_J\_trs\_tra\_api}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Asolid\_des\_api}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_trs\_tra\_api}} - v_{\mathrm{GU\_\_J\_dis\_des\_api}} - v_{\mathrm{GU\_\_J\_trs\_des\_api}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Asolid\_sig\_api}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_trs\_des\_api}} - v_{\mathrm{GU\_\_J\_dis\_sig\_api}} - v_{\mathrm{GU\_\_J\_trs\_sig\_api}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Asolid\_rec\_api}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_trs\_sig\_api}} - v_{\mathrm{GU\_\_J\_dis\_rec\_api}} - v_{\mathrm{GU\_\_J\_trs\_rec\_api}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cpl\_api\_m1}}}{\mathrm{d} t} &= \frac{1}{\mathrm{GU}_{\mathrm{\_Vpl}}} \Bigl( v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{GU\_\_J\_out\_pl\_api\_m1}} + v_{\mathrm{GU\_\_J\_abs\_du\_api\_m1}} + v_{\mathrm{GU\_\_J\_abs\_jej1\_api\_m1}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_abs\_jej2\_api\_m1}} + v_{\mathrm{GU\_\_J\_abs\_ile1\_api\_m1}} + v_{\mathrm{GU\_\_J\_abs\_ile2\_api\_m1}} + v_{\mathrm{GU\_\_J\_abs\_cae\_api\_m1}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_abs\_asc\_api\_m1}} + v_{\mathrm{GU\_\_J\_abs\_tra\_api\_m1}} + v_{\mathrm{GU\_\_J\_abs\_des\_api\_m1}} + v_{\mathrm{GU\_\_J\_abs\_sig\_api\_m1}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_abs\_rec\_api\_m1}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_st\_api\_m1}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{GU\_\_J\_tr\_st\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_st}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_st\_api\_m1}} - v_{\mathrm{GU\_\_J\_tr\_du\_api\_m1}} - v_{\mathrm{GU\_\_J\_abs\_du\_api\_m1}} + v_{\mathrm{GU\_\_J\_bile\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_du}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_du\_api\_m1}} - v_{\mathrm{GU\_\_J\_tr\_jej1\_api\_m1}} - v_{\mathrm{GU\_\_J\_abs\_jej1\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_jej1}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_jej1\_api\_m1}} - v_{\mathrm{GU\_\_J\_tr\_jej2\_api\_m1}} - v_{\mathrm{GU\_\_J\_abs\_jej2\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_jej2}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_jej2\_api\_m1}} - v_{\mathrm{GU\_\_J\_tr\_ile1\_api\_m1}} - v_{\mathrm{GU\_\_J\_abs\_ile1\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_ile1}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_ile1\_api\_m1}} - v_{\mathrm{GU\_\_J\_tr\_ile2\_api\_m1}} - v_{\mathrm{GU\_\_J\_abs\_ile2\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_ile2}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_ile2\_api\_m1}} - v_{\mathrm{GU\_\_J\_tr\_cae\_api\_m1}} - v_{\mathrm{GU\_\_J\_abs\_cae\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_cae}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_cae\_api\_m1}} - v_{\mathrm{GU\_\_J\_tr\_asc\_api\_m1}} - v_{\mathrm{GU\_\_J\_abs\_asc\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_asc}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_asc\_api\_m1}} - v_{\mathrm{GU\_\_J\_tr\_tra\_api\_m1}} - v_{\mathrm{GU\_\_J\_abs\_tra\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_tra}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_tra\_api\_m1}} - v_{\mathrm{GU\_\_J\_tr\_des\_api\_m1}} - v_{\mathrm{GU\_\_J\_abs\_des\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_des}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_des\_api\_m1}} - v_{\mathrm{GU\_\_J\_tr\_sig\_api\_m1}} - v_{\mathrm{GU\_\_J\_abs\_sig\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_sig}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_sig\_api\_m1}} - v_{\mathrm{GU\_\_J\_tr\_rec\_api\_m1}} - v_{\mathrm{GU\_\_J\_abs\_rec\_api\_m1}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_rec}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cpl\_api\_m2}}}{\mathrm{d} t} &= \frac{1}{\mathrm{GU}_{\mathrm{\_Vpl}}} \Bigl( v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{GU\_\_J\_out\_pl\_api\_m2}} + v_{\mathrm{GU\_\_J\_abs\_du\_api\_m2}} + v_{\mathrm{GU\_\_J\_abs\_jej1\_api\_m2}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_abs\_jej2\_api\_m2}} + v_{\mathrm{GU\_\_J\_abs\_ile1\_api\_m2}} + v_{\mathrm{GU\_\_J\_abs\_ile2\_api\_m2}} + v_{\mathrm{GU\_\_J\_abs\_cae\_api\_m2}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_abs\_asc\_api\_m2}} + v_{\mathrm{GU\_\_J\_abs\_tra\_api\_m2}} + v_{\mathrm{GU\_\_J\_abs\_des\_api\_m2}} + v_{\mathrm{GU\_\_J\_abs\_sig\_api\_m2}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_abs\_rec\_api\_m2}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_st\_api\_m2}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{GU\_\_J\_tr\_st\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_st}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_st\_api\_m2}} - v_{\mathrm{GU\_\_J\_tr\_du\_api\_m2}} - v_{\mathrm{GU\_\_J\_abs\_du\_api\_m2}} + v_{\mathrm{GU\_\_J\_bile\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_du}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_du\_api\_m2}} - v_{\mathrm{GU\_\_J\_tr\_jej1\_api\_m2}} - v_{\mathrm{GU\_\_J\_abs\_jej1\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_jej1}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_jej1\_api\_m2}} - v_{\mathrm{GU\_\_J\_tr\_jej2\_api\_m2}} - v_{\mathrm{GU\_\_J\_abs\_jej2\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_jej2}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_jej2\_api\_m2}} - v_{\mathrm{GU\_\_J\_tr\_ile1\_api\_m2}} - v_{\mathrm{GU\_\_J\_abs\_ile1\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_ile1}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_ile1\_api\_m2}} - v_{\mathrm{GU\_\_J\_tr\_ile2\_api\_m2}} - v_{\mathrm{GU\_\_J\_abs\_ile2\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_ile2}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_ile2\_api\_m2}} - v_{\mathrm{GU\_\_J\_tr\_cae\_api\_m2}} - v_{\mathrm{GU\_\_J\_abs\_cae\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_cae}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_cae\_api\_m2}} - v_{\mathrm{GU\_\_J\_tr\_asc\_api\_m2}} - v_{\mathrm{GU\_\_J\_abs\_asc\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_asc}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_asc\_api\_m2}} - v_{\mathrm{GU\_\_J\_tr\_tra\_api\_m2}} - v_{\mathrm{GU\_\_J\_abs\_tra\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_tra}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_tra\_api\_m2}} - v_{\mathrm{GU\_\_J\_tr\_des\_api\_m2}} - v_{\mathrm{GU\_\_J\_abs\_des\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_des}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_des\_api\_m2}} - v_{\mathrm{GU\_\_J\_tr\_sig\_api\_m2}} - v_{\mathrm{GU\_\_J\_abs\_sig\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_sig}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_sig\_api\_m2}} - v_{\mathrm{GU\_\_J\_tr\_rec\_api\_m2}} - v_{\mathrm{GU\_\_J\_abs\_rec\_api\_m2}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_rec}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Cpl\_api\_m7}}}{\mathrm{d} t} &= \frac{1}{\mathrm{GU}_{\mathrm{\_Vpl}}} \Bigl( v_{\mathrm{GU\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{GU\_\_J\_out\_pl\_api\_m7}} + v_{\mathrm{GU\_\_J\_abs\_du\_api\_m7}} + v_{\mathrm{GU\_\_J\_abs\_jej1\_api\_m7}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_abs\_jej2\_api\_m7}} + v_{\mathrm{GU\_\_J\_abs\_ile1\_api\_m7}} + v_{\mathrm{GU\_\_J\_abs\_ile2\_api\_m7}} + v_{\mathrm{GU\_\_J\_abs\_cae\_api\_m7}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_abs\_asc\_api\_m7}} + v_{\mathrm{GU\_\_J\_abs\_tra\_api\_m7}} + v_{\mathrm{GU\_\_J\_abs\_des\_api\_m7}} + v_{\mathrm{GU\_\_J\_abs\_sig\_api\_m7}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_abs\_rec\_api\_m7}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_st\_api\_m7}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{GU\_\_J\_tr\_st\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_st}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_du\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_st\_api\_m7}} - v_{\mathrm{GU\_\_J\_tr\_du\_api\_m7}} - v_{\mathrm{GU\_\_J\_abs\_du\_api\_m7}} + v_{\mathrm{GU\_\_J\_bile\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_du}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_jej1\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_du\_api\_m7}} - v_{\mathrm{GU\_\_J\_tr\_jej1\_api\_m7}} - v_{\mathrm{GU\_\_J\_abs\_jej1\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_jej1}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_jej2\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_jej1\_api\_m7}} - v_{\mathrm{GU\_\_J\_tr\_jej2\_api\_m7}} - v_{\mathrm{GU\_\_J\_abs\_jej2\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_jej2}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_ile1\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_jej2\_api\_m7}} - v_{\mathrm{GU\_\_J\_tr\_ile1\_api\_m7}} - v_{\mathrm{GU\_\_J\_abs\_ile1\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_ile1}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_ile2\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_ile1\_api\_m7}} - v_{\mathrm{GU\_\_J\_tr\_ile2\_api\_m7}} - v_{\mathrm{GU\_\_J\_abs\_ile2\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_ile2}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_cae\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_ile2\_api\_m7}} - v_{\mathrm{GU\_\_J\_tr\_cae\_api\_m7}} - v_{\mathrm{GU\_\_J\_abs\_cae\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_cae}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_asc\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_cae\_api\_m7}} - v_{\mathrm{GU\_\_J\_tr\_asc\_api\_m7}} - v_{\mathrm{GU\_\_J\_abs\_asc\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_asc}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_tra\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_asc\_api\_m7}} - v_{\mathrm{GU\_\_J\_tr\_tra\_api\_m7}} - v_{\mathrm{GU\_\_J\_abs\_tra\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_tra}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_des\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_tra\_api\_m7}} - v_{\mathrm{GU\_\_J\_tr\_des\_api\_m7}} - v_{\mathrm{GU\_\_J\_abs\_des\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_des}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_sig\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_des\_api\_m7}} - v_{\mathrm{GU\_\_J\_tr\_sig\_api\_m7}} - v_{\mathrm{GU\_\_J\_abs\_sig\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_sig}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Clumen\_rec\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_J\_tr\_sig\_api\_m7}} - v_{\mathrm{GU\_\_J\_tr\_rec\_api\_m7}} - v_{\mathrm{GU\_\_J\_abs\_rec\_api\_m7}}}{\mathrm{GU}_{\mathrm{\_Vlumen\_rec}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{SP}_{\mathrm{\_Cpl\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{SP\_\_J\_out\_pl\_api}} - v_{\mathrm{SP\_\_J\_ti\_api}}}{\mathrm{SP}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{SP}_{\mathrm{\_Cti\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{SP\_\_J\_ti\_api}}}{\mathrm{SP}_{\mathrm{\_Vti}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{SP}_{\mathrm{\_Cpl\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{SP\_\_J\_out\_pl\_api\_m1}}}{\mathrm{SP}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{SP}_{\mathrm{\_Cpl\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{SP\_\_J\_out\_pl\_api\_m2}}}{\mathrm{SP}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{SP}_{\mathrm{\_Cpl\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{SP\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{SP\_\_J\_out\_pl\_api\_m7}}}{\mathrm{SP}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{PA}_{\mathrm{\_Cpl\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{PA\_\_J\_out\_pl\_api}} - v_{\mathrm{PA\_\_J\_ti\_api}}}{\mathrm{PA}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{PA}_{\mathrm{\_Cti\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{PA\_\_J\_ti\_api}}}{\mathrm{PA}_{\mathrm{\_Vti}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{PA}_{\mathrm{\_Cpl\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{PA\_\_J\_out\_pl\_api\_m1}}}{\mathrm{PA}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{PA}_{\mathrm{\_Cpl\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{PA\_\_J\_out\_pl\_api\_m2}}}{\mathrm{PA}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{PA}_{\mathrm{\_Cpl\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{PA\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{PA\_\_J\_out\_pl\_api\_m7}}}{\mathrm{PA}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{MU}_{\mathrm{\_Cpl\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{MU\_\_J\_out\_pl\_api}} - v_{\mathrm{MU\_\_J\_ti\_api}}}{\mathrm{MU}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{MU}_{\mathrm{\_Cti\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{MU\_\_J\_ti\_api}}}{\mathrm{MU}_{\mathrm{\_Vti}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{MU}_{\mathrm{\_Cpl\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{MU\_\_J\_out\_pl\_api\_m1}}}{\mathrm{MU}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{MU}_{\mathrm{\_Cpl\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{MU\_\_J\_out\_pl\_api\_m2}}}{\mathrm{MU}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{MU}_{\mathrm{\_Cpl\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{MU\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{MU\_\_J\_out\_pl\_api\_m7}}}{\mathrm{MU}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{SK}_{\mathrm{\_Cpl\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{SK\_\_J\_out\_pl\_api}} - v_{\mathrm{SK\_\_J\_ti\_api}}}{\mathrm{SK}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{SK}_{\mathrm{\_Cti\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{SK\_\_J\_ti\_api}}}{\mathrm{SK}_{\mathrm{\_Vti}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{SK}_{\mathrm{\_Cpl\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{SK\_\_J\_out\_pl\_api\_m1}}}{\mathrm{SK}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{SK}_{\mathrm{\_Cpl\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{SK\_\_J\_out\_pl\_api\_m2}}}{\mathrm{SK}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{SK}_{\mathrm{\_Cpl\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{SK\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{SK\_\_J\_out\_pl\_api\_m7}}}{\mathrm{SK}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{AD}_{\mathrm{\_Cpl\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{AD\_\_J\_out\_pl\_api}} - v_{\mathrm{AD\_\_J\_ti\_api}}}{\mathrm{AD}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{AD}_{\mathrm{\_Cti\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{AD\_\_J\_ti\_api}}}{\mathrm{AD}_{\mathrm{\_Vti}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{AD}_{\mathrm{\_Cpl\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{AD\_\_J\_out\_pl\_api\_m1}}}{\mathrm{AD}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{AD}_{\mathrm{\_Cpl\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{AD\_\_J\_out\_pl\_api\_m2}}}{\mathrm{AD}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{AD}_{\mathrm{\_Cpl\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{AD\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{AD\_\_J\_out\_pl\_api\_m7}}}{\mathrm{AD}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{BO}_{\mathrm{\_Cpl\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{BO\_\_J\_out\_pl\_api}} - v_{\mathrm{BO\_\_J\_ti\_api}}}{\mathrm{BO}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{BO}_{\mathrm{\_Cti\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{BO\_\_J\_ti\_api}}}{\mathrm{BO}_{\mathrm{\_Vti}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{BO}_{\mathrm{\_Cpl\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{BO\_\_J\_out\_pl\_api\_m1}}}{\mathrm{BO}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{BO}_{\mathrm{\_Cpl\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{BO\_\_J\_out\_pl\_api\_m2}}}{\mathrm{BO}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{BO}_{\mathrm{\_Cpl\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{BO\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{BO\_\_J\_out\_pl\_api\_m7}}}{\mathrm{BO}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GO}_{\mathrm{\_Cpl\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api}} - v_{\mathrm{GO\_\_J\_out\_pl\_api}} - v_{\mathrm{GO\_\_J\_ti\_api}}}{\mathrm{GO}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GO}_{\mathrm{\_Cti\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GO\_\_J\_ti\_api}}}{\mathrm{GO}_{\mathrm{\_Vti}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GO}_{\mathrm{\_Cpl\_api\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api\_m1}} - v_{\mathrm{GO\_\_J\_out\_pl\_api\_m1}}}{\mathrm{GO}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GO}_{\mathrm{\_Cpl\_api\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api\_m2}} - v_{\mathrm{GO\_\_J\_out\_pl\_api\_m2}}}{\mathrm{GO}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GO}_{\mathrm{\_Cpl\_api\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GO\_\_J\_in\_ar\_pl\_api\_m7}} - v_{\mathrm{GO\_\_J\_out\_pl\_api\_m7}}}{\mathrm{GO}_{\mathrm{\_Vpl}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{IVDOSE}_{\mathrm{api}}}{\mathrm{d} t} &= -v_{\mathrm{J\_iv\_api}} \cdot \mathrm{Mr}_{\mathrm{api}} + \mathrm{Ri}_{\mathrm{api}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{PODOSE}_{\mathrm{api}}}{\mathrm{d} t} &= -\mathopen{}\left(v_{\mathrm{GU\_\_J\_po\_api}} + v_{\mathrm{GU\_\_J\_trs\_st\_api}}\right) \cdot \mathrm{Mr}_{\mathrm{api}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{SOLDOSE}_{\mathrm{api}}}{\mathrm{d} t} &= -v_{\mathrm{GU\_\_J\_sol\_api}} \cdot \mathrm{Mr}_{\mathrm{api}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Aabs\_api}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_J\_abs\_du\_api}} + v_{\mathrm{GU\_\_J\_abs\_jej1\_api}} + v_{\mathrm{GU\_\_J\_abs\_jej2\_api}} + v_{\mathrm{GU\_\_J\_abs\_ile1\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_abs\_ile2\_api}} + v_{\mathrm{GU\_\_J\_abs\_cae\_api}} + v_{\mathrm{GU\_\_J\_abs\_asc\_api}} + v_{\mathrm{GU\_\_J\_abs\_tra\_api}} \\
&\quad {} + v_{\mathrm{GU\_\_J\_abs\_des\_api}} + v_{\mathrm{GU\_\_J\_abs\_sig\_api}} + v_{\mathrm{GU\_\_J\_abs\_rec\_api}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_Aapp\_api}}}{\mathrm{d} t} &= \frac{\mathopen{}\left(v_{\mathrm{GU\_\_J\_po\_api}} + v_{\mathrm{GU\_\_J\_trs\_st\_api}}\right) \cdot \mathrm{Mr}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}} + \frac{v_{\mathrm{GU\_\_J\_sol\_api}} \cdot \mathrm{Mr}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}} \qquad \text{(rate rule)}
\end{aligned}
$$
