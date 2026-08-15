# ==========================================================
# HOSPITAL KPI ENGINEERING
# Infosys Springboard Virtual Internship
# Module 3
# ==========================================================

import pandas as pd
import numpy as np
from datetime import datetime

# ==========================================================
# LOAD CLEANED DATASET
# ==========================================================

INPUT_FILE = "hospital_cleaned.csv"

print("=" * 60)
print("Loading Cleaned Dataset...")
print("=" * 60)

df = pd.read_csv(INPUT_FILE)

# Remove accidental separator row if present
if "Hospital Name" in df.columns:
    df = df[df["Hospital Name"].astype(str).str.strip() != "======="]

df.reset_index(drop=True, inplace=True)

print(f"Dataset Shape : {df.shape}")

# ==========================================================
# REMOVE OLD KPI COLUMNS (IF THEY EXIST)
# ==========================================================

old_kpis = [
    "Total_Admissions",
    "Overall_Occupancy_Rate",
    "Average_Length_of_Stay",
    "Readmission_Rate",
    "Bed_Utilization_Rate",
]

df.drop(columns=[c for c in old_kpis if c in df.columns],
        inplace=True,
        errors="ignore")
print("\nRemaining Columns:")
print(df.columns.tolist())

# ==========================================================
# DATA VALIDATION
# ==========================================================

print("\nChecking Dataset Quality...\n")

print("Rows               :", df.shape[0])
print("Columns            :", df.shape[1])
print("Missing Values     :", df.isnull().sum().sum())
print("Duplicate Rows     :", df.duplicated().sum())

duplicate_columns = df.columns[df.columns.duplicated()].tolist()

print("Duplicate Columns  :", len(duplicate_columns))

if len(duplicate_columns) > 0:
    print(duplicate_columns)
    print("Rows with Missing  :", df.isnull().any(axis=1).sum())

# ==========================================================
# DATE CONVERSION
# ==========================================================

# Convert dates first

df["Admission Date"] = pd.to_datetime(
    df["Admission Date"],
    errors="coerce"
)

df["Discharge Date"] = pd.to_datetime(
    df["Discharge Date"],
    errors="coerce"
)
# Keep original date column for analysis
df["Transfer_Date_Analysis"] = pd.to_datetime(
    df["Transfer_Date"],
    format="mixed",
    errors="coerce"
)

# Display column as required by mentor
df["Transfer_Date"] = df["Transfer_Date_Analysis"].apply(
    lambda x: x.strftime("%d-%m-%Y")
    if pd.notna(x)
    else "Not Transferred"
)



print("Date Conversion Completed")
# ==========================================================
# LENGTH OF STAY
# ==========================================================

if ("Admission Date" in df.columns) and ("Discharge Date" in df.columns):

    df["Length of Stay"] = (
    df["Discharge Date"] -
    df["Admission Date"]
).dt.days


print("Length of Stay Created")
print("=" * 60)
print("Validation Completed Successfully")
print("=" * 60)

# ============================================================
# BLOCK - 2 : HOSPITAL KPI CALCULATION
# ============================================================

print("\n" + "="*60)
print("Calculating Hospital KPIs...")
print("="*60)

# -------------------------------
# 1. Total Admissions
# -------------------------------
total_admissions = len(df)


# -------------------------------
# 2. Average Length of Stay
# -------------------------------
df["Length of Stay"] = df["Length of Stay"].clip(
    lower=1,
    upper=30
)

average_los = round(
    df["Length of Stay"].mean(),
    2
)


average_los = round(df["Length of Stay"].mean(), 2)


# -------------------------------
# 3. Readmission Rate
# -------------------------------
if "Readmission_Flag" in df.columns:
    readmission_rate = round(
        df["Readmission_Flag"].mean(), 2
    )
else:
    readmission_rate = round(
        (df["Readmission"].astype(str)
         .str.lower()
         .eq("yes")
         .mean()),
        2
    )


# -------------------------------
# 4. Bed Occupancy Rate
# -------------------------------
if "Bed_Occupancy_Rate_Calc" in df.columns:

    bed_occupancy_rate = round(
    df["Bed_Occupancy_Rate_Calc"].mean(),
    2
)

else:

    
    bed_occupancy_rate = round(
    df["Bed_Occupancy_Rate_Calc"].mean(),
    2
)


# -------------------------------
# 5. ICU Utilization Rate
# -------------------------------
if "ICU_Occupancy_Rate_Calc" in df.columns:

    icu_utilization_rate = round(
    df["ICU_Occupancy_Rate_Calc"].mean()/100,
    2
)

else:

    icu_utilization_rate = round(
        df["ICU Beds"].sum() / df["Beds Available"].sum() / 100,
        2
    )



# -------------------------------
# 6. Staff Utilization Rate
# -------------------------------
if "Staff_Utilization_Calc" in df.columns:

    staff_utilization_rate = round(
        df["Staff_Utilization_Calc"].mean()/100,
        2
    )

else:

    staff_utilization_rate = round(
        df["Nurses"].sum() / df["Staff Count"].sum() / 100,
        2
    )


