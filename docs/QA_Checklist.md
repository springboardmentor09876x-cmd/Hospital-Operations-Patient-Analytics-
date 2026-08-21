# MedTrack DV — QA Checklist

## Testing and Validation

**Project:** MedTrack DV – Hospital Operations & Patient Analytics Dashboard
**Testing Phase:** Module 7 – Testing and Validation
**Dashboard Tool:** Microsoft Power BI
**Dataset:** Hospital Patient Analytics Dataset

---

## 1. Data Validation

| Test ID | Test Case                              | Expected Result                              | Status |
| ------- | -------------------------------------- | -------------------------------------------- | ------ |
| DATA-01 | Verify total patient records           | Dataset contains 10,000 records              | PASS   |
| DATA-02 | Verify Patient ID uniqueness           | No duplicate Patient IDs                     | PASS   |
| DATA-03 | Check missing Patient IDs              | No missing Patient IDs                       | PASS   |
| DATA-04 | Check missing Admission Dates          | No missing Admission Dates                   | PASS   |
| DATA-05 | Check missing Discharge Dates          | No missing Discharge Dates                   | PASS   |
| DATA-06 | Validate Length of Stay values         | LOS values are valid                         | PASS   |
| DATA-07 | Validate Admission and Discharge dates | Dates are consistent with LOS                | PASS   |
| DATA-08 | Validate Readmission information       | Readmission values are consistent            | PASS   |
| DATA-09 | Validate Transfer information          | Transfer values are consistent               | PASS   |
| DATA-10 | Validate patient-level records         | Patient records contain required information | PASS   |

---

## 2. KPI Validation

| Test ID | KPI                         |                           Expected Result | Dashboard Result | Status |
| ------- | --------------------------- | ----------------------------------------: | ---------------: | ------ |
| KPI-01  | Total Admissions            |                                    10,000 |              10K | PASS   |
| KPI-02  | Average Length of Stay      |                                78.78 days |        78.8 days | PASS   |
| KPI-03  | Occupancy Rate              |                                    36.76% |           36.76% | PASS   |
| KPI-04  | Readmission Rate            |                                    49.87% |           49.87% | PASS   |
| KPI-05  | Bed Utilization Rate        |                                    36.76% |           36.76% | PASS   |
| KPI-06  | Transfer Rate               |                                    17.60% |            17.6% | PASS   |
| KPI-07  | Staff Utilization           |                                    57.92% |            57.9% | PASS   |
| KPI-08  | Equipment Utilization       |                                    33.55% |            33.6% | PASS   |
| KPI-09  | Department Efficiency Score | Dashboard calculation displayed correctly |             27.9 | PASS   |
| KPI-10  | Resource Availability Rate  | Dashboard calculation displayed correctly |            99.3% | PASS   |

---

## 3. Healthcare Metric Validation

| Test ID | Metric                      | Validation                           | Status |
| ------- | --------------------------- | ------------------------------------ | ------ |
| HM-01   | Occupancy Rate              | Verified against dataset calculation | PASS   |
| HM-02   | Bed Utilization Rate        | Verified against dataset calculation | PASS   |
| HM-03   | Average Length of Stay      | Verified against patient records     | PASS   |
| HM-04   | Readmission Rate            | Verified against readmission records | PASS   |
| HM-05   | Transfer Rate               | Verified against transfer records    | PASS   |
| HM-06   | Staff Utilization           | Verified against resource data       | PASS   |
| HM-07   | Equipment Utilization       | Verified against equipment data      | PASS   |
| HM-08   | Department Efficiency Score | Dashboard calculation verified       | PASS   |
| HM-09   | Resource Availability Rate  | Dashboard calculation verified       | PASS   |

---

## 4. Hospital Overview Dashboard

