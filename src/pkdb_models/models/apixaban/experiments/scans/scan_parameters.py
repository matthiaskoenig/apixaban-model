"""Parameter scans of the apixaban model.

The oral dose, the renal function, the degree of cirrhosis and the body weight
are scanned after a single oral dose of apixaban. The matplotlib figures show
the timecourses of the scans and the pharmacokinetic and pharmacodynamic
parameters of `apixaban_pk` together with the data of the studies.
"""

from pathlib import Path
from typing import Any, ClassVar, Literal, NamedTuple, NotRequired, TypedDict, override

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.cm import ScalarMappable
from matplotlib.colors import (
    Colormap,
    LinearSegmentedColormap,
    LogNorm,
    Normalize,
    TwoSlopeNorm,
    to_hex,
)
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter
from matplotlib.typing import ColorType
from pint import DimensionalityError
from pkpdsim.experiment import rename_units
from pkpdsim.scan import point_band, point_timecourse, scan_dimensions, start_values
from sbmlsim import Q
from sbmlsim.plot.serialization_matplotlib import FigureMPL
from sbmlsim.result import ScanResult
from sbmlsim.simulation import Dimension, Scan, Simulation
from sbmlutils.console import console

from pkdb_models.models.apixaban import MODEL
from pkdb_models.models.apixaban.apixaban_pk import summarize
from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)

#: pharmacokinetic and pharmacodynamic parameters of the studies, one file per scan
STUDY_DATA_PATH = Path(__file__).parent / "study_data"


class ScanSpec(TypedDict):
    """Definition of a single parameter scan."""

    parameter: str
    #: value of the reference simulation
    default: float
    range: np.ndarray
    scale: Literal["linear", "log"]
    #: the colormap, a matplotlib colormap or the colors at positions from 0
    #: to 1 along the range
    colormap: str | list[tuple[float, str]]
    units: str
    label: str
    #: the labels of the ticks of the colorbar, the minimum, the default and
    #: the maximum of the range without
    ticks: NotRequired[dict[float, str]]


class Panel(NamedTuple):
    """A panel of the timecourses of a scan."""

    sid: str
    #: the end of the time axis [hr]
    tend: float
    #: the distance of the ticks of the time axis [hr]
    tick: float


class Marker(NamedTuple):
    """The marker of a study, a shape filled completely or on one half."""

    shape: str
    fillstyle: Literal["full", "left", "bottom"]


def _position(value: float, vmin: float, vmax: float) -> float:
    """Get the position of a value on a logarithmic axis from vmin to vmax."""
    return float((np.log10(value) - np.log10(vmin)) / (np.log10(vmax) - np.log10(vmin)))


def _with(values: np.ndarray, *extra: float) -> np.ndarray:
    """Get the sorted values of a scan with the values `extra` added."""
    return np.unique(np.concatenate([values, np.asarray(extra, dtype=float)]))


def _unit(unit: str) -> str:
    """Get a unit as written on an axis, `-` for a dimensionless quantity."""
    return unit.replace("dimensionless", "-")


_CIRRHOSIS = ApixabanSimulationExperiment.cirrhosis_map
_CIRRHOSIS_COLORS = ApixabanSimulationExperiment.cirrhosis_colors
_RENAL = ApixabanSimulationExperiment.renal_map
_RENAL_COLORS = ApixabanSimulationExperiment.renal_colors
#: the diverging colormaps, whose light center is left out and centered at the
#: default of the scan
_DIVERGING = {"RdBu_r"}
#: the shapes of the markers of the studies, shapes which are told apart at the
#: size of a marker, filled, on the left half and on the bottom half
_SHAPES = ("s", "^", "D", "v", "o", "*", "X", "P", "<", ">")
_FILLSTYLES: tuple[Literal["full", "left", "bottom"], ...] = ("full", "left", "bottom")


