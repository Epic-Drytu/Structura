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
def drop_high_null_cols(df, threshold=0.5):
    """Drop columns where the missing ratio exceeds `threshold`."""
    ratio   = df.isnull().mean()
    to_drop = ratio[ratio > threshold].index.tolist()
    print(f"Dropping {len(to_drop)} column(s): {to_drop}")
    return df.drop(columns=to_drop)


def fill_missing(df, strategy="median"):
    """
    Fill nulls:
      • numeric  → median (default) or mean
      • category → mode
    """
    df = df.copy()
    for col in df.columns:
        if df[col].isnull().sum() == 0:
            continue
        if pd.api.types.is_numeric_dtype(df[col]):
            val = df[col].median() if strategy == "median" else df[col].mean()
        else:
            val = df[col].mode()[0]
        df[col].fillna(val, inplace=True)
    return df


def remove_duplicates(df):
    """Drop exact duplicate rows and report count removed."""
    before = len(df)
    df = df.drop_duplicates()
    print(f"Removed {before - len(df)} duplicate row(s).")
    return df


def clip_outliers_iqr(df, cols=None, factor=1.5):
    """Clip outliers to IQR fences for the given numeric columns."""
    df   = df.copy()
    cols = cols or df.select_dtypes(include=np.number).columns.tolist()
    for col in cols:
        q1, q3 = df[col].quantile(0.25), df[col].quantile(0.75)
        iqr = q3 - q1
        df[col] = df[col].clip(lower=q1 - factor * iqr,
                                upper=q3 + factor * iqr)
    return df




# Merging Two Files




# Functions for columns (Mean, Median, Mode)




# Systematic Formation