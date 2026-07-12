import pandas as pd
import os

# ==========================================================
# MedTrack_DV
# Module 1 : Hospital Data Collection
# ==========================================================

print("=" * 60)
print("MEDTRACK_DV - HOSPITAL DATA COLLECTION")
print("=" * 60)

# ----------------------------------------------------------
# Dataset Location
# ----------------------------------------------------------

dataset_path = r"C:\Users\srira\OneDrive\Desktop\infosys\data\hospital_raw_data.csv"

# ----------------------------------------------------------
# Check if Dataset Exists
# ----------------------------------------------------------

if os.path.exists(dataset_path):
    print("\nDataset Found Successfully.")
else:
    print("\nDataset Not Found!")
    print("Check the file path.")
    exit()

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

df = pd.read_csv(dataset_path)

print("\nDataset Loaded Successfully.")

# ----------------------------------------------------------
# Dataset Summary
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("DATASET SUMMARY")
print("=" * 60)

print(f"Rows               : {df.shape[0]}")
print(f"Columns            : {df.shape[1]}")
print(f"Shape              : {df.shape}")

# ----------------------------------------------------------
# Column Names
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("COLUMN NAMES")
print("=" * 60)

for i, column in enumerate(df.columns, start=1):
    print(f"{i}. {column}")

# ----------------------------------------------------------
# Dataset Information
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

df.info()

# ----------------------------------------------------------
# Data Types
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(df.dtypes)

# ----------------------------------------------------------
# First Five Records
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("FIRST FIVE ROWS")
print("=" * 60)

print(df.head())

# ----------------------------------------------------------
# Last Five Records
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("LAST FIVE ROWS")
print("=" * 60)

print(df.tail())

# ----------------------------------------------------------
# Missing Values
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

missing = df.isnull().sum()

print(missing)

print(f"\nTotal Missing Values : {missing.sum()}")

# ----------------------------------------------------------
# Duplicate Records
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("DUPLICATE RECORDS")
print("=" * 60)

duplicates = df.duplicated().sum()

print(f"Duplicate Records : {duplicates}")

# ----------------------------------------------------------
# Statistical Summary
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("STATISTICAL SUMMARY")
print("=" * 60)

print(df.describe(include="all"))

# ----------------------------------------------------------
# Final Message
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("MODULE 1 COMPLETED SUCCESSFULLY")
print("Hospital Dataset Collected and Verified")
print("=" * 60)