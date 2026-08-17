# ============================================================
# MILESTONE 2: HOSPITAL KPI ENGINEERING
# ============================================================

import pandas as pd
import numpy as np
from pathlib import Path


# ============================================================
# 1. FILE PATHS
# ============================================================

INPUT_FILE = Path("hospital_cleaned.csv")
OUTPUT_FILE = Path("hospital_final_dataset.xlsx")


# ============================================================
# 2. LOAD DATASET
# ============================================================

df = pd.read_csv(INPUT_FILE)

print("Dataset loaded successfully.")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ============================================================
# 3. CONVERT DATE COLUMNS
# ============================================================

date_columns = [
    "Admission Date",
    "Discharge Date",
    "Transfer_Date"
]

for column in date_columns:

    if column in df.columns:

        df[column] = pd.to_datetime(
            df[column],
            dayfirst=True,
            errors="coerce"
        )


# ============================================================
# 4. CONVERT NUMERIC COLUMNS
# ============================================================

numeric_columns = [
    "Length_of_Stay_Days",
    "Readmission_Flag",
    "Wait_Time_Minutes",
    "Treatment_Cost_USD",
    "Staff Count",
    "Nurses",
    "Beds Available",
    "Bed Occupied",
    "Dept_Bed_Capacity_Derived"
]

for column in numeric_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# ============================================================
# 5. CREATE KPI SUPPORTING COLUMNS
# ============================================================

# Every row represents one admission
df["Admission_Count"] = 1


# Patient days = length of stay
df["Patient_Days"] = df["Length_of_Stay_Days"]


# ============================================================
# 6. OCCUPANCY RATE
# ============================================================

if (
    "Bed Occupied" in df.columns
    and "Beds Available" in df.columns
):

    df["Occupancy_Rate_%"] = np.where(

        df["Beds Available"] > 0,

        (
            df["Bed Occupied"]
            /
            df["Beds Available"]
        )
        * 100,

        np.nan
    )

else:

    # Bed information is unavailable
    df["Occupancy_Rate_%"] = np.nan


# ============================================================
# 7. DEPARTMENT-LEVEL KPI CALCULATIONS
# ============================================================

department_kpis = (

    df.groupby(
        "Department",
        dropna=False
    )

    .agg(

        # Total admissions
        Total_Admissions=(
            "Patient_ID",
            "nunique"
        ),

        # Average Length of Stay
        Average_Length_of_Stay_Days=(
            "Length_of_Stay_Days",
            "mean"
        ),

        # Total readmissions
        Readmissions=(
            "Readmission_Flag",
            "sum"
        ),

        # Average waiting time
        Average_Wait_Time_Minutes=(
            "Wait_Time_Minutes",
            "mean"
        ),

        # Total patient days
        Total_Patient_Days=(
            "Patient_Days",
            "sum"
        ),

        # Outcome success rate
        Outcome_Success_Rate=(

            "Outcome",

            lambda x:

            x.astype(str)
            .str.strip()
            .str.lower()
            .isin(

                [
                    "recovered",
                    "improved",
                    "success",
                    "successful"
                ]

            )
            .mean()
            * 100
        )

    )

    .reset_index()
)


# ============================================================
# 8. READMISSION RATE
# ============================================================

department_kpis["Readmission_Rate_%"] = np.where(

    department_kpis["Total_Admissions"] > 0,

    (

        department_kpis["Readmissions"]
        /
        department_kpis["Total_Admissions"]

    )
    * 100,

    np.nan
)


# ============================================================
# 9. BED UTILIZATION RATE
# ============================================================

# Calculate observation period for each department

period_df = (

    df.groupby(
        "Department",
        dropna=False
    )

    .agg(

        Observation_Start=(
            "Admission Date",
            "min"
        ),

        Observation_End=(
            "Discharge Date",
            "max"
        ),

        Bed_Capacity=(
            "Dept_Bed_Capacity_Derived",
            "max"
        )

    )

    .reset_index()
)


# Calculate number of observation days

period_df["Observation_Period_Days"] = (

    period_df["Observation_End"]
    -
    period_df["Observation_Start"]

).dt.days + 1


# Available bed days

period_df["Available_Bed_Days"] = (

    period_df["Bed_Capacity"]
    *
    period_df["Observation_Period_Days"]

)


# Merge with department KPI table

department_kpis = department_kpis.merge(

    period_df,

    on="Department",

    how="left"
)


# Calculate bed utilization

department_kpis["Bed_Utilization_Rate_%"] = np.where(

    department_kpis["Available_Bed_Days"] > 0,

    (

        department_kpis["Total_Patient_Days"]
        /
        department_kpis["Available_Bed_Days"]

    )
    * 100,

    np.nan
)


