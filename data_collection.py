"""Hospital & Patient Analytics Dataset Analysis Script

This script loads, analyzes, and visualizes hospital patient data.
It provides statistical summaries, data quality checks, and comprehensive visualizations.

Requirements:
- pandas
- matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# Load Dataset
# ===============================
# Load the CSV file containing hospital patient data
df = pd.read_csv("hospital_raw_data.csv")

# Clean column names and rename the typo column 'Hosp+C1:BB1ital Type' -> 'Hospital Type'
df.columns = df.columns.astype(str).str.strip()
df = df.rename(columns={
    'Hosp+C1:BB1ital Type': 'Hospital Type',
    'Hosp?ital Type': 'Hospital Type'
})



# ===============================
# Basic Information & Data Quality Checks
# ===============================
# This section displays fundamental dataset statistics and quality metrics
print("=" * 50)
print("HOSPITAL & PATIENT ANALYTICS DATASET")
print("=" * 50)

# Display sample records
print("\nFirst 5 Records:")
print(df.head())

# Display last sample records
print("\nLast 5 Records:")
print(df.tail())

# Check dataset dimensions
print("\nDataset Shape:")
print(df.shape)

print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

# List all column names for reference
print("\nColumn Names:")
print(df.columns.tolist())

# Display detailed dataset information (data types, memory usage)
print("\nDataset Information:")
df.info()

# Check for missing values - important for data quality assessment
print("\nMissing Values:")
print(df.isnull().sum())

# Identify duplicate records that may need cleaning
print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe(include="all"))

# ===============================
# Detailed Analysis (Only if columns exist)
# ===============================
# This section analyzes specific fields only if they exist in the dataset

# Age Analysis
if "Age" in df.columns:
    print("\n--- AGE ANALYSIS ---")
    print("Average Age:", round(df["Age"].mean(), 2))
    print("Minimum Age:", df["Age"].min())
    print("Maximum Age:", df["Age"].max())

# Gender Demographics Analysis
if "Gender" in df.columns:
    print("\n--- GENDER DISTRIBUTION ---")
    print(df["Gender"].value_counts())

# Common Diagnoses Analysis
if "Diagnosis" in df.columns:
    print("\n--- TOP 10 DIAGNOSES ---")
    print(df["Diagnosis"].value_counts().head(10))

# Hospital Classification Analysis
if "Hospital Type" in df.columns:
    print("\n--- HOSPITAL TYPE DISTRIBUTION ---")
    print(df["Hospital Type"].value_counts())

# Admission Method Analysis
if "Admission Type" in df.columns:
    print("\n--- ADMISSION TYPE DISTRIBUTION ---")
    print(df["Admission Type"].value_counts())

# Insurance Provider Analysis
if "Insurance Provider" in df.columns:
    print("\n--- INSURANCE PROVIDER DISTRIBUTION ---")
    print(df["Insurance Provider"].value_counts())

# Length of Stay Analysis (Hospital Resource Planning)
if "Length of Stay" in df.columns:
    print("\n--- LENGTH OF STAY ANALYSIS ---")
    print("Average Length of Stay:", round(df["Length of Stay"].mean(), 2))

# Billing Analysis (Financial Analytics)
if "Billing Amount" in df.columns:
    print("\n--- BILLING AMOUNT ANALYSIS ---")
    print("Total Billing Amount:", df["Billing Amount"].sum())
    print("Average Billing Amount:", round(df["Billing Amount"].mean(), 2))
    print("Maximum Billing Amount:", df["Billing Amount"].max())
    print("Minimum Billing Amount:", df["Billing Amount"].min())

# ===============================
# Data Visualization - Charts & Graphs
# ===============================
# This section creates visual representations of the data for easier interpretation

# Chart 1: Gender Distribution (Bar Chart)
# Shows the count of patients by gender
if "Gender" in df.columns:
    plt.figure(figsize=(6,4))
    df["Gender"].value_counts().plot(kind="bar")
    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


# Chart 2: Diagnosis Distribution (Bar Chart)
# Shows the top 10 most common diagnoses
if "Diagnosis" in df.columns:
    plt.figure(figsize=(8,4))
    df["Diagnosis"].value_counts().head(10).plot(kind="bar")
    plt.title("Top 10 Diagnoses")
    plt.xlabel("Diagnosis")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Chart 3: Admission Type Distribution (Pie Chart)
# Shows the proportion of different admission types
if "Admission Type" in df.columns:
    plt.figure(figsize=(6,6))
    df["Admission Type"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Admission Type Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()


# Chart 4: Age Distribution (Histogram)
# Shows the age range of patients in the dataset
if "Age" in df.columns:
    plt.figure(figsize=(7,4))
    plt.hist(df["Age"], bins=15)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Number of Patients")
    plt.tight_layout()
    plt.show()

# Chart 5: Billing Amount Distribution (Histogram)
# Shows the distribution of billing costs across patients
if "Billing Amount" in df.columns:
    plt.figure(figsize=(7,4))
    plt.hist(df["Billing Amount"], bins=20)
    plt.title("Billing Amount Distribution")
    plt.xlabel("Billing Amount")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()


# Chart 6: Hospital Type Distribution (Bar Chart)
# Shows the count of patients across different hospital types
if "Hospital Type" in df.columns:
    plt.figure(figsize=(7,4))
    df["Hospital Type"].value_counts().plot(kind="bar")
    plt.title("Hospital Type Distribution")
    plt.xlabel("Hospital Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


# Chart 7: Insurance Provider Distribution (Bar Chart)
# Shows the distribution of patients across different insurance providers
if "Insurance Provider" in df.columns:
    plt.figure(figsize=(7,4))
    df["Insurance Provider"].value_counts().plot(kind="bar")
    plt.title("Insurance Provider Distribution")
    plt.xlabel("Insurance Provider")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ===============================
# Analysis Complete
# ===============================
# All reports and visualizations have been generated

print("\n" + "=" * 50)
print("Analysis Completed Successfully!")
print("=" * 50)