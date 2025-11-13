# Neuronal-Spiking-and-Receptive-Fields
simulate V1-like neurons responding to oriented stimuli and fit their tuning curves.

# Neuronal Spiking and Receptive Fields

**Scientific question:**  
How do neurons in the primary visual cortex (V1) encode simple visual features such as orientation?

**Overview:**  
This project simulates spike trains from V1-like neurons responding to drifting grating stimuli using a Poisson model.
We then fit tuning curves, estimate preferred orientations, and visualise receptive field selectivity.

**Key skills:** NumPy · Matplotlib · Poisson processes · tuning-curve fitting · LN model

**Repository structure:**
- `src/` — Python scripts for simulation, analysis, and visualisation.
- `notebooks/` — step-by-step Jupyter notebooks.
- `reports/figures/` — generated figures.

**How to run:**
```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_generate_stimuli.ipynb
