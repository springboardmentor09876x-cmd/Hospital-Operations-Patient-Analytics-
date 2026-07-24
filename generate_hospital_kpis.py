# ==========================================================
# Hospital Operations & Patient Analytics
# KPI Generation Script
# ==========================================================

import pandas as pd
import numpy as np
from pathlib import Path

# ----------------------------------------------------------
# Read Dataset
# ----------------------------------------------------------

FILE_NAME = "hospital_cleaned.csv"

if not Path(FILE_NAME).exists():
    raise FileNotFoundError(
        f"{FILE_NAME} not found in the current folder."
    )

print("Loading dataset...")

df = pd.read_csv(FILE_NAME)

print("Dataset Loaded Successfully.")
print(f"Rows    : {len(df)}")
print(f"Columns : {len(df.columns)}")

# ----------------------------------------------------------
# Remove Duplicates
# ----------------------------------------------------------

df.drop_duplicates(inplace=True)

# ----------------------------------------------------------
# Remove Completely Empty Columns
# ----------------------------------------------------------

df.dropna(axis=1, how="all", inplace=True)

# ----------------------------------------------------------
# Clean Column Names
# ----------------------------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.replace("\n", " ", regex=False)
)

# ----------------------------------------------------------
# Required Columns
# ----------------------------------------------------------

required_columns = [
    "Admission Date",
    "Discharge Date",
    "Department",
    "Readmission",
    "Billing Amount",
    "Bed Occupied",
    "Beds Available",
    "Beds_Occupied_Count",
    "Dept_Bed_Capacity_Derived",
    "Staff Count",
    "Dept_Staff_Capacity_Derived",
    "Equipment_InUse_Flag",
    "Equipment_Total_Inventory"
]

missing = []

for col in required_columns:
    if col not in df.columns:
        missing.append(col)

if len(missing) > 0:
    print("\nMissing Columns:")
    print(missing)
    raise ValueError("Required columns are missing.")

print("\nAll required columns found.")

# ----------------------------------------------------------
# Convert Dates
# ----------------------------------------------------------

df["Admission Date"] = pd.to_datetime(
    df["Admission Date"],
    errors="coerce",
    dayfirst=True
)

df["Discharge Date"] = pd.to_datetime(
    df["Discharge Date"],
    errors="coerce",
    dayfirst=True
)

# ----------------------------------------------------------
# Convert Numeric Columns
# ----------------------------------------------------------

