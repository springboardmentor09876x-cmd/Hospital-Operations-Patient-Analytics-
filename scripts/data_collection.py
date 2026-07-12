import pandas as pd
from pathlib import Path

# -------------------------------
# File Paths
# -------------------------------
input_file = Path("Hospital_RawDataset_Updated.xlsx")
output_file = Path("data") / "hospital_raw_data.csv"

# -------------------------------
# Read Excel Dataset
# -------------------------------
print("Loading Dataset...")

df = pd.read_excel(input_file)

print("Dataset Loaded Successfully!\n")

# -------------------------------
# Dataset Information
# -------------------------------
print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# -------------------------------
# Save Raw Dataset
# -------------------------------
df.to_csv(output_file, index=False)

print("\nRaw Dataset Saved Successfully!")
print(f"Output File: {output_file}")