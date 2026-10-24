# Model for coagulation factors and readouts.

Model `apixaban_coagulation`, SBML Level 3 Version 2, read from apixaban\_coagulation.xml, written by sbmlode 0.3.0.

Model for coagulation factors and readouts.

The effects depend on the total concentration of apixaban in the venous plasma Cve\_api, as the assays measure the total drug in a plasma sample: the anti-factor Xa activity is linear in the concentration, the INR, the prothrombin time (PT), the modified prothrombin time (mPT) and the activated partial thromboplastin time (aPTT) follow an Emax model of the concentration relative to their baseline.

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
| $\mathrm{Vplasma}$ | `Vplasma` | plasma | $5$ | l | ✓ |

## Species

| Symbol | Id | Name | Compartment | Value | Unit | Properties |
| --- | --- | --- | --- | --- | --- | --- |
| $\mathrm{Cve}_{\mathrm{api}}$ | `Cve_api` | apixaban | $\mathrm{Vplasma}$ | $0$ | mmol/l | concentration |

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

## Initial assignments and assignment rules

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
\mathrm{antiXa}_{\mathrm{activity\_gram}} &= \mathrm{antiXa}_{\mathrm{gram\_slope}} \cdot \mathrm{Cve}_{\mathrm{api}}
\end{aligned}
$$