# -------------------------------
# 7. Equipment Utilization Rate
# -------------------------------
if "Equipment_InUse_Flag" in df.columns:

    equipment_utilization_rate = round(
        df["Equipment_InUse_Flag"].mean(),
        2
    )

else:

    equipment_utilization_rate = round(
        (df["Equipment Status"]
        .astype(str)
        .str.lower()
        .eq("in use")
        .mean()),
        2
    )


# -------------------------------
# 8. Transfer Rate
# -------------------------------
if "Transferred_Flag" in df.columns:

    transfer_rate = round(
        df["Transferred_Flag"].mean(),
        2
    )

else:

    transfer_rate = round(
        df["Transferred"]
        .astype(str)
        .str.lower()
        .eq("yes")
        .mean()*100,
        2)


# -------------------------------
# 9. Department Efficiency Score
# -------------------------------
avg_department_los = df.groupby(
    "Department"
)["Length of Stay"].mean().mean()

department_efficiency = round(
    100 - ((avg_department_los / 60) ),
    2
)

department_efficiency = max(
    department_efficiency,0
)


# ============================================================
# KPI SUMMARY
# ============================================================

kpi_summary = {

    "Total Admissions": total_admissions,

    "Average Length of Stay":
        average_los,

    "Readmission Rate (%)":
        readmission_rate,

    "Bed Occupancy Rate (%)":
        bed_occupancy_rate,

    "ICU Utilization Rate (%)":
        icu_utilization_rate,

    "Staff Utilization Rate (%)":
        staff_utilization_rate,

    "Equipment Utilization Rate (%)":
        equipment_utilization_rate,

    "Patient Transfer Rate (%)":
        transfer_rate,

    "Department Efficiency Score":
        department_efficiency
}


print("\nKPI Calculation Completed Successfully")

print("\n" + "="*60)
print("HOSPITAL KPI SUMMARY")
print("="*60)


for key, value in kpi_summary.items():
    print(f"{key:<35}: {value}")


print("="*60)
# ============================================================
# ADD KPI FEATURES INTO DATASET
# ============================================================

df["KPI_Total_Admissions"] = total_admissions

df["KPI_Average_Length_of_Stay"] = average_los

df["KPI_Readmission_Rate_%"] = readmission_rate

df["KPI_Bed_Occupancy_Rate_%"] = bed_occupancy_rate

df["KPI_ICU_Utilization_Rate_%"] = icu_utilization_rate

df["KPI_Staff_Utilization_Rate_%"] = staff_utilization_rate

df["KPI_Equipment_Utilization_Rate_%"] = equipment_utilization_rate

df["KPI_Patient_Transfer_Rate_%"] = transfer_rate

df["KPI_Department_Efficiency_Score"] = department_efficiency


print("\nKPI Columns Added Successfully")
# Format dates for final dataset

date_columns = [
    "Admission Date",
    "Discharge Date"
]

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce")
    df[col] = df[col].dt.strftime("%d-%m-%Y")


if "Transfer_Date" in df.columns:

    df["Transfer_Date"] = df["Transfer_Date"].replace(
        "Not transferred",
        pd.NaT
    )

    df["Transfer_Date"] = pd.to_datetime(
        df["Transfer_Date"],
        errors="coerce"
    )

    df["Transfer_Date"] = df["Transfer_Date"].dt.strftime("%d-%m-%Y")

    df["Transfer_Date"] = df["Transfer_Date"].fillna(
        "Not transferred"
    )


print("All Date Columns Standardized Successfully")

print("Updated Dataset Shape:")
print(df.shape)

if "Transfer_Date_Analysis" in df.columns:
    df.drop(columns=["Transfer_Date_Analysis"], inplace=True)
    print("Transfer_Date_Analysis column removed successfully.")

# ----------------------------
# Generate Patient_ID
# ----------------------------
df["Patient_ID"] = [f"PAT{str(i+1).zfill(5)}" for i in range(len(df))]

# ----------------------------
# Generate Hospital_ID from Hospital_Name
# ----------------------------
hospital_mapping = {
    name: f"HOS{str(i+1).zfill(3)}"
    for i, name in enumerate(sorted(df["Hospital Name"].unique()))
}

df["Hospital_ID"] = df["Hospital Name"].map(hospital_mapping)

# Move Patient_ID and Hospital_ID to the beginning
cols = df.columns.tolist()

cols.remove("Patient_ID")
cols.remove("Hospital_ID")

new_order = ["Patient_ID", "Hospital_ID"] + cols

df = df[new_order]

df.to_excel(
    "hospital_final_dataset.xlsx",
    index=False
)

print("Final Dataset Exported Successfully")

# ==============================
# BLOCK 4: FINAL DATA VALIDATION
# ==============================

print("\nFinal Dataset Validation")

# Check missing values
missing_values = df.isnull().sum().sum()

print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])
print("Total Missing Values:", missing_values)


# Check duplicate rows
duplicates = df.duplicated().sum()

print("Duplicate Rows:", duplicates)


# Check final columns
print("\nFinal Columns:")
print(df.columns.tolist())


# Save final validation report
print("\nDataset Ready for Tableau Dashboard")

print("================================")
print("FINAL DATASET CHECK COMPLETED")
print("================================") 