# ==========================================================
# Hospital Operations & Patient Analytics Dashboard
# Module 3 - KPI Generation
#
# Author : Your Name
# Project : MedTrack_DV
# ==========================================================

# ==========================================================
# Import Libraries
# ==========================================================

import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# ==========================================================
# Load Cleaned Dataset
# ==========================================================

print("=" * 70)
print("        HOSPITAL KPI GENERATION MODULE")
print("=" * 70)

df = pd.read_csv("cleaned_hospital_dataset.csv")

print("\nDataset Loaded Successfully")
print("Dataset Shape :", df.shape)

# ==========================================================
# Dataset Information
# ==========================================================

print("\nDataset Information")
print("-" * 70)

print(df.info())

print("\nColumn Names")

for column in df.columns:
    print(column)

# ==========================================================
# Validate Required Columns
# ==========================================================

required_columns = [

    "Visit ID",
    "Patient ID",
    "Name",
    "Age",
    "Gender",
    "Hospital ID",
    "Hospital Name",
    "Department",
    "Diagnosis",
    "Treatment",
    "Doctor",
    "Admission Date",
    "Discharge Date",
    "Length of Stay",
    "Readmitted",
    "Bed Number",
    "Admission Type",
    "Insurance Provider",
    "Billing Amount",
    "Test Results",
    "Blood Type",
    "City",
    "State",
    "Hospital Type",
    "Beds Available_hospital",
    "ICU Beds",
    "Staff Count",
    "Doctors",
    "Nurses",
    "Equipment",
    "Beds Available_dept",
    "Beds Occupied",
    "Bed Utilization %"

]

print("\nChecking Required Columns...")

missing_columns = [
    col
    for col in required_columns
    if col not in df.columns
]

if len(missing_columns) == 0:

    print("All required columns are present.")

else:

    print("Missing Columns")

    print(missing_columns)

# ==========================================================
# Dataset Quality Check
# ==========================================================

print("\nDataset Quality Check")

print("-" * 70)

print("Rows :", df.shape[0])

print("Columns :", df.shape[1])

print("Duplicate Records :", df.duplicated().sum())

print("\nMissing Values")

print(df.isnull().sum())

# ==========================================================
# Data Type Verification
# ==========================================================

print("\nData Types")

print("-" * 70)

print(df.dtypes)

# ==========================================================
# Convert Date Columns
# ==========================================================

print("\nConverting Date Columns...")

df["Admission Date"] = pd.to_datetime(
    df["Admission Date"]
)

df["Discharge Date"] = pd.to_datetime(
    df["Discharge Date"]
)

print("Date Conversion Completed")

# ==========================================================
# Create Time-Based Features
# ==========================================================

print("\nCreating Date Features...")

df["Admission Year"] = (
    df["Admission Date"].dt.year
)

df["Admission Month"] = (
    df["Admission Date"].dt.month_name()
)

df["Admission Quarter"] = (
    "Q" +
    df["Admission Date"].dt.quarter.astype(str)
)

df["Admission Week"] = (
    df["Admission Date"].dt.isocalendar().week
)

df["Admission Day"] = (
    df["Admission Date"].dt.day_name()
)

df["Discharge Year"] = (
    df["Discharge Date"].dt.year
)

df["Discharge Month"] = (
    df["Discharge Date"].dt.month_name()
)

print("Date Features Created")

# ==========================================================
# Create Age Groups
# ==========================================================

print("\nCreating Age Groups...")

df["Age Group"] = pd.cut(

    df["Age"],

    bins=[0,18,35,50,65,120],

    labels=[
        "0-18",
        "19-35",
        "36-50",
        "51-65",
        "65+"
    ],

    include_lowest=True

)

# ==========================================================
# Billing Categories
# ==========================================================

print("Creating Billing Categories...")

df["Billing Category"] = pd.cut(

    df["Billing Amount"],

    bins=[
        -np.inf,
        1000,
        3000,
        5000,
        np.inf
    ],

    labels=[
        "Low",
        "Medium",
        "High",
        "Very High"
    ]

)

# ==========================================================
# Length of Stay Categories
# ==========================================================

print("Creating Length of Stay Categories...")

df["LOS Category"] = pd.cut(

    df["Length of Stay"],

    bins=[
        -1,
        3,
        7,
        14,
        100
    ],

    labels=[
        "Short Stay",
        "Medium Stay",
        "Long Stay",
        "Critical Stay"
    ]

)

