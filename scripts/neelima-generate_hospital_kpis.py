# ==========================================
# Module 3 - Hospital KPI Engineering
# Project: Hospital Operations & Patient Analytics
# Author: Neelima Alamanda
# ==========================================

import pandas as pd
import sys

# ==========================================
# Load Cleaned Dataset
# ==========================================

try:
    df = pd.read_csv("../data/neelima-hospital_cleaned.csv")
except FileNotFoundError:
    print("Dataset not found.")
    sys.exit(1)

print("Dataset loaded successfully.")
print(f"Number of records: {len(df)}")
print(f"Number of columns: {len(df.columns)}")


# ==========================================
# Validate Required Columns
# ==========================================

required_columns = [
    "Length of Stay",
    "Readmission",
    "Bed Occupied",
    "Bed_Occupancy_Rate_Calc",
    "ICU_Occupancy_Rate_Calc",
    "Staff_Utilization_Calc"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )

print("All required columns are available.")


# ==========================================
# Validate Missing Values
# ==========================================

kpi_columns = [
    "Length of Stay",
    "Readmission",
    "Bed Occupied",
    "Bed_Occupancy_Rate_Calc",
    "ICU_Occupancy_Rate_Calc",
    "Staff_Utilization_Calc"
]

missing_found = False

for column in kpi_columns:

    if df[column].isnull().any():

        print(
            f"Warning: Missing values found in '{column}'"
        )

        missing_found = True

if not missing_found:
    print("No missing values found in KPI columns.")


# ==========================================
# KPI 1: Total Admissions
# ==========================================

total_admissions = len(df)

print(
    f"Total Admissions: {total_admissions}"
)


# ==========================================
# KPI 2: Occupancy Rate
# ==========================================

occupancy_rate = (
    df["Bed_Occupancy_Rate_Calc"].mean()
) * 100

print(
    f"Occupancy Rate: {occupancy_rate:.2f}%"
)


# ==========================================
# KPI 3: Average Length of Stay
# ==========================================

average_los = df["Length of Stay"].mean()

print(
    f"Average Length of Stay: {average_los:.2f} days"
)


# ==========================================
# KPI 4: Readmission Rate
# ==========================================

readmitted_patients = df["Readmission"].sum()

readmission_rate = (
    readmitted_patients / total_admissions
) * 100

print(
    f"Readmission Rate: {readmission_rate:.2f}%"
)


# ==========================================
# KPI 5: Bed Utilization Rate
# ==========================================

occupied_beds = (
    df["Bed Occupied"] == "Yes"
).sum()

bed_utilization_rate = (
    occupied_beds / total_admissions
) * 100

print(
    f"Bed Utilization Rate: "
    f"{bed_utilization_rate:.2f}%"
)


# ==========================================
# Additional KPI: Staff Utilization
# ==========================================

staff_utilization_rate = (
    df["Staff_Utilization_Calc"].mean()
)

print(
    f"Staff Utilization Rate: "
    f"{staff_utilization_rate:.2f}%"
)


# ==========================================
# KPI 6: Department Efficiency Score
# ==========================================

df["Department_Efficiency_Score"] = (

    (
        df["Bed_Occupancy_Rate_Calc"] * 100
        + df["ICU_Occupancy_Rate_Calc"]
        + df["Staff_Utilization_Calc"]
    ) / 3

)

department_efficiency = (
    df["Department_Efficiency_Score"].mean()
)

print(
    f"Department Efficiency Score: "
    f"{department_efficiency:.2f}%"
)


# ==========================================
# KPI Summary
# ==========================================

kpis = {

    "Total Admissions": total_admissions,

    "Occupancy Rate": occupancy_rate,

    "Average Length of Stay": average_los,

    "Readmission Rate": readmission_rate,

    "Bed Utilization Rate": bed_utilization_rate,

    "Department Efficiency Score":
        department_efficiency,

    "Staff Utilization Rate":
        staff_utilization_rate
}


print("\n========== KPI SUMMARY ==========")

for name, value in kpis.items():

    if name == "Average Length of Stay":

        print(
            f"{name:30}: "
            f"{value:.2f} days"
        )

    elif name == "Total Admissions":

        print(
            f"{name:30}: "
            f"{value}"
        )

    else:

        print(
            f"{name:30}: "
            f"{value:.2f}%"
        )

print("=================================")


# ==========================================
# Store KPI Values in Final Dataset
# ==========================================

df["Total_Admissions"] = total_admissions

df["Occupancy_Rate"] = occupancy_rate

df["Average_Length_of_Stay"] = average_los

df["Readmission_Rate"] = readmission_rate

df["Bed_Utilization_Rate"] = bed_utilization_rate

df["Department_Efficiency_Score"] = (
    department_efficiency
)

df["Staff_Utilization_Rate"] = (
    staff_utilization_rate
)


# ==========================================
# Export Final Dataset
# ==========================================

output_path = (
    "../data/neelima-hospital_final_dataset.xlsx"
)

df.to_excel(
    output_path,
    index=False
)

print(
    "\nFinal dataset exported successfully."
)

print(
    f"Location: {output_path}"
)

print(
    "\nModule 3 completed successfully."
)

print(
    "Final dataset is ready for Tableau Dashboard development."
)