# ==========================================================
# Hospital Dataset Preprocessing 
# ==========================================================

# Import required libraries
import pandas as pd
import numpy as np

# ----------------------------------------------------------
# Step 1: Load Dataset
# ----------------------------------------------------------
df = pd.read_csv("hospital_raw_data.csv")

print("Original Dataset Shape:", df.shape)

# ----------------------------------------------------------
# Step 2: Remove Columns with 100% Missing Values
# ----------------------------------------------------------
# Drop columns where every value is missing

df.dropna(axis=1, how='all', inplace=True)

print("Shape after removing empty columns:", df.shape)

# ----------------------------------------------------------
# Step 3: Remove Columns Having Same Value in Every Row
# (Example: Admission_Date and Discharge_Date)
# ----------------------------------------------------------

for column in df.columns:
    if df[column].nunique(dropna=False) == 1:
        print(f"Removing constant column: {column}")
        df.drop(columns=column, inplace=True)

print("Shape after removing constant columns:", df.shape)

# ----------------------------------------------------------
# Step 4: Convert Date Columns to Proper Date Format
# ----------------------------------------------------------

date_columns = [
    'Admission_Date',
    'Discharge_Date'
]

for column in date_columns:
    if column in df.columns:
        df[column] = pd.to_datetime(
            df[column],
            errors='coerce'
        )

        # Convert into YYYY-MM-DD format
        df[column] = df[column].dt.strftime('%Y-%m-%d')

# ----------------------------------------------------------
# Step 5: Handle Missing Values
# ----------------------------------------------------------

# Separate Numerical and Categorical Columns

numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

categorical_columns = df.select_dtypes(include=['object']).columns

# ----------------------------------------------------------
# Fill Numerical Missing Values using Median
# ----------------------------------------------------------

for column in numerical_columns:
    median_value = df[column].median()
    df[column].fillna(median_value, inplace=True)

# ----------------------------------------------------------
# Fill Categorical Missing Values using Mode
# ----------------------------------------------------------

for column in categorical_columns:
    mode_value = df[column].mode()[0]
    df[column].fillna(mode_value, inplace=True)

# ----------------------------------------------------------
# Step 6: Check Missing Values
# ----------------------------------------------------------

print("\nRemaining Missing Values")
print(df.isnull().sum())

# ----------------------------------------------------------
# Step 7: Remove Duplicate Rows (if any)
# ----------------------------------------------------------

duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df.drop_duplicates(inplace=True)

# ----------------------------------------------------------
# Step 8: Save Cleaned Dataset as CSV
# ----------------------------------------------------------

df.to_csv("Cleaned_Hospital_Dataset.csv", index=False)

print("\nDataset preprocessing completed successfully.")
print("Final Dataset Shape:", df.shape)
print("Cleaned dataset saved as 'Cleaned_Hospital_Dataset.csv'")