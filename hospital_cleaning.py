# ==========================================================
# MODULE 2 : DATA CLEANING & TRANSFORMATION
# MedTrack_DV
# ==========================================================

import pandas as pd
import numpy as np

print("="*70)
print("MEDTRACK_DV - HOSPITAL DATA CLEANING")
print("="*70)

# ==========================================================
# 1. Load Dataset
# ==========================================================
df = pd.read_excel("Hospital_RawDataset_Updated.xlsx")
print(f"\nDataset Loaded Successfully. Shape: {df.shape}")

# ==========================================================
# 2. Remove Duplicate Records FIRST
# ==========================================================
print(f"\nDuplicate Records Before Cleaning: {df.duplicated().sum()}")
df = df.drop_duplicates().reset_index(drop=True)
print(f"Duplicate Records After Cleaning: {df.duplicated().sum()}")

# ==========================================================
# 3. Strip Whitespace from Text Columns
# ==========================================================
print("\nRemoving Extra Spaces from Text Columns...")
text_columns = df.select_dtypes(include=["object", "string"]).columns
for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

# ==========================================================
# 4. Standardize / Cast Numeric & Date Types (CRITICAL STEP)
# ==========================================================
print("\nNormalizing Healthcare Indicators & Dates...")

healthcare_columns = [
    "Staff Count", "Beds Available", "ICU Beds", "Length of Stay", 
    "Billing Amount", "Dept_Bed_Capacity_Derived", "Beds_Occupied_Count", 
    "Equipment_Total_Inventory", "Equipment_Usage_Duration_Hours", 
    "Number_of_Transfers", "Dept_ICU_Bed_Capacity_Derived", 
    "Dept_Staff_Capacity_Derived", "Admissions_Rate_%_Derived", 
    "Staff_Utilization_%_Derived", "Bed_Occupancy_Rate_%", "Age"
]

for col in healthcare_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

date_columns = ["Admission Date", "Discharge Date", "Transfer_Date"]
for col in date_columns:
    if col in df.columns:
        df[col] = df[col].replace(["nan", "NaT", "None", "Unknown"], pd.NA)
        df[col] = pd.to_datetime(df[col], format="mixed", errors="coerce")

# ==========================================================
# 5. Handle Missing Values (AFTER TYPE CASTING)
# ==========================================================
print("\nHandling Missing Values...")

# Specific column fill-ins
if "Insurance Provider" in df.columns:
    df["Insurance Provider"] = df["Insurance Provider"].fillna("Self-Pay")
if "Transfer_From_Department" in df.columns:
    df["Transfer_From_Department"] = df["Transfer_From_Department"].fillna("Not Transferred")
if "Transfer_To_Department" in df.columns:
    df["Transfer_To_Department"] = df["Transfer_To_Department"].fillna("Not Transferred")

# Fill any remaining missing text columns
categorical_columns = df.select_dtypes(include=["object", "string"]).columns
for col in categorical_columns:
    df[col] = df[col].replace(["nan", "None", "NaN"], "Unknown").fillna("Unknown")

# Fill missing numerical columns with Median
numerical_columns = df.select_dtypes(include=np.number).columns
for col in numerical_columns:
    median_val = df[col].median()
    # In case the whole column was NaN, fallback to 0
    if pd.isna(median_val): 
        median_val = 0
    df[col] = df[col].fillna(median_val)

# Handle Missing Dates (Forward fill or use Placeholder if essential, or keep as NaT if required)
# For Tableau, we can forward fill or fill with a default date so it doesn't break metrics.
for col in date_columns:
    df[col] = df[col].ffill().bfill() 

# ==========================================================
# 6. Correct Negative Values
# ==========================================================
print("\nChecking and Correcting Negative Values...")
for col in healthcare_columns:
    if col in df.columns:
        negative_values = (df[col] < 0).sum()
        if negative_values > 0:
            df.loc[df[col] < 0, col] = df[col].median()

# ==========================================================
# 7. Standardize Categorical Text
# ==========================================================
print("\nStandardizing Categories (Department, Gender, Hospital Type)...")

