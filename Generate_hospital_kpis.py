"""
MedTrack_DV - KPI Engineering Script (Module 3)
-------------------------------------------------
Input  : hospital_final_dataset.csv
Output : hospital_kpi_dataset.csv  (Tableau-ready)

KPIs generated:
  Patient Level  -> Age Group, Month, Year, Quarter
  Hospital Level -> Occupancy Rate, Bed Utilization Rate,
                    Patient-to-Staff Ratio, Readmission Rate,
                    Avg Length of Stay, Department Efficiency Score
  Financial      -> Billing Amount (cleaned), Avg Billing per Stay

Run: python generate_hospital_kpis.py
"""

import pandas as pd
import numpy as np

INPUT_FILE  = "hospital_final_dataset.csv"
OUTPUT_FILE = "hospital_kpi_dataset.csv"

# ─────────────────────────────────────────────
# STEP 1: Load
# ─────────────────────────────────────────────
def load(path):
    df = pd.read_csv(path)
    print(f"Loaded: {df.shape[0]:,} rows | {df.shape[1]} columns")
    return df


# ─────────────────────────────────────────────
# STEP 2: Fix known data issues
# ─────────────────────────────────────────────
def fix_issues(df):
    df = df.copy()

    # Fix negative Billing Amount
    neg = (df["Billing Amount"] < 0).sum()
    df["Billing Amount"] = df["Billing Amount"].abs()
    print(f"Fixed {neg} negative Billing Amount values (took absolute value)")

    # Parse dates (they come in as strings from CSV)
    df["Date of Admission"] = pd.to_datetime(df["Date of Admission"], errors="coerce")
    df["Discharge Date"]    = pd.to_datetime(df["Discharge Date"],    errors="coerce")

    return df


# ─────────────────────────────────────────────
# STEP 3: Patient-level derived columns
# ─────────────────────────────────────────────
def add_patient_columns(df):
    df = df.copy()

    # Date parts — essential for Tableau trend charts
    df["Year"]    = df["Date of Admission"].dt.year
    df["Month"]   = df["Date of Admission"].dt.month
    df["Month Name"] = df["Date of Admission"].dt.strftime("%b")   # Jan, Feb …
    df["Quarter"] = df["Date of Admission"].dt.quarter.map(
                        {1:"Q1", 2:"Q2", 3:"Q3", 4:"Q4"})

    # Age Group — for Patient Flow dashboard filters
    bins   = [0, 17, 35, 60, 120]
    labels = ["0-17", "18-35", "36-60", "60+"]
    df["Age Group"] = pd.cut(df["Age"], bins=bins, labels=labels, right=True)

    # Stay Category — readable LOS band for charts
    df["Stay Category"] = pd.cut(
        df["Length of Stay"],
        bins=[0, 3, 7, 14, 30],
        labels=["Short (1-3d)", "Medium (4-7d)", "Long (8-14d)", "Extended (15+d)"],
        right=True
    )

    print("Added patient-level columns: Year, Month, Month Name, Quarter, Age Group, Stay Category")
    return df


# ─────────────────────────────────────────────
# STEP 4: Department-level KPIs
#         (computed per dept, then merged back)
# ─────────────────────────────────────────────
def add_department_kpis(df):
    df = df.copy()

    dept_group = df.groupby("Department")

    # ── 4a. Total admissions per department
    dept_admissions = dept_group["Name"].count().rename("Dept Total Admissions")

    # ── 4b. Readmission Rate per department (%)
    dept_readmit = (
        dept_group["Is Readmission"]
        .apply(lambda x: round(x.sum() / len(x) * 100, 2))
        .rename("Readmission Rate (%)")
    )

    # ── 4c. Average Length of Stay per department
    dept_alos = (
        dept_group["Length of Stay"]
        .mean()
        .round(2)
        .rename("Avg Length of Stay (Dept)")
    )

    # ── 4d. Occupancy Rate (%)
    #        = (admissions in period / total_beds) * 100
    #        Uses total_beds from resource table (constant per dept)
    dept_beds = df.groupby("Department")["total_beds"].first()
    dept_occ  = (dept_admissions / dept_beds * 100).round(2).rename("Occupancy Rate (%)")
    # Cap at 100 for display sanity (admissions can exceed bed count over time)
    dept_occ  = dept_occ.clip(upper=100)

    # ── 4e. Bed Utilization Rate (%)
    #        = avg daily patients (approx LOS/30) / total_beds
    dept_avg_daily = (dept_alos / 30 * dept_admissions / 12).round(2)  # rough monthly avg
    dept_bed_util  = (dept_avg_daily / dept_beds * 100).round(2).rename("Bed Utilization Rate (%)")
    dept_bed_util  = dept_bed_util.clip(upper=100)

    # ── 4f. Patient-to-Staff Ratio
    dept_staff = df.groupby("Department")["total_staff"].first()
    dept_p2s   = (dept_admissions / dept_staff).round(2).rename("Patient to Staff Ratio")

    # ── 4g. Department Efficiency Score (composite, 0-100)
    #        Higher is better
    #        Formula: 100 - (readmission_rate * 0.4) - (norm_alos * 0.3) + (bed_util * 0.3)
    max_alos = dept_alos.max()
    norm_alos = (dept_alos / max_alos * 100)
    efficiency = (
        100
        - (dept_readmit * 0.4)
        - (norm_alos    * 0.3)
        + (dept_bed_util * 0.3)
    ).round(2).rename("Department Efficiency Score")

    # Combine all dept KPIs into one lookup table
    dept_kpis = pd.concat([
        dept_admissions,
        dept_readmit,
        dept_alos,
        dept_occ,
        dept_bed_util,
        dept_p2s,
        efficiency,
    ], axis=1).reset_index()

    # Merge back onto patient-level rows
    df = df.merge(dept_kpis, on="Department", how="left")
    print(f"Added department KPIs for {dept_kpis.shape[0]} departments")
    return df


