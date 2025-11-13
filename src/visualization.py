"""
visualization.py
----------------
Plotting functions for spike rasters and orientation tuning curves.
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_raster(
    spike_trains: list,
    orientations: np.ndarray,
    figsize: tuple = (6, 4)
):
    """
    Plot spike rasters for each orientation.

    Parameters
    ----------
    spike_trains : list
        List of arrays containing spike times.
    orientations : np.ndarray
        Stimulus orientations.
    figsize : tuple
        Figure size.
    """
    plt.figure(figsize=figsize)
    for idx, spikes in enumerate(spike_trains):
        plt.vlines(
            spikes,
            ymin=idx + 0.5,
            ymax=idx + 1.5,
            color="black",
            linewidth=0.8
        )

    plt.yticks(
        np.arange(1, len(orientations) + 1),
        [f"{o:.0f}°" for o in orientations]
    )
    plt.xlabel("Time (s)")
    plt.ylabel("Stimulus orientation")
    plt.title("Spike Raster Plot")
    plt.tight_layout()
    plt.show()


def plot_tuning_curve(
    orientations: np.ndarray,
    rates: np.ndarray,
    fit_rates: np.ndarray = None,
    figsize: tuple = (5, 4)
):
    """
    Plot firing rate tuning curve.

    Parameters
    ----------
    orientations : np.ndarray
        Stimulus orientations.
    rates : np.ndarray
        Observed firing rates.
    fit_rates : np.ndarray, optional
        Model-predicted rates.
    figsize : tuple
        Figure size.
    """
    plt.figure(figsize=figsize)
    plt.plot(orientations, rates, "o-", label="Observed firing rate")
    if fit_rates is not None:
        plt.plot(orientations, fit_rates, "r--", label="Fitted curve")

    plt.xlabel("Orientation (°)")
    plt.ylabel("Rate (Hz)")
    plt.title("Orientation Tuning Curve")
    plt.legend()
    plt.tight_layout()
    plt.show()