# ==========================================================
# Bed Occupancy Status
# ==========================================================

print("Creating Bed Occupancy Status...")

df["Bed Status"] = np.where(

    df["Bed Utilization %"] >= 85,

    "High Occupancy",

    np.where(

        df["Bed Utilization %"] >= 60,

        "Moderate Occupancy",

        "Low Occupancy"

    )

)

# ==========================================================
# Revenue Classification
# ==========================================================

average_bill = df["Billing Amount"].mean()

df["Revenue Flag"] = np.where(

    df["Billing Amount"] >= average_bill,

    "Above Average",

    "Below Average"

)

print("\nFeature Engineering Completed Successfully")

# ==========================================================
# Preview Dashboard Dataset
# ==========================================================

print("\nUpdated Dataset Shape :", df.shape)

print(df.head())
# ==========================================================
# HOSPITAL KPI CALCULATIONS
# ==========================================================

print("\n" + "=" * 70)
print("GENERATING HOSPITAL KPIs")
print("=" * 70)

# ----------------------------------------------------------
# Patient KPIs
# ----------------------------------------------------------

total_patients = df["Visit ID"].nunique()

unique_patients = df["Patient ID"].nunique()

male_patients = (
    df["Gender"] == "Male"
).sum()

female_patients = (
    df["Gender"] == "Female"
).sum()

average_age = round(
    df["Age"].mean(),
    2
)

youngest_patient = df["Age"].min()

oldest_patient = df["Age"].max()

print("Patient KPIs Generated")

# ----------------------------------------------------------
# Hospital KPIs
# ----------------------------------------------------------

total_hospitals = df["Hospital ID"].nunique()

hospital_types = df["Hospital Type"].nunique()

total_departments = df["Department"].nunique()

total_doctors = df["Doctor"].nunique()

total_staff = df["Staff Count"].sum()

total_nurses = df["Nurses"].sum()

print("Hospital KPIs Generated")

# ----------------------------------------------------------
# Financial KPIs
# ----------------------------------------------------------

total_revenue = round(
    df["Billing Amount"].sum(),
    2
)

average_bill = round(
    df["Billing Amount"].mean(),
    2
)

highest_bill = round(
    df["Billing Amount"].max(),
    2
)

lowest_bill = round(
    df["Billing Amount"].min(),
    2
)

median_bill = round(
    df["Billing Amount"].median(),
    2
)

print("Financial KPIs Generated")

# ----------------------------------------------------------
# Admission KPIs
# ----------------------------------------------------------

average_los = round(
    df["Length of Stay"].mean(),
    2
)

maximum_los = df["Length of Stay"].max()

minimum_los = df["Length of Stay"].min()

emergency_cases = (
    df["Admission Type"] == "Emergency"
).sum()

elective_cases = (
    df["Admission Type"] == "Elective"
).sum()

urgent_cases = (
    df["Admission Type"] == "Urgent"
).sum()

print("Admission KPIs Generated")

# ----------------------------------------------------------
# Readmission KPIs
# ----------------------------------------------------------

readmitted = (
    df["Readmitted"] == "Yes"
).sum()

not_readmitted = (
    df["Readmitted"] == "No"
).sum()

readmission_rate = round(

    (readmitted / len(df)) * 100,

    2

)

print("Readmission KPIs Generated")

# ----------------------------------------------------------
# Bed KPIs
# ----------------------------------------------------------

occupied_beds = df["Beds Occupied"].sum()

available_beds = df["Beds Available_dept"].sum()

icu_beds = df["ICU Beds"].sum()

average_utilization = round(

    df["Bed Utilization %"].mean(),

    2

)

highest_utilization = round(

    df["Bed Utilization %"].max(),

    2

)

lowest_utilization = round(

    df["Bed Utilization %"].min(),

    2

)

print("Bed KPIs Generated")

# ----------------------------------------------------------
# Blood Group Distribution
# ----------------------------------------------------------

blood_group_summary = (

    df["Blood Type"]

    .value_counts()

    .reset_index()

)

blood_group_summary.columns = [

    "Blood Group",

    "Patients"

]

# ----------------------------------------------------------
# Gender Distribution
# ----------------------------------------------------------

gender_summary = (

    df["Gender"]

    .value_counts()

    .reset_index()

)

gender_summary.columns = [

    "Gender",

    "Patients"

]

# ----------------------------------------------------------
# Age Group Summary
# ----------------------------------------------------------

