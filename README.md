# MedTrack_DV — Hospital Operations & Patient Analytics Dashboard

An end-to-end hospital analytics project built as part of the Infosys Springboard Internship. Raw hospital data is cleaned, engineered into KPIs, and visualized across four interconnected dashboards for hospital administrators, healthcare managers, and policymakers.

> **Tool note:** The original brief specified Tableau. With mentor approval, this project was built and delivered in **Power BI Desktop** instead. All deliverable names, KPIs, and requirements from the brief are otherwise unchanged.

---

## 1. Project Statement

This project develops a comprehensive hospital operations and patient analytics dashboard suite for analyzing hospital performance, patient admissions, department efficiency, and healthcare resource utilization — transforming raw operational data into actionable insights for data-driven decision-making.

**Final deliverable:** a single, unified Power BI workbook (`medtrack_prototype.pbix`) containing four interconnected dashboards:
- Hospital Overview
- Patient Flow
- Department Analytics
- Resource Utilization

---

## 2. Dataset Sources

| File | Description | Rows |
|---|---|---|
| `hospital_raw_data.csv` | Original raw hospital dataset (initial version) | — |
| `Hospital_RawDataset_Updated.xlsx` | Updated raw dataset — selected as the working source after comparison (added 3 equipment-related columns) | — |
| `hospital_cleaned.csv` | Cleaned and standardized dataset (Module 2 output) | — |
| `hospital_final_dataset.xlsx` | Final KPI-engineered dataset used for all dashboards | 10,000 |

**Key columns used:** Hospital/Department/Doctor details, Patient demographics (Age, Gender), Admission Date, Discharge Date, Length of Stay, Admission Type, Diagnosis, Treatment, Beds Available, Beds Occupied, Bed Occupied (Yes/No), Readmission (Yes/No), Transferred (Yes/No), Staff Count, Equipment usage fields, Billing Amount, and derived KPI columns (`Bed_Occupancy_Rate_%`, `Department_Efficiency_Score`, `Staff_Utilization_%_Derived`, `Admissions_Rate_%_Derived`, `Dept_Bed_Capacity_Derived`, `Dept_Staff_Capacity_Derived`).

---

## 3. KPI Definitions

| KPI | Definition | Formula / Source |
|---|---|---|
| **Total Admissions** | Count of all patient admission records | `COUNTROWS(hospital_dataset)` |
| **Occupancy Rate** | Average bed-slot occupancy indicator, pre-derived per admission record | `AVERAGE(Bed_Occupancy_Rate_%)`, where `Bed_Occupancy_Rate_% = Beds_Occupied_Count × 0.2` |
| **Average Length of Stay** | Mean duration of patient stay | `AVERAGE(Length of Stay)` — uses the dataset's provided LOS field directly (see §6, Data Limitations) |
| **Readmission Rate** | Share of admissions flagged as readmissions | `DIVIDE(COUNT(Readmission = "Yes"), COUNT(all rows))` |
| **Bed Utilization Rate** | Same underlying metric as Occupancy Rate, shown broken down by department | `AVERAGE(Bed_Occupancy_Rate_%)` grouped by `Department` |
| **Department Efficiency Score** | Weighted composite score of departmental performance | `0.2 × Admissions_Rate_%_Derived + 0.4 × Staff_Utilization_%_Derived + 0.4 × (Bed_Occupancy_Rate_% × 100)` |

**Supporting/bonus KPIs added beyond the required six:** Total Revenue, Total Transfers, Total Readmissions, Staff Utilization %, Equipment Utilization, Available Beds, Peak Patient Load, Treatment Capacity Utilization.

---

## 4. Dashboard Guide

### 4.1 Hospital Overview
Landing page — top-level hospital-wide KPIs and trends.
- **KPIs:** Total Admissions, Occupancy Rate, Avg Length of Stay, Readmission Rate, Bed Utilization Rate, Department Efficiency Score
- **Charts:** Monthly Admission Trends (line), Admissions by Treatment (donut), Occupancy Monitoring vs. Target (gauge), Readmission Rate by Age Group (bar)
- **Filters:** Admission Date (range slider), Department, Doctor
- **Table:** trimmed patient record view (Patient ID, Name, Department, Doctor, Admission Type, Diagnosis)

### 4.2 Patient Flow
Admission/discharge dynamics and patient movement.
- **KPIs:** Total Admissions, Avg Length of Stay, Total Transfers, % Emergency Admissions
- **Charts:** Admissions vs. Discharges Trend (combo bar+line), Patient Transfers by Department (bar), Length of Stay Distribution (funnel), Peak Patient Load by Day of Week (treemap)

### 4.3 Department Analytics
Cross-department performance comparison.
- **KPIs:** Department Efficiency Score, Total Patient Volume, Average Readmission Rate, Treatment Capacity Utilization
- **Charts:** Patient Volume & Readmission Rate by Department (combo), Department Efficiency Comparison (scatter/bubble), Treatment Capacity Utilization by Department (100% stacked bar), Department Performance Summary (table with data bars)

