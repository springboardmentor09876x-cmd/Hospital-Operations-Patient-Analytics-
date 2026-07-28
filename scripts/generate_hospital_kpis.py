import pandas as pd

# Load cleaned dataset
df = pd.read_csv(
    r"C:\Users\srira\OneDrive\Desktop\Hospital-Operations-Patient-Analytics-\hospital_cleaned.csv"
)
print(df["Bed_Occupancy_Rate_Calc"].head())

print(df["Bed_Occupancy_Rate_Calc"].describe())

# ===========================
# KPI 1 : Total Admissions
# ===========================

total_admissions = df["Patient ID"].nunique()

# ===========================
# KPI 2 : Occupancy Rate
# ===========================

occupancy_rate = df["Bed_Occupancy_Rate_Calc"].mean()

# ===========================
# KPI 3 : Average Length of Stay
# ===========================

avg_length_of_stay = df["Length of Stay"].mean()

# ===========================
# KPI 4 : Readmission Rate
# ===========================

readmission_rate = df["Readmission_Flag"].mean() * 100

# ===========================
# KPI 5 : Bed Utilization Rate
# ===========================

bed_utilization_rate = (
    df["Beds_Occupied_Count"].sum()
    / df["Dept_Bed_Capacity_Derived"].sum()
) * 100

# ===========================
# Display KPIs
# ===========================

print("=" * 40)
print("HOSPITAL KPI SUMMARY")
print("=" * 40)

print(f"Total Admissions       : {total_admissions}")
print(f"Occupancy Rate         : {occupancy_rate*100:.2f}%")
print(f"Average Length of Stay : {avg_length_of_stay:.2f} Days")
print(f"Readmission Rate       : {readmission_rate:.2f}%")
print(f"Bed Utilization Rate   : {bed_utilization_rate*100:.2f}%")


department_efficiency = (
    df.groupby("Department")
      .agg(
          Total_Admissions=("Patient ID", "count"),
          Avg_Length_of_Stay=("Length of Stay", "mean"),
          Avg_Bed_Occupancy=("Bed_Occupancy_Rate_Calc", "mean"),
          Avg_Staff=("Staff Count", "mean")
      )
      .reset_index()
)

department_efficiency["Department_Efficiency_Score"] = (
    department_efficiency["Total_Admissions"]
    * department_efficiency["Avg_Bed_Occupancy"]
) / (
    department_efficiency["Avg_Staff"]
    * department_efficiency["Avg_Length_of_Stay"]
)

print("\nDepartment Efficiency Score")
print(department_efficiency)

department_efficiency = (
    df.groupby("Department")
      .agg(
          Total_Admissions=("Patient ID", "count"),
          Avg_Length_of_Stay=("Length of Stay", "mean"),
          Avg_Bed_Occupancy=("Bed_Occupancy_Rate_Calc", "mean"),
          Avg_Staff=("Staff Count", "mean")
      )
      .reset_index()
)

department_efficiency["Department_Efficiency_Score"] = (
    department_efficiency["Total_Admissions"]
    * department_efficiency["Avg_Bed_Occupancy"]
) / (
    department_efficiency["Avg_Staff"]
    * department_efficiency["Avg_Length_of_Stay"]
)