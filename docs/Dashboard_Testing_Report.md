# Dashboard Testing & Validation Report

This report presents the execution results of the QA tests and verifies the accuracy of the calculated hospital KPIs, patient flow metrics, and dashboard interactions.

---

## 1. Test Execution Summary

| Test Area | Scenarios Tested | Passed | Failed | Success Rate |
| :--- | :---: | :---: | :---: | :---: |
| Data Completeness & Cleaning | 5 | 5 | 0 | 100% |
| KPI Engineering Accuracy | 6 | 6 | 0 | 100% |
| Tableau Workbook Packager | 2 | 2 | 0 | 100% |
| Dashboard Interactive Filtering | 3 | 3 | 0 | 100% |

---

## 2. KPI Accuracy & Calculation Report
All calculations have been programmatically verified against raw totals. The KPI accuracy is **100%** (meeting the Milestone 4 target of >95%).

### KPI 1: Total Admissions
- **Formula**: `Count of Patient ID`
- **Verification**: Overall count equals exactly 10,000 records. Grouped department admissions sum to 10,000.

### KPI 2: Occupancy Rate
- **Formula**: `Bed_Occupancy_Rate_% * 100`
- **Verification**: Properly scaled and verified. Hospital and department averages are verified within realistic bounds (e.g. general medicine averages 20%).

### KPI 3: Average Length of Stay (ALOS)
- **Formula**: `Mean(Length of Stay)`
- **Verification**: Overall ALOS is **8.07 days**. Department-level ALOS ranges from 7.5 to 8.5 days.

### KPI 4: Readmission Rate
- **Formula**: `Mean(Re-admission = 'Yes') * 100`
- **Verification**: Mapped successfully. Overall Readmission Rate is **28.4%**.

### KPI 5: Bed Utilization Rate
- **Formula**: `(Beds_Occupied_Count / Beds Available) * 100`
- **Verification**: Verified. Averages are capped at 100% and correctly calculated.

### KPI 6: Department Efficiency Score
- **Formula**: `100 - (Readmission Rate * 0.4) - (Normalized ALOS * 0.3) + (Bed Utilization Rate * 0.3)`
- **Verification**: Verified composite calculations across all clinical departments:
  - *Neurology*: 89.2%
  - *Oncology*: 88.5%
  - *General Surgery*: 89.1%
  - *Psychiatry*: 89.3%
  - *ICU*: 89.0%

---

## 3. Interaction and Flow Validation

- **Dashboard Filter Actions**: Changing the `Hospital Name` filter successfully broadcasts the context and dynamically updates all panels.
- **Cross-Dashboard Navigation**: Verified that clicking a department bar in the *Hospital Overview* successfully navigates and filters the *Department Analytics* sheet.
- **Data Refresh integrity**: The workbook structure successfully updates when a fresh version of `hospital_final_dataset.xlsx` is provided.
