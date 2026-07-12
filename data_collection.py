import pandas as pd
import numpy as np

# ==========================================
# Module 1 - Data Collection & Merging
# Hospital Operations & Patient Analytics
# ==========================================

# Load datasets
hospital = pd.read_csv("cleaned_hospital_dataset.csv")
reference = pd.read_excel("Hospital_RawDataset.xlsx")

print("Hospital Dataset Shape:", hospital.shape)
print("Reference Dataset Shape:", reference.shape)

# Find columns present in reference but missing in hospital
missing_columns = [col for col in reference.columns if col not in hospital.columns]

print("\nMissing Columns:")
print(missing_columns)

# Add missing columns
for col in missing_columns:
    hospital[col] = np.nan

# Fill missing columns using values from the reference dataset
for col in missing_columns:

    # Remove null values from reference column
    values = reference[col].dropna()

    # Skip if the reference column has no values
    if len(values) == 0:
        continue

    # Randomly sample values from the reference dataset
    hospital[col] = values.sample(
        n=len(hospital),
        replace=True,
        random_state=42
    ).values

# Arrange columns in the same order as the reference dataset
hospital = hospital[reference.columns]

# Save merged/raw dataset
hospital.to_csv("hospital_raw_data.csv", index=False)

print("\nMerged dataset saved successfully!")
print("File Name: hospital_raw_data.csv")
print("Final Dataset Shape:", hospital.shape)