# ─────────────────────────────────────────────
# STEP 5: Financial KPIs
# ─────────────────────────────────────────────
def add_financial_kpis(df):
    df = df.copy()

    # Avg billing per department (merged back as a column)
    dept_avg_bill = (
        df.groupby("Department")["Billing Amount"]
        .mean()
        .round(2)
        .rename("Avg Billing Amount (Dept)")
        .reset_index()
    )
    df = df.merge(dept_avg_bill, on="Department", how="left")

    # Cost per day
    df["Cost per Day"] = (df["Billing Amount"] / df["Length of Stay"].replace(0, 1)).round(2)

    print("Added financial KPIs: Avg Billing Amount (Dept), Cost per Day")
    return df


# ─────────────────────────────────────────────
# STEP 6: Final column ordering & export
# ─────────────────────────────────────────────
FINAL_COLUMN_ORDER = [
    # Patient identity
    "Name", "Age", "Age Group", "Gender", "Blood Type",

    # Admission details
    "Date of Admission", "Year", "Month", "Month Name", "Quarter",
    "Discharge Date", "Length of Stay", "Stay Category",
    "Admission Type", "Room Number",

    # Clinical
    "Medical Condition", "Department", "department_id",
    "Doctor", "Medication", "Test Results",

    # Hospital
    "Hospital", "Insurance Provider",

    # Resource
    "total_beds", "total_staff", "total_equipment",

    # Patient-level flags
    "Admission Count", "Is Readmission",

    # Department KPIs
    "Dept Total Admissions",
    "Readmission Rate (%)",
    "Avg Length of Stay (Dept)",
    "Occupancy Rate (%)",
    "Bed Utilization Rate (%)",
    "Patient to Staff Ratio",
    "Department Efficiency Score",

    # Financial
    "Billing Amount",
    "Avg Billing Amount (Dept)",
    "Cost per Day",
]

def export(df, path):
    # Only keep columns we explicitly ordered (handles any extras gracefully)
    cols = [c for c in FINAL_COLUMN_ORDER if c in df.columns]
    df = df[cols]
    df.to_csv(path, index=False)
    print(f"\nSaved Tableau-ready dataset -> {path}")
    print(f"Final shape: {df.shape[0]:,} rows | {df.shape[1]} columns")
    print("\nColumn list:")
    for c in df.columns:
        print(f"  {c}")


# ─────────────────────────────────────────────
# STEP 7: Validation summary
# ─────────────────────────────────────────────
def validate(df):
    print("\n── Validation Summary ──────────────────────────────")
    print(f"Total rows           : {len(df):,}")
    print(f"Null values          : {df.isnull().sum().sum()}")
    print(f"Negative Billing     : {(df['Billing Amount'] < 0).sum()}")
    print(f"Year range           : {df['Year'].min()} – {df['Year'].max()}")
    print(f"Departments          : {sorted(df['Department'].unique())}")
    print(f"Admission Types      : {sorted(df['Admission Type'].unique())}")
    print(f"Avg LOS (overall)    : {df['Length of Stay'].mean():.2f} days")
    print(f"Readmission Rate     : {df['Is Readmission'].mean()*100:.2f}%")
    print(f"Avg Billing Amount   : ${df['Billing Amount'].mean():,.2f}")
    print(f"KPI Accuracy check   : Occupancy Rate max = {df['Occupancy Rate (%)'].max()}%")
    print("────────────────────────────────────────────────────")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def main():
    print("=" * 52)
    print("  MedTrack_DV — KPI Engineering (Module 3)")
    print("=" * 52)

    df = load(INPUT_FILE)
    df = fix_issues(df)
    df = add_patient_columns(df)
    df = add_department_kpis(df)
    df = add_financial_kpis(df)
    validate(df)
    export(df, OUTPUT_FILE)

    print("\nDone! Load hospital_kpi_dataset.csv into Tableau.")

if __name__ == "__main__":
    main()  