# ============================================================
# 10. DEPARTMENT OCCUPANCY RATE
# ============================================================

if (

    "Bed Occupied" in df.columns
    and
    "Beds Available" in df.columns

):

    occupancy = (

        df.groupby(
            "Department",
            dropna=False
        )

        .apply(

            lambda x:

            (

                x["Bed Occupied"].sum()
                /
                x["Beds Available"].sum()
                *
                100

            )

            if x["Beds Available"].sum() > 0

            else np.nan,

            include_groups=False

        )

        .rename(
            "Occupancy_Rate_%"
        )

        .reset_index()

    )

    department_kpis = department_kpis.merge(

        occupancy,

        on="Department",

        how="left"

    )

else:

    department_kpis["Occupancy_Rate_%"] = np.nan


# ============================================================
# 11. MIN-MAX NORMALIZATION FUNCTION
# ============================================================

def min_max_score(

    series,

    higher_is_better=True

):

    series = pd.to_numeric(

        series,

        errors="coerce"

    )


    # If no values exist

    if series.notna().sum() == 0:

        return pd.Series(

            np.nan,

            index=series.index

        )


    # If all values are equal

    if series.min() == series.max():

        return pd.Series(

            100.0,

            index=series.index

        )


    score = (

        (

            series
            -
            series.min()

        )

        /

        (

            series.max()
            -
            series.min()

        )

    ) * 100


    # Lower value is better

    if not higher_is_better:

        score = 100 - score


    return score


# ============================================================
# 12. EFFICIENCY SCORE COMPONENTS
# ============================================================

# Higher outcome success rate = better

department_kpis["Outcome_Success_Score"] = (

    min_max_score(

        department_kpis[
            "Outcome_Success_Rate"
        ],

        higher_is_better=True

    )

)


# Lower waiting time = better

department_kpis["Wait_Time_Efficiency_Score"] = (

    min_max_score(

        department_kpis[
            "Average_Wait_Time_Minutes"
        ],

        higher_is_better=False

    )

)


# Lower length of stay = better

department_kpis["LOS_Efficiency_Score"] = (

    min_max_score(

        department_kpis[
            "Average_Length_of_Stay_Days"
        ],

        higher_is_better=False

    )

)


# Higher bed utilization = better

department_kpis["Bed_Utilization_Score"] = (

    min_max_score(

        department_kpis[
            "Bed_Utilization_Rate_%"
        ],

        higher_is_better=True

    )

)


# ============================================================
# 13. DEPARTMENT EFFICIENCY SCORE
# ============================================================

# Standard weights:
#
# Outcome Success       = 40%
# Wait Time Efficiency  = 25%
# LOS Efficiency        = 20%
# Bed Utilization       = 15%
#
# If bed utilization is unavailable,
# its weight is removed and remaining weights are normalized.


score_components = {

    "Outcome_Success_Score": 0.40,

    "Wait_Time_Efficiency_Score": 0.25,

    "LOS_Efficiency_Score": 0.20,

    "Bed_Utilization_Score": 0.15

}


available_components = [

    (column, weight)

    for column, weight

    in score_components.items()

    if department_kpis[column].notna().any()

]


total_weight = sum(

    weight

    for column, weight

    in available_components

)


department_kpis[
    "Department_Efficiency_Score"
] = sum(

    department_kpis[column]
    *
    weight
    /
    total_weight

    for column, weight

    in available_components

)


# ============================================================
# 14. OVERALL KPI CALCULATIONS
# ============================================================


# Total Admissions

total_admissions = (

    df["Patient_ID"]
    .nunique()

)


# Average Length of Stay

average_los = (

    df["Length_of_Stay_Days"]
    .mean()

)


# Total Readmissions

total_readmissions = (

    df["Readmission_Flag"]
    .sum()

)


# Readmission Rate

readmission_rate = (

    total_readmissions
    /
    total_admissions
    *
    100

)


# Occupancy Rate

if (

    "Bed Occupied" in df.columns
    and
    "Beds Available" in df.columns
    and
    df["Beds Available"].sum() > 0

):

    occupancy_rate = (

        df["Bed Occupied"].sum()
        /
        df["Beds Available"].sum()
        *
        100

    )

else:

    occupancy_rate = np.nan


# Bed Utilization Rate

if (

    department_kpis[
        "Available_Bed_Days"
    ].sum()
    > 0

):

    bed_utilization_rate = (

        department_kpis[
            "Total_Patient_Days"
        ].sum()

        /

        department_kpis[
            "Available_Bed_Days"
        ].sum()

        *

        100

    )

else:

    bed_utilization_rate = np.nan


# Department Efficiency Score