department_mapping = {
    "icu": "ICU", "Icu": "ICU", "ICU": "ICU",
    "general medicine": "General Medicine", "general surgery": "General Surgery",
    "cardiology": "Cardiology", "neurology": "Neurology", "orthopedics": "Orthopedics",
    "oncology": "Oncology", "pulmonology": "Pulmonology", "nephrology": "Nephrology",
    "psychiatry": "Psychiatry"
}
if "Department" in df.columns:
    df["Department"] = df["Department"].replace(department_mapping).str.title().replace({"Icu": "ICU"})

for col in ["Hospital Type", "Gender", "Admission Type", "Readmission", "Equipment Status"]:
    if col in df.columns:
        df[col] = df[col].str.title()

if "Blood Type" in df.columns:
    df["Blood Type"] = df["Blood Type"].str.upper()

# ==========================================================
# 8. CREATE TABLEAU READY COLUMNS
# ==========================================================
print("\nCreating Tableau Ready Columns...")

# --- Leave these datetime extractions first so they work perfectly ---
df["Admission Year"] = df["Admission Date"].dt.year.astype("Int64")
df["Admission Month"] = df["Admission Date"].dt.month_name()
df["Admission Month Number"] = df["Admission Date"].dt.month.astype("Int64")
df["Admission Quarter"] = "Q" + df["Admission Date"].dt.quarter.astype(str)
df["Admission Day"] = df["Admission Date"].dt.day_name()
df["Admission Week"] = df["Admission Date"].dt.isocalendar().week.astype("Int64")

# Discharge Date Features
df["Discharge Year"] = df["Discharge Date"].dt.year.astype("Int64")
df["Discharge Month"] = df["Discharge Date"].dt.month_name()
df["Discharge Quarter"] = "Q" + df["Discharge Date"].dt.quarter.astype(str)

# Weekend / Weekday
df["Admission Type Day"] = np.where(df["Admission Date"].dt.dayofweek >= 5, "Weekend", "Weekday")


# 🚨 ADD THIS CODE RIGHT HERE (Converts datetime objects into YYYY/MM/DD string format) 🚨
for col in ["Admission Date", "Discharge Date", "Transfer_Date"]:
    if col in df.columns:
        df[col] = df[col].dt.strftime('%Y/%m/%d')

print("Date columns successfully formatted to YYYY/MM/DD strings.")
# ==========================================================
# 9. FEATURE ENGINEERING (Age, Billing, Stay Categories)
# ==========================================================
print("\nCreating Analytical Categories...")

# Age Groups
conditions_age = [
    (df["Age"] <= 12),
    (df["Age"] >= 13) & (df["Age"] <= 19),
    (df["Age"] >= 20) & (df["Age"] <= 39),
    (df["Age"] >= 40) & (df["Age"] <= 59),
    (df["Age"] >= 60)
]
choices_age = ["Child", "Teenager", "Adult", "Middle Age", "Senior Citizen"]
df["Age Group"] = np.select(conditions_age, choices_age, default="Unknown")

# Billing Category (Safely handling duplicates in quantiles using 'rank')
df["Billing Category"] = pd.qcut(df["Billing Amount"].rank(method='first'), q=3, labels=["Low", "Medium", "High"])

# Stay Category
conditions_stay = [
    df["Length of Stay"] <= 3,
    (df["Length of Stay"] > 3) & (df["Length of Stay"] <= 7),
    df["Length of Stay"] > 7
]
choices_stay = ["Short Stay", "Medium Stay", "Long Stay"]
df["Stay Category"] = np.select(conditions_stay, choices_stay, default="Unknown")

# ==========================================================
# 10. FINAL MISSING VALUE CHECK & EXPORT
# ==========================================================
print("\n" + "="*70)
print("FINAL MISSING VALUE REPORT")
print("="*70)
missing_summary = pd.DataFrame({
    "Missing Values": df.isnull().sum(),
    "Percentage": round((df.isnull().sum()/len(df))*100, 2)
})
print(missing_summary.sort_values(by="Percentage", ascending=False).head(10))

# Exporting
output_file = "hospital_cleaned.csv"
df.to_csv(output_file, index=False)
print(f"\nCleaned Dataset Saved Successfully to '{output_file}'!")
print("MODULE 2 COMPLETED WITH 0% MISSING VALUES SUCCESSFULLY")