| Test ID | Test Case                               | Expected Result                                 | Status |
| ------- | --------------------------------------- | ----------------------------------------------- | ------ |
| HO-01   | Verify KPI cards                        | KPI values display correctly                    | PASS   |
| HO-02   | Verify Admission Trends                 | Monthly admission trend displays correctly      | PASS   |
| HO-03   | Verify Occupancy Rate Trend             | Monthly occupancy trend displays correctly      | PASS   |
| HO-04   | Verify Readmission Rate Trend           | Monthly readmission trend displays correctly    | PASS   |
| HO-05   | Verify Admissions by Patient Type       | Patient categories display correctly            | PASS   |
| HO-06   | Verify Admissions by Department         | Department values display correctly             | PASS   |
| HO-07   | Verify Average LOS by Department        | Department LOS values display correctly         | PASS   |
| HO-08   | Verify Readmission Rate by Department   | Department readmission values display correctly | PASS   |
| HO-09   | Verify Total Admissions by Date         | Date-based admission trend displays correctly   | PASS   |
| HO-10   | Verify Monthly Admissions vs Discharges | Monthly comparison displays correctly           | PASS   |
| HO-11   | Verify Department Efficiency Score      | Department comparison displays correctly        | PASS   |

---

## 5. Patient Flow Dashboard

| Test ID | Test Case                          | Expected Result                             | Status |
| ------- | ---------------------------------- | ------------------------------------------- | ------ |
| PF-01   | Verify Total Admissions            | Displays 10K                                | PASS   |
| PF-02   | Verify Average Length of Stay      | Displays approximately 78.8 days            | PASS   |
| PF-03   | Verify Total Discharges            | Displays 10K                                | PASS   |
| PF-04   | Verify Transfer Rate               | Displays 17.6%                              | PASS   |
| PF-05   | Verify Admission Trends            | Monthly trend displays correctly            | PASS   |
| PF-06   | Verify Discharge Tracking          | Monthly discharges display correctly        | PASS   |
| PF-07   | Verify Transfer Rate by Department | Department transfer rates display correctly | PASS   |
| PF-08   | Verify Average Stay Analysis       | Department LOS values display correctly     | PASS   |
| PF-09   | Verify Monthly Patient Load Trend  | Monthly patient load displays correctly     | PASS   |
| PF-10   | Verify Admissions by Patient Type  | Patient categories display correctly        | PASS   |
| PF-11   | Verify Admissions by Age Group     | Age groups display correctly                | PASS   |
| PF-12   | Verify Patient Flow by Day of Week | Weekly patient flow displays correctly      | PASS   |

---

## 6. Department Analytics Dashboard

| Test ID | Test Case                                 | Expected Result                                | Status |
| ------- | ----------------------------------------- | ---------------------------------------------- | ------ |
| DA-01   | Verify Total Admissions                   | Displays 10K                                   | PASS   |
| DA-02   | Verify Average Length of Stay             | Displays approximately 78.8 days               | PASS   |
| DA-03   | Verify Total Discharges                   | Displays 10K                                   | PASS   |
| DA-04   | Verify Readmission Rate                   | Displays 49.87%                                | PASS   |
| DA-05   | Verify Department Efficiency Score        | Displays calculated value                      | PASS   |
| DA-06   | Verify Department Efficiency Chart        | Department values display correctly            | PASS   |
| DA-07   | Verify Patient Volume by Department       | Department volumes display correctly           | PASS   |
| DA-08   | Verify Readmission by Department          | Department readmission rates display correctly | PASS   |
| DA-09   | Verify Department Efficiency Comparison   | Department comparison displays correctly       | PASS   |
| DA-10   | Verify Average LOS by Department          | Department LOS values display correctly        | PASS   |
| DA-11   | Verify Utilization Capacity by Department | Department utilization displays correctly      | PASS   |

---

## 7. Resource Utilization Dashboard

| Test ID | Test Case                                  | Expected Result                          | Status |
| ------- | ------------------------------------------ | ---------------------------------------- | ------ |
| RU-01   | Verify Occupancy Rate                      | Displays 36.76%                          | PASS   |
| RU-02   | Verify Bed Utilization                     | Displays 36.76%                          | PASS   |
| RU-03   | Verify Staff Utilization                   | Displays approximately 57.9%             | PASS   |
| RU-04   | Verify Equipment Utilization               | Displays approximately 33.6%             | PASS   |
| RU-05   | Verify Resource Availability Rate          | Displays calculated value                | PASS   |
| RU-06   | Verify Bed Utilization by Department       | Department values display correctly      | PASS   |
| RU-07   | Verify Resource Availability by Department | Department values display correctly      | PASS   |
| RU-08   | Verify Equipment Utilization by Type       | Equipment categories display correctly   | PASS   |
| RU-09   | Verify Staff Allocation by Department      | Department allocation displays correctly | PASS   |
| RU-10   | Verify Capacity Planning by Department     | Capacity values display correctly        | PASS   |

