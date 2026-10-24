# Apixaban body model

Model `apixaban_body`, SBML Level 3 Version 2, read from apixaban\_body.xml, written by sbmlode 0.3.0.

Apixaban body model

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
| $\mathrm{Vre}$ | `Vre` | rest of body |  | l |  |
| $\mathrm{Vgu}$ | `Vgu` | gut |  | l |  |
| $\mathrm{Vki}$ | `Vki` | kidney |  | l |  |
| $\mathrm{Vli}$ | `Vli` | liver |  | l |  |
| $\mathrm{Vlu}$ | `Vlu` | lung |  | l |  |
| $\mathrm{Vve}$ | `Vve` | venous blood |  | l |  |
| $\mathrm{Var}$ | `Var` | arterial blood |  | l |  |
| $\mathrm{Vurine}$ | `Vurine` | urine | $1$ | l | ✓ |
| $\mathrm{Vfeces}$ | `Vfeces` | feces | $1$ | l | ✓ |
| $\mathrm{Vstomach}$ | `Vstomach` | stomach | $1$ | l | ✓ |
| $\mathrm{Vpo}$ | `Vpo` | portal plasma |  | l |  |
| $\mathrm{Vhv}$ | `Vhv` | hepatic venous plasma |  | l |  |
| $\mathrm{Vki}_{\mathrm{tissue}}$ | `Vki_tissue` | ki tissue |  | l |  |
| $\mathrm{Vki}_{\mathrm{plasma}}$ | `Vki_plasma` | ki plasma |  | l |  |
| $\mathrm{Vli}_{\mathrm{tissue}}$ | `Vli_tissue` | li tissue |  | l |  |
| $\mathrm{Vli}_{\mathrm{plasma}}$ | `Vli_plasma` | li plasma |  | l |  |
| $\mathrm{Vlu}_{\mathrm{tissue}}$ | `Vlu_tissue` | lu tissue |  | l |  |
| $\mathrm{Vlu}_{\mathrm{plasma}}$ | `Vlu_plasma` | lu plasma |  | l |  |
| $\mathrm{Vgu}_{\mathrm{tissue}}$ | `Vgu_tissue` | gu tissue |  | l |  |
| $\mathrm{Vgu}_{\mathrm{plasma}}$ | `Vgu_plasma` | gu plasma |  | l |  |
| $\mathrm{Vre}_{\mathrm{tissue}}$ | `Vre_tissue` | re tissue |  | l |  |
| $\mathrm{Vre}_{\mathrm{plasma}}$ | `Vre_plasma` | re plasma |  | l |  |
| $\mathrm{LI}_{\mathrm{\_Vmem}}$ | `LI__Vmem` | membrane | $\mathrm{NaN}$ | m<sup>2</sup> | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vcolon}}$ | `GU__Vcolon` | colon lumen | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vstomach}}$ | `GU__Vstomach` | stomach | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vapical}}$ | `GU__Vapical` | apical membrane (intestinal membrane enterocytes) | $\mathrm{NaN}$ | m<sup>2</sup> | ✓ |

## Species

| Symbol | Id | Name | Compartment | Value | Unit | Properties |
| --- | --- | --- | --- | --- | --- | --- |
| $\mathrm{Cki}_{\mathrm{plasma\_api}}$ | `Cki_plasma_api` | apixaban (kidney plasma) | $\mathrm{Vki}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cli}_{\mathrm{plasma\_api}}$ | `Cli_plasma_api` | apixaban (liver plasma) | $\mathrm{Vli}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{plasma\_api}}$ | `Clu_plasma_api` | apixaban (lung plasma) | $\mathrm{Vlu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cgu}_{\mathrm{plasma\_api}}$ | `Cgu_plasma_api` | apixaban (gut plasma) | $\mathrm{Vgu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{plasma\_api}}$ | `Cre_plasma_api` | apixaban (rest plasma) | $\mathrm{Vre}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Car}_{\mathrm{api}}$ | `Car_api` | apixaban (arterial blood plasma) | $\mathrm{Var}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{api}}$ | `Cve_api` | apixaban (venous blood plasma) | $\mathrm{Vve}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpo}_{\mathrm{api}}$ | `Cpo_api` | apixaban (portal vein plasma) | $\mathrm{Vpo}$ | $0$ | mmol/l | concentration |
| $\mathrm{Chv}_{\mathrm{api}}$ | `Chv_api` | apixaban (hepatic vein plasma) | $\mathrm{Vhv}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{api}}$ | `Clu_api` | apixaban (lung) | $\mathrm{Vlu}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{api}}$ | `Cre_api` | apixaban (rest) | $\mathrm{Vre}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Aurine}_{\mathrm{api}}$ | `Aurine_api` | apixaban (urine) | $\mathrm{Vurine}$ |  | mmol | amount |
| $\mathrm{Afeces}_{\mathrm{api}}$ | `Afeces_api` | apixaban (feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{Cki}_{\mathrm{plasma\_m1}}$ | `Cki_plasma_m1` | M1 (kidney plasma) | $\mathrm{Vki}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cli}_{\mathrm{plasma\_m1}}$ | `Cli_plasma_m1` | M1 (liver plasma) | $\mathrm{Vli}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{plasma\_m1}}$ | `Clu_plasma_m1` | M1 (lung plasma) | $\mathrm{Vlu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cgu}_{\mathrm{plasma\_m1}}$ | `Cgu_plasma_m1` | M1 (gut plasma) | $\mathrm{Vgu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{plasma\_m1}}$ | `Cre_plasma_m1` | M1 (rest plasma) | $\mathrm{Vre}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Car}_{\mathrm{m1}}$ | `Car_m1` | M1 (arterial blood plasma) | $\mathrm{Var}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{m1}}$ | `Cve_m1` | M1 (venous blood plasma) | $\mathrm{Vve}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpo}_{\mathrm{m1}}$ | `Cpo_m1` | M1 (portal vein plasma) | $\mathrm{Vpo}$ | $0$ | mmol/l | concentration |
| $\mathrm{Chv}_{\mathrm{m1}}$ | `Chv_m1` | M1 (hepatic vein plasma) | $\mathrm{Vhv}$ | $0$ | mmol/l | concentration |
| $\mathrm{Aurine}_{\mathrm{m1}}$ | `Aurine_m1` | M1 (urine) | $\mathrm{Vurine}$ |  | mmol | amount |
| $\mathrm{Afeces}_{\mathrm{m1}}$ | `Afeces_m1` | M1 (feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{Cki}_{\mathrm{plasma\_m7}}$ | `Cki_plasma_m7` | M7 (kidney plasma) | $\mathrm{Vki}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cli}_{\mathrm{plasma\_m7}}$ | `Cli_plasma_m7` | M7 (liver plasma) | $\mathrm{Vli}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{plasma\_m7}}$ | `Clu_plasma_m7` | M7 (lung plasma) | $\mathrm{Vlu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cgu}_{\mathrm{plasma\_m7}}$ | `Cgu_plasma_m7` | M7 (gut plasma) | $\mathrm{Vgu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{plasma\_m7}}$ | `Cre_plasma_m7` | M7 (rest plasma) | $\mathrm{Vre}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Car}_{\mathrm{m7}}$ | `Car_m7` | M7 (arterial blood plasma) | $\mathrm{Var}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{m7}}$ | `Cve_m7` | M7 (venous blood plasma) | $\mathrm{Vve}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpo}_{\mathrm{m7}}$ | `Cpo_m7` | M7 (portal vein plasma) | $\mathrm{Vpo}$ | $0$ | mmol/l | concentration |
| $\mathrm{Chv}_{\mathrm{m7}}$ | `Chv_m7` | M7 (hepatic vein plasma) | $\mathrm{Vhv}$ | $0$ | mmol/l | concentration |
| $\mathrm{Aurine}_{\mathrm{m7}}$ | `Aurine_m7` | M7 (urine) | $\mathrm{Vurine}$ |  | mmol | amount |
| $\mathrm{Afeces}_{\mathrm{m7}}$ | `Afeces_m7` | M7 (feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{Afeces}_{\mathrm{m2}}$ | `Afeces_m2` | M2 (feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{Cgu}_{\mathrm{m1}}$ | `Cgu_m1` | M1 (intestinal volume) | $\mathrm{Vgu}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cgu}_{\mathrm{m2}}$ | `Cgu_m2` | M2 (intestinal volume) | $\mathrm{Vgu}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cgu}_{\mathrm{m7}}$ | `Cgu_m7` | M7 (intestinal volume) | $\mathrm{Vgu}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_api}}$ | `LI__api` | apixaban (api) | $\mathrm{Vli}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_m1}}$ | `LI__m1` | M1 (m1) | $\mathrm{Vli}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_m2}}$ | `LI__m2` | M2 (m2) | $\mathrm{Vli}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_m7}}$ | `LI__m7` | M7 (m7) | $\mathrm{Vli}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_api\_stomach}}$ | `GU__api_stomach` | apixaban (api\_stomach) | $\mathrm{GU}_{\mathrm{\_Vstomach}}$ |  | mmol | amount, boundary |
| $\mathrm{GU}_{\mathrm{\_api\_lumen}}$ | `GU__api_lumen` | apixaban (api\_lumen) | $\mathrm{Vgu}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_api\_colon}}$ | `GU__api_colon` | apixaban (api\_colon) | $\mathrm{GU}_{\mathrm{\_Vcolon}}$ |  | mmol | amount |
| $\mathrm{GU}_{\mathrm{\_m1\_colon}}$ | `GU__m1_colon` | M1 (m1\_colon) | $\mathrm{GU}_{\mathrm{\_Vcolon}}$ |  | mmol | amount |
| $\mathrm{GU}_{\mathrm{\_m2\_colon}}$ | `GU__m2_colon` | M2 (m2\_colon) | $\mathrm{GU}_{\mathrm{\_Vcolon}}$ |  | mmol | amount |
| $\mathrm{GU}_{\mathrm{\_m7\_colon}}$ | `GU__m7_colon` | M7 (m7\_colon) | $\mathrm{GU}_{\mathrm{\_Vcolon}}$ |  | mmol | amount |

## Parameters

