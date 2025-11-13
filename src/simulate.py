"""
simulate.py
-----------
Functions for generating oriented stimuli and simulating Poisson
spiking activity for simple V1-like neurons.
"""

import numpy as np


def generate_orientations(n_orientations: int = 8) -> np.ndarray:
    """
    Generate evenly spaced orientations between 0° and 180°.

    Parameters
    ----------
    n_orientations : int
        Number of stimulus orientations.

    Returns
    -------
    np.ndarray
        Array of orientations in degrees.
    """
    return np.linspace(0, 180, n_orientations, endpoint=False)


def tuning_function(
    theta: np.ndarray,
    pref_orientation: float,
    kappa: float,
    baseline: float = 5.0,
    amplitude: float = 20.0
) -> np.ndarray:
    """
    Cosine-like orientation tuning curve.

    Parameters
    ----------
    theta : np.ndarray
        Stimulus orientations in degrees.
    pref_orientation : float
        Preferred orientation of the neuron.
    kappa : float
        Sharpness of tuning.
    baseline : float
        Baseline firing rate (Hz).
    amplitude : float
        Modulation amplitude (Hz).

    Returns
    -------
    np.ndarray
        Firing rate for each orientation.
    """
    # Convert difference to radians
    rad = np.deg2rad(theta - pref_orientation)
    response = baseline + amplitude * np.exp(kappa * np.cos(rad)) / np.exp(kappa)
    return response


def simulate_spike_train(
    rate: float,
    duration: float = 1.0,
    dt: float = 0.001
) -> np.ndarray:
    """
    Simulate a Poisson spike train for a given firing rate.

    Parameters
    ----------
    rate : float
        Mean firing rate in Hz.
    duration : float
        Trial duration in seconds.
    dt : float
        Time step for simulation.

    Returns
    -------
    np.ndarray
        Array of spike times in seconds.
    """
    n_bins = int(duration / dt)
    spike_prob = rate * dt
    spikes = np.random.rand(n_bins) < spike_prob
    return np.where(spikes)[0] * dt

