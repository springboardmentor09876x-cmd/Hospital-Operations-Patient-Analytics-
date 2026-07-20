# ==========================================
# Module 3 - Hospital KPI Engineering
# Project: Hospital Operations & Patient Analytics
# Author: Neelima Alamanda
# ==========================================

# Import required libraries
import pandas as pd
import sys

# Load the cleaned dataset
try:
    df = pd.read_csv("../data/neelima-hospital_cleaned.csv")
except FileNotFoundError:
    print("Dataset not found.")
    sys.exit(1)

print("Dataset loaded successfully.")
print(f"Number of records: {len(df)}")
print(f"Number of columns: {len(df.columns)}")

# ==========================================
# KPI 1: Total Admissions
# ==========================================

total_admissions = len(df)

print(f"Total Admissions: {total_admissions}")

# ==========================================
# Validate Required Columns
# ==========================================

required_columns = [
    "Length of Stay",
    "Readmission_Flag",
    "Beds_Occupied_Count",
    "Dept_Bed_Capacity_Derived",
    "Staff_Utilization_Calc",
    "Bed_Occupancy_Rate_Calc",
    "Admissions_Rate_%_Derived"
]

missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

print("All required columns are available.")

# ==========================================
# KPI 2: Average Length of Stay
# ==========================================

# ==========================================
# Validate Missing Values in KPI Columns
# ==========================================

kpi_columns = [
    "Length of Stay",
    "Readmission_Flag",
    "Bed_Occupancy_Rate_Calc",
    "Staff_Utilization_Calc",
    "ICU_Occupancy_Rate_Calc"
]
missing_found = False

for column in kpi_columns:
    if df[column].isnull().any():
        print(f"Warning: Missing values found in '{column}'")
        missing_found = True

if not missing_found:
    print("No missing values found in KPI columns.")


average_los = df["Length of Stay"].mean()
print(f"Average Length of Stay: {average_los:.2f} days")


# ==========================================
# KPI 3: Readmission Rate
# ==========================================

readmitted_patients = df["Readmission_Flag"].sum()

readmission_rate = (readmitted_patients / total_admissions) * 100

print(f"Readmission Rate: {readmission_rate:.2f}%")

# ==========================================
# KPI 4: Overall Occupancy Rate
# ==========================================

occupancy_rate = df["Bed_Occupancy_Rate_Calc"].mean() * 100

print(f"Overall Occupancy Rate: {occupancy_rate:.2f}%")

# ==========================================
# KPI 5: Overall Staff Utilization Rate
# ==========================================

staff_utilization_rate = df["Staff_Utilization_Calc"].mean()

print(f"Overall Staff Utilization Rate: {staff_utilization_rate:.2f}%")

# ==========================================
# KPI 6: Department Efficiency Score
# ==========================================
# Composite KPI created for dashboard analysis.
# It represents the average of:
# - Bed Occupancy Rate
# - ICU Occupancy Rate
# - Staff Utilization Rate
# Bed Occupancy is converted from decimal to percentage.

df["Department_Efficiency_Score"] = (
    (
        df["Bed_Occupancy_Rate_Calc"] * 100 +
        df["ICU_Occupancy_Rate_Calc"] +
        df["Staff_Utilization_Calc"]
    ) / 3
)

department_efficiency = df["Department_Efficiency_Score"].mean()

print("Department Efficiency Score column created.")

# ==========================================
# Store KPI Values
# ==========================================

kpis = {
    "Total Admissions": total_admissions,
    "Average Length of Stay": average_los,
    "Readmission Rate": readmission_rate,
    "Overall Occupancy Rate": occupancy_rate,
    "Overall Staff Utilization": staff_utilization_rate,
    "Department Efficiency": department_efficiency
}
# ==========================================
# KPI Summary
# ==========================================

print("\n========== KPI SUMMARY ==========")

for name, value in kpis.items():

    if isinstance(value, float):

        if "Length" in name:
            print(f"{name:30}: {value:.2f} days")
        else:
            print(f"{name:30}: {value:.2f}%")

    else:
        print(f"{name:30}: {value}")

print("=================================")
# ==========================================
# Export Final Dataset
# ==========================================

output_path = "../data/neelima-hospital_final_dataset.xlsx"

df.to_excel(output_path, index=False)

print(f"\nFinal dataset exported successfully.")
print(f"Location: {output_path}")
print("\nModule 3 completed successfully.")
print("Final dataset is ready for Tableau Dashboard development.")

