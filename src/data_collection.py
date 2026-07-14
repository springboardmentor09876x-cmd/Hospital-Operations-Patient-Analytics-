import pandas as pd
import numpy as np
import os

# ============================================================
# Load Datasets
# ============================================================

patient = pd.read_csv("Hospital.csv")
hospital = pd.read_csv("Hospitals&Beds.csv")
icu = pd.read_csv("ICU.csv")
reference = pd.read_csv("Final.csv")
print("Datasets Loaded Successfully")

# ============================================================
# Rename Columns
# ============================================================

hospital = hospital.rename(columns={
    "Unnamed: 0": "State",
    "Total": "Hospitals_Count",
    "Unnamed: 6": "Beds Available"
})

icu = icu.rename(columns={
    "States/UTs": "State",
    "Total number of ICU beds (public + private)": "ICU Beds"
})

# ============================================================
# Remove Summary Row
# ============================================================

hospital = hospital[hospital["State"] != "All India"]

# ============================================================
# Standardize State Names
# ============================================================

replace_states = {
    "Andaman & Nicobar Islands": "Andaman Nicobar Islands",
    "Jammu & Kashmir": "Jammu And Kashmir",
    "Daman & Diu": "Daman And Diu"
}

hospital["State"] = hospital["State"].replace(replace_states)
icu["State"] = icu["State"].replace(replace_states)

# ============================================================
# Assign Random State to Patient Dataset
# ============================================================

np.random.seed(42)

patient["State"] = np.random.choice(
    hospital["State"],
    size=len(patient),
    replace=True
)

# ============================================================
# Merge Hospital Dataset
# ============================================================

patient = patient.merge(
    hospital[["State", "Beds Available"]],
    on="State",
    how="left"
)

# ============================================================
# Merge ICU Dataset
# ============================================================

patient = patient.merge(
    icu[["State", "ICU Beds"]],
    on="State",
    how="left"
)

# ============================================================
# Rename Patient Columns
# ============================================================

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

# ============================================================
# Add & Expand Reference Columns Safely
# ============================================================

