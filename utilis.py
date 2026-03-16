import os
import glob
import numpy as np
import pandas as pd
import kagglehub


# ──────────────────────────────────────────────
# 1. DATA LOADING
# ──────────────────────────────────────────────

def load_dataset(verbose=True):
    """Download and load the Student Performance dataset."""
    path = kagglehub.dataset_download("amar5693/student-performance-dataset")
    csv_files = glob.glob(os.path.join(path, "**/*.csv"), recursive=True)

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found at: {path}")

    dfs = {}
    for f in csv_files:
        name = os.path.basename(f).replace(".csv", "")
        dfs[name] = pd.read_csv(f)
        if verbose:
            print(f"✅ Loaded '{name}': {dfs[name].shape}")

    return list(dfs.values())[0] if len(dfs) == 1 else dfs
# Cleaning Step




# Merging Two Files




# Functions for columns (Mean, Median, Mode)




# Systematic Formation