efficiency_score = (

    department_kpis[
        "Department_Efficiency_Score"
    ]

    .mean()

)


# ============================================================
# 15. CREATE KPI SUMMARY TABLE
# ============================================================

kpi_summary = pd.DataFrame(

    {

        "KPI": [

            "Total Admissions",

            "Occupancy Rate (%)",

            "Average Length of Stay (Days)",

            "Readmission Rate (%)",

            "Bed Utilization Rate (%)",

            "Department Efficiency Score"

        ],


        "Value": [

            total_admissions,

            occupancy_rate,

            average_los,

            readmission_rate,

            bed_utilization_rate,

            efficiency_score

        ],


        "Definition": [

            "Count of unique patients",

            "Total occupied beds / total available beds × 100",

            "Mean length of stay in days",

            "Readmitted patients / total admissions × 100",

            "Total patient-days / total available bed-days × 100",

            "Weighted score from outcome, wait time, LOS and bed utilization"

        ]

    }

)


# ============================================================
# 16. TABLEAU DASHBOARD PLANNING
# ============================================================

dashboard_fields = pd.DataFrame(

    {

        "Dashboard Area": [

            "Executive KPI Cards",

            "Executive KPI Cards",

            "Executive KPI Cards",

            "Executive KPI Cards",

            "Executive KPI Cards",

            "Department Performance",

            "Department Performance",

            "Department Performance",

            "Department Performance",

            "Patient Analysis",

            "Patient Analysis",

            "Patient Analysis"

        ],


        "Field": [

            "Total Admissions",

            "Occupancy Rate (%)",

            "Average Length of Stay (Days)",

            "Readmission Rate (%)",

            "Bed Utilization Rate (%)",

            "Department",

            "Department_Efficiency_Score",

            "Average_Length_of_Stay_Days",

            "Readmission_Rate_%",

            "Admission Type",

            "Severity_Level",

            "Outcome"

        ],


        "Recommended Visual": [

            "KPI Card",

            "KPI Card / Gauge",

            "KPI Card",

            "KPI Card",

            "KPI Card / Gauge",

            "Bar Chart",

            "Bar Chart",

            "Bar Chart",

            "Bar Chart",

            "Stacked Bar Chart",

            "Heatmap / Bar Chart",

            "Donut / Bar Chart"

        ]

    }

)


# ============================================================
# 17. EXPORT FINAL EXCEL FILE
# ============================================================

with pd.ExcelWriter(

    OUTPUT_FILE,

    engine="xlsxwriter"

) as writer:


    # Main dataset

    df.to_excel(

        writer,

        sheet_name="Patient_Data",

        index=False

    )


    # Overall KPIs

    kpi_summary.to_excel(

        writer,

        sheet_name="KPI_Summary",

        index=False

    )


    # Department KPIs

    department_kpis.to_excel(

        writer,

        sheet_name="Department_KPIs",

        index=False

    )


    # Tableau dashboard planning

    dashboard_fields.to_excel(

        writer,

        sheet_name="Dashboard_Fields",

        index=False

    )


    # Excel formatting

    workbook = writer.book


    header_format = workbook.add_format(

        {

            "bold": True,

            "bg_color": "#D9EAF7",

            "border": 1

        }

    )


    for sheet_name, table in {

        "Patient_Data": df,

        "KPI_Summary": kpi_summary,

        "Department_KPIs": department_kpis,

        "Dashboard_Fields": dashboard_fields

    }.items():


        worksheet = writer.sheets[sheet_name]


        # Freeze header row

        worksheet.freeze_panes(

            1,

            0

        )


        # Add filters

        worksheet.autofilter(

            0,

            0,

            len(table),

            len(table.columns) - 1

        )


        # Format headers

        for col_num, column_name in enumerate(

            table.columns

        ):


            worksheet.write(

                0,

                col_num,

                column_name,

                header_format

            )


            worksheet.set_column(

                col_num,

                col_num,

                min(

                    max(

                        len(

                            str(

                                column_name

                            )

                        )

                        + 2,

                        12

                    ),

                    32

                )

            )


# ============================================================
# 18. DISPLAY RESULTS
# ============================================================

print("\n========================================")
print("HOSPITAL KPI ENGINEERING COMPLETED")
print("========================================")

print("\nKPI SUMMARY")

print(

    kpi_summary.to_string(

        index=False

    )

)


print("\nDEPARTMENT KPI SUMMARY")

print(

    department_kpis[

        [

            "Department",

            "Total_Admissions",

            "Average_Length_of_Stay_Days",

            "Readmission_Rate_%",

            "Department_Efficiency_Score"

        ]

    ]

    .round(2)

    .to_string(

        index=False

    )

)


print(

    "\nFinal file created:",

    OUTPUT_FILE

)