| Symbol | Id | Name | Value | Unit | Constant |
| --- | --- | --- | --- | --- | :---: |
| $\mathrm{INR}_{\mathrm{ref}}$ | `INR_ref` | INR reference | $1$ | \- | ✓ |
| $\mathrm{PT}_{\mathrm{ref}}$ | `PT_ref` | prothrombin time reference | $12.5$ | s | ✓ |
| $\mathrm{aPTT}_{\mathrm{ref}}$ | `aPTT_ref` | activated partial thromboplastin reference | $28.4$ | s | ✓ |
| $\mathrm{mPT}_{\mathrm{ref}}$ | `mPT_ref` | modified prothrombin time reference | $53.4$ | s | ✓ |
| $\mathrm{INR}$ | `INR` | INR |  | \- |  |
| $\mathrm{PT}$ | `PT` | prothrombin time |  | s |  |
| $\mathrm{aPTT}$ | `aPTT` | activated partial thromboplastin |  | s |  |
| $\mathrm{mPT}$ | `mPT` | modified prothrombin time |  | s |  |
| $\mathrm{antiXa}_{\mathrm{activity}}$ | `antiXa_activity` | anti-FXa activity |  | 1/ml |  |
| $\mathrm{antiXa}_{\mathrm{activity\_gram}}$ | `antiXa_activity_gram` | anti-FXa activity (apixaban calibrated) |  | ng/ml |  |
| $\mathrm{INR}_{\mathrm{change}}$ | `INR_change` | INR change |  | \- |  |
| $\mathrm{INR}_{\mathrm{ratio}}$ | `INR_ratio` | INR ratio |  | \- |  |
| $\mathrm{INR}_{\mathrm{relchange}}$ | `INR_relchange` | INR relative change |  | \- |  |
| $\mathrm{PT}_{\mathrm{change}}$ | `PT_change` | prothrombin time change |  | s |  |
| $\mathrm{PT}_{\mathrm{ratio}}$ | `PT_ratio` | prothrombin time ratio |  | \- |  |
| $\mathrm{PT}_{\mathrm{relchange}}$ | `PT_relchange` | prothrombin time relative change |  | \- |  |
| $\mathrm{aPTT}_{\mathrm{change}}$ | `aPTT_change` | activated partial thromboplastin change |  | s |  |
| $\mathrm{aPTT}_{\mathrm{ratio}}$ | `aPTT_ratio` | activated partial thromboplastin ratio |  | \- |  |
| $\mathrm{aPTT}_{\mathrm{relchange}}$ | `aPTT_relchange` | activated partial thromboplastin relative change |  | \- |  |
| $\mathrm{mPT}_{\mathrm{change}}$ | `mPT_change` | modified prothrombin time change |  | s |  |
| $\mathrm{mPT}_{\mathrm{ratio}}$ | `mPT_ratio` | modified prothrombin time ratio |  | \- |  |
| $\mathrm{mPT}_{\mathrm{relchange}}$ | `mPT_relchange` | modified prothrombin time relative change |  | \- |  |
| $\mathrm{Emax}_{\mathrm{INR}}$ | `Emax_INR` | maximal relative increase of the INR | $1.207017390822$ | \- | ✓ |
| $\mathrm{EC50}_{\mathrm{api\_INR}}$ | `EC50_api_INR` | apixaban concentration of the half-maximal effect on the INR | $0.00198645267620782$ | mmol/l | ✓ |
| $\mathrm{Emax}_{\mathrm{PT}}$ | `Emax_PT` | maximal relative increase of the prothrombin time | $0.29936231741972$ | \- | ✓ |
| $\mathrm{EC50}_{\mathrm{api\_PT}}$ | `EC50_api_PT` | apixaban concentration of the half-maximal effect on the prothrombin time | $0.000172287637749756$ | mmol/l | ✓ |
| $\mathrm{Emax}_{\mathrm{aPTT}}$ | `Emax_aPTT` | maximal relative increase of the activated partial thromboplastin | $0.308173507984222$ | \- | ✓ |
| $\mathrm{EC50}_{\mathrm{api\_aPTT}}$ | `EC50_api_aPTT` | apixaban concentration of the half-maximal effect on the activated partial thromboplastin | $0.000576789947354969$ | mmol/l | ✓ |
| $\mathrm{Emax}_{\mathrm{mPT}}$ | `Emax_mPT` | maximal relative increase of the modified prothrombin time | $5.30233343512346$ | \- | ✓ |
| $\mathrm{EC50}_{\mathrm{api\_mPT}}$ | `EC50_api_mPT` | apixaban concentration of the half-maximal effect on the modified prothrombin time | $0.00169466808872766$ | mmol/l | ✓ |
| $\mathrm{antiXa}_{\mathrm{slope}}$ | `antiXa_slope` | anti-FXa activity per apixaban concentration | $5728.15077902583$ | l/ml/mmol | ✓ |
| $\mathrm{antiXa}_{\mathrm{gram\_slope}}$ | `antiXa_gram_slope` | anti-FXa activity (apixaban calibrated) per apixaban concentration | $420605.759397863$ | ng·l/ml/mmol | ✓ |
| $\mathrm{BW}$ | `BW` | body weight \[kg\] | $75$ | kg | ✓ |
| $\mathrm{BW}_{\mathrm{ref}}$ | `BW_ref` | reference body weight \[kg\] | $75$ | kg | ✓ |
| $\mathrm{HEIGHT}_{\mathrm{ref}}$ | `HEIGHT_ref` | reference height \[cm\] | $170$ | cm | ✓ |
| $\mathrm{BSA}_{\mathrm{ref}}$ | `BSA_ref` | reference body surface area \[m^2\] |  | m<sup>2</sup> |  |
| $\mathrm{HEIGHT}$ | `HEIGHT` | height \[cm\] | $170$ | cm | ✓ |
| $\mathrm{BSA}$ | `BSA` | body surface area \[m^2\] |  | m<sup>2</sup> |  |
| $\mathrm{COBW}$ | `COBW` | cardiac output per bodyweight \[ml/s/kg\] | $1.548$ | ml/s/kg | ✓ |
| $f_{\mathrm{cardiac\_function}}$ | `f_cardiac_function` | heart function | $1$ | \- |  |
| $\mathrm{CO}$ | `CO` | cardiac output \[ml/s\] |  | ml/s |  |
| $\mathrm{QC}$ | `QC` | cardiac output \[l/min\] |  | l/min |  |
| $\mathrm{Fblood}$ | `Fblood` | blood fraction of organ volume | $0.02$ | \- |  |
| $\mathrm{HCT}$ | `HCT` | hematocrit | $0.51$ | \- | ✓ |
| $\mathrm{FVgu}$ | `FVgu` | gut fractional tissue volume | $0.0171$ | l/kg | ✓ |
| $\mathrm{FVki}$ | `FVki` | kidney fractional tissue volume | $0.0044$ | l/kg | ✓ |
| $\mathrm{FVli}$ | `FVli` | liver fractional tissue volume | $0.021$ | l/kg | ✓ |
| $\mathrm{FVlu}$ | `FVlu` | lung fractional tissue volume | $0.0076$ | l/kg | ✓ |
| $\mathrm{FVre}$ | `FVre` | rest of body fractional tissue volume |  | l/kg |  |
| $\mathrm{FVve}$ | `FVve` | venous fractional tissue volume | $0.0514$ | l/kg | ✓ |
| $\mathrm{FVar}$ | `FVar` | arterial fractional tissue volume | $0.0257$ | l/kg | ✓ |
| $\mathrm{FVpo}$ | `FVpo` | portal fractional tissue volume | $0.001$ | l/kg | ✓ |
| $\mathrm{FVhv}$ | `FVhv` | hepatic venous fractional tissue volume | $0.001$ | l/kg | ✓ |
| $\mathrm{FQgu}$ | `FQgu` | gut fractional tissue blood flow | $0.18$ | \- | ✓ |
| $\mathrm{FQki}$ | `FQki` | kidney fractional tissue blood flow | $0.19$ | \- | ✓ |
| $\mathrm{FQh}$ | `FQh` | hepatic (venous side) fractional tissue blood flow | $0.215$ | \- | ✓ |
| $\mathrm{FQlu}$ | `FQlu` | lung fractional tissue blood flow | $1$ | \- | ✓ |
| $\mathrm{FQre}$ | `FQre` | rest of body fractional tissue blood flow |  | \- |  |
| $f_{\mathrm{cirrhosis}}$ | `f_cirrhosis` | severity of cirrhosis \[0, 0.95\] | $0$ | \- | ✓ |
| $f_{\mathrm{shunts}}$ | `f_shunts` | fraction of portal venous blood shunted by the liver |  | \- |  |
| $f_{\mathrm{tissue\_loss}}$ | `f_tissue_loss` | fraction of lost parenchymal liver volume |  | \- |  |
| $\mathrm{PODOSE}_{\mathrm{api}}$ | `PODOSE_api` | oral dose api in tablet \[mg\] | $0$ | mg |  |
| $\mathrm{SOLDOSE}_{\mathrm{api}}$ | `SOLDOSE_api` | oral dose api in solution \[mg\] | $0$ | mg |  |
| $\mathrm{Mr}_{\mathrm{api}}$ | `Mr_api` | Molecular weight api \[g/mole\] | $459.5$ | g/mol | ✓ |
| $\mathrm{ftissue}_{\mathrm{api}}$ | `ftissue_api` | tissue distribution api | $4.89531575905584$ | l/min | ✓ |
| $\mathrm{Kp}_{\mathrm{api}}$ | `Kp_api` | tissue/unbound plasma partition coefficient (Kp,u) api | $1.39938738915569$ | \- | ✓ |
| $\mathrm{fu}_{\mathrm{api}}$ | `fu_api` | fraction unbound in plasma api | $0.131$ | \- | ✓ |
| $\mathrm{IVDOSE}_{\mathrm{api}}$ | `IVDOSE_api` | IV bolus dose api \[mg\] | $0$ | mg |  |
| $\mathrm{ti}_{\mathrm{api}}$ | `ti_api` | injection time api \[s\] | $10$ | s | ✓ |
| $\mathrm{Ki}_{\mathrm{api}}$ | `Ki_api` | Ki \[1/min\] injection api |  | 1/min |  |
| $\mathrm{Ri}_{\mathrm{api}}$ | `Ri_api` | Ri \[mg/min\] rate of infusion api | $0$ | mg/min | ✓ |
| $\mathrm{Mr}_{\mathrm{m1}}$ | `Mr_m1` | Molecular weight m1 \[g/mole\] | $525.5$ | g/mol | ✓ |
| $\mathrm{Mr}_{\mathrm{m7}}$ | `Mr_m7` | Molecular weight m7 \[g/mole\] | $475.5$ | g/mol | ✓ |
| $\mathrm{Cki}_{\mathrm{free\_api}}$ | `Cki_free_api` | apixaban free concentration (kidney) |  | mmol/l |  |
| $\mathrm{Cli}_{\mathrm{free\_api}}$ | `Cli_free_api` | apixaban free concentration (liver) |  | mmol/l |  |
| $\mathrm{Clu}_{\mathrm{free\_api}}$ | `Clu_free_api` | apixaban free concentration (lung) |  | mmol/l |  |
| $\mathrm{Cgu}_{\mathrm{free\_api}}$ | `Cgu_free_api` | apixaban free concentration (gut) |  | mmol/l |  |
| $\mathrm{Cre}_{\mathrm{free\_api}}$ | `Cre_free_api` | apixaban free concentration (rest) |  | mmol/l |  |
| $\mathrm{Car}_{\mathrm{free\_api}}$ | `Car_free_api` | apixaban free concentration (arterial blood) |  | mmol/l |  |
| $\mathrm{Cve}_{\mathrm{free\_api}}$ | `Cve_free_api` | apixaban free concentration (venous blood) |  | mmol/l |  |
| $\mathrm{Cpo}_{\mathrm{free\_api}}$ | `Cpo_free_api` | apixaban free concentration (portal vein) |  | mmol/l |  |
| $\mathrm{Chv}_{\mathrm{free\_api}}$ | `Chv_free_api` | apixaban free concentration (hepatic vein) |  | mmol/l |  |
| $\mathrm{Qgu}$ | `Qgu` | gut blood flow |  | l/min |  |
| $\mathrm{Qki}$ | `Qki` | kidney blood flow |  | l/min |  |
| $\mathrm{Qh}$ | `Qh` | hepatic (venous side) blood flow |  | l/min |  |
| $\mathrm{Qha}$ | `Qha` | hepatic artery blood flow |  | l/min |  |
| $\mathrm{Qlu}$ | `Qlu` | lung blood flow |  | l/min |  |
| $\mathrm{Qre}$ | `Qre` | rest of body blood flow |  | l/min |  |
| $\mathrm{Qpo}$ | `Qpo` | portal blood flow |  | l/min |  |
| $\mathrm{KI}_{\mathrm{\_f\_renal\_function}}$ | `KI__f_renal_function` | renal function | $1$ | \- | ✓ |
| $\mathrm{KI}_{\mathrm{\_GFR\_base}}$ | `KI__GFR_base` | glomerular filtration rate (healthy) | $101$ | ml/min | ✓ |
| $\mathrm{KI}_{\mathrm{\_APIEX\_f}}$ | `KI__APIEX_f` | renal clearance of unbound apixaban relative to the GFR | $1.01497104264872$ | \- | ✓ |
| $\mathrm{KI}_{\mathrm{\_M1EX\_f}}$ | `KI__M1EX_f` | renal clearance of M1 relative to the GFR | $0.0459801360234629$ | \- | ✓ |
| $\mathrm{KI}_{\mathrm{\_M7EX\_f}}$ | `KI__M7EX_f` | renal clearance of M7 relative to the GFR | $0.0141866056661887$ | \- | ✓ |
| $\mathrm{KI}_{\mathrm{\_GFR}}$ | `KI__GFR` | glomerular filtration rate |  | ml/min |  |
| $\mathrm{LI}_{\mathrm{\_API2M\_k}}$ | `LI__API2M_k` | rate of the CYP3A4 metabolism of apixaban | $0.0875891081052202$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_f\_m2}}$ | `LI__f_m2` | fraction of the CYP3A4 metabolism to M2 | $0.78$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_f\_cyp3a4}}$ | `LI__f_cyp3a4` | CYP3A4 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_MXEXBI\_k}}$ | `LI__MXEXBI_k` | rate of the biliary excretion of the apixaban metabolites | $0.00245100330106179$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_APIIM\_k}}$ | `LI__APIIM_k` | rate apixaban import | $1000$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_M22M1\_k}}$ | `LI__M22M1_k` | rate of the sulfation M2 -&gt; M1 | $0.00049319446956451$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_M1EX\_k}}$ | `LI__M1EX_k` | rate M1 export | $1000$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_M7EX\_k}}$ | `LI__M7EX_k` | rate M7 export | $1000$ | 1/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_APIABS\_k}}$ | `GU__APIABS_k` | rate of apixaban absorption | $0.0185164315331011$ | 1/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_SITRANS\_k}}$ | `GU__SITRANS_k` | rate of the small intestinal transit | $0.00735101034145177$ | 1/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_LUMEX\_k}}$ | `GU__LUMEX_k` | rate of the fecal transit | $0.000555555555555556$ | 1/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_APISEC\_k}}$ | `GU__APISEC_k` | intestinal secretion clearance of unbound apixaban | $0.426931317033668$ | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_pgp}}$ | `GU__f_pgp` | P-gp/BCRP activity | $1$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_Ka\_dis\_api}}$ | `GU__Ka_dis_api` | Ka\_dis \[1/hr\] dissolution apixaban in tablet | $1.62989766741564$ | 1/hr | ✓ |
| $\mathrm{GU}_{\mathrm{\_PODOSE\_50}}$ | `GU__PODOSE_50` | undissolved dose of half-maximal dissolution \[mg\] | $5.74095936453337$ | mg | ✓ |
| $\mathrm{GU}_{\mathrm{\_Ka\_sol\_api}}$ | `GU__Ka_sol_api` | Ka\_sol \[1/hr\] transport apixaban in solution | $6.40581223519076$ | 1/hr | ✓ |
| $\mathrm{GU}_{\mathrm{\_F\_api\_abs}}$ | `GU__F_api_abs` | fraction absorbed apixaban |  | \- |  |

