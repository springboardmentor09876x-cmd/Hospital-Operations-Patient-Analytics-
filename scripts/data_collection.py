#Module - 1


import pandas as pd
import numpy as np


hospital = pd.read_csv("Hospital_Operations_Dataset.csv")
reference = pd.read_excel("Hospital_RawDataset_Updated.xlsx")

print("Hospital Operations Dataset Shape:", hospital.shape)
print("Reference Dataset Shape:", reference.shape)

missing_columns = [col for col in reference.columns if col not in hospital.columns]

print("\nMissing Columns:")
print(missing_columns)

for col in missing_columns:
    hospital[col] = np.nan

for col in missing_columns:

    # Remove null values from reference column
    values = reference[col].dropna()

    # If the reference column has no values, keep NaN
    if len(values) == 0:
        continue

    # Randomly sample values to fill every row
    hospital[col] = values.sample(
        n=len(hospital),
        replace=True,
        random_state=42
    ).values

    hospital.to_csv("hospital_raw_data.csv", index=False)

print("\nMerged dataset saved successfully!")
print("File Name: hospital_raw_data.csv")

