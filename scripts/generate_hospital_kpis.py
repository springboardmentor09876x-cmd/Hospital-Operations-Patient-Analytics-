import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/hospital_cleaned.csv")

# -----------------------------
# Hospital KPIs
# -----------------------------

# Total Admissions
total_admissions = len(df)

# Occupancy Rate
occupancy_rate = df["Bed_Occupancy_Rate_Calc"].mean() * 100

# Average Length of Stay
avg_los = df["Length of Stay"].mean()

# Readmission Rate
readmission_rate = df["Readmission_Flag"].mean() * 100

# Bed Utilization Rate
bed_utilization_rate = df["Bed_Occupancy_Rate_Calc"].mean() * 100

# Department Efficiency Score
df["Department_Efficiency_Score"] = (
    df["Staff_Utilization_Calc"] +
    df["Bed_Occupancy_Rate_Calc"]
) / 2

department_efficiency = df.groupby("Department")[
    "Department_Efficiency_Score"
].mean().reset_index()

# -----------------------------
# Print KPIs
# -----------------------------

print("\nHospital KPIs")
print("-" * 35)
print(f"Total Admissions          : {total_admissions}")
print(f"Occupancy Rate (%)        : {occupancy_rate:.2f}")
print(f"Average Length of Stay    : {avg_los:.2f}")
print(f"Readmission Rate (%)      : {readmission_rate:.2f}")
print(f"Bed Utilization Rate (%)  : {bed_utilization_rate:.2f}")

print("\nDepartment Efficiency Scores")
print(department_efficiency)

# -----------------------------
# Save Final Dataset
# -----------------------------

df.to_excel(
    "data/hospital_final_dataset.xlsx",
    index=False
)

print("\nFinal dataset saved successfully!")