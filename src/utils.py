"""
utils.py
--------
Helper functions for reproducibility and signal processing.
"""

import numpy as np


def set_seed(seed: int = 0):
    """
    Set NumPy random seed for reproducibility.
    """
    np.random.seed(seed)