age_group_summary = (

    df["Age Group"]

    .value_counts()

    .reset_index()

)

age_group_summary.columns = [

    "Age Group",

    "Patients"

]

print("Patient Demographic KPIs Generated")

# ==========================================================
# CREATE KPI REPORT
# ==========================================================

kpi_report = pd.DataFrame({

"KPI":[

"Total Visits",

"Unique Patients",

"Male Patients",

"Female Patients",

"Average Age",

"Youngest Patient",

"Oldest Patient",

"Total Hospitals",

"Hospital Types",

"Departments",

"Doctors",

"Staff Count",

"Nurses",

"Total Revenue",

"Average Billing",

"Highest Bill",

"Lowest Bill",

"Median Billing",

"Average Length of Stay",

"Maximum Length of Stay",

"Minimum Length of Stay",

"Emergency Admissions",

"Elective Admissions",

"Urgent Admissions",

"Readmitted Patients",

"Not Readmitted",

"Readmission Rate (%)",

"Beds Occupied",

"Beds Available",

"ICU Beds",

"Average Bed Utilization (%)",

"Highest Bed Utilization",

"Lowest Bed Utilization"

],

"Value":[

total_patients,

unique_patients,

male_patients,

female_patients,

average_age,

youngest_patient,

oldest_patient,

total_hospitals,

hospital_types,

total_departments,

total_doctors,

total_staff,

total_nurses,

total_revenue,

average_bill,

highest_bill,

lowest_bill,

median_bill,

average_los,

maximum_los,

minimum_los,

emergency_cases,

elective_cases,

urgent_cases,

readmitted,

not_readmitted,

readmission_rate,

occupied_beds,

available_beds,

icu_beds,

average_utilization,

highest_utilization,

lowest_utilization

]

})

print("\nHospital KPI Report Created Successfully")

print(kpi_report.head(15))
# ==========================================================
# DEPARTMENT KPI SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("GENERATING DEPARTMENT SUMMARY")
print("=" * 70)

department_summary = (

    df.groupby("Department")

    .agg(

        Total_Patients=("Visit ID","count"),

        Total_Revenue=("Billing Amount","sum"),

        Average_Billing=("Billing Amount","mean"),

        Average_LOS=("Length of Stay","mean"),

        Readmission_Count=("Readmitted",
                           lambda x:(x=="Yes").sum()),

        Average_Bed_Utilization=("Bed Utilization %","mean")

    )

    .reset_index()

)

department_summary["Average_Billing"] = (
    department_summary["Average_Billing"].round(2)
)

department_summary["Average_LOS"] = (
    department_summary["Average_LOS"].round(2)
)

department_summary["Average_Bed_Utilization"] = (
    department_summary["Average_Bed_Utilization"].round(2)
)

print("Department Summary Created")

# ==========================================================
# HOSPITAL SUMMARY
# ==========================================================

print("\nGenerating Hospital Summary...")

hospital_summary = (

    df.groupby("Hospital Name")

    .agg(

        Total_Visits=("Visit ID","count"),

        Total_Revenue=("Billing Amount","sum"),

        Average_Billing=("Billing Amount","mean"),

        Beds_Occupied=("Beds Occupied","sum"),

        Beds_Available=("Beds Available_dept","sum"),

        Average_Bed_Utilization=("Bed Utilization %","mean")

    )

    .reset_index()

)

hospital_summary["Occupancy Rate"] = (

    hospital_summary["Beds_Occupied"]

    /

    hospital_summary["Beds_Available"]

) * 100

hospital_summary["Average_Billing"] = (
    hospital_summary["Average_Billing"].round(2)
)

hospital_summary["Occupancy Rate"] = (
    hospital_summary["Occupancy Rate"].round(2)
)

print("Hospital Summary Created")

# ==========================================================
# DOCTOR PERFORMANCE SUMMARY
# ==========================================================

print("\nGenerating Doctor Summary...")

doctor_summary = (

    df.groupby("Doctor")

    .agg(

        Patients=("Visit ID","count"),

        Revenue=("Billing Amount","sum"),

        Average_Billing=("Billing Amount","mean"),

        Average_LOS=("Length of Stay","mean")

    )

    .reset_index()

)

doctor_summary = doctor_summary.sort_values(

    by="Revenue",

    ascending=False

)

doctor_summary["Average_Billing"] = (
    doctor_summary["Average_Billing"].round(2)
)

doctor_summary["Average_LOS"] = (
    doctor_summary["Average_LOS"].round(2)
)

