"""Pharmacokinetic and pharmacodynamic parameters of the apixaban scans.

The pharmacokinetic parameters are the non-compartmental analysis of
`pkpdutils`, named like the variables of its `NCAResult` (e.g. `auc_last`,
`auc_inf_obs`, `cmax`, `tmax`, `thalf`, `lambda_z`, `cl_f`, `vz_f`), with the
unit of every parameter in `<name>_unit`, for apixaban and its metabolites M1
and M7 in plasma. The dose is the oral dose of apixaban; the metabolites have
no dose, so they have no apparent clearance and volume. The concentrations
below `LLOQ_FRACTION` of the maximum are below the limit of quantification, so
that the noise of the integrator is not the terminal phase. In addition:

- `aucend_<hr>`: the AUC until 12, 24, 48, 72 and 96 hr (trapezoidal rule),
- the amounts excreted in the urine and feces until the end of the simulation
  (`Aurine_<id>`, `Afeces_<id>`, the ids of the model) and the renal clearance
  `cl_renal` (the amount
  in the urine over `auc_last`). The amount in the feces is no clearance: after
  an oral dose it is mostly the apixaban which is not absorbed.

The pharmacodynamic parameters are the minimum and maximum of the
pharmacodynamic outputs.

A scan has one dimension, the scanned parameter; a run over the draws of the
fitted parameters (`run_simulation pkdb_models.models.apixaban --uncertainty`)
adds the dimension of the draws. The parameters are calculated for every point
of every dimension, a row per point with its position along each dimension
(the columns `point` and, with draws, `draw`), see `summarize`.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
import pandas as pd
from pkpdsim.pk import nca_frame, scan_nca
from pkpdutils import Route
from sbmlsim import Q
from sbmlsim.result import ScanResult
from sbmlsim.result.scan import end_values, scan_dimensions, start_values
from sbmlsim.units import Quantity

if TYPE_CHECKING:
    from pkdb_models.models.apixaban.experiments.base_experiment import (
        ApixabanSimulationExperiment,
    )

#: oral dose of the scans
DOSE = "PODOSE_api"
#: the substances by their short name (the column `substance`): the id of
#: the substance in the model (the concentration in the plasma of the arm vein
#: `Carm_<id>`, the amounts excreted `Aurine_<id>` and `Afeces_<id>`) and its
#: name
SUBSTANCES: dict[str, tuple[str, str]] = {
    "api": ("api", "apixaban"),
    "m1": ("api_m1", "M1"),
    "m7": ("api_m7", "M7"),
}
#: end times of the partial AUCs [hr]
AUC_END_TIMES: list[int] = [12, 24, 48, 72, 96]
#: the limit of quantification relative to the maximal concentration
LLOQ_FRACTION = 1e-6
#: the pharmacodynamic outputs of `calculate_apixaban_pd`, the outputs of the
#: coagulation model
PD_OUTPUTS: list[str] = [
    "COAG__INR",
    "COAG__mPT",
    "COAG__PT",
    "COAG__aPTT",
    "COAG__antiXa_activity",
    "COAG__INR_ratio",
    "COAG__mPT_ratio",
    "COAG__PT_ratio",
    "COAG__aPTT_ratio",
]


def _dimensions(res: ScanResult, across: str | None) -> list[str]:
    """Get the dimension of a scan and the draws `across`, in the order of the rows.

    Raises:
        ValueError: if the scan has not one dimension besides the draws.
    """
    dims = scan_dimensions(res, across)
    if len(dims) != 1:
        raise ValueError(
            f"A scan of one dimension is required, not of {dims} (draws: {across})."
        )
    return [dims[0], *([across] if across is not None else [])]


def _timecourses(res: ScanResult, key: str) -> tuple[np.ndarray, np.ndarray]:
    """Get the timecourse of a variable at every point of a scan.

    Args:
        res: result of the scan.
        key: the variable.

    Returns:
        The time and the values over the dimensions of the scan and the time
        (`point_timecourse` of every point), the time of the padding of a
        ragged result is NaN.
    """
    timecourses = res.to_timecourses(key)
    return timecourses.times, timecourses.values


def calculate_apixaban_pk(
    experiment: ApixabanSimulationExperiment,
    res: ScanResult,
    across: str | None = None,
) -> pd.DataFrame:
    """Calculate the pharmacokinetic parameters of every simulation of a scan.

    Every substance is analysed at all points of the scan at once
    (`scan_nca`). The renal clearance is the amount excreted in the urine
    until the end of the simulation over `auc_last`.

    Args:
        experiment: experiment of the scan, for the molecular weight.
        res: result of the scan.
        across: the dimension of the draws of the fitted parameters, `None`
            for a scan without draws.

    Returns:
        One row per substance and simulation of the scan, the substances one
        after the other, with the position of the simulation (`point`, and
        `draw` with draws), the parameters and their units (`<name>_unit`).
    """
    units = res.units
    names = dict(zip(_dimensions(res, across), ["point", "draw"], strict=False))
    positions = list(names.values())
    time_unit = str(units["time"])
    dfs = []
    for sid, (model_id, substance) in SUBSTANCES.items():
        concentration = f"Carm_{model_id}"
        if sid == "api":
            # the dose of apixaban in the substance unit of the concentration,
            # which `cl_f` and `vz_f` require
            dose = Q(start_values(res, DOSE).values, units[DOSE]) / experiment.Mr["api"]
            result = scan_nca(
                res,
                concentration,
                dose=dose.to("mmole"),
                route=Route.ORAL,
                substance=substance,
                lloq_fraction=LLOQ_FRACTION,
            )
        else:
            result = scan_nca(
                res,
                concentration,
                dose=None,
                route=None,
                substance=substance,
                lloq_fraction=LLOQ_FRACTION,
            )
        df = nca_frame(result).drop(columns="nca_flags")
        position = tuple(df[dim].to_numpy() for dim in res.dims)
        pk: dict[str, Quantity] = {}
        # partial AUCs until the end times (trapezoidal rule, `np.trapezoid`)
        time, c = _timecourses(res, concentration)
        segments = np.diff(time, axis=-1) * (c[..., 1:] + c[..., :-1]) / 2.0
        for t_end in AUC_END_TIMES:
            until = time[..., 1:] <= Q(t_end, "hr").to(time_unit).magnitude
            auc = np.where(until, segments, 0.0).sum(axis=-1)
            pk[f"aucend_{t_end}"] = Q(
                auc[position], f"{units[concentration]}*{time_unit}"
            )
        # the amounts excreted and the renal clearance
        for key in [f"Aurine_{model_id}", f"Afeces_{model_id}"]:
            pk[key] = Q(end_values(res, key).values[position], units[key])
        auc_last = Q(df["auc_last"].to_numpy(), df["auc_last_unit"].iloc[0])
        pk["cl_renal"] = (pk[f"Aurine_{model_id}"] / auc_last).to("ml/min")
        for key, value in pk.items():
            df[key] = value.magnitude
            df[f"{key}_unit"] = str(value.units)
        df = df.rename(columns=names)
        df.insert(len(positions), "substance", sid)
        df = df[[*positions, *df.columns.drop(positions)]]
        dfs.append(df.sort_values(positions, kind="stable"))
    return pd.concat(dfs, ignore_index=True)


def calculate_apixaban_pd(
    res: ScanResult, across: str | None = None
) -> dict[str, pd.DataFrame]:
    """Calculate the minimum and maximum of the pharmacodynamic outputs of a scan.

    Args:
        res: result of the scan.
        across: the dimension of the draws of the fitted parameters, `None`
            for a scan without draws.

    Returns:
        One table per output, one row per simulation of the scan with its
        position (`point`, and `draw` with draws).
    """
    dims = _dimensions(res, across)
    # the positions of the points, the scan dimension slowest
    grid = np.indices([res.ds.sizes[dim] for dim in dims]).reshape(len(dims), -1)
    position = tuple(grid[dims.index(dim)] for dim in res.dims)
    dfs = {}
    for sid in PD_OUTPUTS:
        time, values = _timecourses(res, sid)
        padding = np.isnan(time)
        df = pd.DataFrame(dict(zip(["point", "draw"], grid, strict=False)))
        df["sid"] = sid
        df["min"] = np.where(padding, np.inf, values).min(axis=-1)[position]
        df["max"] = np.where(padding, -np.inf, values).max(axis=-1)[position]
        df["unit"] = Q(1, res.units[sid]).units
        dfs[sid] = df
    return dfs


def summarize(
    df: pd.DataFrame, key: str, quantiles: tuple[float, float]
) -> pd.DataFrame:
    """Get the median and the quantiles of a parameter over the draws of every point.

    Args:
        df: the parameters with the columns `point` and `draw`.
        key: the parameter.
        quantiles: the lower and the upper quantile.

    Returns:
        One row per point (the index), the columns `lower`, `median`, `upper`.
    """
    low, high = quantiles
    grouped = df.groupby("point")[key]
    return pd.DataFrame(
        {
            "lower": grouped.quantile(low),
            "median": grouped.median(),
            "upper": grouped.quantile(high),
        }
    ).astype(np.float64)