# Expand the reference dataframe to match the size of patient
repeat = (len(patient) // len(reference)) + 1
expanded_reference = pd.concat(
    [reference] * repeat,
    ignore_index=True
).iloc[:len(patient)].reset_index(drop=True)

# Define columns we want to retain from original patient dataset
keep_columns = [
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

# Pull the other columns directly from our expanded reference
for col in expanded_reference.columns:
    if col not in keep_columns:
        patient[col] = expanded_reference[col].values

# ============================================================
# Generate Admission & Discharge Dates
# ============================================================

patient["Admission Date"] = pd.date_range(
    start="2024-01-01",
    periods=len(patient),
    freq="h"
)

patient["Discharge Date"] = (
    patient["Admission Date"]
    + pd.to_timedelta(
        np.random.randint(1, 15, len(patient)),
        unit="D"
    )
)

patient["Length of Stay"] = (
    patient["Discharge Date"]
    - patient["Admission Date"]
).dt.days

patient["Admission Date"] = patient["Admission Date"].dt.strftime("%Y-%m-%d")
patient["Discharge Date"] = patient["Discharge Date"].dt.strftime("%Y-%m-%d")

# ============================================================
# Create Doctor Names
# ============================================================

first_names = [
    "Amit","Rahul","Priya","Sneha","Anjali",
    "Kiran","Arjun","Neha","Divya","Lakshmi",
    "Harish","Akash","Vivek","Ramesh","Sai",
    "Naveen","Suresh","Pavan","Rohit","Deepak"
]

last_names = [
    "Sharma","Reddy","Patel","Kumar","Verma",
    "Iyer","Singh","Rao","Gupta","Menon",
    "Naidu","Yadav","Joshi","Kapoor","Mishra"
]

unique_doctors = sorted(expanded_reference["Doctor"].unique())

doctor_map = {}
for i, d in enumerate(unique_doctors):
    doctor_map[d] = f"Dr. {first_names[i % len(first_names)]} {last_names[(i // len(first_names)) % len(last_names)]}"

patient["Doctor"] = expanded_reference["Doctor"].map(doctor_map)

# ============================================================
# Save Final Dataset
# ============================================================

patient.to_csv("hospital_raw_data.csv", index=False)

print("=" * 60)
print("Merge Completed Successfully")
print("=" * 60)

print("Rows :", patient.shape[0])
print("Columns :", patient.shape[1])

print("\nMissing Values After Merge")
print(patient[["State", "Beds Available", "ICU Beds"]].isnull().sum())

print("\nFinal Dataset Saved As : hospital_raw_data.csv")


# ============================================================
# Master Integration Script
# ============================================================

print("\nLoading your raw dataset...")
try:
    main_df = pd.read_csv('hospital_raw_data.csv')
except FileNotFoundError:
    print("❌ Error: 'hospital_raw_data.csv' not found.")
    raise

n_rows = len(main_df)
np.random.seed(42)

print("Generating and mapping the remaining columns...")

hospitals = main_df['Hospital'].unique() if 'Hospital' in main_df.columns else ['General Hospital']
hospital_mapping = {h: {
    'Hospital ID': f"HOSP_{i+1:03d}",
    'Hospital Name': f"{h} Medical Center",
    'Hospital Type': np.random.choice(['Private', 'Public', 'Trust'], p=[0.5, 0.3, 0.2])
} for i, h in enumerate(hospitals)}

departments = main_df['Department'].unique() if 'Department' in main_df.columns else ['Emergency']
dept_mapping = {d: f"DEPT_{i+1:02d}" for i, d in enumerate(departments)}

h_ids = [hospital_mapping[h]['Hospital ID'] for h in main_df['Hospital']] if 'Hospital' in main_df.columns else [f"HOSP_{np.random.randint(1,10):03d}" for _ in range(n_rows)]
h_names = [hospital_mapping[h]['Hospital Name'] for h in main_df['Hospital']] if 'Hospital' in main_df.columns else [f"General Hospital_{np.random.randint(1,10)}" for _ in range(n_rows)]
h_types = [hospital_mapping[h]['Hospital Type'] for h in main_df['Hospital']] if 'Hospital' in main_df.columns else [np.random.choice(['Private', 'Public', 'Trust']) for _ in range(n_rows)]
d_ids = [dept_mapping[d] for d in main_df['Department']] if 'Department' in main_df.columns else [f"DEPT_{np.random.randint(1,5):02d}" for _ in range(n_rows)]

# 3. Create the dataframe for the missing columns
remaining_df = pd.DataFrame({
    'Patient ID': main_df['Patient ID'], # Merge Key
    'Hospital ID': h_ids,
    'Hospital Name': h_names,
    'Hospital Type': h_types,
    'Department ID': d_ids,
    'Patient Name': [f"Patient_{i+1}" for i in range(n_rows)],
    'Nurses': np.random.randint(5, 25, size=n_rows),
    'Staff Count': np.random.randint(20, 100, size=n_rows),
    'Treatment': np.random.choice(['Antibiotics', 'Surgery', 'Physical Therapy', 'Chemotherapy', 'Observation'], size=n_rows),
    'Medication': np.random.choice(['Paracetamol', 'Ibuprofen', 'Amoxicillin', 'Metformin', 'None'], size=n_rows),
    'Test Result': np.random.choice(['Normal', 'Abnormal', 'Inconclusive'], size=n_rows, p=[0.7, 0.2, 0.1]),
    'Blood Type': np.random.choice(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'], size=n_rows),
    'Bed Number': np.random.randint(100, 500, size=n_rows),
    'Bed Occupied': np.random.choice(['Yes', 'No'], size=n_rows, p=[0.8, 0.2]),
    'Equipment': np.random.choice(['X-Ray', 'MRI', 'Ultrasound', 'Ventilator', 'None'], size=n_rows),
    'Room No': np.random.randint(101, 499, size=n_rows),
    'Dept_Bed_Capacity': np.random.randint(50, 200, size=n_rows),
    'Beds_Occupied_Count': np.random.randint(10, 50, size=n_rows),
    'Equipment ID': [f"EQ_{np.random.randint(1000, 9999)}" for _ in range(n_rows)],
    'Equipment Number': [f"EQ-NUM-{np.random.randint(100, 999)}" for _ in range(n_rows)],
    'Equipment Status': np.random.choice(['Functional', 'Under Maintenance', 'Stored'], size=n_rows, p=[0.85, 0.10, 0.05]),
    'Equipment_Total_Inventory': np.random.randint(5, 30, size=n_rows),
    'Equipment_Usage_Duration': np.random.randint(1, 24, size=n_rows),
    'Transferred': np.random.choice(['Yes', 'No'], size=n_rows, p=[0.15, 0.85]),
    'Transfer_From_Department': np.random.choice(departments, size=n_rows),
    'Transfer_To_Department': np.random.choice(departments, size=n_rows),
    'Transfer_Date': main_df['Admission Date'], 
    'Number_of_Transfers': np.random.randint(0, 3, size=n_rows),
    'Dept_ICU_Bed_Capacity': np.random.randint(10, 40, size=n_rows),
    'Dept_Staff_Capacity': np.random.randint(30, 120, size=n_rows),
    'Admissions_Rate_Percentage': np.random.uniform(60, 95, size=n_rows).round(2),
    'Staff_Utilization_Percentage': np.random.uniform(50, 90, size=n_rows).round(2),
    'Bed_Occupancy_Rate': np.random.uniform(65, 98, size=n_rows).round(2),
    'ICU_Occupancy_Rate': np.random.uniform(40, 90, size=n_rows).round(2),
    'Staff_Utilization_Calculation': np.random.uniform(50, 90, size=n_rows).round(2),
    'Readmission_Flag': main_df['Readmission'],
    'Transferred_Flag': np.where(main_df['Wait_Time_Minutes'] > 120, 1, 0) if 'Wait_Time_Minutes' in main_df.columns else np.random.choice([0, 1], size=n_rows, p=[0.1, 0.9]),
    'Equipment_InUse_Flag': np.random.choice([0, 1], size=n_rows, p=[0.3, 0.7])
})

# Merge datasets
print("Merging datasets together...")
merged_df = pd.merge(main_df, remaining_df, on='Patient ID', how='left')

# Save final master dataset
merged_df.to_csv('hospital_master_dataset.csv', index=False)
print("\n🎉 Success! Combined dataset saved as 'hospital_master_dataset.csv'")
print(f"Total rows and columns: {merged_df.shape}")