print("Doctor Summary Created")

# ==========================================================
# INSURANCE PROVIDER ANALYSIS
# ==========================================================

print("\nGenerating Insurance Summary...")

insurance_summary = (

    df.groupby("Insurance Provider")

    .agg(

        Patients=("Visit ID","count"),

        Revenue=("Billing Amount","sum"),

        Average_Billing=("Billing Amount","mean")

    )

    .reset_index()

)

insurance_summary["Average_Billing"] = (
    insurance_summary["Average_Billing"].round(2)
)

insurance_summary = insurance_summary.sort_values(

    by="Revenue",

    ascending=False

)

print("Insurance Summary Created")

# ==========================================================
# CITY-WISE ANALYSIS
# ==========================================================

print("\nGenerating City Analysis...")

city_summary = (

    df.groupby("City")

    .agg(

        Patients=("Visit ID","count"),

        Revenue=("Billing Amount","sum"),

        Average_Billing=("Billing Amount","mean")

    )

    .reset_index()

)

city_summary["Average_Billing"] = (
    city_summary["Average_Billing"].round(2)
)

city_summary = city_summary.sort_values(

    by="Patients",

    ascending=False

)

print("City Analysis Created")

# ==========================================================
# STATE-WISE ANALYSIS
# ==========================================================

print("\nGenerating State Analysis...")

state_summary = (

    df.groupby("State")

    .agg(

        Patients=("Visit ID","count"),

        Revenue=("Billing Amount","sum"),

        Average_Billing=("Billing Amount","mean")

    )

    .reset_index()

)

state_summary["Average_Billing"] = (
    state_summary["Average_Billing"].round(2)
)

state_summary = state_summary.sort_values(

    by="Revenue",

    ascending=False

)

print("State Analysis Created")

# ==========================================================
# DIAGNOSIS ANALYSIS
# ==========================================================

print("\nGenerating Diagnosis Summary...")

diagnosis_summary = (

    df.groupby("Diagnosis")

    .agg(

        Patients=("Visit ID","count"),

        Revenue=("Billing Amount","sum"),

        Average_LOS=("Length of Stay","mean")

    )

    .reset_index()

)

diagnosis_summary["Average_LOS"] = (
    diagnosis_summary["Average_LOS"].round(2)
)

diagnosis_summary = diagnosis_summary.sort_values(

    by="Patients",

    ascending=False

)

print("Diagnosis Summary Created")

# ==========================================================
# TREATMENT ANALYSIS
# ==========================================================

print("\nGenerating Treatment Summary...")

treatment_summary = (

    df.groupby("Treatment")

    .agg(

        Patients=("Visit ID","count"),

        Revenue=("Billing Amount","sum"),

        Average_Billing=("Billing Amount","mean")

    )

    .reset_index()

)

treatment_summary["Average_Billing"] = (
    treatment_summary["Average_Billing"].round(2)
)

treatment_summary = treatment_summary.sort_values(

    by="Revenue",

    ascending=False

)

print("Treatment Summary Created")

# ==========================================================
# EQUIPMENT ANALYSIS
# ==========================================================

print("\nGenerating Equipment Summary...")

equipment_summary = (

    df.groupby("Equipment")

    .agg(

        Departments=("Department","nunique"),

        Hospitals=("Hospital Name","nunique"),

        Usage=("Equipment","count")

    )

    .reset_index()

)

equipment_summary = equipment_summary.sort_values(

    by="Usage",

    ascending=False

)

print("Equipment Summary Created")

# ==========================================================
# MONTHLY ADMISSION TREND
# ==========================================================

print("\nGenerating Monthly Trend...")

monthly_summary = (

    df.groupby(

        ["Admission Year","Admission Month"]

    )

    .agg(

        Patients=("Visit ID","count"),

        Revenue=("Billing Amount","sum")

    )

    .reset_index()

)

print("Monthly Trend Created")

print("\nAll Summary Tables Generated Successfully.")
# ==========================================================
# TOP 10 DASHBOARD TABLES
# ==========================================================

print("\n" + "=" * 70)
print("CREATING DASHBOARD TABLES")
print("=" * 70)

# ----------------------------------------------------------
# Top 10 Hospitals by Revenue
# ----------------------------------------------------------

top_hospitals = (

    hospital_summary

    .sort_values(
        by="Total_Revenue",
        ascending=False
    )

    .head(10)

)

# ----------------------------------------------------------
# Top 10 Doctors by Revenue
# ----------------------------------------------------------

