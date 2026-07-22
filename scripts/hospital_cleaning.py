import pandas as pd
from pathlib import Path

# -----------------------------------
# File Paths
# -----------------------------------
input_file = Path("data") / "hospital_cleaned.csv"
output_file = Path("data") / "hospital_cleaned.csv"

print("Loading Mentor's Cleaned Dataset...")

# -----------------------------------
# Load Dataset
# -----------------------------------
df = pd.read_csv(input_file)

print("Dataset Loaded Successfully!")

# -----------------------------------
# Remove Duplicate Rows (if any)
# -----------------------------------
duplicates = df.duplicated().sum()
print(f"Duplicate Rows Found: {duplicates}")

df.drop_duplicates(inplace=True)

# -----------------------------------
# Missing Values Before Cleaning
# -----------------------------------
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# -----------------------------------
# Update Transfer_Date
# -----------------------------------
if "Transfer_Date" in df.columns:
    df["Transfer_Date"] = (
        df["Transfer_Date"]
        .replace("", pd.NA)
        .fillna("Not Transferred")
    )

# -----------------------------------
# Missing Values After Cleaning
# -----------------------------------
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# -----------------------------------
# Save Dataset
# -----------------------------------
df.to_csv(output_file, index=False)

print("\nCleaning Completed Successfully!")
print(f"Updated dataset saved to: {output_file}")