## Initial assignments and assignment rules

The initial assignments set the values at $t = 0$:

$$
\begin{aligned}
\mathrm{Aurine}_{\mathrm{api}} &= 0 \cdot \mathrm{Vurine} \\[1ex]
\mathrm{Afeces}_{\mathrm{api}} &= 0 \cdot \mathrm{Vfeces} \\[1ex]
\mathrm{Aurine}_{\mathrm{m1}} &= 0 \cdot \mathrm{Vurine} \\[1ex]
\mathrm{Afeces}_{\mathrm{m1}} &= 0 \cdot \mathrm{Vfeces} \\[1ex]
\mathrm{Aurine}_{\mathrm{m7}} &= 0 \cdot \mathrm{Vurine} \\[1ex]
\mathrm{Afeces}_{\mathrm{m7}} &= 0 \cdot \mathrm{Vfeces} \\[1ex]
\mathrm{Afeces}_{\mathrm{m2}} &= 0 \cdot \mathrm{Vfeces} \\[1ex]
\mathrm{GU}_{\mathrm{\_api\_stomach}} &= 0 \cdot \mathrm{GU}_{\mathrm{\_Vstomach}} \\[1ex]
\mathrm{GU}_{\mathrm{\_api\_colon}} &= 0 \cdot \mathrm{GU}_{\mathrm{\_Vcolon}} \\[1ex]
\mathrm{GU}_{\mathrm{\_m1\_colon}} &= 0 \cdot \mathrm{GU}_{\mathrm{\_Vcolon}} \\[1ex]
\mathrm{GU}_{\mathrm{\_m2\_colon}} &= 0 \cdot \mathrm{GU}_{\mathrm{\_Vcolon}} \\[1ex]
\mathrm{GU}_{\mathrm{\_m7\_colon}} &= 0 \cdot \mathrm{GU}_{\mathrm{\_Vcolon}}
\end{aligned}
$$

The assignment rules hold at every time $t$:

