"""
MedTrack_DV - Data Preparation Script
--------------------------------------
Source dataset: "Healthcare Dataset" by prasad22 (Kaggle)
https://www.kaggle.com/datasets/prasad22/healthcare-dataset

This script:
1. Loads the raw healthcare_dataset.csv
2. Cleans it (dedupe, fix casing, standardize text, parse dates)
3. Maps each "Medical Condition" to a Department
4. Builds a synthetic department-level resource table
   (department_id, total_beds, total_staff, total_equipment)
5. Merges patient-level data with department-level resource data
6. Saves hospital_cleaned.csv and hospital_final_dataset.csv

Run: python build_medtrack_dataset.py
Expected input file: healthcare_dataset.csv in the same folder
(download from Kaggle and place it here before running)
"""

import pandas as pd
import numpy as np

RAW_FILE = "healthcare_dataset.csv"
CLEANED_FILE = "hospital_cleaned.csv"
FINAL_FILE = "hospital_final_dataset.csv"
RESOURCE_FILE = "department_resources.csv"

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

# ---------------------------------------------------------------------
# STEP 1: Load raw data
# ---------------------------------------------------------------------
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"Loaded raw dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


# ---------------------------------------------------------------------
# STEP 2: Clean data
# ---------------------------------------------------------------------
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Standardize column names (the public CSV uses Title Case with spaces)
    df.columns = [c.strip() for c in df.columns]

    # Strip whitespace and fix casing on key text fields
    text_cols = ["Name", "Gender", "Blood Type", "Medical Condition",
                 "Doctor", "Hospital", "Insurance Provider",
                 "Admission Type", "Medication", "Test Results"]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.title()

    # Remove exact duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    print(f"Removed {before - len(df)} duplicate rows")

    # Parse dates
    df["Date of Admission"] = pd.to_datetime(df["Date of Admission"], errors="coerce")
    df["Discharge Date"] = pd.to_datetime(df["Discharge Date"], errors="coerce")

    # Drop rows with missing admission or discharge dates (needed for LOS)
    before = len(df)
    df = df.dropna(subset=["Date of Admission", "Discharge Date"])
    print(f"Dropped {before - len(df)} rows with missing admission/discharge dates")

    # Fix any discharge date earlier than admission date (data entry errors)
    bad_rows = df["Discharge Date"] < df["Date of Admission"]
    print(f"Found {bad_rows.sum()} rows with discharge before admission — swapping dates")
    df.loc[bad_rows, ["Date of Admission", "Discharge Date"]] = (
        df.loc[bad_rows, ["Discharge Date", "Date of Admission"]].values
    )

    # Compute Length of Stay (days)
    df["Length of Stay"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days
    df["Length of Stay"] = df["Length of Stay"].clip(lower=0)

    # Fill missing categorical values with "Unknown" rather than dropping
    fill_unknown = ["Gender", "Blood Type", "Insurance Provider", "Admission Type",
                     "Medication", "Test Results", "Hospital", "Doctor"]
    for col in fill_unknown:
        if col in df.columns:
            df[col] = df[col].replace("Nan", np.nan).fillna("Unknown")

    # Age must be a reasonable positive integer
    df = df[(df["Age"] > 0) & (df["Age"] < 120)]

    print(f"Cleaned dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


# ---------------------------------------------------------------------
# STEP 3: Map Medical Condition -> Department
# ---------------------------------------------------------------------
CONDITION_TO_DEPARTMENT = {
    "Diabetes": "Endocrinology",
    "Hypertension": "Cardiology",
    "Asthma": "Pulmonology",
    "Obesity": "General Medicine",
    "Cancer": "Oncology",
    "Arthritis": "Orthopedics",
}

def map_department(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Department"] = df["Medical Condition"].map(CONDITION_TO_DEPARTMENT)
    df["Department"] = df["Department"].fillna("General Medicine")

    unmapped = df[df["Department"] == "General Medicine"]["Medical Condition"].unique()
    print(f"Departments assigned. Conditions defaulted to General Medicine: {list(unmapped)}")
    return df


# ---------------------------------------------------------------------
# STEP 4: Build synthetic department resource table
# ---------------------------------------------------------------------
def build_resource_table(departments: list) -> pd.DataFrame:
    """
    Generates plausible (synthetic) department-level capacity data.
    Documented as synthetically generated since public datasets do not
    publish real hospital staffing/equipment numbers at this granularity.
    """
    rows = []
    for i, dept in enumerate(sorted(departments), start=1):
        total_beds = np.random.randint(20, 80)
        total_staff = np.random.randint(15, 60)
        total_equipment = np.random.randint(10, 40)
        rows.append({
            "department_id": f"D{i:03d}",
            "Department": dept,
            "total_beds": total_beds,
            "total_staff": total_staff,
            "total_equipment": total_equipment,
        })
    resource_df = pd.DataFrame(rows)
    print(f"Built resource table for {len(resource_df)} departments")
    return resource_df


# ---------------------------------------------------------------------
# STEP 5: Merge patient data with department resource data
# ---------------------------------------------------------------------
def merge_data(patient_df: pd.DataFrame, resource_df: pd.DataFrame) -> pd.DataFrame:
    before = len(patient_df)
    merged = patient_df.merge(resource_df, on="Department", how="left")

    # Validate merge integrity
    unmatched = merged["department_id"].isna().sum()
    print(f"Merge complete: {len(merged)} rows (input had {before})")
    if unmatched > 0:
        print(f"WARNING: {unmatched} rows failed to match a department — check naming consistency")
    else:
        print("All rows matched a department successfully")

    return merged


# ---------------------------------------------------------------------
# STEP 6: Basic KPI sanity columns (optional preview, full KPI engineering
# happens in generate_hospital_kpis.py per project plan)
# ---------------------------------------------------------------------
def add_basic_flags(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Flag readmissions: same patient name + hospital admitted more than once
    # (Name is not a unique patient ID in this public dataset — documented limitation)
    df["Admission Count"] = df.groupby(["Name", "Hospital"])["Date of Admission"].transform("count")
    df["Is Readmission"] = df["Admission Count"] > 1
    return df


# ---------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------
def main():
    raw_df = load_data(RAW_FILE)
    cleaned_df = clean_data(raw_df)
    cleaned_df = map_department(cleaned_df)
    cleaned_df.to_csv(CLEANED_FILE, index=False)
    print(f"Saved cleaned dataset -> {CLEANED_FILE}")

    resource_df = build_resource_table(cleaned_df["Department"].unique().tolist())
    resource_df.to_csv(RESOURCE_FILE, index=False)
    print(f"Saved department resource table -> {RESOURCE_FILE}")

    final_df = merge_data(cleaned_df, resource_df)
    final_df = add_basic_flags(final_df)
    final_df.to_csv(FINAL_FILE, index=False)
    print(f"Saved final merged dataset -> {FINAL_FILE}")

    print("\nPreview of final dataset:")
    print(final_df.head())


if __name__ == "__main__":
    main()
