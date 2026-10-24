# Model for hepatic apixaban metabolism.

Model `apixaban_liver`, SBML Level 3 Version 2, read from apixaban\_liver.xml, written by sbmlode 0.3.0.

Model for hepatic apixaban metabolism.

The unbound apixaban in plasma equilibrates with the hepatocytes and is metabolized by CYP3A4/5 (API2M\_k, activity f\_cyp3a4) to O-demethyl apixaban (M2, fraction f\_m2) and hydroxy apixaban (M7). M2 is sulfated to M1. M1 and M7 are exported into the plasma, M1, M2 and M7 are excreted with the bile into the intestinal lumen.

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
| $\mathrm{Vli}$ | `Vli` | liver | $1.5$ | l | ✓ |
| $\mathrm{Vmem}$ | `Vmem` | membrane | $\mathrm{NaN}$ | m<sup>2</sup> | ✓ |
| $\mathrm{Vlumen}$ | `Vlumen` | gut lumen | $1$ | l | ✓ |

## Species

| Symbol | Id | Name | Compartment | Value | Unit | Properties |
| --- | --- | --- | --- | --- | --- | --- |
| $\mathrm{api}_{\mathrm{ext}}$ | `api_ext` | apixaban (api\_ext) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{api}$ | `api` | apixaban (api) | $\mathrm{Vli}$ | $0$ | mmol/l | concentration |
| $\mathrm{m1}_{\mathrm{ext}}$ | `m1_ext` | M1 (m1\_ext) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $m_{1}$ | `m1` | M1 (m1) | $\mathrm{Vli}$ | $0$ | mmol/l | concentration |
| $\mathrm{m1}_{\mathrm{lumen}}$ | `m1_lumen` | M1 (m1\_lumen) | $\mathrm{Vlumen}$ |  | mmol | amount |
| $m_{2}$ | `m2` | M2 (m2) | $\mathrm{Vli}$ | $0$ | mmol/l | concentration |
| $\mathrm{m2}_{\mathrm{lumen}}$ | `m2_lumen` | M2 (m2\_lumen) | $\mathrm{Vlumen}$ |  | mmol | amount |
| $\mathrm{m7}_{\mathrm{ext}}$ | `m7_ext` | M7 (m7\_ext) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $m_{7}$ | `m7` | M7 (m7) | $\mathrm{Vli}$ | $0$ | mmol/l | concentration |
| $\mathrm{m7}_{\mathrm{lumen}}$ | `m7_lumen` | M7 (m7\_lumen) | $\mathrm{Vlumen}$ |  | mmol | amount |

## Parameters

| Symbol | Id | Name | Value | Unit | Constant |
| --- | --- | --- | --- | --- | :---: |
| $\mathrm{API2M}_{\mathrm{k}}$ | `API2M_k` | rate of the CYP3A4 metabolism of apixaban | $0.0875891081052202$ | 1/min | ✓ |
| $f_{\mathrm{m2}}$ | `f_m2` | fraction of the CYP3A4 metabolism to M2 | $0.78$ | \- | ✓ |
| $f_{\mathrm{cyp3a4}}$ | `f_cyp3a4` | CYP3A4 activity | $1$ | \- | ✓ |
| $\mathrm{MXEXBI}_{\mathrm{k}}$ | `MXEXBI_k` | rate of the biliary excretion of the apixaban metabolites | $0.00245100330106179$ | 1/min | ✓ |
| $\mathrm{APIIM}_{\mathrm{k}}$ | `APIIM_k` | rate apixaban import | $1000$ | 1/min | ✓ |
| $\mathrm{fu}_{\mathrm{api}}$ | `fu_api` | fraction unbound in plasma apixaban | $0.131$ | \- | ✓ |
| $\mathrm{M22M1}_{\mathrm{k}}$ | `M22M1_k` | rate of the sulfation M2 -&gt; M1 | $0.00049319446956451$ | 1/min | ✓ |
| $\mathrm{M1EX}_{\mathrm{k}}$ | `M1EX_k` | rate M1 export | $1000$ | 1/min | ✓ |
| $\mathrm{M7EX}_{\mathrm{k}}$ | `M7EX_k` | rate M7 export | $1000$ | 1/min | ✓ |

## Initial assignments and assignment rules

The initial assignments set the values at $t = 0$:

$$
\begin{aligned}
\mathrm{m1}_{\mathrm{lumen}} &= 0 \cdot \mathrm{Vlumen} \\[1ex]
\mathrm{m2}_{\mathrm{lumen}} &= 0 \cdot \mathrm{Vlumen} \\[1ex]
\mathrm{m7}_{\mathrm{lumen}} &= 0 \cdot \mathrm{Vlumen}
\end{aligned}
$$

## Reactions

