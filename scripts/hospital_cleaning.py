import pandas as pd
from pathlib import Path

# -------------------------------
# File Paths
# -------------------------------
input_file = Path("data") / "hospital_raw_data.csv"
output_file = Path("data") / "hospital_cleaned.csv"

# -------------------------------
# Load Dataset
# -------------------------------
print("Loading Raw Dataset...")

df = pd.read_csv(input_file)

print("Dataset Loaded Successfully!")

# -------------------------------
# Remove Duplicate Rows
# -------------------------------
duplicates = df.duplicated().sum()
print(f"Duplicate Rows Found: {duplicates}")

df = df.drop_duplicates()

# -------------------------------
# Handle Missing Values
# -------------------------------
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill numeric columns with median
numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Fill text columns with "Unknown"
text_cols = df.select_dtypes(include=['object']).columns
df[text_cols] = df[text_cols].fillna("Unknown")

# -------------------------------
# Standardize Column Names
# -------------------------------
df.columns = (
    df.columns.str.strip()
              .str.lower()
              .str.replace(" ", "_")
)

# -------------------------------
# Save Cleaned Dataset
# -------------------------------
df.to_csv(output_file, index=False)

print("\nCleaning Completed Successfully!")
print(f"Cleaned Dataset Saved To: {output_file}")