$$
\begin{aligned}
\mathrm{INR} &= \mathrm{INR}_{\mathrm{ref}} \cdot \mathopen{}\left(1 + \frac{\mathrm{Emax}_{\mathrm{INR}} \cdot \mathrm{Cve}_{\mathrm{api}}}{\mathrm{Cve}_{\mathrm{api}} + \mathrm{EC50}_{\mathrm{api\_INR}}}\right) \\[1ex]
\mathrm{INR}_{\mathrm{change}} &= \mathrm{INR} - \mathrm{INR}_{\mathrm{ref}} \\[1ex]
\mathrm{INR}_{\mathrm{ratio}} &= \frac{\mathrm{INR}}{\mathrm{INR}_{\mathrm{ref}}} \\[1ex]
\mathrm{INR}_{\mathrm{relchange}} &= \frac{\mathrm{INR} - \mathrm{INR}_{\mathrm{ref}}}{\mathrm{INR}_{\mathrm{ref}}} \\[1ex]
\mathrm{PT} &= \mathrm{PT}_{\mathrm{ref}} \cdot \mathopen{}\left(1 + \frac{\mathrm{Emax}_{\mathrm{PT}} \cdot \mathrm{Cve}_{\mathrm{api}}}{\mathrm{Cve}_{\mathrm{api}} + \mathrm{EC50}_{\mathrm{api\_PT}}}\right) \\[1ex]
\mathrm{PT}_{\mathrm{change}} &= \mathrm{PT} - \mathrm{PT}_{\mathrm{ref}} \\[1ex]
\mathrm{PT}_{\mathrm{ratio}} &= \frac{\mathrm{PT}}{\mathrm{PT}_{\mathrm{ref}}} \\[1ex]
\mathrm{PT}_{\mathrm{relchange}} &= \frac{\mathrm{PT} - \mathrm{PT}_{\mathrm{ref}}}{\mathrm{PT}_{\mathrm{ref}}} \\[1ex]
\mathrm{aPTT} &= \mathrm{aPTT}_{\mathrm{ref}} \cdot \mathopen{}\left(1 + \frac{\mathrm{Emax}_{\mathrm{aPTT}} \cdot \mathrm{Cve}_{\mathrm{api}}}{\mathrm{Cve}_{\mathrm{api}} + \mathrm{EC50}_{\mathrm{api\_aPTT}}}\right) \\[1ex]
\mathrm{aPTT}_{\mathrm{change}} &= \mathrm{aPTT} - \mathrm{aPTT}_{\mathrm{ref}} \\[1ex]
\mathrm{aPTT}_{\mathrm{ratio}} &= \frac{\mathrm{aPTT}}{\mathrm{aPTT}_{\mathrm{ref}}} \\[1ex]
\mathrm{aPTT}_{\mathrm{relchange}} &= \frac{\mathrm{aPTT} - \mathrm{aPTT}_{\mathrm{ref}}}{\mathrm{aPTT}_{\mathrm{ref}}} \\[1ex]
\mathrm{mPT} &= \mathrm{mPT}_{\mathrm{ref}} \cdot \mathopen{}\left(1 + \frac{\mathrm{Emax}_{\mathrm{mPT}} \cdot \mathrm{Cve}_{\mathrm{api}}}{\mathrm{Cve}_{\mathrm{api}} + \mathrm{EC50}_{\mathrm{api\_mPT}}}\right) \\[1ex]
\mathrm{mPT}_{\mathrm{change}} &= \mathrm{mPT} - \mathrm{mPT}_{\mathrm{ref}} \\[1ex]
\mathrm{mPT}_{\mathrm{ratio}} &= \frac{\mathrm{mPT}}{\mathrm{mPT}_{\mathrm{ref}}} \\[1ex]
\mathrm{mPT}_{\mathrm{relchange}} &= \frac{\mathrm{mPT} - \mathrm{mPT}_{\mathrm{ref}}}{\mathrm{mPT}_{\mathrm{ref}}} \\[1ex]
\mathrm{antiXa}_{\mathrm{activity}} &= \mathrm{antiXa}_{\mathrm{slope}} \cdot \mathrm{Cve}_{\mathrm{api}} \\[1ex]
\mathrm{antiXa}_{\mathrm{activity\_gram}} &= \mathrm{antiXa}_{\mathrm{gram\_slope}} \cdot \mathrm{Cve}_{\mathrm{api}} \\[1ex]
f_{\mathrm{shunts}} &= f_{\mathrm{cirrhosis}} \\[1ex]
f_{\mathrm{tissue\_loss}} &= f_{\mathrm{cirrhosis}} \\[1ex]
\mathrm{Cki}_{\mathrm{free\_api}} &= \mathrm{Cki}_{\mathrm{plasma\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \\[1ex]
\mathrm{Cli}_{\mathrm{free\_api}} &= \mathrm{Cli}_{\mathrm{plasma\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \\[1ex]
\mathrm{Clu}_{\mathrm{free\_api}} &= \mathrm{Clu}_{\mathrm{plasma\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \\[1ex]
\mathrm{Cgu}_{\mathrm{free\_api}} &= \mathrm{Cgu}_{\mathrm{plasma\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \\[1ex]
\mathrm{Cre}_{\mathrm{free\_api}} &= \mathrm{Cre}_{\mathrm{plasma\_api}} \cdot \mathrm{fu}_{\mathrm{api}} \\[1ex]
\mathrm{Car}_{\mathrm{free\_api}} &= \mathrm{Car}_{\mathrm{api}} \cdot \mathrm{fu}_{\mathrm{api}} \\[1ex]
\mathrm{Cve}_{\mathrm{free\_api}} &= \mathrm{Cve}_{\mathrm{api}} \cdot \mathrm{fu}_{\mathrm{api}} \\[1ex]
\mathrm{Cpo}_{\mathrm{free\_api}} &= \mathrm{Cpo}_{\mathrm{api}} \cdot \mathrm{fu}_{\mathrm{api}} \\[1ex]
\mathrm{Chv}_{\mathrm{free\_api}} &= \mathrm{Chv}_{\mathrm{api}} \cdot \mathrm{fu}_{\mathrm{api}} \\[1ex]
\mathrm{FVre} &= 1 - \mathrm{FVgu} - \mathrm{FVki} - \mathrm{FVli} \\
&\quad {} - \mathrm{FVlu} - \mathrm{FVve} - \mathrm{FVar} \\[1ex]
\mathrm{FQre} &= 1 - \mathrm{FQki} - \mathrm{FQh} \\[1ex]
\mathrm{BSA} &= 0.024265 \cdot \mathopen{}\left(\frac{\mathrm{BW}}{1}\right)^{0.5378} \cdot \mathopen{}\left(\frac{\mathrm{HEIGHT}}{1}\right)^{0.3964} \\[1ex]
\mathrm{BSA}_{\mathrm{ref}} &= 0.024265 \cdot \mathopen{}\left(\frac{\mathrm{BW}_{\mathrm{ref}}}{1}\right)^{0.5378} \cdot \mathopen{}\left(\frac{\mathrm{HEIGHT}_{\mathrm{ref}}}{1}\right)^{0.3964} \\[1ex]
\mathrm{CO} &= f_{\mathrm{cardiac\_function}} \cdot \mathrm{BW} \cdot \mathrm{COBW} \\[1ex]
\mathrm{QC} &= \frac{\mathrm{CO}}{1000} \cdot 60 \\[1ex]
\mathrm{Vgu} &= \mathrm{BW} \cdot \mathrm{FVgu} \\[1ex]
\mathrm{Vki} &= \mathrm{BW} \cdot \mathrm{FVki} \\[1ex]
\mathrm{Vli} &= \frac{\mathrm{BW}_{\mathrm{ref}} \cdot \mathrm{FVli} \cdot \mathrm{BSA}}{\mathrm{BSA}_{\mathrm{ref}}} \\[1ex]
\mathrm{Vlu} &= \mathrm{BW} \cdot \mathrm{FVlu} \\[1ex]
\mathrm{Vre} &= \mathrm{BW} \cdot \mathopen{}\left(\mathrm{FVre} + \mathrm{FVli}\right) - \mathrm{Vli} \\[1ex]
\mathrm{Vve} &= \mathrm{BW} \cdot \mathrm{FVve} - \frac{\mathrm{FVve}}{\mathrm{FVar} + \mathrm{FVve}} \cdot \mathrm{BW} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{FVve} - \mathrm{FVar}\right) \\[1ex]
\mathrm{Var} &= \mathrm{BW} \cdot \mathrm{FVar} - \frac{\mathrm{FVar}}{\mathrm{FVar} + \mathrm{FVve}} \cdot \mathrm{BW} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{FVve} - \mathrm{FVar}\right) \\[1ex]
\mathrm{Vpo} &= \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathopen{}\left(\mathrm{BW} \cdot \mathrm{FVpo} - \frac{\mathrm{FVpo}}{\mathrm{FVar} + \mathrm{FVve} + \mathrm{FVpo} + \mathrm{FVhv}} \cdot \mathrm{BW} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{FVar} - \mathrm{FVve} - \mathrm{FVpo} - \mathrm{FVhv}\right)\right) \\[1ex]
\mathrm{Vhv} &= \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathopen{}\left(\mathrm{BW} \cdot \mathrm{FVhv} - \frac{\mathrm{FVhv}}{\mathrm{FVar} + \mathrm{FVve} + \mathrm{FVpo} + \mathrm{FVhv}} \cdot \mathrm{BW} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{FVar} - \mathrm{FVve} - \mathrm{FVpo} - \mathrm{FVhv}\right)\right) \\[1ex]
\mathrm{Qgu} &= \mathrm{QC} \cdot \mathrm{FQgu} \\[1ex]
\mathrm{Qki} &= \mathrm{QC} \cdot \mathrm{FQki} \\[1ex]
\mathrm{Qh} &= \mathrm{QC} \cdot \mathrm{FQh} \\[1ex]
\mathrm{Qha} &= \mathrm{Qh} - \mathrm{Qgu} \\[1ex]
\mathrm{Qlu} &= \mathrm{QC} \cdot \mathrm{FQlu} \\[1ex]
\mathrm{Qre} &= \mathrm{QC} \cdot \mathrm{FQre} \\[1ex]
\mathrm{Qpo} &= \mathrm{Qgu} \\[1ex]
\mathrm{Vki}_{\mathrm{plasma}} &= \mathrm{Vki} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{Vki}_{\mathrm{tissue}} &= \mathrm{Vki} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Vli}_{\mathrm{plasma}} &= \mathrm{Vli} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{Vli}_{\mathrm{tissue}} &= \mathrm{Vli} \cdot \mathopen{}\left(1 - f_{\mathrm{tissue\_loss}}\right) \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Vlu}_{\mathrm{plasma}} &= \mathrm{Vlu} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{Vlu}_{\mathrm{tissue}} &= \mathrm{Vlu} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Vgu}_{\mathrm{plasma}} &= \mathrm{Vgu} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{Vgu}_{\mathrm{tissue}} &= \mathrm{Vgu} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Vre}_{\mathrm{plasma}} &= \mathrm{Vre} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{Vre}_{\mathrm{tissue}} &= \mathrm{Vre} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Ki}_{\mathrm{api}} &= \frac{0.693}{\mathrm{ti}_{\mathrm{api}}} \cdot 60 \\[1ex]
\mathrm{KI}_{\mathrm{\_GFR}} &= \mathrm{KI}_{\mathrm{\_f\_renal\_function}} \cdot \mathrm{KI}_{\mathrm{\_GFR\_base}} \\[1ex]
\mathrm{GU}_{\mathrm{\_F\_api\_abs}} &= \frac{\mathrm{GU}_{\mathrm{\_APIABS\_k}}}{\mathrm{GU}_{\mathrm{\_APIABS\_k}} + \mathrm{GU}_{\mathrm{\_SITRANS\_k}}}
\end{aligned}
$$

## Reactions

