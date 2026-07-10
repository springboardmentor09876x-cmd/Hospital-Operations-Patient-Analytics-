"""
data_collection.py
-------------------
Merges two raw hospital Excel exports into a single, de-duplicated
CSV dataset: hospital_raw_data.csv

Input files (edit paths in CONFIG below if needed):
    1. hospital_dst_1.xlsx   -> sheet 'Hospital_RawDataset_Updated'  (49 columns)
    2. Hospital_Ds.xlsx      -> sheet 'Merged_Hospital_Dataset'      (23 columns)

Logic:
    1. Load both sheets into DataFrames.
    2. Normalize column names (case/whitespace/singular-plural/derived-suffix
       insensitive) to detect columns that represent the same field even when
       named slightly differently (e.g. "Doctor" vs "Doctors").
    3. Drop duplicate columns that exist *within* a single file first
       (e.g. File 2 has both "Department" and "Department.1" because the
       original sheet had the column twice).
    4. Join the two files on the shared unique key "Patient ID".
    5. Where a field exists in both files (same normalized name), keep only
       the File 1 ("Hospital_RawDataset_Updated") version, since it is the
       more complete/authoritative source.
    6. Append any column that is genuinely unique to File 2 (e.g.
       "Beds Occupied", which does not exist in File 1).
    7. Write the combined, deduplicated table to hospital_raw_data.csv.
"""

import re
from pathlib import Path
from collections import defaultdict

import pandas as pd

# ----------------------------- CONFIG ------------------------------------
FILE_1 = "hospital_dst_1.xlsx"   # primary / richer dataset
FILE_2 = "Hospital_Ds.xlsx"      # secondary dataset
SHEET_1 = "Hospital_RawDataset_Updated"
SHEET_2 = "Merged_Hospital_Dataset"
JOIN_KEY = "Patient ID"
OUTPUT_CSV = "hospital_raw_data.csv"
# ---------------------------------------------------------------------------


def normalize_col(col: str) -> str:
    """Normalize a column name so that near-duplicates map to the same key.

    - lowercases and trims whitespace
    - collapses internal whitespace / underscores to a single space
    - strips pandas' auto-generated duplicate suffix (e.g. "Department.1" -> "department")
    - strips a trailing plural 's' (e.g. "Doctors" -> "doctor", "Nurses" -> "nurse")
    """
    col = col.strip().lower()
    col = col.split(".")[0]                 # drop ".1", ".2" pandas dup suffixes
    col = col.replace("_", " ").replace("%", " pct ")
    col = re.sub(r"\s+", " ", col).strip()
    if col.endswith("s") and not col.endswith("ss"):
        col = col[:-1]
    return col


def drop_internal_duplicate_columns(df: pd.DataFrame, label: str) -> pd.DataFrame:
    """Within a single dataframe, if two columns normalize to the same name,
    keep only the first occurrence and drop the rest."""
    seen = {}
    keep_cols = []
    for col in df.columns:
        key = normalize_col(col)
        if key not in seen:
            seen[key] = col
            keep_cols.append(col)
        else:
            print(f"  [{label}] Dropping internal duplicate column "
                  f"'{col}' (duplicate of '{seen[key]}')")
    return df[keep_cols]


def load_data(file_path: str, sheet_name: str, label: str) -> pd.DataFrame:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Could not find input file: {path}")
    print(f"Loading {label}: {path} [{sheet_name}]")
    df = pd.read_excel(path, sheet_name=sheet_name)
    print(f"  -> {df.shape[0]} rows, {df.shape[1]} columns")
    return drop_internal_duplicate_columns(df, label)


def merge_datasets(df1: pd.DataFrame, df2: pd.DataFrame, join_key: str) -> pd.DataFrame:
    if join_key not in df1.columns or join_key not in df2.columns:
        raise KeyError(f"Join key '{join_key}' must exist in both datasets")

    if not df1[join_key].is_unique or not df2[join_key].is_unique:
        raise ValueError(f"Join key '{join_key}' must be unique in both datasets")

    # Map normalized column name -> original column name, per dataframe
    norm_to_orig_1 = {normalize_col(c): c for c in df1.columns}
    norm_to_orig_2 = {normalize_col(c): c for c in df2.columns}

    shared = set(norm_to_orig_1) & set(norm_to_orig_2)
    only_in_2 = set(norm_to_orig_2) - set(norm_to_orig_1)

    print(f"\n{len(shared)} fields present in both files (keeping File 1's version):")
    for key in sorted(shared):
        col1, col2 = norm_to_orig_1[key], norm_to_orig_2[key]
        marker = "" if col1 == col2 else f"  (File 2 called it '{col2}')"
        print(f"  - {col1}{marker}")

    print(f"\n{len(only_in_2)} field(s) unique to File 2 (added to merged output):")
    extra_cols = []
    for key in sorted(only_in_2):
        col2 = norm_to_orig_2[key]
        print(f"  - {col2}")
        extra_cols.append(col2)

    # Build the merged frame: all of df1's columns + unique columns from df2,
    # aligned row-for-row on the join key.
    df2_extra = df2[[join_key] + extra_cols].set_index(join_key)
    merged = df1.set_index(join_key).join(df2_extra, how="left").reset_index()

    # Put the join key back as the first column
    cols = [join_key] + [c for c in merged.columns if c != join_key]
    merged = merged[cols]

    return merged


def main():
    print("=" * 70)
    print("Hospital data collection: merging raw source files")
    print("=" * 70)

    df1 = load_data(FILE_1, SHEET_1, "File 1")
    df2 = load_data(FILE_2, SHEET_2, "File 2")

    merged = merge_datasets(df1, df2, JOIN_KEY)

    print(f"\nFinal merged dataset: {merged.shape[0]} rows, {merged.shape[1]} columns")

    merged.to_csv(OUTPUT_CSV, index=False)
    print(f"\nSaved -> {OUTPUT_CSV}")


if __name__ == "__main__":
    main()