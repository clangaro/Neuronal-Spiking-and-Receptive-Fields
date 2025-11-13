"""
analysis.py
-----------
Analysis utilities for computing orientation tuning curves and
fitting simple parametric models.
"""

import numpy as np
from scipy.optimize import curve_fit
from src.simulate import tuning_function


def compute_firing_rates(
    spike_trains: list,
    duration: float
) -> np.ndarray:
    """
    Compute firing rate of each spike train.

    Parameters
    ----------
    spike_trains : list
        List of arrays containing spike times.
    duration : float
        Trial duration in seconds.

    Returns
    -------
    np.ndarray
        Firing rates (Hz).
    """
    return np.array([len(train) / duration for train in spike_trains])


def fit_tuning_curve(
    orientations: np.ndarray,
    rates: np.ndarray
):
    """
    Fit a parametric tuning curve using nonlinear least squares.

    Parameters
    ----------
    orientations : np.ndarray
        Stimulus orientations.
    rates : np.ndarray
        Observed firing rates.

    Returns
    -------
    tuple
        (best_params, predicted_rates)
    """

    def model(theta, pref, kappa, baseline, amplitude):
        return tuning_function(theta, pref, kappa, baseline, amplitude)

    # Initial guess
    guess = [
        orientations[np.argmax(rates)],   # preferred orientation guess
        2.0,                               # kappa guess
        np.min(rates),                     # baseline
        np.max(rates) - np.min(rates)      # amplitude
    ]

    params, _ = curve_fit(model, orientations, rates, p0=guess)
    predictions = model(orientations, *params)

    return params, predictions

