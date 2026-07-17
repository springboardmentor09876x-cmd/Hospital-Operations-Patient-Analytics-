"""Hospital KPI Engineering Script (Module 3)

This script loads the cleaned hospital dataset, calculates essential hospital performance KPIs, 
and exports the final dataset as an Excel file ready for Tableau dashboards.

Calculated KPIs:
1. Total Admissions (Overall, Department-level, Hospital-level)
2. Occupancy Rate (Patient-level, Department-level, Hospital-level)
3. Average Length of Stay (Overall, Department-level, Hospital-level)
4. Readmission Rate (Overall, Department-level, Hospital-level)
5. Bed Utilization Rate (Patient-level, Department-level, Hospital-level)
6. Department Efficiency Score (Composite Score)
"""

import pandas as pd
import numpy as np

# Define file paths
INPUT_FILE = "hospital_cleaned.csv"
OUTPUT_EXCEL = "hospital_final_dataset.xlsx"
OUTPUT_CSV = "hospital_final_dataset.csv"

def load_data(path):
    print(f"Loading cleaned dataset from {path}...")
    df = pd.read_csv(path)
    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

def calculate_kpis(df):
    df = df.copy()
    
    # ---------------------------------------------------------
    # 1. Total Admissions
    # ---------------------------------------------------------
    df["Total Admissions (Overall)"] = len(df)
    
    # Grouped admissions counts
    dept_counts = df.groupby("Department")["Patient ID"].transform("count")
    df["Total Admissions (Dept)"] = dept_counts
    
    hospital_counts = df.groupby("Hospital Name")["Patient ID"].transform("count")
    df["Total Admissions (Hospital)"] = hospital_counts
    
    # ---------------------------------------------------------
    # 2. Occupancy Rate
    # ---------------------------------------------------------
    # Convert Bed_Occupancy_Rate_% (decimal) to a percentage scale (0-100)
    df["Occupancy Rate (%)"] = (df["Bed_Occupancy_Rate_%"] * 100).round(2)
    
    # Department average occupancy rate
    dept_occ_avg = df.groupby("Department")["Occupancy Rate (%)"].transform("mean").round(2)
    df["Occupancy Rate (Dept) (%)"] = dept_occ_avg
    
    # Hospital average occupancy rate
    hosp_occ_avg = df.groupby("Hospital Name")["Occupancy Rate (%)"].transform("mean").round(2)
    df["Occupancy Rate (Hospital) (%)"] = hosp_occ_avg
    
    # ---------------------------------------------------------
    # 3. Average Length of Stay
    # ---------------------------------------------------------
    df["Average Length of Stay (Overall)"] = df["Length of Stay"].mean().round(2)
    
    dept_alos = df.groupby("Department")["Length of Stay"].transform("mean").round(2)
    df["Average Length of Stay (Dept)"] = dept_alos
    
    hosp_alos = df.groupby("Hospital Name")["Length of Stay"].transform("mean").round(2)
    df["Average Length of Stay (Hospital)"] = hosp_alos
    
    # ---------------------------------------------------------
    # 4. Readmission Rate
    # ---------------------------------------------------------
    # Map Re-admission (Yes/No) to numeric (1/0)
    df["readmit_numeric"] = df["Re-admission"].str.strip().str.title().map({"Yes": 1, "No": 0}).fillna(0)
    
    # Overall Readmission Rate
    df["Readmission Rate (%)"] = (df["readmit_numeric"].mean() * 100).round(2)
    
    # Grouped Readmission Rates
    dept_readmit = df.groupby("Department")["readmit_numeric"].transform("mean") * 100
    df["Readmission Rate (Dept) (%)"] = dept_readmit.round(2)
    
    hosp_readmit = df.groupby("Hospital Name")["readmit_numeric"].transform("mean") * 100
    df["Readmission Rate (Hospital) (%)"] = hosp_readmit.round(2)
    
    # Drop intermediate column
    df = df.drop(columns=["readmit_numeric"])
    
    # ---------------------------------------------------------
    # 5. Bed Utilization Rate
    # ---------------------------------------------------------
    # Bed Utilization = (Beds_Occupied_Count / Beds Available) * 100
    # Add a small epsilon to avoid division by zero
    df["Bed Utilization Rate (%)"] = (df["Beds_Occupied_Count"] / (df["Beds Available"] + 1e-9) * 100).round(2)
    df["Bed Utilization Rate (%)"] = df["Bed Utilization Rate (%)"].clip(upper=100.0)
    
    # Grouped Bed Utilization Rates
    dept_bed_util = df.groupby("Department")["Bed Utilization Rate (%)"].transform("mean").round(2)
    df["Bed Utilization Rate (Dept) (%)"] = dept_bed_util
    
    hosp_bed_util = df.groupby("Hospital Name")["Bed Utilization Rate (%)"].transform("mean").round(2)
    df["Bed Utilization Rate (Hospital) (%)"] = hosp_bed_util
    
    # ---------------------------------------------------------
    # 6. Department Efficiency Score (Composite Score)
    # ---------------------------------------------------------
    # Formula: 100 - (Readmission Rate (Dept) (%) * 0.4) - (Normalized ALOS * 0.3) + (Bed Utilization Rate (Dept) (%) * 0.3)
    # Normalizing ALOS: (Dept ALOS / Max Dept ALOS) * 100
    dept_alos_dict = df.groupby("Department")["Length of Stay"].mean().to_dict()
    max_dept_alos = max(dept_alos_dict.values())
    
    # Get department-level metrics
    dept_readmit_dict = df.groupby("Department")["Readmission Rate (Dept) (%)"].first().to_dict()
    dept_bed_util_dict = df.groupby("Department")["Bed Utilization Rate (Dept) (%)"].first().to_dict()
    
    dept_efficiency = {}
    for dept, alos in dept_alos_dict.items():
        norm_alos = (alos / max_dept_alos) * 100
        readmit = dept_readmit_dict[dept]
        bed_util = dept_bed_util_dict[dept]
        
        # Calculate score
        score = 100 - (readmit * 0.4) - (norm_alos * 0.3) + (bed_util * 0.3)
        dept_efficiency[dept] = round(score, 2)
        
    df["Department Efficiency Score"] = df["Department"].map(dept_efficiency)
    
    print("KPIs successfully calculated!")
    return df

def save_datasets(df):
    print(f"Saving final dataset to Excel: {OUTPUT_EXCEL}...")
    df.to_excel(OUTPUT_EXCEL, index=False)
    print(f"Saving final dataset to CSV: {OUTPUT_CSV}...")
    df.to_csv(OUTPUT_CSV, index=False)
    print("Data export complete!")

def main():
    df = load_data(INPUT_FILE)
    df_kpi = calculate_kpis(df)
    save_datasets(df_kpi)
    
    print("\n" + "=" * 50)
    print("KPI ENGINEERING COMPLETED SUCCESSFULLY!")
    print("=" * 50)
    print(f"Total Rows: {df_kpi.shape[0]:,}")
    print(f"Total Columns: {df_kpi.shape[1]}")
    print(f"Excel File: {OUTPUT_EXCEL}")
    print(f"CSV File: {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
