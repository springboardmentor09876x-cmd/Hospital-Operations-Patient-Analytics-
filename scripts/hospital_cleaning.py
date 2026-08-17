# ============================================================
# HOSPITAL DATASET PREPROCESSING
# ============================================================

import pandas as pd

# ------------------------------------------------------------
# STEP 1: Load Raw CSV Dataset
# ------------------------------------------------------------

df = pd.read_csv("hospital_raw_data.csv")

print("Original Shape:", df.shape)
print(df.head())

# ------------------------------------------------------------
# STEP 2: Remove Duplicate Rows
# ------------------------------------------------------------

df.drop_duplicates(inplace=True)

# ------------------------------------------------------------
# STEP 3: Remove Duplicate Columns
# ------------------------------------------------------------

df = df.loc[:, ~df.columns.duplicated()]

# ------------------------------------------------------------
# STEP 4: Rename Columns (Optional)
# ------------------------------------------------------------

df.columns = df.columns.str.strip()

# ------------------------------------------------------------
# STEP 5: Convert Admission Date
# ------------------------------------------------------------

# Handles mixed date formats

df["Admission Date"] = pd.to_datetime(
    df["Admission Date"],
    errors="coerce",
    dayfirst=True
).dt.strftime("%d/%m/%Y")

# ------------------------------------------------------------
# STEP 6: Convert Discharge Date
# ------------------------------------------------------------

df["Discharge Date"] = pd.to_datetime(
    df["Discharge Date"],
    errors="coerce",
    dayfirst=True
).dt.strftime("%d/%m/%Y")

# ------------------------------------------------------------
# STEP 7: Remove Unnecessary Timestamp Columns
# ------------------------------------------------------------

if "Admission_Date" in df.columns:
    df.drop(columns=["Admission_Date"], inplace=True)

if "Discharge_Date" in df.columns:
    df.drop(columns=["Discharge_Date"], inplace=True)

# ------------------------------------------------------------
# STEP 8: Handle Missing Values
# ------------------------------------------------------------

# Fill numerical columns with median
num_cols = df.select_dtypes(include=["int64","float64"]).columns

for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

# Fill categorical columns with mode
cat_cols = df.select_dtypes(include="object").columns

for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# ------------------------------------------------------------
# STEP 9: Remove Extra Spaces
# ------------------------------------------------------------

for col in cat_cols:
    df[col] = df[col].astype(str).str.strip()

# ------------------------------------------------------------
# STEP 10: Keep Only Required Columns
# ------------------------------------------------------------
# Remove duplicate columns if any
df = df.loc[:, ~df.columns.duplicated()]

# Keep only valid columns (maintains original order)
df = df[df.columns]

# ------------------------------------------------------------
# STEP 11: Save Cleaned Dataset as Excel
# ------------------------------------------------------------

df.to_excel("Cleaned_Hospital_Dataset.xlsx", index=False)

print("Excel file created successfully.")

# ------------------------------------------------------------
# STEP 12: Convert Excel to CSV
# ------------------------------------------------------------

clean_df = pd.read_excel("Cleaned_Hospital_Dataset.xlsx")

# Save the final cleaned dataset as CSV
clean_df.to_csv("hospital_cleaned.csv", index=False)

print("Final CSV file 'hospital_cleaned.csv' created successfully.")

print("\nFinal Shape:", clean_df.shape)
print(clean_df.head(10))
