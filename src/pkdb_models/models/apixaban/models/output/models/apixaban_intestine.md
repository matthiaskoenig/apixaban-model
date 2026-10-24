# Model for apixaban absorption and intestinal secretion

Model `apixaban_intestine`, SBML Level 3 Version 2, read from apixaban\_intestine.xml, written by sbmlode 0.3.0.

Model for apixaban absorption and intestinal secretion

The tablet dissolves with a rate which saturates with the dose (PODOSE\_50), the solution reaches the lumen of the small intestine with Ka\_sol\_api. The dissolved apixaban is absorbed with first order kinetics (APIABS\_k) in competition with the small intestinal transit into the colon (SITRANS\_k), which also carries the undissolved tablet, the apixaban secreted from the plasma into the small intestine (P-gp/BCRP, APISEC\_k, f\_pgp) and the metabolites secreted with the bile. Nothing is absorbed from the colon, its content is excreted with the fecal transit (LUMEX\_k).

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
| $\mathrm{Vext}$ | `Vext` | plasma | $1$ | l | ✓ |
| $\mathrm{Vlumen}$ | `Vlumen` | lumen | $1$ | l |  |
| $\mathrm{Vfeces}$ | `Vfeces` | feces | $1$ | l | ✓ |
| $\mathrm{Vcolon}$ | `Vcolon` | colon lumen | $1$ | l | ✓ |
| $\mathrm{Vstomach}$ | `Vstomach` | stomach | $1$ | l | ✓ |
| $\mathrm{Vapical}$ | `Vapical` | apical membrane (intestinal membrane enterocytes) | $\mathrm{NaN}$ | m<sup>2</sup> | ✓ |

## Species

