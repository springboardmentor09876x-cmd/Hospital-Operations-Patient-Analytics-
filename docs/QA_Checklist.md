# Quality Assurance (QA) Checklist

This checklist defines the validation and test scenarios executed on the MedTrack_DV datasets, scripts, and Tableau dashboards to ensure data integrity, calculation accuracy, and dashboard usability.

---

## 1. Data Integrity & Pipeline Verification

- [x] **Raw Data Load Test**: Verify that both `Hospital_Dataset.xlsx` (10,000 rows, 32 columns) and `Patient_Dataset.xlsx` (1,000 rows, 6 columns) load without error.
- [x] **Deduplication Check**: Run duplicate verification on the merged datasets.
  - *Result*: 0 duplicate rows found in `hospital_raw_data.csv`.
- [x] **Null Value Threshold Test**: Check that missing value ratios are below the target thresholds.
  - *Target*: Overall dataset missingness < 2%.
  - *Result*: 0.00% missing values in the cleaned file `hospital_cleaned.csv` (perfectly handled using median/mode imputation).
- [x] **Date Chronology Check**: Ensure `Discharge Date` is equal to or after `Admission Date` for all patient admissions.
  - *Result*: Automated date-swapping logic successfully corrected entries where discharge preceded admission.

---

## 2. KPI Engineering Validation

- [x] **Admissions Count Consistency**: Check that row counts across KPI aggregates sum exactly to 10,000.
  - *Result*: Total admissions sum aligns perfectly across overall, hospital, and department columns.
- [x] **Occupancy Rate Range Check**: Ensure occupancy rates are within bounds (0% to 100%).
  - *Result*: `Occupancy Rate (%)` values successfully converted and scaled to 0-100%.
- [x] **Length of Stay (LOS) Logic**: Verify that Average Length of Stay calculations are positive and accurate.
  - *Result*: Overall ALOS calculated as 8.07 days.
- [x] **Readmission Rate Verification**: Ensure readmission rates are calculated from the mapped numeric `Re-admission` column.
  - *Result*: Mapped numeric values mapped to 0 (No) or 1 (Yes) correctly.
- [x] **Bed Utilization Rate Logic**: Ensure utilization is calculated using `(Beds_Occupied_Count / Beds Available) * 100` and capped at 100%.
  - *Result*: Calculations successfully generated and bounded.
- [x] **Composite Efficiency Score Calculation**: Verify composite formulas for all clinical departments.
  - *Result*: Composite scores successfully generated per department (ranging between 60.00 and 100.00).

---

## 3. Tableau Dashboard Usability & Navigation

- [x] **Global Filters Check**:
  - Verify that changing the `Hospital Name` filter updates charts across all sheets.
  - Verify that changing the `Department` filter correctly updates data points.
  - Verify that the `Admission Date` date slider filters trends correctly.
- [x] **Interactive Action Links**:
  - Test the filter action linking the **Hospital Overview** dashboard to the **Department Analytics** dashboard. Clicking a department bar must trigger navigation and filter selection.
- [x] **Device Responsiveness**:
  - Verify that the dashboard layouts scale dynamically on laptop screens and standard tablets.
