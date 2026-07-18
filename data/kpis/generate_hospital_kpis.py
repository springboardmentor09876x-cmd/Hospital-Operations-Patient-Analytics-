"""
generate_hospital_kpis.py

MedTrack_DV - Milestone 2, Module 3: Hospital KPI Engineering

Reads the cleaned, full-spec hospital dataset and computes:
- Department-level KPIs (Total Admissions, Avg Length of Stay, Readmission Rate,
  Bed Occupancy Rate, Staff Utilization, Bed Utilization Rate, Department Efficiency Score)
- Hospital-level KPIs (Total Admissions, Avg Length of Stay, Readmission Rate,
  Occupancy Rate, Billing)

Outputs a single Excel workbook (hospital_final_dataset.xlsx) with three sheets:
Row_Level_Data, Department_KPIs, Hospital_KPIs.

Usage:
    python generate_hospital_kpis.py

Expects these input files in the same directory:
    hospital_complete_dataset.csv
    resource_dataset_cleaned.csv
"""

import pandas as pd


INPUT_COMPLETE_DATASET = "hospital_complete_dataset.csv"
INPUT_RESOURCE_DATASET = "resource_dataset_cleaned.csv"
OUTPUT_FILE = "hospital_final_dataset.xlsx"


def load_data():
    df = pd.read_csv(INPUT_COMPLETE_DATASET)
    resource = pd.read_csv(INPUT_RESOURCE_DATASET)
    return df, resource


def build_department_kpis(df: pd.DataFrame, resource: pd.DataFrame) -> pd.DataFrame:
    """Aggregate row-level visits into Hospital x Department KPIs."""
    kpi = df.groupby(["Hospital ID", "Hospital Name", "Department"]).agg(
        Total_Admissions=("Visit ID", "count"),
        Avg_Length_of_Stay=("Length of Stay", "mean"),
        Readmission_Rate_pct=("Readmission_Flag", lambda x: round(x.mean() * 100, 1)),
        Avg_Bed_Occupancy_Rate_pct=("Bed_Occupancy_Rate_%", "mean"),
        Avg_Staff_Utilization_pct=("Staff_Utilization_%_Derived", "mean"),
        Total_Billing=("Billing Amount", "sum"),
        Avg_Billing=("Billing Amount", "mean"),
        Transferred_Count=("Transferred_Flag", "sum"),
    ).reset_index()

    kpi["Avg_Length_of_Stay"] = kpi["Avg_Length_of_Stay"].round(1)
    kpi["Avg_Bed_Occupancy_Rate_pct"] = kpi["Avg_Bed_Occupancy_Rate_pct"].round(1)
    kpi["Avg_Staff_Utilization_pct"] = kpi["Avg_Staff_Utilization_pct"].round(1)
    kpi["Avg_Billing"] = kpi["Avg_Billing"].round(2)
    kpi["Total_Billing"] = kpi["Total_Billing"].round(2)

    # Bed Utilization Rate from the Resource dataset (true capacity-based figure)
    kpi = kpi.merge(
        resource[["Hospital ID", "Department", "Beds Available", "Beds Occupied", "Bed Utilization %"]],
        on=["Hospital ID", "Department"], how="left"
    )
    kpi = kpi.rename(columns={"Bed Utilization %": "Bed_Utilization_Rate_pct"})

    kpi["Department_Efficiency_Score"] = compute_efficiency_score(kpi)

    return kpi


def compute_efficiency_score(kpi: pd.DataFrame) -> pd.Series:
    """
    Composite score (0-100) per department, weighting:
    - Avg Length of Stay (30%, lower is better)
    - Readmission Rate (30%, lower is better)
    - Bed Utilization Rate (20%, higher is better)
    - Staff Utilization (20%, higher is better)
    """

    def normalize(series, invert=False):
        norm = (series - series.min()) / (series.max() - series.min()) * 100
        return 100 - norm if invert else norm

    los_score = normalize(kpi["Avg_Length_of_Stay"], invert=True)
    readmission_score = normalize(kpi["Readmission_Rate_pct"], invert=True)
    bed_util_score = normalize(kpi["Bed_Utilization_Rate_pct"], invert=False)
    staff_util_score = normalize(kpi["Avg_Staff_Utilization_pct"], invert=False)

    score = (
        los_score * 0.3
        + readmission_score * 0.3
        + bed_util_score * 0.2
        + staff_util_score * 0.2
    )
    return score.round(1)


def build_hospital_kpis(df: pd.DataFrame, resource: pd.DataFrame) -> pd.DataFrame:
    """Aggregate row-level visits into Hospital-level KPIs."""
    hospital_kpi = df.groupby(
        ["Hospital ID", "Hospital Name", "City", "State", "Hospital Type"]
    ).agg(
        Total_Admissions=("Visit ID", "count"),
        Avg_Length_of_Stay=("Length of Stay", "mean"),
        Readmission_Rate_pct=("Readmission_Flag", lambda x: round(x.mean() * 100, 1)),
        Avg_Billing=("Billing Amount", "mean"),
        Total_Billing=("Billing Amount", "sum"),
    ).reset_index()

    hospital_kpi["Avg_Length_of_Stay"] = hospital_kpi["Avg_Length_of_Stay"].round(1)
    hospital_kpi["Avg_Billing"] = hospital_kpi["Avg_Billing"].round(2)
    hospital_kpi["Total_Billing"] = hospital_kpi["Total_Billing"].round(2)

    hosp_bed_rollup = resource.groupby("Hospital ID").agg(
        Total_Beds_Available=("Beds Available", "sum"),
        Total_Beds_Occupied=("Beds Occupied", "sum"),
    ).reset_index()
    hosp_bed_rollup["Occupancy_Rate_pct"] = (
        hosp_bed_rollup["Total_Beds_Occupied"] / hosp_bed_rollup["Total_Beds_Available"] * 100
    ).round(1)

    hospital_kpi = hospital_kpi.merge(hosp_bed_rollup, on="Hospital ID", how="left")

    return hospital_kpi


def main():
    print("Loading data...")
    df, resource = load_data()
    print(f"  Row-level dataset: {df.shape}")
    print(f"  Resource dataset:  {resource.shape}")

    print("Building department-level KPIs...")
    department_kpis = build_department_kpis(df, resource)
    print(f"  Department_KPIs: {department_kpis.shape}")

    print("Building hospital-level KPIs...")
    hospital_kpis = build_hospital_kpis(df, resource)
    print(f"  Hospital_KPIs: {hospital_kpis.shape}")

    print(f"Writing {OUTPUT_FILE}...")
    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Row_Level_Data", index=False)
        department_kpis.to_excel(writer, sheet_name="Department_KPIs", index=False)
        hospital_kpis.to_excel(writer, sheet_name="Hospital_KPIs", index=False)

    print("Done.")


if __name__ == "__main__":
    main()
