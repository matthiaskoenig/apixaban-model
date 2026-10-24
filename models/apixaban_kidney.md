# Model for renal apixaban excretion.

Model `apixaban_kidney`, SBML Level 3 Version 2, read from apixaban\_kidney.xml, written by sbmlode 0.3.0.

Model for the renal excretion of apixaban and its metabolites M1 and M7.

The renal clearances are given relative to the glomerular filtration rate (GFR), which scales with the renal function; the GFR does not depend on the body weight (Upreti2013: the renal clearance was similar across the groups of body weight).

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
| $\mathrm{Vext}$ | `Vext` | plasma | $1.5$ | l | ✓ |
| $\mathrm{Vurine}$ | `Vurine` | urine | $1$ | l | ✓ |

## Species

| Symbol | Id | Name | Compartment | Value | Unit | Properties |
| --- | --- | --- | --- | --- | --- | --- |
| $\mathrm{api}_{\mathrm{ext}}$ | `api_ext` | apixaban (api\_ext) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{api}_{\mathrm{urine}}$ | `api_urine` | apixaban (api\_urine) | $\mathrm{Vurine}$ |  | mmol | amount |
| $\mathrm{m1}_{\mathrm{ext}}$ | `m1_ext` | M1 (m1\_ext) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{m1}_{\mathrm{urine}}$ | `m1_urine` | M1 (m1\_urine) | $\mathrm{Vurine}$ |  | mmol | amount |
| $\mathrm{m7}_{\mathrm{ext}}$ | `m7_ext` | M7 (m7\_ext) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{m7}_{\mathrm{urine}}$ | `m7_urine` | M7 (m7\_urine) | $\mathrm{Vurine}$ |  | mmol | amount |

## Parameters

| Symbol | Id | Name | Value | Unit | Constant |
| --- | --- | --- | --- | --- | :---: |
| $f_{\mathrm{renal\_function}}$ | `f_renal_function` | renal function | $1$ | \- | ✓ |
| $\mathrm{GFR}_{\mathrm{base}}$ | `GFR_base` | glomerular filtration rate (healthy) | $101$ | ml/min | ✓ |
| $\mathrm{fu}_{\mathrm{api}}$ | `fu_api` | fraction unbound in plasma apixaban | $0.131$ | \- | ✓ |
| $\mathrm{APIEX}_{\mathrm{f}}$ | `APIEX_f` | renal clearance of unbound apixaban relative to the GFR | $1.01497104264872$ | \- | ✓ |
| $\mathrm{M1EX}_{\mathrm{f}}$ | `M1EX_f` | renal clearance of M1 relative to the GFR | $0.0459801360234629$ | \- | ✓ |
| $\mathrm{M7EX}_{\mathrm{f}}$ | `M7EX_f` | renal clearance of M7 relative to the GFR | $0.0141866056661887$ | \- | ✓ |
| $\mathrm{GFR}$ | `GFR` | glomerular filtration rate |  | ml/min |  |

## Initial assignments and assignment rules

The initial assignments set the values at $t = 0$:

$$
\begin{aligned}
\mathrm{api}_{\mathrm{urine}} &= 0 \cdot \mathrm{Vurine} \\[1ex]
\mathrm{m1}_{\mathrm{urine}} &= 0 \cdot \mathrm{Vurine} \\[1ex]
\mathrm{m7}_{\mathrm{urine}} &= 0 \cdot \mathrm{Vurine}
\end{aligned}
$$

The assignment rules hold at every time $t$:

$$
\begin{aligned}
\mathrm{GFR} &= f_{\mathrm{renal\_function}} \cdot \mathrm{GFR}_{\mathrm{base}}
\end{aligned}
$$

## Reactions

| Rate | Id | Name | Equation |
| --- | --- | --- | --- |
| $v_{\mathrm{APIEX}}$ | `APIEX` | excretion apixaban (APIEX) | $\mathrm{api}_{\mathrm{ext}} \longrightarrow \mathrm{api}_{\mathrm{urine}}$ |
| $v_{\mathrm{M1EX}}$ | `M1EX` | excretion M1 (M1EX) | $\mathrm{m1}_{\mathrm{ext}} \longrightarrow \mathrm{m1}_{\mathrm{urine}}$ |
| $v_{\mathrm{M7EX}}$ | `M7EX` | excretion M7 (M7EX) | $\mathrm{m7}_{\mathrm{ext}} \longrightarrow \mathrm{m7}_{\mathrm{urine}}$ |

The rates of the reactions are:

$$
\begin{aligned}
v_{\mathrm{APIEX}} &= \mathrm{GFR} \cdot 0.001 \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathrm{APIEX}_{\mathrm{f}} \cdot \mathrm{api}_{\mathrm{ext}} \\[1ex]
v_{\mathrm{M1EX}} &= \mathrm{GFR} \cdot 0.001 \cdot \mathrm{M1EX}_{\mathrm{f}} \cdot \mathrm{m1}_{\mathrm{ext}} \\[1ex]
v_{\mathrm{M7EX}} &= \mathrm{GFR} \cdot 0.001 \cdot \mathrm{M7EX}_{\mathrm{f}} \cdot \mathrm{m7}_{\mathrm{ext}}
\end{aligned}
$$

## ODE system

The states change in time with the rates of the reactions:

$$
\begin{aligned}
\frac{\mathrm{d} \,\mathrm{api}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{APIEX}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{api}_{\mathrm{urine}}}{\mathrm{d} t} &= v_{\mathrm{APIEX}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m1}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{M1EX}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m1}_{\mathrm{urine}}}{\mathrm{d} t} &= v_{\mathrm{M1EX}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m7}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{M7EX}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m7}_{\mathrm{urine}}}{\mathrm{d} t} &= v_{\mathrm{M7EX}}
\end{aligned}
$$