top_doctors = (

    doctor_summary

    .sort_values(
        by="Revenue",
        ascending=False
    )

    .head(10)

)

# ----------------------------------------------------------
# Top Departments
# ----------------------------------------------------------

top_departments = (

    department_summary

    .sort_values(
        by="Total_Revenue",
        ascending=False
    )

    .head(10)

)

# ----------------------------------------------------------
# Top Diagnoses
# ----------------------------------------------------------

top_diagnosis = (

    diagnosis_summary

    .sort_values(
        by="Patients",
        ascending=False
    )

    .head(10)

)

# ----------------------------------------------------------
# Top Treatments
# ----------------------------------------------------------

top_treatments = (

    treatment_summary

    .sort_values(
        by="Revenue",
        ascending=False
    )

    .head(10)

)

print("Dashboard Tables Created Successfully")

# ==========================================================
# DASHBOARD DATASET
# ==========================================================

print("\nPreparing Dashboard Dataset...")

dashboard_dataset = df.copy()

dashboard_dataset["Billing Amount"] = (
    dashboard_dataset["Billing Amount"].round(2)
)

dashboard_dataset["Length of Stay"] = (
    dashboard_dataset["Length of Stay"].round(2)
)

dashboard_dataset["Bed Utilization %"] = (
    dashboard_dataset["Bed Utilization %"].round(2)
)

dashboard_dataset = dashboard_dataset.sort_values(

    by="Admission Date",

    ascending=True

)

print("Dashboard Dataset Ready")

# ==========================================================
# EXPORT REPORTS
# ==========================================================

print("\nExporting Files...")

# KPI Report

kpi_report.to_csv(

    "Hospital_KPI_Report.csv",

    index=False

)

# Summary Tables

department_summary.to_csv(

    "Department_Summary.csv",

    index=False

)

hospital_summary.to_csv(

    "Hospital_Summary.csv",

    index=False

)

doctor_summary.to_csv(

    "Doctor_Summary.csv",

    index=False

)

insurance_summary.to_csv(

    "Insurance_Summary.csv",

    index=False

)

city_summary.to_csv(

    "City_Summary.csv",

    index=False

)

state_summary.to_csv(

    "State_Summary.csv",

    index=False

)

diagnosis_summary.to_csv(

    "Diagnosis_Summary.csv",

    index=False

)

treatment_summary.to_csv(

    "Treatment_Summary.csv",

    index=False

)

equipment_summary.to_csv(

    "Equipment_Summary.csv",

    index=False

)

monthly_summary.to_csv(

    "Monthly_Trend.csv",

    index=False

)

top_hospitals.to_csv(

    "Top_10_Hospitals.csv",

    index=False

)

top_doctors.to_csv(

    "Top_10_Doctors.csv",

    index=False

)

top_departments.to_csv(

    "Top_10_Departments.csv",

    index=False

)

top_diagnosis.to_csv(

    "Top_10_Diagnosis.csv",

    index=False

)

top_treatments.to_csv(

    "Top_10_Treatments.csv",

    index=False

)

dashboard_dataset.to_csv(

    "hospital_dashboard_dataset.csv",

    index=False

)

print("All Reports Exported Successfully")

# ==========================================================
# EXECUTION SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("MODULE 3 COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nFiles Generated:")

print("1. Hospital_KPI_Report.csv")
print("2. Department_Summary.csv")
print("3. Hospital_Summary.csv")
print("4. Doctor_Summary.csv")
print("5. Insurance_Summary.csv")
print("6. City_Summary.csv")
print("7. State_Summary.csv")
print("8. Diagnosis_Summary.csv")
print("9. Treatment_Summary.csv")
print("10. Equipment_Summary.csv")
print("11. Monthly_Trend.csv")
print("12. Top_10_Hospitals.csv")
print("13. Top_10_Doctors.csv")
print("14. Top_10_Departments.csv")
print("15. Top_10_Diagnosis.csv")
print("16. Top_10_Treatments.csv")
print("17. hospital_dashboard_dataset.csv")

print("\nTotal Records Processed :", len(df))
print("Total Hospitals :", df["Hospital ID"].nunique())
print("Total Departments :", df["Department"].nunique())
print("Total Doctors :", df["Doctor"].nunique())
print("Dashboard Dataset Shape :", dashboard_dataset.shape)

print("\nHospital KPI Generation Completed Successfully.")
print("=" * 70)