### 4.4 Resource Utilization
Bed, staff, and equipment capacity tracking.
- **KPIs:** Bed Utilization Rate, Staff Utilization %, Equipment Utilization, Available Beds
- **Charts:** Capacity Planning: Bed Usage by Department (waterfall), Staff Allocation by Department (pie), Equipment Utilization Tracking (decomposition tree), Resource Availability Trend (KPI visual with target)

### 4.5 Navigation & Integration
- All four dashboards share a persistent top navigation bar (Power BI **Page Navigator** visual), enabling one-click switching between pages.
- **Filters are synchronized** across all four pages via **Sync Slicers** (Admission Date, Department, Doctor) — a filter applied on one page carries through to the others.
- Consistent color theme, KPI card styling, and layout structure across all four pages for a unified feel.

---

## 5. Healthcare Operations Methodology

The KPI set was chosen to reflect four operational lenses commonly used in hospital performance monitoring:

1. **Volume** (Total Admissions) — how many patients the hospital is serving
2. **Capacity** (Occupancy Rate, Bed Utilization Rate) — how much of available bed capacity is in use
3. **Quality/Outcomes** (Readmission Rate, Avg Length of Stay) — how effectively patients are being treated and discharged
4. **Departmental Performance** (Department Efficiency Score) — a composite view combining admission load, staffing, and bed usage to compare departments on a level footing

This mirrors a standard hospital operations reporting structure: a single Overview page for executive-level monitoring, supported by drill-down pages for Patient Flow (operations), Department Analytics (management), and Resource Utilization (capacity planning) — each aimed at a different stakeholder need described in the project statement.

---

## 6. Known Data Limitations (documented for transparency)

These were identified during KPI validation and intentionally worked around rather than "fixed" in the source data, since they reflect characteristics of the underlying (synthetic) dataset:

- **Admission Date and Discharge Date are not reliably related to Length of Stay.** Calculating LOS as `Discharge Date − Admission Date` produces results (range: -322 to +338 days) inconsistent with the provided `Length of Stay` column (range: 1–15 days, ~56% match rate even on valid rows). **Resolution:** the provided `Length of Stay` column is used directly for all duration-based KPIs; Admission/Discharge dates are used only for trend-axis grouping (month/day), not duration math.
- **2,964 rows (~30%) have Discharge Date earlier than Admission Date.** Consistent with the point above — these are not treated as data entry errors requiring correction, since the date fields are independently randomized in this dataset.
- **`Bed_Occupancy_Rate_%` can exceed 100%** (max observed: 140%), since it is derived as `Beds_Occupied_Count × 0.2` (a bed-slot count) rather than a strict occupied/available ratio. Retained as-is per Module 3 KPI engineering; documented here so the >100% values are understood as expected, not erroneous.
- **`Dept_Bed_Capacity_Derived` and `Staff Count` are near-constant per department** but repeat on every patient row. `SUM` aggregation was avoided in favor of `AVERAGE`/`MAX` throughout the workbook to prevent capacity/staffing totals from being inflated by row count.

---

## 7. Project Structure

```
MedTrack_DV/
├── /scripts     → data_collection.py, hospital_cleaning.ipynb, generate_hospital_kpis.py
├── /data        → hospital_raw_data.csv, hospital_cleaned.csv, hospital_final_dataset.xlsx
├── /dashboard   → medtrack_prototype.pbix
├── /docs        → README.md, QA_Testing_Report.md, dashboard_storyboard.pptx, module documentation PDFs
```

---

## 8. Modules Completed

| Module | Status |
|---|---|
| 1. Healthcare Data Collection | ✅ Complete |
| 2. Data Cleaning & Transformation | ✅ Complete |
| 3. Hospital KPI Engineering | ✅ Complete |
| 4. Dashboard Planning & Prototyping (Storyboard) | ✅ Complete |
| 5. Build Hospital Overview & Patient Flow | ✅ Complete |
| 6. Build Department Analytics & Resource Utilization | ✅ Complete |
| 7. Testing & Validation | ✅ Complete — see `QA_Testing_Report.md` |
| 8. Documentation & Project Delivery | ✅ Complete — this README + GitHub repository |

---

## 9. Tech Stack

| Area | Tools |
|---|---|
| Data Collection | Python |
| Data Processing | Pandas, NumPy |
| Data Cleaning | Python |
| Visualization | **Power BI Desktop** (mentor-approved substitute for Tableau) |
| Dashboard Integration | Power BI Page Navigator, Bookmarks, Sync Slicers, DAX Measures |
| Documentation | Markdown, GitHub |

---

## 10. Author

**Sanika** — Infosys Springboard Internship, MedTrack_DV Project