| Symbol | Id | Name | Compartment | Value | Unit | Properties |
| --- | --- | --- | --- | --- | --- | --- |
| $\mathrm{api}_{\mathrm{stomach}}$ | `api_stomach` | apixaban (api\_stomach) | $\mathrm{Vstomach}$ |  | mmol | amount, boundary |
| $\mathrm{api}_{\mathrm{ext}}$ | `api_ext` | apixaban (api\_ext) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{api}_{\mathrm{lumen}}$ | `api_lumen` | apixaban (api\_lumen) | $\mathrm{Vlumen}$ | $0$ | mmol/l | concentration |
| $\mathrm{api}_{\mathrm{feces}}$ | `api_feces` | apixaban (api\_feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{m1}_{\mathrm{lumen}}$ | `m1_lumen` | M1 (m1\_lumen) | $\mathrm{Vlumen}$ | $0$ | mmol/l | concentration |
| $\mathrm{m2}_{\mathrm{lumen}}$ | `m2_lumen` | M2 (m2\_lumen) | $\mathrm{Vlumen}$ | $0$ | mmol/l | concentration |
| $\mathrm{m7}_{\mathrm{lumen}}$ | `m7_lumen` | M7 (m7\_lumen) | $\mathrm{Vlumen}$ | $0$ | mmol/l | concentration |
| $\mathrm{m1}_{\mathrm{feces}}$ | `m1_feces` | M1 (m1\_feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{m2}_{\mathrm{feces}}$ | `m2_feces` | M2 (m2\_feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{m7}_{\mathrm{feces}}$ | `m7_feces` | M7 (m7\_feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{api}_{\mathrm{colon}}$ | `api_colon` | apixaban (api\_colon) | $\mathrm{Vcolon}$ |  | mmol | amount |
| $\mathrm{m1}_{\mathrm{colon}}$ | `m1_colon` | M1 (m1\_colon) | $\mathrm{Vcolon}$ |  | mmol | amount |
| $\mathrm{m2}_{\mathrm{colon}}$ | `m2_colon` | M2 (m2\_colon) | $\mathrm{Vcolon}$ |  | mmol | amount |
| $\mathrm{m7}_{\mathrm{colon}}$ | `m7_colon` | M7 (m7\_colon) | $\mathrm{Vcolon}$ |  | mmol | amount |

## Parameters

| Symbol | Id | Name | Value | Unit | Constant |
| --- | --- | --- | --- | --- | :---: |
| $\mathrm{fu}_{\mathrm{api}}$ | `fu_api` | fraction unbound in plasma apixaban | $0.131$ | \- | ✓ |
| $\mathrm{APIABS}_{\mathrm{k}}$ | `APIABS_k` | rate of apixaban absorption | $0.0185164315331011$ | 1/min | ✓ |
| $\mathrm{SITRANS}_{\mathrm{k}}$ | `SITRANS_k` | rate of the small intestinal transit | $0.00735101034145177$ | 1/min | ✓ |
| $\mathrm{LUMEX}_{\mathrm{k}}$ | `LUMEX_k` | rate of the fecal transit | $0.000555555555555556$ | 1/min | ✓ |
| $\mathrm{APISEC}_{\mathrm{k}}$ | `APISEC_k` | intestinal secretion clearance of unbound apixaban | $0.426931317033668$ | l/min | ✓ |
| $f_{\mathrm{pgp}}$ | `f_pgp` | P-gp/BCRP activity | $1$ | \- | ✓ |
| $\mathrm{PODOSE}_{\mathrm{api}}$ | `PODOSE_api` | oral dose apixaban in tablet \[mg\] | $0$ | mg |  |
| $\mathrm{SOLDOSE}_{\mathrm{api}}$ | `SOLDOSE_api` | oral dose apixaban in solution \[mg\] | $0$ | mg |  |
| $\mathrm{Ka}_{\mathrm{dis\_api}}$ | `Ka_dis_api` | Ka\_dis \[1/hr\] dissolution apixaban in tablet | $1.62989766741564$ | 1/hr | ✓ |
| $\mathrm{PODOSE}_{50}$ | `PODOSE_50` | undissolved dose of half-maximal dissolution \[mg\] | $5.74095936453337$ | mg | ✓ |
| $\mathrm{Ka}_{\mathrm{sol\_api}}$ | `Ka_sol_api` | Ka\_sol \[1/hr\] transport apixaban in solution | $6.40581223519076$ | 1/hr | ✓ |
| $\mathrm{Mr}_{\mathrm{api}}$ | `Mr_api` | Molecular weight apixaban \[g/mole\] | $459.5$ | g/mol | ✓ |
| $F_{\mathrm{api\_abs}}$ | `F_api_abs` | fraction absorbed apixaban |  | \- |  |

## Initial assignments and assignment rules

The initial assignments set the values at $t = 0$:

$$
\begin{aligned}
\mathrm{api}_{\mathrm{stomach}} &= 0 \cdot \mathrm{Vstomach} \\[1ex]
\mathrm{api}_{\mathrm{feces}} &= 0 \cdot \mathrm{Vfeces} \\[1ex]
\mathrm{m1}_{\mathrm{feces}} &= 0 \cdot \mathrm{Vfeces} \\[1ex]
\mathrm{m2}_{\mathrm{feces}} &= 0 \cdot \mathrm{Vfeces} \\[1ex]
\mathrm{m7}_{\mathrm{feces}} &= 0 \cdot \mathrm{Vfeces} \\[1ex]
\mathrm{api}_{\mathrm{colon}} &= 0 \cdot \mathrm{Vcolon} \\[1ex]
\mathrm{m1}_{\mathrm{colon}} &= 0 \cdot \mathrm{Vcolon} \\[1ex]
\mathrm{m2}_{\mathrm{colon}} &= 0 \cdot \mathrm{Vcolon} \\[1ex]
\mathrm{m7}_{\mathrm{colon}} &= 0 \cdot \mathrm{Vcolon}
\end{aligned}
$$

The assignment rules hold at every time $t$:

$$
\begin{aligned}
F_{\mathrm{api\_abs}} &= \frac{\mathrm{APIABS}_{\mathrm{k}}}{\mathrm{APIABS}_{\mathrm{k}} + \mathrm{SITRANS}_{\mathrm{k}}}
\end{aligned}
$$

## Reactions

| Rate | Id | Name | Equation |
| --- | --- | --- | --- |
| $v_{\mathrm{APIABS}}$ | `APIABS` | absorption apixaban (APIABS) | $\mathrm{api}_{\mathrm{lumen}} \longrightarrow \mathrm{api}_{\mathrm{ext}}$ |
| $v_{\mathrm{APISEC}}$ | `APISEC` | intestinal secretion apixaban (APISEC) | $\mathrm{api}_{\mathrm{ext}} \longrightarrow \mathrm{api}_{\mathrm{lumen}}$ |
| $v_{\mathrm{APISITR}}$ | `APISITR` | small intestinal transit apixaban (APISITR) | $\mathrm{api}_{\mathrm{lumen}} \longrightarrow \mathrm{api}_{\mathrm{colon}}$ |
| $v_{\mathrm{M1SITR}}$ | `M1SITR` | small intestinal transit M1 (M1SITR) | $\mathrm{m1}_{\mathrm{lumen}} \longrightarrow \mathrm{m1}_{\mathrm{colon}}$ |
| $v_{\mathrm{M2SITR}}$ | `M2SITR` | small intestinal transit M2 (M2SITR) | $\mathrm{m2}_{\mathrm{lumen}} \longrightarrow \mathrm{m2}_{\mathrm{colon}}$ |
| $v_{\mathrm{M7SITR}}$ | `M7SITR` | small intestinal transit M7 (M7SITR) | $\mathrm{m7}_{\mathrm{lumen}} \longrightarrow \mathrm{m7}_{\mathrm{colon}}$ |
| $v_{\mathrm{APIEXC}}$ | `APIEXC` | fecal excretion apixaban (APIEXC) | $\mathrm{api}_{\mathrm{colon}} \longrightarrow \mathrm{api}_{\mathrm{feces}}$ |
| $v_{\mathrm{M1EXC}}$ | `M1EXC` | fecal excretion M1 (M1EXC) | $\mathrm{m1}_{\mathrm{colon}} \longrightarrow \mathrm{m1}_{\mathrm{feces}}$ |
| $v_{\mathrm{M2EXC}}$ | `M2EXC` | fecal excretion M2 (M2EXC) | $\mathrm{m2}_{\mathrm{colon}} \longrightarrow \mathrm{m2}_{\mathrm{feces}}$ |
| $v_{\mathrm{M7EXC}}$ | `M7EXC` | fecal excretion M7 (M7EXC) | $\mathrm{m7}_{\mathrm{colon}} \longrightarrow \mathrm{m7}_{\mathrm{feces}}$ |
| $v_{\mathrm{APITAB}}$ | `APITAB` | tablet dissolution apixaban (APITAB) | $\mathrm{api}_{\mathrm{stomach}} \longrightarrow \mathrm{api}_{\mathrm{lumen}}$ |
| $v_{\mathrm{APIUNDIS}}$ | `APIUNDIS` | transit undissolved apixaban (APIUNDIS) | $\mathrm{api}_{\mathrm{stomach}} \longrightarrow \mathrm{api}_{\mathrm{colon}}$ |
| $v_{\mathrm{APISOL}}$ | `APISOL` | solution transport apixaban (APISOL) | $\mathrm{api}_{\mathrm{stomach}} \longrightarrow \mathrm{api}_{\mathrm{lumen}}$ |

The rates of the reactions are:

$$
\begin{aligned}
v_{\mathrm{APIABS}} &= \mathrm{APIABS}_{\mathrm{k}} \cdot \mathrm{Vlumen} \cdot \mathrm{api}_{\mathrm{lumen}} \\[1ex]
v_{\mathrm{APISEC}} &= f_{\mathrm{pgp}} \cdot \mathrm{APISEC}_{\mathrm{k}} \cdot \mathrm{fu}_{\mathrm{api}} \cdot \mathrm{api}_{\mathrm{ext}} \\[1ex]
v_{\mathrm{APISITR}} &= \mathrm{SITRANS}_{\mathrm{k}} \cdot \mathrm{Vlumen} \cdot \mathrm{api}_{\mathrm{lumen}} \\[1ex]
v_{\mathrm{M1SITR}} &= \mathrm{SITRANS}_{\mathrm{k}} \cdot \mathrm{Vlumen} \cdot \mathrm{m1}_{\mathrm{lumen}} \\[1ex]
v_{\mathrm{M2SITR}} &= \mathrm{SITRANS}_{\mathrm{k}} \cdot \mathrm{Vlumen} \cdot \mathrm{m2}_{\mathrm{lumen}} \\[1ex]
v_{\mathrm{M7SITR}} &= \mathrm{SITRANS}_{\mathrm{k}} \cdot \mathrm{Vlumen} \cdot \mathrm{m7}_{\mathrm{lumen}} \\[1ex]
v_{\mathrm{APIEXC}} &= \mathrm{LUMEX}_{\mathrm{k}} \cdot \mathrm{api}_{\mathrm{colon}} \\[1ex]
v_{\mathrm{M1EXC}} &= \mathrm{LUMEX}_{\mathrm{k}} \cdot \mathrm{m1}_{\mathrm{colon}} \\[1ex]
v_{\mathrm{M2EXC}} &= \mathrm{LUMEX}_{\mathrm{k}} \cdot \mathrm{m2}_{\mathrm{colon}} \\[1ex]
v_{\mathrm{M7EXC}} &= \mathrm{LUMEX}_{\mathrm{k}} \cdot \mathrm{m7}_{\mathrm{colon}} \\[1ex]
v_{\mathrm{APITAB}} &= \frac{\frac{\frac{\mathrm{Ka}_{\mathrm{dis\_api}}}{60} \cdot \mathrm{PODOSE}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}}}{1 + \frac{\mathrm{PODOSE}_{\mathrm{api}}}{\mathrm{PODOSE}_{50}}} \\[1ex]
v_{\mathrm{APIUNDIS}} &= \frac{\mathrm{SITRANS}_{\mathrm{k}} \cdot \mathrm{PODOSE}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}} \\[1ex]
v_{\mathrm{APISOL}} &= \frac{\frac{\mathrm{Ka}_{\mathrm{sol\_api}}}{60} \cdot \mathrm{SOLDOSE}_{\mathrm{api}}}{\mathrm{Mr}_{\mathrm{api}}}
\end{aligned}
$$

## ODE system

The states change in time with the rates of the reactions and the rate rules:

$$
\begin{aligned}
\frac{\mathrm{d} \,\mathrm{api}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{v_{\mathrm{APIABS}} - v_{\mathrm{APISEC}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{api}_{\mathrm{lumen}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vlumen}} \Bigl( -v_{\mathrm{APIABS}} + v_{\mathrm{APISEC}} - v_{\mathrm{APISITR}} + v_{\mathrm{APITAB}} \\
&\quad {} + v_{\mathrm{APISOL}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{api}_{\mathrm{feces}}}{\mathrm{d} t} &= v_{\mathrm{APIEXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m1}_{\mathrm{lumen}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{M1SITR}}}{\mathrm{Vlumen}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m2}_{\mathrm{lumen}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{M2SITR}}}{\mathrm{Vlumen}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m7}_{\mathrm{lumen}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{M7SITR}}}{\mathrm{Vlumen}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m1}_{\mathrm{feces}}}{\mathrm{d} t} &= v_{\mathrm{M1EXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m2}_{\mathrm{feces}}}{\mathrm{d} t} &= v_{\mathrm{M2EXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m7}_{\mathrm{feces}}}{\mathrm{d} t} &= v_{\mathrm{M7EXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{api}_{\mathrm{colon}}}{\mathrm{d} t} &= v_{\mathrm{APISITR}} - v_{\mathrm{APIEXC}} + v_{\mathrm{APIUNDIS}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m1}_{\mathrm{colon}}}{\mathrm{d} t} &= v_{\mathrm{M1SITR}} - v_{\mathrm{M1EXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m2}_{\mathrm{colon}}}{\mathrm{d} t} &= v_{\mathrm{M2SITR}} - v_{\mathrm{M2EXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m7}_{\mathrm{colon}}}{\mathrm{d} t} &= v_{\mathrm{M7SITR}} - v_{\mathrm{M7EXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{PODOSE}_{\mathrm{api}}}{\mathrm{d} t} &= -\mathopen{}\left(v_{\mathrm{APITAB}} + v_{\mathrm{APIUNDIS}}\right) \cdot \mathrm{Mr}_{\mathrm{api}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{SOLDOSE}_{\mathrm{api}}}{\mathrm{d} t} &= -v_{\mathrm{APISOL}} \cdot \mathrm{Mr}_{\mathrm{api}} \qquad \text{(rate rule)}
\end{aligned}
$$