---

## 8. Dashboard Interaction Testing

| Test ID | Interaction                     | Expected Result                            | Status |
| ------- | ------------------------------- | ------------------------------------------ | ------ |
| INT-01  | Date Range Filter               | Relevant visuals update correctly          | PASS   |
| INT-02  | Hospital Filter                 | Relevant visuals update correctly          | PASS   |
| INT-03  | Department Filter               | Relevant visuals update correctly          | PASS   |
| INT-04  | Patient Type Filter             | Relevant visuals update correctly          | PASS   |
| INT-05  | Age Filter                      | Relevant visuals update correctly          | PASS   |
| INT-06  | Gender Filter                   | Relevant visuals update correctly          | PASS   |
| INT-07  | Visual Cross-Filtering          | Selecting a visual updates related visuals | PASS   |
| INT-08  | Reset Filters                   | Filters return to default state            | PASS   |
| INT-09  | Home Button                     | Opens Home/About page                      | PASS   |
| INT-10  | Dashboards Button               | Opens dashboard navigation                 | PASS   |
| INT-11  | Hospital Overview Navigation    | Opens Hospital Overview                    | PASS   |
| INT-12  | Patient Flow Navigation         | Opens Patient Flow                         | PASS   |
| INT-13  | Department Analytics Navigation | Opens Department Analytics                 | PASS   |
| INT-14  | Resource Utilization Navigation | Opens Resource Utilization                 | PASS   |
| INT-15  | About Button                    | Opens About page                           | PASS   |

---

## 9. Patient Flow Validation

| Test ID | Test Case                          | Expected Result               | Status |
| ------- | ---------------------------------- | ----------------------------- | ------ |
| FLOW-01 | Validate total admissions          | 10,000                        | PASS   |
| FLOW-02 | Validate total discharges          | 10,000                        | PASS   |
| FLOW-03 | Validate transferred patients      | 1,760                         | PASS   |
| FLOW-04 | Validate transfer rate             | 17.60%                        | PASS   |
| FLOW-05 | Validate average LOS               | 78.78 days                    | PASS   |
| FLOW-06 | Validate monthly admissions        | Matches dashboard/source data | PASS   |
| FLOW-07 | Validate monthly discharges        | Matches dashboard/source data | PASS   |
| FLOW-08 | Validate department transfer rates | Values display correctly      | PASS   |
| FLOW-09 | Validate monthly patient load      | Values display correctly      | PASS   |
| FLOW-10 | Validate day-of-week patient flow  | Values display correctly      | PASS   |

---

## 10. Navigation Testing

| Test ID | Button / Navigation  | Expected Result            | Status |
| ------- | -------------------- | -------------------------- | ------ |
| NAV-01  | Home                 | Opens Home/About page      | PASS   |
| NAV-02  | Dashboards           | Opens dashboard navigation | PASS   |
| NAV-03  | Reset                | Clears active filters      | PASS   |
| NAV-04  | About                | Opens About page           | PASS   |
| NAV-05  | Hospital Overview    | Opens Hospital Overview    | PASS   |
| NAV-06  | Patient Flow         | Opens Patient Flow         | PASS   |
| NAV-07  | Department Analytics | Opens Department Analytics | PASS   |
| NAV-08  | Resource Utilization | Opens Resource Utilization | PASS   |

---

# 11. Overall QA Result

| Testing Category              | Result |
| ----------------------------- | ------ |
| Data Validation               | PASS   |
| KPI Validation                | PASS   |
| Healthcare Metric Validation  | PASS   |
| Hospital Overview Testing     | PASS   |
| Patient Flow Testing          | PASS   |
| Department Analytics Testing  | PASS   |
| Resource Utilization Testing  | PASS   |
| Dashboard Interaction Testing | PASS   |
| Patient Flow Validation       | PASS   |
| Navigation Testing            | PASS   |

## Final Status

**Overall QA Result: PASS**

All major dashboard components, KPI calculations, healthcare metrics, visualizations, filters, interactions, and navigation elements were tested and functioned as expected.

The MedTrack DV dashboard is considered **ready for final delivery**.
