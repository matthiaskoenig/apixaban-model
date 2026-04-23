"""Parameter scans apixaban."""
from pathlib import Path
from typing import Dict

import matplotlib.axes
import numpy as np
import pandas as pd
from matplotlib.colors import to_hex, Colormap
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from pint import DimensionalityError
from sbmlsim.simulation import Timecourse, TimecourseSim, ScanSim, Dimension
from sbmlsim.plot.serialization_matplotlib import FigureMPL
from sbmlsim.plot.serialization_matplotlib import plt
from sbmlutils.console import console
from sympy.physics.units import Quantity

from pkdb_models.models.apixaban.experiments.base_experiment import (
    ApixabanSimulationExperiment,
)
from pkdb_models.models.apixaban.helpers import run_experiments


class ApixabanDataParameterScan(ApixabanSimulationExperiment):
    """Scan the effect of parameters on pharmacokinetics."""

    tend = 48 * 60
    steps = 2000
    dose_api = 5  # [mg]

    study_markers = ['s', '^', 'D', 'v', '<', '>', 'p', '*', 'h', 'X', 'P', 'o']

    substances = {"api": "apixaban"}
    # Define scalable parameters
    scalable_params = ["cmax", "aucinf", "aucend_12", "aucend_24", "aucend_48",
                       "aucend_72", "aucend_96", "inrmax", "ptmax", "apttmax",
                       "antixa_activitymax", "inr_ratiomax", "pt_ratiomax",
                       "aptt_ratiomax"
                       ]

    study_data_files = {
        "renal_scan":
            str(Path(__file__).parent / "study_data" / "parameters_renal.tsv"),
        "hepatic_scan":
            str(Path(__file__).parent / "study_data" / "parameters_hepatic.tsv"),
        "dose_scan":
            str(Path(__file__).parent / "study_data" / "parameters_dose.tsv"), # check doses
        "bodyweight_scan":
            str(Path(__file__).parent / "study_data" / "parameters_bodyweight.tsv"),
        "food_scan":
            str(Path(__file__).parent / "study_data" / "parameters_food.tsv"),
    }

    font = {"weight": "bold", "size": 20}
    tick_font_size = 17

    plot_kwargs = {
        "markeredgecolor": 'black',
        "markeredgewidth": 0.8,
        "markersize": 8,
        "alpha": 0.9,
        "linestyle": ''
    }

    num_points = 10
    scan_map = {
        "bodyweight_scan": {
            "parameter": "BW",
            "default": 75.0,
            "range": np.sort(
                np.append(np.linspace(38, 200, num=num_points), [75.0])
            ),
            # "range": np.logspace(-2, 2, num=21),
            "scale": "linear",
            "colormap": "bwr",
            "units": "kg",
            "label": "bodyweight [kg]",
            "legend_position": (0.95, 0.95),
        },
        "hepatic_scan": {
            "parameter": "f_cirrhosis",
            "default": 0.0,
            "range": np.linspace(0, 0.7, num=num_points),
            # "range": np.logspace(-2, 2, num=21),
            "scale": "linear",
            "colormap": "Blues",
            "units": "dimensionless",
            "label": "cirrhosis degree [-]",
            "legend_position": (0.95, 0.95),
        },
        "renal_scan": {
            "parameter": "KI__f_renal_function",
            # "range": np.linspace(0.1, 1.9, num=num_points),
            "default": 1.0,
            "range": np.sort(
                np.append(np.logspace(-1, 1, num=num_points), [1.0])
            ),  # [10^-1=0.1, 10^1=10]
            "scale": "log",
            "colormap": "Greens_r",
            "units": "dimensionless",
            "label": "renal function [-]",
            "legend_position": (0.95, 0.95),
        },
        "dose_scan": {
            "parameter": "PODOSE_api",
            "default": 5,
            "range": np.sort(
                # np.append(np.linspace(1, 100, num=num_points), [10])
                [0.5, 1, 2.5, 5, 10, 20, 40, 60, 80, 100]
            ),  # [10^-1=0.1, 10^1=10]
            # "range": np.sort(
            #     np.append(np.logspace(1, 2, num=num_points), [50])
            # ),  # [10^-1=0.1, 10^1=10]
            "scale": "linear",
            "colormap": "Oranges",
            "units": "mg",
            "label": "apixaban dose [mg]",
            "legend_position": (0.95, 0.95),
        },
        "food_scan": {
            "parameter": "GU__f_absorption",
            # "range": np.linspace(0.1, 1.9, num=num_points),
            "default": 1,
            "range": np.sort(
                np.append(np.logspace(-1, 0.18, num=num_points), [1])
            ),  # [10^-1=0.1, 10^0.18=1.5]
            "scale": "log",
            "colormap": "Purples",
            "units": "dimensionless",
            "label": "fraction absorbed [-]",
            "legend_position": (0.25, 0.95),
        },
    }

    def simulations(self) -> Dict[str, ScanSim]:
        Q_ = self.Q_
        tcscans = {}

        for scan_key, scan_data in self.scan_map.items():
            if scan_key == "dose_scan":

                tcscans[f"scan_po_{scan_key}"] = ScanSim(
                    simulation=TimecourseSim(
                        Timecourse(
                            start=0,
                            end=24 * 60,  # 24 hours
                            steps=5000,
                            changes={
                                **self.default_changes(),
                            },
                        )
                    ),
                    dimensions=[
                        Dimension(
                            "dim_scan",
                            changes={
                                scan_data["parameter"]: Q_(
                                    scan_data["range"], scan_data["units"]
                                )
                            },
                        ),
                    ],
                )
            else:
                tcscans[f"scan_po_{scan_key}"] = ScanSim(
                    simulation=TimecourseSim(
                        Timecourse(
                            start=0,
                            end=24 * 60,  # 24 hours
                            steps=5000,
                            changes={
                                **self.default_changes(),
                                "PODOSE_api": Q_(self.dose_api, "mg"),
                            },
                        )
                    ),
                    dimensions=[
                        Dimension(
                            "dim_scan",
                            changes={
                                scan_data["parameter"]: Q_(
                                    scan_data["range"], scan_data["units"]
                                )
                            },
                        ),
                    ],
                )

        return tcscans

    def figures_mpl(self) -> Dict[str, FigureMPL]:
        """Matplotlib figures."""
        # calculate pharmacokinetic and pharmacodynamic parameters
        pk_dfs = self.calculate_apixaban_pk()
        pd_dfs = self.calculate_apixaban_pd()
        reformated_pd_dfs = {}
        pk_pd_df = {}

        for scan_id, pddata_dict in pd_dfs.items():
            for par_id, df in pddata_dict.items():
                renamed_cols = {
                    "sid": f"{par_id.lower()}",
                    "min": f"{par_id.lower()}min",
                    "max": f"{par_id.lower()}max",
                    "unit": f"{par_id.lower()}max_unit",
                }
                df.rename(columns=renamed_cols, inplace=True)
                if not f"scan_po_{scan_id}" in reformated_pd_dfs:
                    reformated_pd_dfs[f"scan_po_{scan_id}"] = df
                else:
                    reformated_pd_dfs[f"scan_po_{scan_id}"] = pd.concat([reformated_pd_dfs[f"scan_po_{scan_id}"], df], axis=1)

        for scan_id, pk_df in pk_dfs.items():
            pk_pd_df[scan_id] = pd.concat([pk_df, reformated_pd_dfs[f"scan_po_{scan_id}"]], axis=1)

        return {
            **self.figures_mpl_pk_pd(pk_pd_df),
        }

    def figures_mpl_pk_pd(self, pk_pd_dfs: dict[str, pd.DataFrame]) -> Dict[str, FigureMPL]:
        """Visualize dependency of pharmacokinetic and pharmacodynamic parameters for each scan type."""
        figures = {}

        # Create one figure per scan type
        for scan_id, scan_info in self.scan_map.items():
            # Read study data
            df_exp = pd.read_csv(self.study_data_files[scan_id], sep='\t', comment='#')

            # Run scan simulation
            xres = self.results[f"task_scan_po_{scan_id}"]
            # Get scanned parameter's values vector (x axis), ensure units are correct
            par_values = self.Q_(
                xres[scan_info["parameter"]].values[0], xres.uinfo[scan_info["parameter"]]
            ).to(scan_info["units"])

            # Get calculated for this scan pk and pd parameters
            df_sim = pk_pd_dfs[f"scan_po_{scan_id}"]

            colors = self.get_color_map(scan_id, scan_info)

            # Prepare data dictionary for plotting
            data_dict = {
                "df_exp": df_exp,
                "par_values": par_values,
                "df_sim": df_sim,
            }

            fig_key = f"fig_can_po__{scan_id}"
            figures[fig_key] = self._plot_scan_combined(
                data_dict=data_dict,
                colors=colors,
                scan_id=scan_id,
                scan_info=scan_info
            )

        return figures

    def _plot_scan_combined(self, data_dict: dict[str, pd.DataFrame | Quantity], colors: Colormap, scan_id: str, scan_info: dict):
        """Create combined figure with all PK parameters for a single scan type."""

        # Scan options
        is_dose_scan = scan_id == "dose_scan"
        is_bodyweight_scan = scan_id == "bodyweight_scan"

        # Get PK and PD parameters to plot for each scan
        param_studies = data_dict["df_exp"]['parameter'].unique()
        pk_parameters = [pk_parameter for pk_parameter in param_studies if pk_parameter in self.pk_labels.keys()]
        pd_parameters = [pd_parameter for pd_parameter in self.pd_labels.keys()]
        parameters = pk_parameters + pd_parameters

        ncols = 4
        nrows = (len(parameters) + ncols - 1) // ncols
        fig, axes = plt.subplots(
            nrows=nrows, ncols=ncols, figsize=(6.5 * ncols, 6 * nrows), dpi=150,
            layout="constrained",
            squeeze=False,
        )
        axes = axes.flatten()

        for kp, par_id in enumerate(parameters):
            ax = axes[kp]
            max_yaxis = 0.0
            legend_study_markers = {}

            # Only show reference line for non-dose scans
            if not is_dose_scan:
                ax.axvline(x=scan_info["default"], color="grey", linestyle="--", linewidth=1.5)

            for substance_id, substance_name in self.substances.items():

                # Filter simulation results for the current substance
                df_sim_subs = data_dict["df_sim"][data_dict["df_sim"].substance == substance_id].copy()
                if not df_sim_subs.empty:
                    # Get PK or PD parameter values, ensure units are correct
                    if par_id in self.pk_labels.keys():
                        units = self.pk_units[par_id]
                    if par_id in self.pd_labels.keys():
                        units = self.pd_units[par_id]
                    y = (self.Q_(df_sim_subs[f"{par_id}"].to_numpy(), df_sim_subs[f"{par_id}_unit"].values[0]).
                         to(units))

                    # Plot simulations
                    ax.plot(
                        data_dict["par_values"],
                        y,
                        marker="o",
                        linestyle="-",
                        color="black",
                        markeredgecolor="black",
                        linewidth=2.5,
                        markersize=7,
                        label="",
                    )

                    # Get maximum y-value for axis scaling
                    max_yaxis = max(max_yaxis, np.nanmax(y.magnitude))

                if not data_dict["df_exp"].empty:
                    # Filter studies data for the current substance and current parameter
                    df_exp_subs = data_dict["df_exp"][
                        (data_dict["df_exp"]['substance'] == substance_name) &
                        (data_dict["df_exp"]['parameter'] == par_id)
                        ]
                    if not df_exp_subs.empty:
                        # Get unique markers for studies
                        studies = df_exp_subs['study'].unique()
                        study_marker_map = {study: self.study_markers[i % len(self.study_markers)] for i, study in
                                            enumerate(studies)}
                        # Plot experimental data and get maximum y-value for axis scaling
                        ax, max_exp = self._add_study_data_to_plot(
                            df_exp_subs,
                            par_id,
                            ax,
                            study_marker_map,
                            scan_id,
                            scan_info,
                            is_dose_scan,
                            is_bodyweight_scan,
                            colors,
                        )
                        # Track which studies have been added to legend across all substances
                        legend_study_markers.update(study_marker_map)
                        if max_exp is not None:
                            max_yaxis = max(max_yaxis, max_exp)

            ax = self._add_legend_based_on_study_map(ax, legend_study_markers, scan_info["legend_position"])
            ax = self._styling(ax, par_id, max_yaxis, scan_info, is_dose_scan)

            axes[kp] = ax

        # Hide unused axes
        for i in range(len(parameters), len(axes)):
            axes[i].set_visible(False)

        return fig

    def _add_study_data_to_plot(self, df_exp_subs: pd.DataFrame, pk_par_id: str, ax: plt.Axes,
                                study_marker_map: dict, scan_id: str, scan_info: dict,
                                is_dose_scan: bool, is_bodyweight_scan: bool, colors: dict = None) -> tuple[plt.Axes, float]:
        """Add experimental study data to the plot for a given PK parameter."""
        Q_ = self.Q_

        # Get condition to x-axis mapping
        condition_map = self.get_class_data(scan_id=scan_id)

        # Track maximum y-value for axis scaling
        max_y = 0.0

        # Plot each data point
        for idx, row in df_exp_subs.iterrows():
            # Get x-position (scanned parameter value) based on scan type
            if is_dose_scan:
                spar_value = Q_(row['dose'], row["dose_unit"]).to(scan_info["units"]).magnitude
                dose_ratio = 1.0  # No scaling for dose scan
                study_color = self._get_color_for_value(row["dose"], scan_info)
            else:
                if is_bodyweight_scan:
                    spar_value = Q_(row['weight'], row["weight_unit"]).to(scan_info["units"]).magnitude
                    study_color = self._get_color_for_value(row["weight"], scan_info)
                else:
                    # For renal/hepatic scans, map condition to x-position
                    condition = row['condition'].lower().strip() if pd.notna(row['condition']) else None
                    if condition not in condition_map:
                        continue
                    spar_value = condition_map[condition]
                    study_color = colors.get(condition, "grey")

                # Check if scaling is needed
                dose_ratio = self.dose_api / row['dose'] if row['dose'] > 0 else 1.0

            # Get study marker
            marker = study_marker_map.get(row['study'], 's')

            # Determine data column
            data_column = None
            for col in ["mean", "value", "median", "geom_mean"]:
                if col in row and not pd.isna(row[col]):
                    data_column = col
                    break
            if data_column is None:
                continue  # Skip if no valid data

            y_value = self._extract_data_point(row[data_column], row['unit'], pk_par_id, dose_ratio)

            # Plot optional SD error bars
            y_err = None
            x_err = None
            min_value = None
            max_value = None
            if 'sd' in row and pd.notna(row['sd']):
                y_err = self._extract_data_point(row["sd"], row['unit'], pk_par_id, dose_ratio)
            if "min" in row and pd.notna(row["min"]):
                min_value = self._extract_data_point(row["min"], row['unit'], pk_par_id, dose_ratio)

            if "max" in row and pd.notna(row["max"]):
                max_value = self._extract_data_point(row["max"], row['unit'], pk_par_id, dose_ratio)

            if is_bodyweight_scan and 'weight_sd' in row and pd.notna(row['weight_sd']):
                x_err = row['weight_sd']  # FIXME: units handling


            ax, max_row_y = self._add_data_point_to_plot(ax, spar_value, y_value, x_err, y_err, min_value, max_value, marker, study_color)
            max_y = max(max_y, max_row_y)

        return ax, max_y

    def _extract_data_point(self, data_point, units, parameter, dose_ratio):
        """Extracts the data point from the row and applies scaling if necessary."""
        # FIXME: can be generalized
        if parameter in self.pk_units.keys():
            st_units = self.pk_units[parameter]
        if parameter in self.pd_units.keys():
            st_units = self.pd_units[parameter]
        try:
            # units for PK parameters are defined in the Base Experiment
            value = self.Q_(float(data_point), units).to(st_units).magnitude
        except DimensionalityError:
            data_point = self.Q_(float(data_point), units) / self.Mr.api # FIXME: not only api Mr
            try:
                value = data_point.to(st_units).magnitude
            except Exception as e:
                console.print(
                    f"An error occurred while transforming units: {e}. "
                    "Check whether the units of the data can be transformed "
                    "to the units of the pk parameter in the base experiment."
                )

        if parameter in self.scalable_params and dose_ratio != 1.0:
            return value * dose_ratio

        return value

    def _add_data_point_to_plot(self, ax, x_pos, y_value, x_err, y_err, min_value, max_value, marker: str, study_color: str) -> tuple:

        if y_err is not None:
            if x_err is not None:
                kwargs = dict(
                    xerr=x_err,
                    yerr=y_err,
                    fmt=marker,
                    markerfacecolor=study_color,
                    ecolor="black",
                )
            else:
                kwargs = dict(
                    yerr=y_err,
                    fmt=marker,
                    markerfacecolor=study_color,
                    ecolor="black",
                )
            ax.errorbar(
                x_pos, y_value,
                capsize=6,
                **kwargs,
                **self.plot_kwargs
            )
            y_limit = y_value + y_err
        elif x_err is not None:
            ax.errorbar(
                x_pos, y_value,
                xerr=x_err,
                fmt=marker,
                markerfacecolor=study_color,
                markeredgecolor="black",
                ecolor="black",
            )
            y_limit = y_value
        else:
            ax.plot(
                x_pos, y_value,
                marker=marker,
                markerfacecolor=study_color,
                **self.plot_kwargs
            )
            y_limit = y_value

        if min_value is not None and max_value is not None:
            ax.vlines(x_pos, min_value, max_value, color="black", linewidth=2, zorder=4, linestyles="dashed")
            ax.scatter(x_pos, min_value, s=15, color="black", zorder=5)
            ax.scatter(x_pos, max_value, s=15, color="black", zorder=5)
            y_limit = max(y_limit, max_value)

        return ax, y_limit

    def _styling(self, ax: plt.Axes, key: str, ymax: float, scan_info: dict, is_dose_scan: bool) -> plt.Axes:
        """Apply styling to the axis for PK parameter plots."""
        # Formatting
        ax.tick_params(axis="x", labelsize=self.tick_font_size)
        ax.tick_params(axis="y", labelsize=self.tick_font_size)
        ax.set_xlabel(scan_info["label"], fontdict=self.font)
        if key in self.pk_labels.keys():
            label = f"{self.pk_labels[key]} [{self.pk_units[key]}]"
        elif key in self.pd_labels.keys():
            label = f"{self.pd_labels[key]} [{self.pd_units[key]}]"
        ax.set_ylabel(
            label,
            fontdict=self.font,
        )
        if "ratio" in key and scan_info["parameter"] in ["f_cirrhosis", "GU__f_absorption"]:
            ax.set_ylim(bottom=0.0, top=2.05 * ymax)
        else:
            ax.set_ylim(bottom=0.0, top=1.05 * ymax)

        if scan_info["scale"] == "log":
            ax.set_xscale("log")
            from matplotlib.ticker import ScalarFormatter
            ax.xaxis.set_major_formatter(ScalarFormatter())
            ax.xaxis.get_major_formatter().set_scientific(False)

        # Major ticks: long and thick
        ax.tick_params(axis='both', which='major', length=8, width=3)
        # if is_dose_scan:
        #     ax.set_xticks(scan_info["range"])
        #     ax.set_xticklabels(scan_info["range"])

        # Add colorbar
        ax = self._add_colorbar_strip(ax, scan_info)

        return ax

    def get_class_data(self, scan_id: str) -> dict:
        if scan_id == "renal_scan":
            # renal_map from base experiment
            return {
                "normal": self.renal_map["Normal renal function"],
                "mild": self.renal_map["Mild renal impairment"],
                "moderate": self.renal_map["Moderate renal impairment"],
                "severe": self.renal_map["Severe renal impairment"],
                "end_stage": self.renal_map["End stage renal impairment"],
            }
        elif scan_id == "hepatic_scan":
            # cirrhosis_map from base experiment
            return {
                "normal": self.cirrhosis_map["Control"],
                "mild": self.cirrhosis_map["Mild cirrhosis"],
                "moderate": self.cirrhosis_map["Moderate cirrhosis"],
                "severe": self.cirrhosis_map["Severe cirrhosis"],
            }
        elif scan_id == "food_scan":
            return {
                "fasted": self.fasting_map["fasted"],
                "fed": self.fasting_map["fed"],
            }

        return None

    def get_color_map(self, scan_key: str, scan_data: dict) -> dict | None:
        """Returns predefined color maps for renal/hepatic scans, None for others."""
        predefined_maps = {
            "renal_scan": {
                "normal": self.renal_colors["Normal renal function"],
                "mild": self.renal_colors["Mild renal impairment"],
                "moderate": self.renal_colors["Moderate renal impairment"],
                "severe": self.renal_colors["Severe renal impairment"],
                "end_stage": self.renal_colors["End stage renal impairment"],
            },
            "hepatic_scan": {
                "normal": self.cirrhosis_colors["Control"],
                "mild": self.cirrhosis_colors["Mild cirrhosis"],
                "moderate": self.cirrhosis_colors["Moderate cirrhosis"],
                "severe": self.cirrhosis_colors["Severe cirrhosis"],
            },
            "food_scan": {
                "fasted": "#61409b",
                "fed": "#3f007d",
            }
        }
        return predefined_maps.get(scan_key)

    def _get_color_for_value(self, value: float, scan_info: dict) -> str:
        """
        Assigns a normalized color for any scan_key based on the provided value, range (vmin, vmax), and colormap.

        :param value: The value to assign a color to.
        :param scan_info: Scan info dict containing scale, colormap, range.
        :return: Hex color string.
        """
        cmap_name = scan_info.get("colormap", "Oranges")
        cmap = matplotlib.colormaps.get_cmap(cmap_name)
        range_min, range_max = min(scan_info["range"]), max(scan_info["range"])

        # Choose normalization type based on the scale
        if scan_info["scale"] == "linear":
            norm = matplotlib.colors.Normalize(vmin=range_min, vmax=range_max)
        elif scan_info["scale"] == "log":
            norm = matplotlib.colors.LogNorm(vmin=range_min, vmax=range_max)
        else:
            raise ValueError(f"Unsupported scale: {scan_info['scale']}")

        if range_min <= value <= range_max:
            rgba_color = cmap(norm(value))
            return to_hex(rgba_color, keep_alpha=False)
        else:
            raise ValueError(f"Value {value} is out of range ({range_min}, {range_max}).")

    def _add_legend_based_on_study_map(self, ax, study_marker_map, legend_position: tuple) -> matplotlib.axes.Axes:
        """
        Add legend to the plot based on the study marker map.

        Parameters:
        ax : matplotlib.axes.Axes
            The axis on which the legend is added.
        study_marker_map : dict
            A dictionary mapping studies to marker/color/label properties.
        """
        # Create dummy artists for legend
        legend_elements = []
        for study, marker in study_marker_map.items():
            legend_elements.append(
                plt.Line2D(
                    [0], [0],  # Dummy data
                    marker=marker, color="grey", label=study,
                    linestyle="None", markersize=8,
                )
            )

        # Add the legend to the axis
        ax.legend(
            handles=legend_elements,
            title="Studies",  # Optional legend title
            loc="upper right",
            fontsize=9,
            bbox_to_anchor=legend_position,
        )

        return ax


    @staticmethod
    def _add_colorbar_strip(ax, scan_data: dict) -> matplotlib.axes.Axes:
        """Add a colorbar strip at the top of a subplot."""
        height_frac = 0.03
        range_vals = scan_data["range"]
        rmin, rmax = range_vals[0], range_vals[-1]
        cmap = scan_data["colormap"]

        # Create colorbar normalization
        if scan_data["scale"] == "linear":
            norm = matplotlib.colors.Normalize(vmin=rmin, vmax=rmax, clip=False)
        elif scan_data["scale"] == "log":
            norm = matplotlib.colors.LogNorm(vmin=rmin, vmax=rmax, clip=False)

        # Create inset axes for colorbar strip
        strip_ax = inset_axes(ax, width="100%", height=f"{height_frac * 100:.2f}%", loc="upper center", borderpad=0)

        # Draw colorbar gradient
        if isinstance(norm, matplotlib.colors.LogNorm) or scan_data["scale"] == "log":
            xs = np.geomspace(max(rmin, 1e-12), rmax, 256)
        else:
            xs = np.linspace(rmin, rmax, 256)

        strip_ax.imshow(xs[np.newaxis, :], aspect="auto", cmap=cmap, norm=norm, origin="lower", extent=(0, 1, 0, 1))
        strip_ax.set_axis_off()
        strip_ax.set_zorder(ax.get_zorder() + 1)

        return strip_ax

if __name__ == "__main__":
    run_experiments(ApixabanDataParameterScan, output_dir=ApixabanDataParameterScan.__name__)