class ApixabanParameterScan(ApixabanSimulationExperiment):
    """Scan the effect of parameters on the pharmacokinetics and pharmacodynamics.

    A single oral dose of 5 mg apixaban, simulated for 96 hr, the end of the
    longest partial AUC of the studies (`apixaban_pk.AUC_END_TIMES`). The
    figures show the timecourses of apixaban, its metabolites and the
    coagulation in the first 48 hr and the excreted amounts in the 96 hr,
    and the pharmacokinetic and pharmacodynamic parameters over the scanned
    parameter with the data of the studies.

    In a run over the draws of the fitted parameters (`run_simulation
    pkdb_models.models.apixaban --uncertainty`) every point of a scan is
    simulated for every draw; the figures draw the median of the draws with
    the band of their quantiles.
    """

    #: the end of the simulations [hr]
    tend = 96
    #: the output times of a run over the draws [hr]: every 0.05 hr in the
    #: first day (absorption and maximum, tmax about 2 hr), every 0.5 hr after
    #: it. The grid of `steps` for every draw of every point would need about
    #: 3.5 GB, this grid 0.5 GB.
    times_uncertainty: ClassVar[tuple[float, ...]] = tuple(
        np.unique(
            np.concatenate([np.linspace(0, 24, 481), np.linspace(24, tend, 145)])
        ).tolist()
    )
    #: the oral dose of the scans [mg]
    dose_api = 5
    #: the opacity of the bands of the draws of the fitted parameters
    band_alpha = 0.15

    #: the variables of the figures and of the parameters of `apixaban_pk`
    selections = (
        "time",
        "PODOSE_api",
        "KI__f_renal_function",
        "f_cirrhosis",
        "BW",
        "[Cve_api]",
        "[Cve_m1]",
        "[Cve_m7]",
        "Aurine_api",
        "Aurine_m1",
        "Aurine_m7",
        "Afeces_api",
        "Afeces_m1",
        "Afeces_m7",
        "INR",
        "PT",
        "mPT",
        "aPTT",
        "antiXa_activity",
        "INR_ratio",
        "PT_ratio",
        "mPT_ratio",
        "aPTT_ratio",
    )

    #: the substance of the data of the studies
    data_substance = "apixaban"
    # parameters of the studies which scale with the dose
    scalable_params: ClassVar[list[str]] = [
        "cmax",
        "auc_inf_obs",
        "aucend_12",
        "aucend_24",
        "aucend_48",
        "aucend_72",
        "aucend_96",
        "inrmax",
        "ptmax",
        "apttmax",
        "antixa_activitymax",
        "inr_ratiomax",
        "pt_ratiomax",
        "aptt_ratiomax",
    ]
    #: the pharmacodynamic outputs of the pharmacodynamic parameters
    #: (`<output>max`, the maximum of the output)
    pd_outputs: ClassVar[dict[str, str]] = {
        "inrmax": "INR",
        "ptmax": "PT",
        "apttmax": "aPTT",
        "inr_ratiomax": "INR_ratio",
        "pt_ratiomax": "PT_ratio",
        "aptt_ratiomax": "aPTT_ratio",
        "antixa_activitymax": "antiXa_activity",
    }

    study_data_files: ClassVar[dict[str, Path]] = {
        "renal_scan": STUDY_DATA_PATH / "parameters_renal.tsv",
        "hepatic_scan": STUDY_DATA_PATH / "parameters_hepatic.tsv",
        "dose_scan": STUDY_DATA_PATH / "parameters_dose.tsv",
        "bodyweight_scan": STUDY_DATA_PATH / "parameters_bodyweight.tsv",
    }

    font: ClassVar[dict[str, str | int]] = {"weight": "bold", "size": 20}
    tick_font_size = 17

    # keyword arguments of the markers of the data
    plot_kwargs: ClassVar[dict[str, Any]] = {
        "markeredgecolor": "black",
        "markeredgewidth": 0.8,
        "markersize": 8,
        "markerfacecoloralt": "white",
        "alpha": 0.9,
        "linestyle": "",
    }

    scan_map: ClassVar[dict[str, ScanSpec]] = {
        "dose_scan": {
            "parameter": "PODOSE_api",
            "default": dose_api,
            # the doses of the studies, 2.5 to 50 mg
            "range": np.array([0.5, 1, 2.5, 5, 7.5, 10, 15, 20, 25, 35, 50]),
            "scale": "linear",
            "colormap": "Oranges",
            "units": "mg",
            "label": "apixaban dose [mg]",
            "ticks": {0.5: "0.5", 5: "5", 25: "25", 50: "50"},
        },
        "renal_scan": {
            "parameter": "KI__f_renal_function",
            "default": 1.0,
            # 0.1 to 2, with the limits of the classes of the GFR
            "range": _with(
                np.array([0.1, 0.14, 0.27, 0.7, 1.4, 2.0]),
                *(v for k, v in _RENAL.items() if k != "End stage renal disease"),
            ),
            "scale": "log",
            # the colors of the classes at their renal function (of 0.1 to 2),
            # light greens for a normal and an increased renal function
            "colormap": [
                (0.0, _RENAL_COLORS["End stage renal disease"]),
                *(
                    (_position(_RENAL[key], 0.1, 2), _RENAL_COLORS[key])
                    for key in (
                        "Severe renal impairment",
                        "Moderate renal impairment",
                        "Mild renal impairment",
                    )
                ),
                (_position(1.0, 0.1, 2), "#a1d99b"),
                (1.0, "#c7e9c0"),
            ],
            "units": "dimensionless",
            "label": "renal function [-]",
            "ticks": {0.1: "0.1", 1.0: "1", 2.0: "2"},
        },
        "hepatic_scan": {
            "parameter": "f_cirrhosis",
            "default": 0.0,
            # with the degrees of the Child-Pugh classes
            "range": _with(
                np.array([0, 0.1, 0.2, 0.3, 0.5, 0.6, 0.9]),
                *(v for k, v in _CIRRHOSIS.items() if k != "Control"),
            ),
            "scale": "linear",
            # the colors of the classes at their degrees (of 0 to 0.9)
            "colormap": [
                (0.0, "#d0e1f2"),
                *(
                    (_CIRRHOSIS[key] / 0.9, _CIRRHOSIS_COLORS[key])
                    for key in (
                        "Mild cirrhosis",
                        "Moderate cirrhosis",
                        "Severe cirrhosis",
                    )
                ),
                (1.0, "#023858"),
            ],
            "units": "dimensionless",
            "label": "cirrhosis degree [-]",
            "ticks": {
                0.0: "0",
                _CIRRHOSIS["Mild cirrhosis"]: "CPT A",
                _CIRRHOSIS["Moderate cirrhosis"]: "CPT B",
                _CIRRHOSIS["Severe cirrhosis"]: "CPT C",
            },
        },
        "bodyweight_scan": {
            "parameter": "BW",
            "default": 75.0,
            # the body weights of the studies, 38 to 170 kg
            "range": np.array([38, 45, 55, 65, 75, 90, 105, 120, 140, 170, 200]),
            "scale": "linear",
            "colormap": "RdBu_r",
            "units": "kg",
            "label": "body weight [kg]",
        },
    }

    #: the timecourses of the figures of the scans
    scan_sids: ClassVar[dict[str, list[str]]] = {
        "dose_scan": [
            "[Cve_api]",
            "[Cve_m1]",
            "[Cve_m7]",
            "Aurine_api",
            "Afeces_api",
        ],
        "renal_scan": [
            "[Cve_api]",
            "Aurine_api",
            "Aurine_m1",
            "Aurine_m7",
            "Afeces_m1",
        ],
        "hepatic_scan": [
            "[Cve_api]",
            "[Cve_m1]",
            "[Cve_m7]",
            "Afeces_m1",
            "Afeces_m7",
        ],
        "bodyweight_scan": [
            "[Cve_api]",
            "[Cve_m1]",
            "[Cve_m7]",
            "Aurine_api",
            "Afeces_api",
        ],
    }
    #: the pharmacodynamic timecourses of every scan, the second row
    pd_sids: ClassVar[list[str]] = ["INR", "PT", "mPT", "aPTT", "antiXa_activity"]

    @override
    def simulations(self) -> dict[str, Scan]:
        scans = {}
        grid: dict[str, Any] = (
            {} if self.uncertainty is None else {"times": self.times_uncertainty}
        )
        for scan_key, scan_data in self.scan_map.items():
            # the simulation does not set what the dimension scans (the dose
            # of the dose scan), the dimension would replace it
            preinit_changes = {
                **self.default_changes(),
                "PODOSE_api": Q(self.dose_api, "mg"),
            }
            preinit_changes.pop(scan_data["parameter"], None)
            scans[f"scan_po_{scan_key}"] = Scan(
                simulation=Simulation(
                    time_unit="hr",
                    end=self.tend,
                    preinit_changes=preinit_changes,
                    **grid,
                ),
                dimensions=[
                    Dimension(
                        "dim_scan",
                        values={
                            scan_data["parameter"]: Q(
                                scan_data["range"], scan_data["units"]
                            )
                        },
                    ),
                ],
            )
        return scans

    def _scanned(self, res: ScanResult, scan: ScanSpec) -> np.ndarray:
        """Get the values of the scanned parameter at the points of the scan."""
        parameter_id = scan["parameter"]
        values = start_values(res, parameter_id)
        across = self._across()
        if across is not None:
            values = values.isel({across: 0})
        return Q(values.values, res.units[parameter_id]).to(scan["units"]).magnitude

    def _colormap(self, scan: ScanSpec) -> tuple[Colormap, Normalize]:
        """Get the colormap of a scan and the normalization of its values.

        The scans of the cirrhosis and of the renal function have the colors
        of the classes of the impairments (`pkpdsim.impairment`) at the values
        of the classes. The colormaps of matplotlib leave out their lightest
        colors, so that every curve is visible on white: the start of a
        sequential colormap, the center of a diverging one, which is centered
        at the default of the scan.
        """
        rmin, rmax = float(scan["range"][0]), float(scan["range"][-1])
        colormap = scan["colormap"]
        if isinstance(colormap, str):
            base = mpl.colormaps[colormap]
            positions = (
                np.concatenate([np.linspace(0, 0.4, 128), np.linspace(0.6, 1, 128)])
                if colormap in _DIVERGING
                else np.linspace(0.3, 1.0, 256)
            )
            cmap: Colormap = LinearSegmentedColormap.from_list(
                f"{colormap}_visible", [base(v) for v in positions]
            )
            if colormap in _DIVERGING:
                return cmap, TwoSlopeNorm(vmin=rmin, vcenter=scan["default"], vmax=rmax)
        else:
            cmap = LinearSegmentedColormap.from_list("impairment", colormap)
        if scan["scale"] == "linear":
            return cmap, Normalize(vmin=rmin, vmax=rmax, clip=False)
        return cmap, LogNorm(vmin=rmin, vmax=rmax, clip=False)

    def _color(self, scan: ScanSpec, value: float) -> str:
        """Get the color of a value of the scanned parameter, the default black.

        Raises:
            ValueError: if the value is out of the scanned range.
        """
        rmin, rmax = float(scan["range"][0]), float(scan["range"][-1])
        if not rmin <= value <= rmax:
            raise ValueError(f"Value {value} is out of range ({rmin}, {rmax}).")
        if np.isclose(value, scan["default"]):
            return "black"
        cmap, norm = self._colormap(scan)
        return to_hex(cmap(norm(value)), keep_alpha=False)

    def _colorbar(self, f: Figure, axes: np.ndarray, scan: ScanSpec) -> None:
        """Draw the colorbar of a scan above its panels, the default in black."""
        cmap, norm = self._colormap(scan)
        cbar = f.colorbar(
            ScalarMappable(norm=norm, cmap=cmap),
            ax=axes.ravel().tolist(),
            location="top",
            shrink=0.4,
            aspect=30,
        )
        # the gradient as vector cells: matplotlib rasterizes it into an
        # embedded image, which some SVG viewers do not show; the edges of
        # the cells in their color close the seams between them
        if cbar.solids is not None:
            cbar.solids.set_rasterized(False)
            cbar.solids.set_edgecolor("face")
        rmin, rmax = float(scan["range"][0]), float(scan["range"][-1])
        ticks = scan.get(
            "ticks",
            {value: f"{value:g}" for value in sorted({rmin, rmax, scan["default"]})},
        )
        cbar.ax.minorticks_off()
        cbar.set_ticks(list(ticks), labels=list(ticks.values()))
        cbar.ax.tick_params(labelsize=self.tick_font_size)
        cbar.ax.axvline(x=scan["default"], color="black", linewidth=4)
        cbar.set_label(scan["label"], size=self.tick_font_size + 3, weight="bold")

    @override
    def figures_mpl(self) -> dict[str, FigureMPL]:
        """Matplotlib figures."""
        return {
            **self.figures_mpl_timecourses(),
            **self.figures_mpl_pk_pd(self._parameters()),
        }

    def _parameters(self) -> dict[str, pd.DataFrame]:
        """Get the parameters of apixaban of every scan, per draw with draws.

        The pharmacokinetic parameters of apixaban with the pharmacodynamic
        parameters (`<output>max`, `<output>max_unit`), one row per point of
        the scan (and draw), by simulation key.
        """
        pk_dfs = self.calculate_apixaban_pk()
        pd_dfs = self.calculate_apixaban_pd()
        position = ["point"] if self.uncertainty is None else ["point", "draw"]
        tables = {}
        for key, pk_df in pk_dfs.items():
            table = pk_df[pk_df.substance == "api"]
            for par_id, output in self.pd_outputs.items():
                df = pd_dfs[key][output]
                table = table.merge(
                    pd.DataFrame(
                        {
                            **{column: df[column] for column in position},
                            par_id: df["max"].astype(float),
                            f"{par_id}_unit": df["unit"].map(str),
                        }
                    ),
                    on=position,
                    validate="one_to_one",
                )
            tables[key] = table
        return tables

    def _timecourse(
        self,
        ax: Axes,
        res: ScanResult,
        panel: Panel,
        point: dict[str, int],
        color: ColorType,
        band: bool,
    ) -> tuple[np.ndarray, np.ndarray, float, float]:
        """Draw the timecourse of a point of a scan, with the band of its draws.

        Args:
            ax: the panel.
            res: the result of the scan.
            panel: the variable and the time axis of the panel.
            point: the position of the point along the dimension of the scan.
            color: the color of the point.
            band: draw the band of the draws in a run over them.

        Returns:
            The time and the values (the median of the draws in a run over
            them) until the end of the panel, and the lowest and the highest
            value drawn, of the band if it is drawn.
        """
        sid = panel.sid
        run = self.uncertainty
        if run is None:
            time, values = point_timecourse(res, sid, **point)
            lower = upper = values
        else:
            time, lower, values, upper = point_band(
                res, sid, across=run.id, quantiles=run.quantiles, **point
            )
        t = Q(time, res.units["time"]).to(self.units["time"]).magnitude
        shown = t <= panel.tend

        def convert(v: np.ndarray) -> np.ndarray:
            """Get the values until the end of the panel in the unit of the figure."""
            return Q(v[shown], res.units[sid]).to(self.units[sid]).magnitude

        c, c_lower, c_upper = convert(values), convert(lower), convert(upper)
        if not band:
            c_lower = c_upper = c
        elif run is not None:
            ax.fill_between(
                t[shown],
                c_lower,
                c_upper,
                color=color,
                alpha=self.band_alpha,
                linewidth=0,
            )
        ax.plot(t[shown], c, color=color, linewidth=2.0)
        return t[shown], c, float(np.nanmin(c_lower)), float(np.nanmax(c_upper))

    def _panels(self, scan_key: str) -> list[Panel]:
        """Get the panels of the timecourses of a scan.

        The concentrations and the coagulation in the first 48 hr, the
        excreted amounts until the end of the simulation.
        """
        return [
            Panel(sid, self.tend, 24)
            if sid.startswith(("Aurine", "Afeces"))
            else Panel(sid, 48, 12)
            for sid in [*self.scan_sids[scan_key], *self.pd_sids]
        ]

    def figures_mpl_timecourses(self) -> dict[str, FigureMPL]:
        """Timecourses of the scans, a figure per scan.

        The default of the scanned parameter is black and drawn on top. In a
        run over the draws the default and the ends of the range have the
        band of their draws (the bands of every point cover each other); the
        axes include the bands. The concentrations and amounts start at zero,
        the coagulation at its lowest value.
        """
        figures: dict[str, FigureMPL] = {}
        for scan_key, scan_data in self.scan_map.items():
            panels = self._panels(scan_key)
            ncols = 5
            nrows = len(panels) // ncols
            f, axes = plt.subplots(
                nrows=nrows,
                ncols=ncols,
                figsize=(6 * ncols, 5 * nrows + 1),
                dpi=150,
                layout="constrained",
                squeeze=False,
            )
            res = self.results[f"task_scan_po_{scan_key}"]
            (scandim,) = scan_dimensions(res, self._across())
            par_vec = self._scanned(res, scan_data)

            for ax, panel in zip(axes.flatten(), panels, strict=True):
                bottom, top = np.inf, -np.inf
                default: tuple[np.ndarray, np.ndarray] | None = None
                for k_par, par in enumerate(par_vec):
                    color = self._color(scan_data, float(par))
                    band = color == "black" or k_par in (0, len(par_vec) - 1)
                    t, c, low, high = self._timecourse(
                        ax, res, panel, {scandim: k_par}, color, band
                    )
                    bottom, top = min(bottom, low), max(top, high)
                    if color == "black":
                        default = (t, c)

                # the default on top
                if default is not None:
                    ax.plot(*default, color="black", linewidth=2.0)

                ax.set_xlim(0, panel.tend)
                ax.set_xticks(np.arange(0, panel.tend + 1, panel.tick))
                if panel.sid in self.pd_sids:
                    margin = 0.05 * (top - bottom)
                    ax.set_ylim(bottom - margin, top + margin)
                else:
                    ax.set_ylim(0, 1.05 * top if top > 0 else 1.0)
                ax.set_xlabel(
                    f"{self.label_time} [{self.units['time']}]", fontdict=self.font
                )
                ax.set_ylabel(
                    f"{self.labels[panel.sid]} [{_unit(self.units[panel.sid])}]",
                    fontdict=self.font,
                )
                ax.tick_params(axis="both", labelsize=self.tick_font_size)

            self._colorbar(f, axes, scan_data)
            figures[f"timecourse__pk__{scan_key}"] = f

        return figures

    def _summary(
        self, df: pd.DataFrame, key: str, target: str
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Get a parameter at the points of a scan, the median and the band of the draws.

        Returns:
            The values (the median of the draws in a run over them), and the
            lower and the upper quantile, the values without draws, in the
            unit `target`.
        """
        unit = str(df[f"{key}_unit"].iloc[0])
        run = self.uncertainty
        if run is None:
            values = Q(df[key].to_numpy(dtype=float), unit).to(target).magnitude
            return values, values, values
        summary = summarize(df, key, run.quantiles)
        median, lower, upper = (
            Q(summary[column].to_numpy(), unit).to(target).magnitude
            for column in ["median", "lower", "upper"]
        )
        return median, lower, upper

    def figures_mpl_pk_pd(
        self, tables: dict[str, pd.DataFrame]
    ) -> dict[str, FigureMPL]:
        """Pharmacokinetic and pharmacodynamic parameters of the scans, a figure per scan."""
        figures = {}
        for scan_id, scan_info in self.scan_map.items():
            # parameters of the studies, the international units of the
            # anti-factor Xa activity read as the units of the data (`data_units`)
            df_exp = rename_units(
                pd.read_csv(self.study_data_files[scan_id], sep="\t", comment="#"),
                self.data_unit_names(),
            )
            res: ScanResult = self.results[f"task_scan_po_{scan_id}"]
            figures[f"fig_can_po__{scan_id}"] = self._plot_scan_combined(
                df_exp=df_exp[df_exp["substance"] == self.data_substance],
                par_values=self._scanned(res, scan_info),
                df_sim=tables[f"scan_po_{scan_id}"],
                scan_id=scan_id,
                scan_info=scan_info,
            )

        return figures

    def _plot_scan_combined(
        self,
        df_exp: pd.DataFrame,
        par_values: np.ndarray,
        df_sim: pd.DataFrame,
        scan_id: str,
        scan_info: ScanSpec,
    ) -> FigureMPL:
        """Create the figure of the parameters of a scan with the data of the studies.

        A panel per pharmacokinetic parameter of the studies and per
        pharmacodynamic parameter; the studies have one legend right of the
        panels, a study one marker in every panel.
        """
        present = set(df_exp["parameter"].astype(str))
        parameters = [p for p in self.pk_labels if p in present] + list(self.pd_labels)
        studies = sorted(df_exp["study"].astype(str).unique())
        markers = {
            study: Marker(
                _SHAPES[k % len(_SHAPES)],
                _FILLSTYLES[(k // len(_SHAPES)) % len(_FILLSTYLES)],
            )
            for k, study in enumerate(studies)
        }

        ncols = 4
        nrows = (len(parameters) + ncols - 1) // ncols
        fig, axes = plt.subplots(
            nrows=nrows,
            ncols=ncols,
            figsize=(6.5 * ncols + 3, 6 * nrows),
            dpi=150,
            layout="constrained",
            squeeze=False,
        )
        axes = axes.flatten()
        colors = np.array([self._color(scan_info, float(v)) for v in par_values])

        for ax, par_id in zip(axes, parameters, strict=False):
            ax.axvline(
                x=scan_info["default"],
                color="grey",
                linestyle="--",
                linewidth=1.5,
                zorder=1,
            )
            y, y_lower, y_upper = self._summary(
                df_sim, par_id, self._parameter_unit(par_id)
            )
            if self.uncertainty is not None:
                ax.fill_between(
                    par_values,
                    y_lower,
                    y_upper,
                    color="black",
                    alpha=self.band_alpha,
                    linewidth=0,
                )
            ax.plot(par_values, y, color="black", linewidth=2.5, zorder=2)
            ax.scatter(
                par_values,
                y,
                s=60,
                c=colors,
                edgecolors="black",
                linewidths=1.2,
                zorder=3,
            )
            max_exp = self._add_study_data_to_plot(
                df_exp[df_exp["parameter"] == par_id],
                par_id,
                ax,
                markers,
                scan_id,
                scan_info,
            )
            self._styling(
                ax, par_id, max(float(np.nanmax(y_upper)), max_exp), scan_info
            )

        # Hide unused axes
        for ax in axes[len(parameters) :]:
            ax.set_visible(False)

        if markers:
            fig.legend(
                handles=[
                    Line2D(
                        [0],
                        [0],
                        marker=marker.shape,
                        fillstyle=marker.fillstyle,
                        markerfacecolor="grey",
                        markerfacecoloralt="white",
                        markeredgecolor="black",
                        linestyle="None",
                        markersize=10,
                        label=study,
                    )
                    for study, marker in markers.items()
                ],
                title="Studies",
                title_fontproperties={"weight": "bold", "size": self.tick_font_size},
                fontsize=self.tick_font_size - 2,
                loc="outside right upper",
            )

        return fig

    def _parameter_unit(self, parameter: str) -> str:
        """Unit of a pharmacokinetic or pharmacodynamic parameter in the figures."""
        if parameter in self.pd_units:
            return self.pd_units[parameter]
        return self.pk_units[parameter]

    def _parameter_label(self, parameter: str) -> str:
        """Axis label of a pharmacokinetic or pharmacodynamic parameter."""
        label = (
            self.pk_labels[parameter]
            if parameter in self.pk_labels
            else self.pd_labels[parameter]
        )
        return f"{label} [{_unit(self._parameter_unit(parameter))}]"

    def _add_study_data_to_plot(
        self,
        df_exp_par: pd.DataFrame,
        par_id: str,
        ax: Axes,
        markers: dict[str, Marker],
        scan_id: str,
        scan_info: ScanSpec,
    ) -> float:
        """Add the data of the studies of a parameter to the plot.

        The data of other doses are scaled to the dose of the scans, but in
        the dose scan.

        Returns:
            The largest value of the data with its errors, for the scaling of
            the axis.
        """
        # values of the scanned parameter of the conditions of the studies
        condition_map = self.get_class_data(scan_id=scan_id)
        colors = self.get_color_map(scan_id) or {}

        max_y = 0.0
        for _, row in df_exp_par.iterrows():
            x_err = None
            dose_ratio = 1.0
            # x position (value of the scanned parameter) by scan
            if scan_id == "dose_scan":
                spar_value = (
                    Q(row["dose"], row["dose_unit"]).to(scan_info["units"]).magnitude
                )
                study_color = self._color(scan_info, spar_value)
            else:
                if scan_id == "bodyweight_scan":
                    spar_value = (
                        Q(row["weight"], row["weight_unit"])
                        .to(scan_info["units"])
                        .magnitude
                    )
                    study_color = self._color(scan_info, spar_value)
                    if "weight_sd" in row and pd.notna(row["weight_sd"]):
                        x_err = (
                            Q(row["weight_sd"], row["weight_unit"])
                            .to(scan_info["units"])
                            .magnitude
                        )
                else:
                    # renal and hepatic scans: the condition is the x position
                    condition = (
                        str(row["condition"]).lower().strip()
                        if pd.notna(row["condition"])
                        else None
                    )
                    if condition is None or condition not in condition_map:
                        continue
                    spar_value = condition_map[condition]
                    study_color = colors.get(condition, "grey")

                if row["dose"] > 0:
                    dose_ratio = self.dose_api / row["dose"]

            # column of the data
            data_column = None
            for col in ["mean", "value", "median", "geom_mean"]:
                if col in row and not pd.isna(row[col]):
                    data_column = col
                    break
            if data_column is None:
                continue

            y_value = self._row_value(row, data_column, par_id, dose_ratio)
            if y_value is None or not np.isfinite(y_value):
                continue
            max_row_y = self._add_data_point_to_plot(
                ax,
                spar_value,
                y_value,
                x_err,
                self._row_value(row, "sd", par_id, dose_ratio),
                self._row_value(row, "min", par_id, dose_ratio),
                self._row_value(row, "max", par_id, dose_ratio),
                markers[str(row["study"])],
                study_color,
            )
            max_y = max(max_y, max_row_y)

        return max_y

    def _row_value(
        self, row: pd.Series, column: str, parameter: str, dose_ratio: float
    ) -> float | None:
        """Get a value of a row of the data in the unit of the parameter, `None` if missing."""
        if column not in row or pd.isna(row[column]):
            return None
        return self._extract_data_point(row[column], row["unit"], parameter, dose_ratio)

    def _extract_data_point(
        self, data_point: float, units: str, parameter: str, dose_ratio: float
    ) -> float:
        """Convert a value of the data to the unit of the parameter, scaled to the dose."""
        st_units = self._parameter_unit(parameter)
        try:
            value = Q(float(data_point), units).to(st_units).magnitude
        except DimensionalityError:
            # a mass concentration of apixaban
            quantity = Q(float(data_point), units) / self.Mr.api
            try:
                value = quantity.to(st_units).magnitude
            except DimensionalityError as err:
                console.print(
                    f"An error occurred while transforming units: {err}. "
                    "Check whether the units of the data can be transformed "
                    "to the units of the pk parameter in the base experiment."
                )
                value = np.nan

        if parameter in self.scalable_params and dose_ratio != 1.0:
            return value * dose_ratio

        return value

    def _add_data_point_to_plot(
        self,
        ax: Axes,
        x_pos: float,
        y_value: float,
        x_err: float | None,
        y_err: float | None,
        min_value: float | None,
        max_value: float | None,
        marker: Marker,
        study_color: str,
    ) -> float:
        """Plot a data point of a study with its errors and range.

        Returns:
            The upper end of the point with its error, for the scaling of the axis.
        """
        style: dict[str, Any] = {
            "marker": marker.shape,
            "fillstyle": marker.fillstyle,
            "markerfacecolor": study_color,
            **self.plot_kwargs,
        }
        if y_err is not None or x_err is not None:
            (point, *_) = ax.errorbar(
                x_pos,
                y_value,
                xerr=x_err,
                yerr=y_err,
                capsize=6,
                ecolor="black",
                zorder=4,
                **style,
            )
        else:
            (point,) = ax.plot(x_pos, y_value, zorder=4, **style)
        # the marker of a value at the limit of the axis is not cut (a renal
        # clearance of zero), the error bars below zero are
        point.set_clip_on(False)
        y_limit = y_value + (y_err or 0.0)

        if min_value is not None and max_value is not None:
            ax.vlines(
                x_pos,
                min_value,
                max_value,
                color="black",
                linewidth=2,
                zorder=4,
                linestyles="dashed",
            )
            ax.scatter(x_pos, min_value, s=15, color="black", zorder=5)
            ax.scatter(x_pos, max_value, s=15, color="black", zorder=5)
            y_limit = max(y_limit, max_value)

        return y_limit

    def _styling(self, ax: Axes, key: str, ymax: float, scan_info: ScanSpec) -> None:
        """Apply styling to the axis of a parameter, the y axis from zero."""
        ax.tick_params(axis="both", labelsize=self.tick_font_size)
        ax.tick_params(axis="both", which="major", length=8, width=3)
        ax.set_xlabel(scan_info["label"], fontdict=self.font)
        ax.set_ylabel(self._parameter_label(key), fontdict=self.font)
        ax.set_ylim(bottom=0.0, top=1.1 * ymax if ymax > 0 else 1.0)
        ax.set_xscale(scan_info["scale"])
        if scan_info["scale"] == "log":
            # the ticks of the colorbar instead of the powers of ten
            ticks = scan_info.get("ticks")
            if ticks is not None:
                ax.set_xticks(list(ticks), labels=list(ticks.values()))
            else:
                ax.xaxis.set_major_formatter(
                    FuncFormatter(lambda value, _: f"{value:g}")
                )
            ax.xaxis.set_minor_formatter(FuncFormatter(lambda *_: ""))

    def get_class_data(self, scan_id: str) -> dict[str, float]:
        """Get the values of the scanned parameter of the conditions of the studies.

        Args:
            scan_id: the scan, a key of `scan_map`.

        Returns:
            The value of the scanned parameter by condition, empty for the dose
            and body weight scans.
        """
        if scan_id == "renal_scan":
            return {
                "normal": self.renal_map["Normal renal function"],
                "mild": self.renal_map["Mild renal impairment"],
                "moderate": self.renal_map["Moderate renal impairment"],
                "severe": self.renal_map["Severe renal impairment"],
                "end_stage": self.renal_map["End stage renal disease"],
            }
        if scan_id == "hepatic_scan":
            return {
                "normal": self.cirrhosis_map["Control"],
                "mild": self.cirrhosis_map["Mild cirrhosis"],
                "moderate": self.cirrhosis_map["Moderate cirrhosis"],
                "severe": self.cirrhosis_map["Severe cirrhosis"],
            }
        return {}

    def get_color_map(self, scan_key: str) -> dict[str, str] | None:
        """Get the colors of the conditions of the renal and hepatic scans.

        Args:
            scan_key: the scan, a key of `scan_map`.

        Returns:
            The colors by condition, None for the other scans.
        """
        predefined_maps = {
            "renal_scan": {
                "normal": self.renal_colors["Normal renal function"],
                "mild": self.renal_colors["Mild renal impairment"],
                "moderate": self.renal_colors["Moderate renal impairment"],
                "severe": self.renal_colors["Severe renal impairment"],
                "end_stage": self.renal_colors["End stage renal disease"],
            },
            "hepatic_scan": {
                "normal": self.cirrhosis_colors["Control"],
                "mild": self.cirrhosis_colors["Mild cirrhosis"],
                "moderate": self.cirrhosis_colors["Moderate cirrhosis"],
                "severe": self.cirrhosis_colors["Severe cirrhosis"],
            },
        }
        return predefined_maps.get(scan_key)


if __name__ == "__main__":
    MODEL.run_experiments(
        ApixabanParameterScan, output_dir=ApixabanParameterScan.__name__
    )