| Rate | Id | Name | Equation |
| --- | --- | --- | --- |
| $v_{\mathrm{transport\_lu\_api}}$ | `transport_lu_api` | transport apixaban | $\mathrm{Clu}_{\mathrm{plasma\_api}} \rightleftharpoons \mathrm{Clu}_{\mathrm{api}}$ |
| $v_{\mathrm{transport\_re\_api}}$ | `transport_re_api` | transport apixaban | $\mathrm{Cre}_{\mathrm{plasma\_api}} \rightleftharpoons \mathrm{Cre}_{\mathrm{api}}$ |
| $v_{\mathrm{iv\_api}}$ | `iv_api` | iv apixaban | $\varnothing \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |
| $v_{\mathrm{Flow\_ar\_ki\_api}}$ | `Flow_ar_ki_api` | inflow kidney apixaban | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{Cki}_{\mathrm{plasma\_api}}$ |
| $v_{\mathrm{Flow\_ki\_ve\_api}}$ | `Flow_ki_ve_api` | outflow kidney apixaban | $\mathrm{Cki}_{\mathrm{plasma\_api}} \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |
| $v_{\mathrm{Flow\_arli\_li\_api}}$ | `Flow_arli_li_api` | arterial inflow liver apixaban | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_api}}$ |
| $v_{\mathrm{Flow\_arli\_hv\_api}}$ | `Flow_arli_hv_api` | flow arterial shunts | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{Chv}_{\mathrm{api}}$ |
| $v_{\mathrm{Flow\_po\_li\_api}}$ | `Flow_po_li_api` | outflow po apixaban | $\mathrm{Cpo}_{\mathrm{api}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_api}}$ |
| $v_{\mathrm{Flow\_po\_hv\_api}}$ | `Flow_po_hv_api` | flow portal shunts | $\mathrm{Cpo}_{\mathrm{api}} \longrightarrow \mathrm{Chv}_{\mathrm{api}}$ |
| $v_{\mathrm{Flow\_li\_hv\_api}}$ | `Flow_li_hv_api` | outflow liver apixaban | $\mathrm{Cli}_{\mathrm{plasma\_api}} \longrightarrow \mathrm{Chv}_{\mathrm{api}}$ |
| $v_{\mathrm{Flow\_hv\_ve\_api}}$ | `Flow_hv_ve_api` | outflow hepatic vein apixaban | $\mathrm{Chv}_{\mathrm{api}} \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |
| $v_{\mathrm{Flow\_ve\_lu\_api}}$ | `Flow_ve_lu_api` | inflow lung apixaban | $\mathrm{Cve}_{\mathrm{api}} \longrightarrow \mathrm{Clu}_{\mathrm{plasma\_api}}$ |
| $v_{\mathrm{Flow\_lu\_ar\_api}}$ | `Flow_lu_ar_api` | outflow lung apixaban | $\mathrm{Clu}_{\mathrm{plasma\_api}} \longrightarrow \mathrm{Car}_{\mathrm{api}}$ |
| $v_{\mathrm{Flow\_ar\_gu\_api}}$ | `Flow_ar_gu_api` | inflow gut apixaban | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{Cgu}_{\mathrm{plasma\_api}}$ |
| $v_{\mathrm{Flow\_gu\_po\_api}}$ | `Flow_gu_po_api` | outflow gut apixaban | $\mathrm{Cgu}_{\mathrm{plasma\_api}} \longrightarrow \mathrm{Cpo}_{\mathrm{api}}$ |
| $v_{\mathrm{Flow\_ar\_re\_api}}$ | `Flow_ar_re_api` | inflow rest apixaban | $\mathrm{Car}_{\mathrm{api}} \longrightarrow \mathrm{Cre}_{\mathrm{plasma\_api}}$ |
| $v_{\mathrm{Flow\_re\_ve\_api}}$ | `Flow_re_ve_api` | outflow rest apixaban | $\mathrm{Cre}_{\mathrm{plasma\_api}} \longrightarrow \mathrm{Cve}_{\mathrm{api}}$ |
| $v_{\mathrm{Flow\_ar\_ki\_m1}}$ | `Flow_ar_ki_m1` | inflow kidney M1 | $\mathrm{Car}_{\mathrm{m1}} \longrightarrow \mathrm{Cki}_{\mathrm{plasma\_m1}}$ |
| $v_{\mathrm{Flow\_ki\_ve\_m1}}$ | `Flow_ki_ve_m1` | outflow kidney M1 | $\mathrm{Cki}_{\mathrm{plasma\_m1}} \longrightarrow \mathrm{Cve}_{\mathrm{m1}}$ |
| $v_{\mathrm{Flow\_arli\_li\_m1}}$ | `Flow_arli_li_m1` | arterial inflow liver M1 | $\mathrm{Car}_{\mathrm{m1}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_m1}}$ |
| $v_{\mathrm{Flow\_arli\_hv\_m1}}$ | `Flow_arli_hv_m1` | flow arterial shunts | $\mathrm{Car}_{\mathrm{m1}} \longrightarrow \mathrm{Chv}_{\mathrm{m1}}$ |
| $v_{\mathrm{Flow\_po\_li\_m1}}$ | `Flow_po_li_m1` | outflow po M1 | $\mathrm{Cpo}_{\mathrm{m1}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_m1}}$ |
| $v_{\mathrm{Flow\_po\_hv\_m1}}$ | `Flow_po_hv_m1` | flow portal shunts | $\mathrm{Cpo}_{\mathrm{m1}} \longrightarrow \mathrm{Chv}_{\mathrm{m1}}$ |
| $v_{\mathrm{Flow\_li\_hv\_m1}}$ | `Flow_li_hv_m1` | outflow liver M1 | $\mathrm{Cli}_{\mathrm{plasma\_m1}} \longrightarrow \mathrm{Chv}_{\mathrm{m1}}$ |
| $v_{\mathrm{Flow\_hv\_ve\_m1}}$ | `Flow_hv_ve_m1` | outflow hepatic vein M1 | $\mathrm{Chv}_{\mathrm{m1}} \longrightarrow \mathrm{Cve}_{\mathrm{m1}}$ |
| $v_{\mathrm{Flow\_ve\_lu\_m1}}$ | `Flow_ve_lu_m1` | inflow lung M1 | $\mathrm{Cve}_{\mathrm{m1}} \longrightarrow \mathrm{Clu}_{\mathrm{plasma\_m1}}$ |
| $v_{\mathrm{Flow\_lu\_ar\_m1}}$ | `Flow_lu_ar_m1` | outflow lung M1 | $\mathrm{Clu}_{\mathrm{plasma\_m1}} \longrightarrow \mathrm{Car}_{\mathrm{m1}}$ |
| $v_{\mathrm{Flow\_ar\_gu\_m1}}$ | `Flow_ar_gu_m1` | inflow gut M1 | $\mathrm{Car}_{\mathrm{m1}} \longrightarrow \mathrm{Cgu}_{\mathrm{plasma\_m1}}$ |
| $v_{\mathrm{Flow\_gu\_po\_m1}}$ | `Flow_gu_po_m1` | outflow gut M1 | $\mathrm{Cgu}_{\mathrm{plasma\_m1}} \longrightarrow \mathrm{Cpo}_{\mathrm{m1}}$ |
| $v_{\mathrm{Flow\_ar\_re\_m1}}$ | `Flow_ar_re_m1` | inflow rest M1 | $\mathrm{Car}_{\mathrm{m1}} \longrightarrow \mathrm{Cre}_{\mathrm{plasma\_m1}}$ |
| $v_{\mathrm{Flow\_re\_ve\_m1}}$ | `Flow_re_ve_m1` | outflow rest M1 | $\mathrm{Cre}_{\mathrm{plasma\_m1}} \longrightarrow \mathrm{Cve}_{\mathrm{m1}}$ |
| $v_{\mathrm{Flow\_ar\_ki\_m7}}$ | `Flow_ar_ki_m7` | inflow kidney M7 | $\mathrm{Car}_{\mathrm{m7}} \longrightarrow \mathrm{Cki}_{\mathrm{plasma\_m7}}$ |
| $v_{\mathrm{Flow\_ki\_ve\_m7}}$ | `Flow_ki_ve_m7` | outflow kidney M7 | $\mathrm{Cki}_{\mathrm{plasma\_m7}} \longrightarrow \mathrm{Cve}_{\mathrm{m7}}$ |
| $v_{\mathrm{Flow\_arli\_li\_m7}}$ | `Flow_arli_li_m7` | arterial inflow liver M7 | $\mathrm{Car}_{\mathrm{m7}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_m7}}$ |
| $v_{\mathrm{Flow\_arli\_hv\_m7}}$ | `Flow_arli_hv_m7` | flow arterial shunts | $\mathrm{Car}_{\mathrm{m7}} \longrightarrow \mathrm{Chv}_{\mathrm{m7}}$ |
| $v_{\mathrm{Flow\_po\_li\_m7}}$ | `Flow_po_li_m7` | outflow po M7 | $\mathrm{Cpo}_{\mathrm{m7}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_m7}}$ |
| $v_{\mathrm{Flow\_po\_hv\_m7}}$ | `Flow_po_hv_m7` | flow portal shunts | $\mathrm{Cpo}_{\mathrm{m7}} \longrightarrow \mathrm{Chv}_{\mathrm{m7}}$ |
| $v_{\mathrm{Flow\_li\_hv\_m7}}$ | `Flow_li_hv_m7` | outflow liver M7 | $\mathrm{Cli}_{\mathrm{plasma\_m7}} \longrightarrow \mathrm{Chv}_{\mathrm{m7}}$ |
| $v_{\mathrm{Flow\_hv\_ve\_m7}}$ | `Flow_hv_ve_m7` | outflow hepatic vein M7 | $\mathrm{Chv}_{\mathrm{m7}} \longrightarrow \mathrm{Cve}_{\mathrm{m7}}$ |
| $v_{\mathrm{Flow\_ve\_lu\_m7}}$ | `Flow_ve_lu_m7` | inflow lung M7 | $\mathrm{Cve}_{\mathrm{m7}} \longrightarrow \mathrm{Clu}_{\mathrm{plasma\_m7}}$ |
| $v_{\mathrm{Flow\_lu\_ar\_m7}}$ | `Flow_lu_ar_m7` | outflow lung M7 | $\mathrm{Clu}_{\mathrm{plasma\_m7}} \longrightarrow \mathrm{Car}_{\mathrm{m7}}$ |
| $v_{\mathrm{Flow\_ar\_gu\_m7}}$ | `Flow_ar_gu_m7` | inflow gut M7 | $\mathrm{Car}_{\mathrm{m7}} \longrightarrow \mathrm{Cgu}_{\mathrm{plasma\_m7}}$ |
| $v_{\mathrm{Flow\_gu\_po\_m7}}$ | `Flow_gu_po_m7` | outflow gut M7 | $\mathrm{Cgu}_{\mathrm{plasma\_m7}} \longrightarrow \mathrm{Cpo}_{\mathrm{m7}}$ |
| $v_{\mathrm{Flow\_ar\_re\_m7}}$ | `Flow_ar_re_m7` | inflow rest M7 | $\mathrm{Car}_{\mathrm{m7}} \longrightarrow \mathrm{Cre}_{\mathrm{plasma\_m7}}$ |
| $v_{\mathrm{Flow\_re\_ve\_m7}}$ | `Flow_re_ve_m7` | outflow rest M7 | $\mathrm{Cre}_{\mathrm{plasma\_m7}} \longrightarrow \mathrm{Cve}_{\mathrm{m7}}$ |
| $v_{\mathrm{KI\_\_APIEX}}$ | `KI__APIEX` | excretion apixaban (APIEX) | $\mathrm{Cki}_{\mathrm{plasma\_api}} \longrightarrow \mathrm{Aurine}_{\mathrm{api}}$ |
| $v_{\mathrm{KI\_\_M1EX}}$ | `KI__M1EX` | excretion M1 (M1EX) | $\mathrm{Cki}_{\mathrm{plasma\_m1}} \longrightarrow \mathrm{Aurine}_{\mathrm{m1}}$ |
| $v_{\mathrm{KI\_\_M7EX}}$ | `KI__M7EX` | excretion M7 (M7EX) | $\mathrm{Cki}_{\mathrm{plasma\_m7}} \longrightarrow \mathrm{Aurine}_{\mathrm{m7}}$ |
| $v_{\mathrm{LI\_\_APIIM}}$ | `LI__APIIM` | import apixaban (APIIM) | $\mathrm{Cli}_{\mathrm{plasma\_api}} \rightleftharpoons \mathrm{LI}_{\mathrm{\_api}}$ |
| $v_{\mathrm{LI\_\_API2M2}}$ | `LI__API2M2` | apixaban -&gt; M2 (API2M2) | $\mathrm{LI}_{\mathrm{\_api}} \longrightarrow \mathrm{LI}_{\mathrm{\_m2}}$ |
| $v_{\mathrm{LI\_\_API2M7}}$ | `LI__API2M7` | apixaban -&gt; M7 (API2M7) | $\mathrm{LI}_{\mathrm{\_api}} \longrightarrow \mathrm{LI}_{\mathrm{\_m7}}$ |
| $v_{\mathrm{LI\_\_M22M1}}$ | `LI__M22M1` | M2 -&gt; M1 (M22M1) | $\mathrm{LI}_{\mathrm{\_m2}} \longrightarrow \mathrm{LI}_{\mathrm{\_m1}}$ |
| $v_{\mathrm{LI\_\_M1EX}}$ | `LI__M1EX` | export M1 (M1EX) | $\mathrm{LI}_{\mathrm{\_m1}} \rightleftharpoons \mathrm{Cli}_{\mathrm{plasma\_m1}}$ |
| $v_{\mathrm{LI\_\_M7EX}}$ | `LI__M7EX` | export M7 (M7EX) | $\mathrm{LI}_{\mathrm{\_m7}} \rightleftharpoons \mathrm{Cli}_{\mathrm{plasma\_m7}}$ |
| $v_{\mathrm{LI\_\_M1EXBI}}$ | `LI__M1EXBI` | biliary excretion M1 (M1EXBI) | $\mathrm{LI}_{\mathrm{\_m1}} \longrightarrow \mathrm{Cgu}_{\mathrm{m1}}$ |
| $v_{\mathrm{LI\_\_M2EXBI}}$ | `LI__M2EXBI` | biliary excretion M2 (M2EXBI) | $\mathrm{LI}_{\mathrm{\_m2}} \longrightarrow \mathrm{Cgu}_{\mathrm{m2}}$ |
| $v_{\mathrm{LI\_\_M7EXBI}}$ | `LI__M7EXBI` | biliary excretion M7 (M7EXBI) | $\mathrm{LI}_{\mathrm{\_m7}} \longrightarrow \mathrm{Cgu}_{\mathrm{m7}}$ |
| $v_{\mathrm{GU\_\_APIABS}}$ | `GU__APIABS` | absorption apixaban (APIABS) | $\mathrm{GU}_{\mathrm{\_api\_lumen}} \longrightarrow \mathrm{Cgu}_{\mathrm{plasma\_api}}$ |
| $v_{\mathrm{GU\_\_APISEC}}$ | `GU__APISEC` | intestinal secretion apixaban (APISEC) | $\mathrm{Cgu}_{\mathrm{plasma\_api}} \longrightarrow \mathrm{GU}_{\mathrm{\_api\_lumen}}$ |
| $v_{\mathrm{GU\_\_APISITR}}$ | `GU__APISITR` | small intestinal transit apixaban (APISITR) | $\mathrm{GU}_{\mathrm{\_api\_lumen}} \longrightarrow \mathrm{GU}_{\mathrm{\_api\_colon}}$ |
| $v_{\mathrm{GU\_\_M1SITR}}$ | `GU__M1SITR` | small intestinal transit M1 (M1SITR) | $\mathrm{Cgu}_{\mathrm{m1}} \longrightarrow \mathrm{GU}_{\mathrm{\_m1\_colon}}$ |
| $v_{\mathrm{GU\_\_M2SITR}}$ | `GU__M2SITR` | small intestinal transit M2 (M2SITR) | $\mathrm{Cgu}_{\mathrm{m2}} \longrightarrow \mathrm{GU}_{\mathrm{\_m2\_colon}}$ |
| $v_{\mathrm{GU\_\_M7SITR}}$ | `GU__M7SITR` | small intestinal transit M7 (M7SITR) | $\mathrm{Cgu}_{\mathrm{m7}} \longrightarrow \mathrm{GU}_{\mathrm{\_m7\_colon}}$ |
| $v_{\mathrm{GU\_\_APIEXC}}$ | `GU__APIEXC` | fecal excretion apixaban (APIEXC) | $\mathrm{GU}_{\mathrm{\_api\_colon}} \longrightarrow \mathrm{Afeces}_{\mathrm{api}}$ |
| $v_{\mathrm{GU\_\_M1EXC}}$ | `GU__M1EXC` | fecal excretion M1 (M1EXC) | $\mathrm{GU}_{\mathrm{\_m1\_colon}} \longrightarrow \mathrm{Afeces}_{\mathrm{m1}}$ |
| $v_{\mathrm{GU\_\_M2EXC}}$ | `GU__M2EXC` | fecal excretion M2 (M2EXC) | $\mathrm{GU}_{\mathrm{\_m2\_colon}} \longrightarrow \mathrm{Afeces}_{\mathrm{m2}}$ |
| $v_{\mathrm{GU\_\_M7EXC}}$ | `GU__M7EXC` | fecal excretion M7 (M7EXC) | $\mathrm{GU}_{\mathrm{\_m7\_colon}} \longrightarrow \mathrm{Afeces}_{\mathrm{m7}}$ |
| $v_{\mathrm{GU\_\_APITAB}}$ | `GU__APITAB` | tablet dissolution apixaban (APITAB) | $\mathrm{GU}_{\mathrm{\_api\_stomach}} \longrightarrow \mathrm{GU}_{\mathrm{\_api\_lumen}}$ |
| $v_{\mathrm{GU\_\_APIUNDIS}}$ | `GU__APIUNDIS` | transit undissolved apixaban (APIUNDIS) | $\mathrm{GU}_{\mathrm{\_api\_stomach}} \longrightarrow \mathrm{GU}_{\mathrm{\_api\_colon}}$ |
| $v_{\mathrm{GU\_\_APISOL}}$ | `GU__APISOL` | solution transport apixaban (APISOL) | $\mathrm{GU}_{\mathrm{\_api\_stomach}} \longrightarrow \mathrm{GU}_{\mathrm{\_api\_lumen}}$ |

