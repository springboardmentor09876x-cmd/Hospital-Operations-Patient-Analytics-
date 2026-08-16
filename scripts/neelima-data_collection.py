# ============================================================
# Module 1 : Data Collection & Data Merging
# Project : Hospital Operations & Patient Analytics
#
# Objective:
# 1. Load datasets
# 2. Perform basic EDA
# 3. Integrate hospital level information
# 4. Generate Final Raw Dataset
#
# NOTE:
# Data Cleaning is NOT performed in this module.
# ============================================================

import pandas as pd
import numpy as np

print("=" * 70)
print("Loading datasets...")
print("=" * 70)

# ------------------------------------------------------------
# Load datasets
# ------------------------------------------------------------

patient = pd.read_csv("../data/raw_sources/Hospital Operation Dataset.csv")

hospital = pd.read_csv("../data/raw_sources/Hospitals_and_Beds_statewise.csv")

icu = pd.read_csv("../data/raw_sources/ICU beds count in India - Statewise.csv")

print("Datasets loaded successfully.\n")

# ------------------------------------------------------------
# Rename columns
# ------------------------------------------------------------

hospital = hospital.rename(columns={
    "Unnamed: 0": "State",
    "Total": "Hospitals_Count",
    "Unnamed: 6": "Beds Available"
})

icu = icu.rename(columns={
    "States/UTs": "State",
    "Total number of ICU beds (public + private)": "ICU Beds"
})

# ------------------------------------------------------------
# Remove summary row
# ------------------------------------------------------------

hospital = hospital[hospital["State"] != "All India"]

hospital = hospital.reset_index(drop=True)

# ------------------------------------------------------------
# Basic EDA
# ------------------------------------------------------------

print("=" * 70)
print("PATIENT DATASET")
print("=" * 70)

print(patient.info())

print("\nShape :", patient.shape)

print("\nMissing Values")
print(patient.isnull().sum())

print("\n")

print("=" * 70)
print("HOSPITAL DATASET")
print("=" * 70)

print(hospital.info())

print("\nShape :", hospital.shape)

print("\n")

print("=" * 70)
print("ICU DATASET")
print("=" * 70)

print(icu.info())

print("\nShape :", icu.shape)

print("\n")

# ------------------------------------------------------------
# Assign State to Patient Dataset
#
# Since the public patient dataset does not contain a State
# column, states are assigned randomly from the hospital
# dataset only for educational data integration.
# ------------------------------------------------------------
hospital["State"] = hospital["State"].replace({
    "Andaman & Nicobar Islands": "Andaman Nicobar Islands",
    "Jammu & Kashmir": "Jammu And Kashmir",
    "Daman & Diu": "Daman And Diu"
})

icu["State"] = icu["State"].replace({
    "Andaman & Nicobar Islands": "Andaman Nicobar Islands",
    "Jammu & Kashmir": "Jammu And Kashmir",
    "Daman & Diu": "Daman And Diu"
})
patient["State"] = hospital["State"].sample(
    n=len(patient),
    replace=True,
    random_state=42
).values

# ------------------------------------------------------------
# Merge Hospital Bed Information
# ------------------------------------------------------------

patient = patient.merge(

    hospital[["State", "Beds Available"]],

    on="State",

    how="left"

)

# ------------------------------------------------------------
# Merge ICU Information
# ------------------------------------------------------------

patient = patient.merge(

    icu[["State", "ICU Beds"]],

    on="State",

    how="left"

)


# ------------------------------------------------------------
# Rename existing columns to match project schema
# ------------------------------------------------------------

patient.rename(columns={

    "Patient_ID": "Patient ID",

    "Doctor_ID": "Doctor",

    "Admission_Date": "Admission Date",

    "Discharge_Date": "Discharge Date",

    "Length_of_Stay_Days": "Length of Stay",

    "Treatment_Cost_USD": "Billing Amount",

    "Insurance_Type": "Insurance Provider",

    "Readmission_Flag": "Readmission"

}, inplace=True)

# ------------------------------------------------------------
# Load mentor reference dataset
# ------------------------------------------------------------

reference = pd.read_csv("../data/reference/hospital_final_dataset(row_level).csv")

# ------------------------------------------------------------
# Create any missing columns
# ------------------------------------------------------------