| Rate | Id | Name | Equation |
| --- | --- | --- | --- |
| $v_{\mathrm{APIIM}}$ | `APIIM` | import apixaban (APIIM) | $\mathrm{api}_{\mathrm{ext}} \rightleftharpoons \mathrm{api}$ |
| $v_{\mathrm{API2M2}}$ | `API2M2` | apixaban -&gt; M2 (API2M2) | $\mathrm{api} \longrightarrow m_{2}$ |
| $v_{\mathrm{API2M7}}$ | `API2M7` | apixaban -&gt; M7 (API2M7) | $\mathrm{api} \longrightarrow m_{7}$ |
| $v_{\mathrm{M22M1}}$ | `M22M1` | M2 -&gt; M1 (M22M1) | $m_{2} \longrightarrow m_{1}$ |
| $v_{\mathrm{M1EX}}$ | `M1EX` | export M1 (M1EX) | $m_{1} \rightleftharpoons \mathrm{m1}_{\mathrm{ext}}$ |
| $v_{\mathrm{M7EX}}$ | `M7EX` | export M7 (M7EX) | $m_{7} \rightleftharpoons \mathrm{m7}_{\mathrm{ext}}$ |
| $v_{\mathrm{M1EXBI}}$ | `M1EXBI` | biliary excretion M1 (M1EXBI) | $m_{1} \longrightarrow \mathrm{m1}_{\mathrm{lumen}}$ |
| $v_{\mathrm{M2EXBI}}$ | `M2EXBI` | biliary excretion M2 (M2EXBI) | $m_{2} \longrightarrow \mathrm{m2}_{\mathrm{lumen}}$ |
| $v_{\mathrm{M7EXBI}}$ | `M7EXBI` | biliary excretion M7 (M7EXBI) | $m_{7} \longrightarrow \mathrm{m7}_{\mathrm{lumen}}$ |

The rates of the reactions are:

$$
\begin{aligned}
v_{\mathrm{APIIM}} &= \mathrm{APIIM}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot \mathopen{}\left(\mathrm{api}_{\mathrm{ext}} \cdot \mathrm{fu}_{\mathrm{api}} - \mathrm{api}\right) \\[1ex]
v_{\mathrm{API2M2}} &= f_{\mathrm{cyp3a4}} \cdot \mathrm{API2M}_{\mathrm{k}} \cdot f_{\mathrm{m2}} \cdot \mathrm{Vli} \cdot \mathrm{api} \\[1ex]
v_{\mathrm{API2M7}} &= f_{\mathrm{cyp3a4}} \cdot \mathrm{API2M}_{\mathrm{k}} \cdot \mathopen{}\left(1 - f_{\mathrm{m2}}\right) \cdot \mathrm{Vli} \cdot \mathrm{api} \\[1ex]
v_{\mathrm{M22M1}} &= \mathrm{M22M1}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot m_{2} \\[1ex]
v_{\mathrm{M1EX}} &= \mathrm{M1EX}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot \mathopen{}\left(m_{1} - \mathrm{m1}_{\mathrm{ext}}\right) \\[1ex]
v_{\mathrm{M7EX}} &= \mathrm{M7EX}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot \mathopen{}\left(m_{7} - \mathrm{m7}_{\mathrm{ext}}\right) \\[1ex]
v_{\mathrm{M1EXBI}} &= \mathrm{MXEXBI}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot m_{1} \\[1ex]
v_{\mathrm{M2EXBI}} &= \mathrm{MXEXBI}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot m_{2} \\[1ex]
v_{\mathrm{M7EXBI}} &= \mathrm{MXEXBI}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot m_{7}
\end{aligned}
$$

## ODE system

The states change in time with the rates of the reactions:

$$
\begin{aligned}
\frac{\mathrm{d} \,\mathrm{api}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{APIIM}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{api}}{\mathrm{d} t} &= \frac{v_{\mathrm{APIIM}} - v_{\mathrm{API2M2}} - v_{\mathrm{API2M7}}}{\mathrm{Vli}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m1}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{v_{\mathrm{M1EX}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} m_{1}}{\mathrm{d} t} &= \frac{v_{\mathrm{M22M1}} - v_{\mathrm{M1EX}} - v_{\mathrm{M1EXBI}}}{\mathrm{Vli}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m1}_{\mathrm{lumen}}}{\mathrm{d} t} &= v_{\mathrm{M1EXBI}} \\[1ex]
\frac{\mathrm{d} m_{2}}{\mathrm{d} t} &= \frac{v_{\mathrm{API2M2}} - v_{\mathrm{M22M1}} - v_{\mathrm{M2EXBI}}}{\mathrm{Vli}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m2}_{\mathrm{lumen}}}{\mathrm{d} t} &= v_{\mathrm{M2EXBI}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m7}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{v_{\mathrm{M7EX}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} m_{7}}{\mathrm{d} t} &= \frac{v_{\mathrm{API2M7}} - v_{\mathrm{M7EX}} - v_{\mathrm{M7EXBI}}}{\mathrm{Vli}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{m7}_{\mathrm{lumen}}}{\mathrm{d} t} &= v_{\mathrm{M7EXBI}}
\end{aligned}
$$