The rates of the reactions are:

$$
\begin{aligned}
v_{\mathrm{transport\_lu\_api}} &= \frac{\mathrm{ftissue}_{\mathrm{api}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Clu}_{\mathrm{plasma\_api}} \cdot \mathrm{Kp}_{\mathrm{api}} \cdot \mathrm{fu}_{\mathrm{api}} - \mathrm{Clu}_{\mathrm{api}}\right) \\[1ex]
v_{\mathrm{transport\_re\_api}} &= \frac{\mathrm{ftissue}_{\mathrm{api}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cre}_{\mathrm{plasma\_api}} \cdot \mathrm{Kp}_{\mathrm{api}} \cdot \mathrm{fu}_{\mathrm{api}} - \mathrm{Cre}_{\mathrm{api}}\right) \\[1ex]
v_{\mathrm{iv\_api}} &= \frac{\mathrm{Ki}_{\mathrm{api}} \cdot \mathrm{IVDOSE}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}} \\[1ex]
v_{\mathrm{Flow\_ar\_ki\_api}} &= \mathrm{Qki} \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{Flow\_ki\_ve\_api}} &= \mathrm{Qki} \cdot \mathrm{Cki}_{\mathrm{plasma\_api}} \\[1ex]
v_{\mathrm{Flow\_arli\_li\_api}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qha} \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{Flow\_arli\_hv\_api}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qha} \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{Flow\_po\_li\_api}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qpo} \cdot \mathrm{Cpo}_{\mathrm{api}} \\[1ex]
v_{\mathrm{Flow\_po\_hv\_api}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qpo} \cdot \mathrm{Cpo}_{\mathrm{api}} \\[1ex]
v_{\mathrm{Flow\_li\_hv\_api}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathopen{}\left(\mathrm{Qpo} + \mathrm{Qha}\right) \cdot \mathrm{Cli}_{\mathrm{plasma\_api}} \\[1ex]
v_{\mathrm{Flow\_hv\_ve\_api}} &= \mathrm{Qh} \cdot \mathrm{Chv}_{\mathrm{api}} \\[1ex]
v_{\mathrm{Flow\_ve\_lu\_api}} &= \mathrm{Qlu} \cdot \mathrm{Cve}_{\mathrm{api}} \\[1ex]
v_{\mathrm{Flow\_lu\_ar\_api}} &= \mathrm{Qlu} \cdot \mathrm{Clu}_{\mathrm{plasma\_api}} \\[1ex]
v_{\mathrm{Flow\_ar\_gu\_api}} &= \mathrm{Qgu} \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{Flow\_gu\_po\_api}} &= \mathrm{Qgu} \cdot \mathrm{Cgu}_{\mathrm{plasma\_api}} \\[1ex]
v_{\mathrm{Flow\_ar\_re\_api}} &= \mathrm{Qre} \cdot \mathrm{Car}_{\mathrm{api}} \\[1ex]
v_{\mathrm{Flow\_re\_ve\_api}} &= \mathrm{Qre} \cdot \mathrm{Cre}_{\mathrm{plasma\_api}} \\[1ex]
v_{\mathrm{Flow\_ar\_ki\_m1}} &= \mathrm{Qki} \cdot \mathrm{Car}_{\mathrm{m1}} \\[1ex]
v_{\mathrm{Flow\_ki\_ve\_m1}} &= \mathrm{Qki} \cdot \mathrm{Cki}_{\mathrm{plasma\_m1}} \\[1ex]
v_{\mathrm{Flow\_arli\_li\_m1}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qha} \cdot \mathrm{Car}_{\mathrm{m1}} \\[1ex]
v_{\mathrm{Flow\_arli\_hv\_m1}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qha} \cdot \mathrm{Car}_{\mathrm{m1}} \\[1ex]
v_{\mathrm{Flow\_po\_li\_m1}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qpo} \cdot \mathrm{Cpo}_{\mathrm{m1}} \\[1ex]
v_{\mathrm{Flow\_po\_hv\_m1}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qpo} \cdot \mathrm{Cpo}_{\mathrm{m1}} \\[1ex]
v_{\mathrm{Flow\_li\_hv\_m1}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathopen{}\left(\mathrm{Qpo} + \mathrm{Qha}\right) \cdot \mathrm{Cli}_{\mathrm{plasma\_m1}} \\[1ex]
v_{\mathrm{Flow\_hv\_ve\_m1}} &= \mathrm{Qh} \cdot \mathrm{Chv}_{\mathrm{m1}} \\[1ex]
v_{\mathrm{Flow\_ve\_lu\_m1}} &= \mathrm{Qlu} \cdot \mathrm{Cve}_{\mathrm{m1}} \\[1ex]
v_{\mathrm{Flow\_lu\_ar\_m1}} &= \mathrm{Qlu} \cdot \mathrm{Clu}_{\mathrm{plasma\_m1}} \\[1ex]
v_{\mathrm{Flow\_ar\_gu\_m1}} &= \mathrm{Qgu} \cdot \mathrm{Car}_{\mathrm{m1}} \\[1ex]
v_{\mathrm{Flow\_gu\_po\_m1}} &= \mathrm{Qgu} \cdot \mathrm{Cgu}_{\mathrm{plasma\_m1}} \\[1ex]
v_{\mathrm{Flow\_ar\_re\_m1}} &= \mathrm{Qre} \cdot \mathrm{Car}_{\mathrm{m1}} \\[1ex]
v_{\mathrm{Flow\_re\_ve\_m1}} &= \mathrm{Qre} \cdot \mathrm{Cre}_{\mathrm{plasma\_m1}} \\[1ex]
v_{\mathrm{Flow\_ar\_ki\_m7}} &= \mathrm{Qki} \cdot \mathrm{Car}_{\mathrm{m7}} \\[1ex]
v_{\mathrm{Flow\_ki\_ve\_m7}} &= \mathrm{Qki} \cdot \mathrm{Cki}_{\mathrm{plasma\_m7}} \\[1ex]
v_{\mathrm{Flow\_arli\_li\_m7}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qha} \cdot \mathrm{Car}_{\mathrm{m7}} \\[1ex]
v_{\mathrm{Flow\_arli\_hv\_m7}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qha} \cdot \mathrm{Car}_{\mathrm{m7}} \\[1ex]
v_{\mathrm{Flow\_po\_li\_m7}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qpo} \cdot \mathrm{Cpo}_{\mathrm{m7}} \\[1ex]
v_{\mathrm{Flow\_po\_hv\_m7}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qpo} \cdot \mathrm{Cpo}_{\mathrm{m7}} \\[1ex]
v_{\mathrm{Flow\_li\_hv\_m7}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathopen{}\left(\mathrm{Qpo} + \mathrm{Qha}\right) \cdot \mathrm{Cli}_{\mathrm{plasma\_m7}} \\[1ex]
v_{\mathrm{Flow\_hv\_ve\_m7}} &= \mathrm{Qh} \cdot \mathrm{Chv}_{\mathrm{m7}} \\[1ex]
v_{\mathrm{Flow\_ve\_lu\_m7}} &= \mathrm{Qlu} \cdot \mathrm{Cve}_{\mathrm{m7}} \\[1ex]
v_{\mathrm{Flow\_lu\_ar\_m7}} &= \mathrm{Qlu} \cdot \mathrm{Clu}_{\mathrm{plasma\_m7}} \\[1ex]
v_{\mathrm{Flow\_ar\_gu\_m7}} &= \mathrm{Qgu} \cdot \mathrm{Car}_{\mathrm{m7}} \\[1ex]
v_{\mathrm{Flow\_gu\_po\_m7}} &= \mathrm{Qgu} \cdot \mathrm{Cgu}_{\mathrm{plasma\_m7}} \\[1ex]
v_{\mathrm{Flow\_ar\_re\_m7}} &= \mathrm{Qre} \cdot \mathrm{Car}_{\mathrm{m7}} \\[1ex]
v_{\mathrm{Flow\_re\_ve\_m7}} &= \mathrm{Qre} \cdot \mathrm{Cre}_{\mathrm{plasma\_m7}} \\[1ex]
v_{\mathrm{KI\_\_APIEX}} &= \mathrm{KI}_{\mathrm{\_GFR}} \cdot 0.001 \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathrm{KI}_{\mathrm{\_APIEX\_f}} \cdot \mathrm{Cki}_{\mathrm{plasma\_api}} \\[1ex]
v_{\mathrm{KI\_\_M1EX}} &= \mathrm{KI}_{\mathrm{\_GFR}} \cdot 0.001 \cdot \mathrm{KI}_{\mathrm{\_M1EX\_f}} \cdot \mathrm{Cki}_{\mathrm{plasma\_m1}} \\[1ex]
v_{\mathrm{KI\_\_M7EX}} &= \mathrm{KI}_{\mathrm{\_GFR}} \cdot 0.001 \cdot \mathrm{KI}_{\mathrm{\_M7EX\_f}} \cdot \mathrm{Cki}_{\mathrm{plasma\_m7}} \\[1ex]
v_{\mathrm{LI\_\_APIIM}} &= \mathrm{LI}_{\mathrm{\_APIIM\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathopen{}\left(\mathrm{Cli}_{\mathrm{plasma\_api}} \cdot \mathrm{fu}_{\mathrm{api}} - \mathrm{LI}_{\mathrm{\_api}}\right) \\[1ex]
v_{\mathrm{LI\_\_API2M2}} &= \mathrm{LI}_{\mathrm{\_f\_cyp3a4}} \cdot \mathrm{LI}_{\mathrm{\_API2M\_k}} \cdot \mathrm{LI}_{\mathrm{\_f\_m2}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_api}} \\[1ex]
v_{\mathrm{LI\_\_API2M7}} &= \mathrm{LI}_{\mathrm{\_f\_cyp3a4}} \cdot \mathrm{LI}_{\mathrm{\_API2M\_k}} \cdot \mathopen{}\left(1 - \mathrm{LI}_{\mathrm{\_f\_m2}}\right) \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_api}} \\[1ex]
v_{\mathrm{LI\_\_M22M1}} &= \mathrm{LI}_{\mathrm{\_M22M1\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_m2}} \\[1ex]
v_{\mathrm{LI\_\_M1EX}} &= \mathrm{LI}_{\mathrm{\_M1EX\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathopen{}\left(\mathrm{LI}_{\mathrm{\_m1}} - \mathrm{Cli}_{\mathrm{plasma\_m1}}\right) \\[1ex]
v_{\mathrm{LI\_\_M7EX}} &= \mathrm{LI}_{\mathrm{\_M7EX\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathopen{}\left(\mathrm{LI}_{\mathrm{\_m7}} - \mathrm{Cli}_{\mathrm{plasma\_m7}}\right) \\[1ex]
v_{\mathrm{LI\_\_M1EXBI}} &= \mathrm{LI}_{\mathrm{\_MXEXBI\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_m1}} \\[1ex]
v_{\mathrm{LI\_\_M2EXBI}} &= \mathrm{LI}_{\mathrm{\_MXEXBI\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_m2}} \\[1ex]
v_{\mathrm{LI\_\_M7EXBI}} &= \mathrm{LI}_{\mathrm{\_MXEXBI\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_m7}} \\[1ex]
v_{\mathrm{GU\_\_APIABS}} &= \mathrm{GU}_{\mathrm{\_APIABS\_k}} \cdot \mathrm{Vgu} \cdot \mathrm{GU}_{\mathrm{\_api\_lumen}} \\[1ex]
v_{\mathrm{GU\_\_APISEC}} &= \mathrm{GU}_{\mathrm{\_f\_pgp}} \cdot \mathrm{GU}_{\mathrm{\_APISEC\_k}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathrm{Cgu}_{\mathrm{plasma\_api}} \\[1ex]
v_{\mathrm{GU\_\_APISITR}} &= \mathrm{GU}_{\mathrm{\_SITRANS\_k}} \cdot \mathrm{Vgu} \cdot \mathrm{GU}_{\mathrm{\_api\_lumen}} \\[1ex]
v_{\mathrm{GU\_\_M1SITR}} &= \mathrm{GU}_{\mathrm{\_SITRANS\_k}} \cdot \mathrm{Vgu} \cdot \mathrm{Cgu}_{\mathrm{m1}} \\[1ex]
v_{\mathrm{GU\_\_M2SITR}} &= \mathrm{GU}_{\mathrm{\_SITRANS\_k}} \cdot \mathrm{Vgu} \cdot \mathrm{Cgu}_{\mathrm{m2}} \\[1ex]
v_{\mathrm{GU\_\_M7SITR}} &= \mathrm{GU}_{\mathrm{\_SITRANS\_k}} \cdot \mathrm{Vgu} \cdot \mathrm{Cgu}_{\mathrm{m7}} \\[1ex]
v_{\mathrm{GU\_\_APIEXC}} &= \mathrm{GU}_{\mathrm{\_LUMEX\_k}} \cdot \mathrm{GU}_{\mathrm{\_api\_colon}} \\[1ex]
v_{\mathrm{GU\_\_M1EXC}} &= \mathrm{GU}_{\mathrm{\_LUMEX\_k}} \cdot \mathrm{GU}_{\mathrm{\_m1\_colon}} \\[1ex]
v_{\mathrm{GU\_\_M2EXC}} &= \mathrm{GU}_{\mathrm{\_LUMEX\_k}} \cdot \mathrm{GU}_{\mathrm{\_m2\_colon}} \\[1ex]
v_{\mathrm{GU\_\_M7EXC}} &= \mathrm{GU}_{\mathrm{\_LUMEX\_k}} \cdot \mathrm{GU}_{\mathrm{\_m7\_colon}} \\[1ex]
v_{\mathrm{GU\_\_APITAB}} &= \frac{\frac{\frac{\mathrm{GU}_{\mathrm{\_Ka\_dis\_api}}}{60} \cdot \mathrm{PODOSE}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}}}{1 + \frac{\mathrm{PODOSE}_{\mathrm{api}}}{\mathrm{GU}_{\mathrm{\_PODOSE\_50}}}} \\[1ex]
v_{\mathrm{GU\_\_APIUNDIS}} &= \frac{\mathrm{GU}_{\mathrm{\_SITRANS\_k}} \cdot \mathrm{PODOSE}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}} \\[1ex]
v_{\mathrm{GU\_\_APISOL}} &= \frac{\frac{\mathrm{GU}_{\mathrm{\_Ka\_sol\_api}}}{60} \cdot \mathrm{SOLDOSE}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}}
\end{aligned}
$$

## ODE system

The states change in time with the rates of the reactions and the rate rules:

$$
\begin{aligned}
\frac{\mathrm{d} \,\mathrm{Cki}_{\mathrm{plasma\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_ki\_api}} - v_{\mathrm{Flow\_ki\_ve\_api}} - v_{\mathrm{KI\_\_APIEX}}}{\mathrm{Vki}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cli}_{\mathrm{plasma\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_li\_api}} + v_{\mathrm{Flow\_po\_li\_api}} - v_{\mathrm{Flow\_li\_hv\_api}} - v_{\mathrm{LI\_\_APIIM}}}{\mathrm{Vli}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{plasma\_api}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_lu\_api}} + v_{\mathrm{Flow\_ve\_lu\_api}} - v_{\mathrm{Flow\_lu\_ar\_api}}}{\mathrm{Vlu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{plasma\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_gu\_api}} - v_{\mathrm{Flow\_gu\_po\_api}} + v_{\mathrm{GU\_\_APIABS}} - v_{\mathrm{GU\_\_APISEC}}}{\mathrm{Vgu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{plasma\_api}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_re\_api}} + v_{\mathrm{Flow\_ar\_re\_api}} - v_{\mathrm{Flow\_re\_ve\_api}}}{\mathrm{Vre}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Car}_{\mathrm{api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Var}} \Bigl( -v_{\mathrm{Flow\_ar\_ki\_api}} - v_{\mathrm{Flow\_arli\_li\_api}} - v_{\mathrm{Flow\_arli\_hv\_api}} + v_{\mathrm{Flow\_lu\_ar\_api}} \\
&\quad {} - v_{\mathrm{Flow\_ar\_gu\_api}} - v_{\mathrm{Flow\_ar\_re\_api}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cve}_{\mathrm{api}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vve}} \Bigl( v_{\mathrm{iv\_api}} + v_{\mathrm{Flow\_ki\_ve\_api}} + v_{\mathrm{Flow\_hv\_ve\_api}} - v_{\mathrm{Flow\_ve\_lu\_api}} \\
&\quad {} + v_{\mathrm{Flow\_re\_ve\_api}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpo}_{\mathrm{api}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{Flow\_po\_li\_api}} - v_{\mathrm{Flow\_po\_hv\_api}} + v_{\mathrm{Flow\_gu\_po\_api}}}{\mathrm{Vpo}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Chv}_{\mathrm{api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_hv\_api}} + v_{\mathrm{Flow\_po\_hv\_api}} + v_{\mathrm{Flow\_li\_hv\_api}} - v_{\mathrm{Flow\_hv\_ve\_api}}}{\mathrm{Vhv}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_lu\_api}}}{\mathrm{Vlu}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_re\_api}}}{\mathrm{Vre}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Aurine}_{\mathrm{api}}}{\mathrm{d} t} &= v_{\mathrm{KI\_\_APIEX}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Afeces}_{\mathrm{api}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_APIEXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cki}_{\mathrm{plasma\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_ki\_m1}} - v_{\mathrm{Flow\_ki\_ve\_m1}} - v_{\mathrm{KI\_\_M1EX}}}{\mathrm{Vki}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cli}_{\mathrm{plasma\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_li\_m1}} + v_{\mathrm{Flow\_po\_li\_m1}} - v_{\mathrm{Flow\_li\_hv\_m1}} + v_{\mathrm{LI\_\_M1EX}}}{\mathrm{Vli}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{plasma\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ve\_lu\_m1}} - v_{\mathrm{Flow\_lu\_ar\_m1}}}{\mathrm{Vlu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{plasma\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_gu\_m1}} - v_{\mathrm{Flow\_gu\_po\_m1}}}{\mathrm{Vgu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{plasma\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_re\_m1}} - v_{\mathrm{Flow\_re\_ve\_m1}}}{\mathrm{Vre}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Car}_{\mathrm{m1}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Var}} \Bigl( -v_{\mathrm{Flow\_ar\_ki\_m1}} - v_{\mathrm{Flow\_arli\_li\_m1}} - v_{\mathrm{Flow\_arli\_hv\_m1}} + v_{\mathrm{Flow\_lu\_ar\_m1}} \\
&\quad {} - v_{\mathrm{Flow\_ar\_gu\_m1}} - v_{\mathrm{Flow\_ar\_re\_m1}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cve}_{\mathrm{m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ki\_ve\_m1}} + v_{\mathrm{Flow\_hv\_ve\_m1}} - v_{\mathrm{Flow\_ve\_lu\_m1}} + v_{\mathrm{Flow\_re\_ve\_m1}}}{\mathrm{Vve}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpo}_{\mathrm{m1}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{Flow\_po\_li\_m1}} - v_{\mathrm{Flow\_po\_hv\_m1}} + v_{\mathrm{Flow\_gu\_po\_m1}}}{\mathrm{Vpo}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Chv}_{\mathrm{m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_hv\_m1}} + v_{\mathrm{Flow\_po\_hv\_m1}} + v_{\mathrm{Flow\_li\_hv\_m1}} - v_{\mathrm{Flow\_hv\_ve\_m1}}}{\mathrm{Vhv}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Aurine}_{\mathrm{m1}}}{\mathrm{d} t} &= v_{\mathrm{KI\_\_M1EX}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Afeces}_{\mathrm{m1}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_M1EXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cki}_{\mathrm{plasma\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_ki\_m7}} - v_{\mathrm{Flow\_ki\_ve\_m7}} - v_{\mathrm{KI\_\_M7EX}}}{\mathrm{Vki}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cli}_{\mathrm{plasma\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_li\_m7}} + v_{\mathrm{Flow\_po\_li\_m7}} - v_{\mathrm{Flow\_li\_hv\_m7}} + v_{\mathrm{LI\_\_M7EX}}}{\mathrm{Vli}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{plasma\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ve\_lu\_m7}} - v_{\mathrm{Flow\_lu\_ar\_m7}}}{\mathrm{Vlu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{plasma\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_gu\_m7}} - v_{\mathrm{Flow\_gu\_po\_m7}}}{\mathrm{Vgu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{plasma\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_re\_m7}} - v_{\mathrm{Flow\_re\_ve\_m7}}}{\mathrm{Vre}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Car}_{\mathrm{m7}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Var}} \Bigl( -v_{\mathrm{Flow\_ar\_ki\_m7}} - v_{\mathrm{Flow\_arli\_li\_m7}} - v_{\mathrm{Flow\_arli\_hv\_m7}} + v_{\mathrm{Flow\_lu\_ar\_m7}} \\
&\quad {} - v_{\mathrm{Flow\_ar\_gu\_m7}} - v_{\mathrm{Flow\_ar\_re\_m7}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cve}_{\mathrm{m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ki\_ve\_m7}} + v_{\mathrm{Flow\_hv\_ve\_m7}} - v_{\mathrm{Flow\_ve\_lu\_m7}} + v_{\mathrm{Flow\_re\_ve\_m7}}}{\mathrm{Vve}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpo}_{\mathrm{m7}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{Flow\_po\_li\_m7}} - v_{\mathrm{Flow\_po\_hv\_m7}} + v_{\mathrm{Flow\_gu\_po\_m7}}}{\mathrm{Vpo}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Chv}_{\mathrm{m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_hv\_m7}} + v_{\mathrm{Flow\_po\_hv\_m7}} + v_{\mathrm{Flow\_li\_hv\_m7}} - v_{\mathrm{Flow\_hv\_ve\_m7}}}{\mathrm{Vhv}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Aurine}_{\mathrm{m7}}}{\mathrm{d} t} &= v_{\mathrm{KI\_\_M7EX}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Afeces}_{\mathrm{m7}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_M7EXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Afeces}_{\mathrm{m2}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_M2EXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_M1EXBI}} - v_{\mathrm{GU\_\_M1SITR}}}{\mathrm{Vgu}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_M2EXBI}} - v_{\mathrm{GU\_\_M2SITR}}}{\mathrm{Vgu}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_M7EXBI}} - v_{\mathrm{GU\_\_M7SITR}}}{\mathrm{Vgu}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_api}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_APIIM}} - v_{\mathrm{LI\_\_API2M2}} - v_{\mathrm{LI\_\_API2M7}}}{\mathrm{Vli}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_m1}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_M22M1}} - v_{\mathrm{LI\_\_M1EX}} - v_{\mathrm{LI\_\_M1EXBI}}}{\mathrm{Vli}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_m2}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_API2M2}} - v_{\mathrm{LI\_\_M22M1}} - v_{\mathrm{LI\_\_M2EXBI}}}{\mathrm{Vli}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_m7}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_API2M7}} - v_{\mathrm{LI\_\_M7EX}} - v_{\mathrm{LI\_\_M7EXBI}}}{\mathrm{Vli}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_api\_lumen}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vgu}} \Bigl( -v_{\mathrm{GU\_\_APIABS}} + v_{\mathrm{GU\_\_APISEC}} - v_{\mathrm{GU\_\_APISITR}} + v_{\mathrm{GU\_\_APITAB}} \\
&\quad {} + v_{\mathrm{GU\_\_APISOL}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_api\_colon}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_APISITR}} - v_{\mathrm{GU\_\_APIEXC}} + v_{\mathrm{GU\_\_APIUNDIS}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_m1\_colon}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_M1SITR}} - v_{\mathrm{GU\_\_M1EXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_m2\_colon}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_M2SITR}} - v_{\mathrm{GU\_\_M2EXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_m7\_colon}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_M7SITR}} - v_{\mathrm{GU\_\_M7EXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{PODOSE}_{\mathrm{api}}}{\mathrm{d} t} &= -\mathopen{}\left(v_{\mathrm{GU\_\_APITAB}} + v_{\mathrm{GU\_\_APIUNDIS}}\right) \cdot \mathrm{Mr}_{\mathrm{api}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{SOLDOSE}_{\mathrm{api}}}{\mathrm{d} t} &= -v_{\mathrm{GU\_\_APISOL}} \cdot \mathrm{Mr}_{\mathrm{api}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{IVDOSE}_{\mathrm{api}}}{\mathrm{d} t} &= -v_{\mathrm{iv\_api}} \cdot \mathrm{Mr}_{\mathrm{api}} + \mathrm{Ri}_{\mathrm{api}} \qquad \text{(rate rule)}
\end{aligned}
$$