numeric_cols = [
    "Billing Amount",
    "Beds Available",
    "Beds_Occupied_Count",
    "Dept_Bed_Capacity_Derived",
    "Staff Count",
    "Dept_Staff_Capacity_Derived",
    "Equipment_InUse_Flag",
    "Equipment_Total_Inventory"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# ----------------------------------------------------------
# Fill Missing Numeric Values
# ----------------------------------------------------------

for col in numeric_cols:
    df[col] = df[col].fillna(
        df[col].median()
    )

# ----------------------------------------------------------
# Fill Missing Text Values
# ----------------------------------------------------------

categorical_cols = [
    "Department",
    "Readmission",
    "Bed Occupied"
]

for col in categorical_cols:
    df[col] = df[col].fillna("Unknown")

print("\nData Cleaning Completed Successfully.")

# ----------------------------------------------------------
# Preview
# ----------------------------------------------------------

print(df.head())



# ==========================================================
# KPI CALCULATIONS
# ==========================================================

print("\nCalculating KPIs...")

# ----------------------------------------------------------
# KPI 1 : Length of Stay
# ----------------------------------------------------------

df["Length_of_Stay_Days"] = (
    df["Discharge Date"] -
    df["Admission Date"]
).dt.days

df["Length_of_Stay_Days"] = df["Length_of_Stay_Days"].clip(
    lower=0,
    upper=30
)

average_los = round(
    df["Length_of_Stay_Days"].mean(),
    2
)
# ----------------------------------------------------------
# KPI 2 : Total Admissions
# ----------------------------------------------------------

total_admissions = len(df)

df["Total_Admissions"] = total_admissions

# ----------------------------------------------------------
# KPI 3 : Average Length of Stay
# ----------------------------------------------------------

average_los = round(
    df["Length_of_Stay_Days"].mean(),
    2
)

df["Average_Length_of_Stay"] = average_los

# ----------------------------------------------------------
# KPI 4 : Readmission Rate
# ----------------------------------------------------------

df["Readmission_Flag"] = np.where(

    df["Readmission"]
      .astype(str)
      .str.upper()
      .str.strip()
      .isin(["YES","Y","TRUE","1"]),

    1,

    0

)

readmission_rate = round(

    (df["Readmission_Flag"].sum() /
     total_admissions) * 100,

    2

)

df["Readmission_Rate"] = readmission_rate

# ----------------------------------------------------------
# KPI 5 : Occupancy Rate
# ----------------------------------------------------------

occupied = (
    df["Bed Occupied"]
      .astype(str)
      .str.strip()
      .str.upper()
      .isin(["YES", "Y", "OCCUPIED", "1"])
)

occupancy_rate = round(occupied.mean() * 100, 2)

df["Occupancy_Rate"] = occupancy_rate


# ----------------------------------------------------------
# KPI 6 : Bed Utilization Rate
# ----------------------------------------------------------

bed_utilization = round(

    (
        df["Bed Occupied"]
        .astype(str)
        .str.upper()
        .eq("YES")
        .mean()

    ) * 100,

    2

)

df["Bed_Utilization_Rate"] = bed_utilization
# ----------------------------------------------------------
# KPI 7 : Department Efficiency Score
# ----------------------------------------------------------

department_average = (

    df.groupby("Department")

    ["Length_of_Stay_Days"]

    .transform("mean")

)

overall_average = df["Length_of_Stay_Days"].mean()

df["Department_Efficiency_Score"] = (

    overall_average /

    department_average

) * 100

df["Department_Efficiency_Score"] = (

    df["Department_Efficiency_Score"]

    .round(2)

)

# ----------------------------------------------------------
# KPI 8 : Staff Utilization Rate
# ----------------------------------------------------------

staff_utilization = round(

    (

        df["Staff Count"].sum()

        /

        df["Dept_Staff_Capacity_Derived"].sum()

    ) * 100,

    2

)

df["Staff_Utilization_Rate"] = staff_utilization

# ----------------------------------------------------------
# BONUS KPI : Equipment Utilization Rate
# ----------------------------------------------------------

equipment_utilization = round(
    df["Equipment_InUse_Flag"].mean() * 100,
    2
)
df["Equipment_Utilization_Rate"] = equipment_utilization

# ----------------------------------------------------------
# KPI Summary
# ----------------------------------------------------------

print("\n================ KPI SUMMARY ================\n")

print(f"Total Admissions              : {total_admissions}")

print(f"Average Length of Stay        : {average_los}")

print(f"Readmission Rate (%)          : {readmission_rate}")

print(f"Occupancy Rate (%)            : {occupancy_rate}")

print(f"Bed Utilization Rate (%)      : {bed_utilization}")

print(f"Staff Utilization Rate (%)    : {staff_utilization}")

print(f"Equipment Utilization Rate (%) : {equipment_utilization}")


# ----------------------------------------------------------
# KPI 7 : Department Efficiency Score
# ----------------------------------------------------------

dept_avg_los = (
    df.groupby("Department")["Length_of_Stay_Days"]
      .transform("mean")
)

# Replace 0 with NaN to avoid division by zero
dept_avg_los = dept_avg_los.replace(0, np.nan)

overall_avg_los = df["Length_of_Stay_Days"].mean()

df["Department_Efficiency_Score"] = (
    (overall_avg_los / dept_avg_los) * 100
)

# Remove inf values
df["Department_Efficiency_Score"] = (
    df["Department_Efficiency_Score"]
      .replace([np.inf, -np.inf], np.nan)
      .fillna(0)
      .round(2)
)

department_efficiency = round(
    df["Department_Efficiency_Score"].mean(),
    2
)

print(f"Department Efficiency Score : {department_efficiency}")
# ----------------------------------------------------------
# KPI 9 : ICU Utilization Rate
# ----------------------------------------------------------

icu_utilization = round(

    (
        df["ICU Beds"].sum()

        /

        df["Beds Available"].sum()

    ) * 100,

    2

)

df["ICU_Utilization_Rate"] = icu_utilization

print(f"ICU Utilization Rate (%)      : {icu_utilization}")

print("\nKPIs Calculated Successfully.")


# ==========================================================
# BLOCK 3 - TABLEAU OPTIMIZATION & FEATURE ENGINEERING
# ==========================================================

print("\nCreating Tableau Features...")

# ----------------------------------------------------------
# Admission Month
# ----------------------------------------------------------

df["Admission_Month"] = df["Admission Date"].dt.month_name()

# ----------------------------------------------------------
# Admission Year
# ----------------------------------------------------------

df["Admission_Year"] = df["Admission Date"].dt.year

# ----------------------------------------------------------
# Admission Quarter
# ----------------------------------------------------------

df["Admission_Quarter"] = (
    "Q" + df["Admission Date"].dt.quarter.astype(str)
)

# ----------------------------------------------------------
# Admission Weekday
# ----------------------------------------------------------

df["Admission_Day"] = (
    df["Admission Date"].dt.day_name()
)

# ----------------------------------------------------------
# Discharge Month
# ----------------------------------------------------------

df["Discharge_Month"] = (
    df["Discharge Date"].dt.month_name()
)

# ----------------------------------------------------------
# Length of Stay Category
# ----------------------------------------------------------

def los_category(days):

    if days <= 3:
        return "Short Stay"

    elif days <= 7:
        return "Medium Stay"

    else:
        return "Long Stay"

df["LOS_Category"] = (
    df["Length_of_Stay_Days"]
      .apply(los_category)
)

# ----------------------------------------------------------
# Billing Category
# ----------------------------------------------------------

billing_q1 = df["Billing Amount"].quantile(0.25)
billing_q3 = df["Billing Amount"].quantile(0.75)

def billing_category(amount):

    if amount <= billing_q1:
        return "Low"

    elif amount <= billing_q3:
        return "Medium"

    else:
        return "High"

df["Billing_Category"] = (
    df["Billing Amount"]
      .apply(billing_category)
)

# ----------------------------------------------------------
# Bed Status
# ----------------------------------------------------------

df["Bed_Status"] = np.where(

    df["Bed Occupied"]
      .astype(str)
      .str.upper()
      .isin(["YES","Y","1","OCCUPIED"]),

    "Occupied",

    "Available"

)

# ----------------------------------------------------------
# Staff Capacity Status
# ----------------------------------------------------------

df["Staff_Capacity_Status"] = np.where(

    df["Staff_Utilization_Rate"] >= 90,

    "Highly Utilized",

    np.where(

        df["Staff_Utilization_Rate"] >= 70,

        "Moderately Utilized",

        "Low Utilization"

    )

)

# ----------------------------------------------------------
# Department Performance
# ----------------------------------------------------------

df["Department_Performance"] = np.where(

    df["Department_Efficiency_Score"] >= 100,

    "Efficient",

    "Needs Improvement"

)

# ----------------------------------------------------------
# Equipment Status
# ----------------------------------------------------------

df["Equipment_Status"] = np.where(

    df["Equipment_InUse_Flag"] == 1,

    "In Use",

    "Available"

)

# ----------------------------------------------------------
# High Readmission Risk
# ----------------------------------------------------------

df["High_Readmission_Risk"] = np.where(

    df["Readmission_Flag"] == 1,

    "High",

    "Low"

)

# ----------------------------------------------------------
# KPI Dashboard Label
# ----------------------------------------------------------

df["Dashboard_Label"] = (
    df["Department"] +
    " - " +
    df["LOS_Category"]
)

print("\nFeature Engineering Completed Successfully.")
print("\nCurrent Dataset Shape :", df.shape)

# ==========================================================
# BLOCK 4 - EXPORT FINAL DATASET
# ==========================================================

print("\nGenerating Final Dataset...")

# Save Final Dataset for Tableau

output_file = "hospital_final_dataset.xlsx"

df.to_excel(
    output_file,
    index=False
)

print(f"\nFinal Dataset Saved : {output_file}")

print("\n===========================================")
print("Hospital Analytics Project Completed Successfully!")
print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])
print("Output  :", output_file)
print("Status  : SUCCESS")
print("===========================================")