for col in reference.columns:
    if col not in patient.columns:
        patient[col] = pd.NA

# ------------------------------------------------------------
# Expand reference dataset to match patient dataset size
# ------------------------------------------------------------

repeat_count = (len(patient) // len(reference)) + 1

reference_expanded = pd.concat(
    [reference] * repeat_count,
    ignore_index=True
)

reference_expanded = reference_expanded.iloc[:len(patient)]

# ------------------------------------------------------------
# Copy hospital-related columns from reference dataset
# Keep patient-specific columns from the public dataset
# ------------------------------------------------------------

keep_patient_columns = [
    "Patient ID",
    "Age",
    "Gender",
    "Department",
    "Diagnosis",
    "Admission Date",
    "Discharge Date",
    "Doctor",
    "Insurance Provider",
    "Billing Amount",
    "Readmission",
    "State",
    "Beds Available",
    "ICU Beds"
]

for col in reference.columns:
    if col not in keep_patient_columns:
      patient[col] = reference_expanded[col].values

# Remove duplicate columns
#patient = patient.drop(columns=["Beds Available", "ICU Beds"], errors="ignore")

np.random.seed(42)

patient["Admission Date"] = pd.date_range(
    start="2024-01-01",
    periods=len(patient),
    freq="h"
)

patient["Discharge Date"] = (
    patient["Admission Date"] +
    pd.to_timedelta(
        np.random.randint(1, 15, len(patient)),
        unit="D"
    )
)
patient["Admission Date"] = patient["Admission Date"].dt.strftime("%Y-%m-%d")
patient["Discharge Date"] = patient["Discharge Date"].dt.strftime("%Y-%m-%d")
# Convert back to datetime for calculation
patient["Admission Date"] = pd.to_datetime(patient["Admission Date"])
patient["Discharge Date"] = pd.to_datetime(patient["Discharge Date"])

# Calculate Length of Stay from the new dates
patient["Length of Stay"] = (
    patient["Discharge Date"] - patient["Admission Date"]
).dt.days

# Convert dates back to YYYY-MM-DD format
patient["Admission Date"] = patient["Admission Date"].dt.strftime("%Y-%m-%d")
patient["Discharge Date"] = patient["Discharge Date"].dt.strftime("%Y-%m-%d")
# ------------------------------------------------------------
# Convert Doctor IDs into consistent Doctor Names
# ------------------------------------------------------------

first_names = [
    "Amit", "Rahul", "Priya", "Sneha", "Anjali",
    "Kiran", "Arjun", "Neha", "Divya", "Lakshmi",
    "Harish", "Akash", "Vivek", "Ramesh", "Sai",
    "Naveen", "Suresh", "Pavan", "Rohit", "Deepak"
]

last_names = [
    "Sharma", "Reddy", "Patel", "Kumar", "Verma",
    "Iyer", "Singh", "Rao", "Gupta", "Menon",
    "Naidu", "Yadav", "Joshi", "Kapoor", "Mishra"
]

# Get all unique doctor IDs
unique_doctors = sorted(reference["Doctor"].unique())

# Create a consistent mapping
doctor_map = {}

for i, doctor_id in enumerate(unique_doctors):
    first = first_names[i % len(first_names)]
    last = last_names[(i // len(first_names)) % len(last_names)]
    doctor_map[doctor_id] = f"Dr. {first} {last}"

# Apply mapping
patient["Doctor"] = reference_expanded["Doctor"].map(doctor_map)
#------------------------------------------------------------
# Save Final Dataset
# ------------------------------------------------------------
print("\nChecking merged columns...")

print(
    patient[
        ["State", "Beds Available", "ICU Beds"]
    ].isnull().sum()
)
output = "../data/hospital_raw_data.csv"

patient.to_csv(output, index=False)

# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------

print("=" * 70)
print("MODULE 1 COMPLETED SUCCESSFULLY")
print("=" * 70)

print("Rows :", patient.shape[0])
print("Columns :", patient.shape[1])

print("\nFinal dataset saved at:")
print(output)

print("\nDone.")

# NOTE:
# The public patient dataset does not contain State information.
# States are assigned randomly only to demonstrate the data integration
# workflow for educational purposes.