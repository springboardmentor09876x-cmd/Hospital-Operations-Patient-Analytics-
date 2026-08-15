# Dashboard Testing Report: MedTrack_DV
**Project:** MedTrack_DV - Hospital Operations and Patient Analytics Dashboard  
**Milestone:** Milestone 4 Final Testing & Sign-Off Report  

---

## 1. Report Summary

- **Report title:** MedTrack_DV Analytics Dashboard Validation Report
- **Report version:** v1.0.0
- **Dashboard version:** v1.2-Build2026
- **Dataset version:** v1.1_Cleaned
- **Test window:** 12 August 2026 – 15 August 2026
- **Tester:** [Insert Your Name]
- **Reviewer:** [Insert Your Infosys Mentor's Name] (Infosys Mentor)
- **Overall verdict:** **PASS** *(All data logic and visual layout issues verified)*

---

## 2. Scope

### In Scope
- **KPI calculation validation**: Total counts, maximum bounds, and mathematical consistency across all 8 core metrics.
- **Healthcare metric verification**: Distribution balances across hospital types, departments, and demographics.
- **Dashboard interaction testing**: Cross-filtering responsiveness, Area Chart trends, and slicer mapping across pages (each featuring exactly 5 synchronized visual blocks).
- **Patient flow analytics validation**: Chronological timeline compliance and visualization mapping.

### Out of Scope
- Optional visual/aesthetic color scheme or theme changes.
- *Note:* Responsive layout testing (UI-04) is strictly limited to functional element visibility and object scaling on target screen boundaries, not subjective aesthetic adjustments.

---

## 3. Test Environment

| Item | Details |
| --- | --- |
| OS | Windows 11 |
| Browser / app runtime | Google Chrome v121+ / Power BI Desktop |
| Dashboard platform | Power BI |
| IDE / Scripting Platform | Jupyter Notebook |
| Python version | Python 3.11.5 |
| Test framework | Pandas Validation Logic & Manual UI Inspection |
| Source dataset | `hospital_cleaned.csv` |
| Final dataset | `hospital_final_dataset.xlsx` |

---

## 4. Data and Logic Basis

Documented backend rules applied during validation processing:

* `Length of Stay (LOS) = Discharge Date - Admission Date`
* `Average Length of Stay` = Sum of all valid records' LOS divided by total row count.
* `Readmission Rate` = Count of records where `Readmission_Flag` == 1 or "Yes" / Total unique admissions.
* `Bed Occupancy Rate` = Total filled beds / Total functional hospital beds.
* `ICU Utilization Rate` = Active ICU occupants / Maximum configured ICU bed capacity.
* `Staff Utilization Rate` = Aggregated active duty staff assignment value indicators.
* `Equipment Utilization Rate` = Total machine assets flagged with "In Use" status tags.
* `Patient Transfer Rate` = Count of records with documented departmental routing changes.
* `Department Efficiency Score` = Calculated as an *inverse relationship* to average department LOS (a lower average department length of stay equals a higher efficiency metric performance score).

---

## 5. Test Execution Summary

| Area | Planned | Executed | Passed | Failed | Blocked |
| --- | --- | --- | --- | --- | --- |
| KPI calculations (8 Total) | 8 | 8 | 8 | 0 | 0 |
| Healthcare metrics | 5 | 5 | 5 | 0 | 0 |
| Dashboard interactions | 4 | 4 | 4 | 0 | 0 |
| Patient flow analytics (5 Total) | 5 | 5 | 5 | 0 | 0 |

---

## 6. Detailed Test Results

### 6.1 KPI Calculation Validation (Overview & Resource Pages)

| Test ID | Test description | Automation / manual evidence | Expected result | Actual result | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| KPI-01 | **6 Overview KPIs** match source data criteria | Jupyter script calculation check | All 6 primary operational metrics balance completely. | Value balances align. | **PASSED** | Verified on Overview Page. |
| KPI-02 | **2 Resource KPIs** match capacity constraints | Aggregation bounds check log | Utilization indicators stay safely within 0-100% logic. | Bounds check validated. | **PASSED** | Verified on Resource Page. |
| KPI-03 | Total row counters equal dataset row count | Notebook validation check output | Summary metrics display exactly 10K records. | 10K display confirmed. | **PASSED** | Data parsed completely. |
| KPI-04 | Average LOS matches computed mean | Notebook backend validation code | Mean value calculations line up to 2 decimal places. | Target means match exactly. | **PASSED** | Verified backend logic. |
| KPI-05 | Readmission rate matches source flags | Pandas matrix aggregation logic | Aggregated counts equal split segment proportions. | Proportions resolve correctly. | **PASSED** | Verified backend logic. |
| KPI-06 | Occupancy calculations are true | Database cross-check script | Aggregated utilization values match underlying variables. | Gauge calculations line up. | **PASSED** | Verified backend logic. |
| KPI-07 | Department efficiency is non-negative | Math limit rule test script | No negative scores or null division operations. | Values remain non-negative. | **PASSED** | Verified backend logic. |
| KPI-08 | Utilization flags evaluate accurately | Code execution run log | Logical values align with operational run schedules. | Flag parameters balance. | **PASSED** | Verified backend logic. |

### 6.2 Healthcare Metrics Verification

| Test ID | Test description | Automation / manual evidence | Expected result | Actual result | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| HM-01 | Hospital type distribution matches dataset | Manual cross-validation check | Chart distributions sync to reference targets. | Distro sync complete. | **PASSED** | Verified. |
| HM-02 | Department counts and KPIs match dataset | Row grouping value script | Visual counts match raw database values. | Value counts align. | **PASSED** | Verified. |
| HM-03 | Age, gender, and diagnosis are accurate | Aggregation script comparison | Demographics map cleanly without dropping fields. | Records align cleanly. | **PASSED** | Verified. |
| HM-04 | Billing and insurance values are correct | Column financial sum checks | Asset balances equal source metrics. | Sum balances match. | **PASSED** | Verified. |
| HM-05 | 5 Visualizations per Dashboard Verification | Visual component count verification | Canvas contains exactly 5 clean visualization structures per dashboard layout. | Layout density matches parameters. | **PASSED** | Verified structural consistency across pages. |

### 6.3 Dashboard Interaction Testing

| Test ID | Test description | Automation / manual evidence | Expected result | Actual result | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| UI-01 | Slicers filter all related visuals correctly | Manual cross-filter check | Visual values filter smoothly when options change. | Values adapt smoothly. | **PASSED** | Verified. |
| UI-02 | Drill-down and drill-through navigation works | Component click testing | Sub-menus load secondary structural layouts. | Navigation loops execute. | **PASSED** | Verified. |
| UI-03 | Cross-filter updates visuals correctly | Multi-select click validation | Highlighted dashboard interactions balance layouts. | Canvas states update. | **PASSED** | Verified. |
| UI-04 | Responsive layout behaves on target boundaries | Browser sizing view test | Visual containers scale to screen sizes cleanly without clipping. | Sizing checks out clean. | **PASSED** | Verified. |

### 6.4 Patient Flow Analytics Validation

| Test ID | Test description | Automation / manual evidence | Expected result | Actual result | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| PF-01 | Patient journey sequence is chronological | Date-order sorting pipeline check | Event pathways move progressively forward in time. | Sequences trace forward. | **PASSED** | Verified. |
| PF-02 | Transfer path is correct for transferred records | Location movement array check | Visual graphs trace correct movements. | Graph trails verify fine. | **PASSED** | Verified. |
| PF-03 | Number of transfers matches recorded history | Count cross-check check | Path histories total cleanly. | Historic totals balance. | **PASSED** | Verified. |
| PF-04 | Missing or partial journey data handled safely | Edge case null value injection | Null entries show as blank or generic markers without crashing. | Visuals display blanks safely. | **PASSED** | Verified. |
| PF-05 | 5 Key Visualizations structural audit | Visual panel layout sweep | Canvas maps 5 explicit visual analytics blocks without grid clipping. | Layout density balances. | **PASSED** | Verified on Patient Flow Page. |

---

## 7. Defects and Issues (Production Review Status)

| Issue ID | Severity | Area | Description | Resolution Actions | Status |
| --- | --- | --- | --- | --- | --- |
| **DEF-01** | 🔥 **High** | UI - Hospital Overview | Overlapping focus boundaries on filter headers. | Resized layout containers and modified alignment coordinates. | **PASSED** |
| **DEF-02** | ⚠️ **Medium** | UI - Patient Flow | Over-segmented pie chart used for monthly time distribution. | Switched layout type to a continuous Area Chart trend visual. | **PASSED** |
| **DEF-03** | ⚠️ **Medium** | UI - Resource Utilization | Card metrics displaying raw database implicit formulas (`Max of...`). | Applied clean custom business renames to individual fields. | **PASSED** |
| **DEF-04** | 📉 **Low** | UI - Axis Formatting | Axis text crowding and label bleeding on charts. | Adjusted axis padding and word wrap properties. | **PASSED** |

---

## 8. Retest Log

| Date | Test ID | Fix verified | Result | Notes |
| --- | --- | --- | --- | --- |
| 15/08/2026 | DEF-01 | Container boundary constraints | **PASSED** | Grid spacing traces correctly now. |
| 15/08/2026 | DEF-02 | Area Chart rendering transition | **PASSED** | Monthly intervals scale perfectly. |
| 15/08/2026 | DEF-03 | Value card custom text labels | **PASSED** | Clear business naming verified. |
| 15/08/2026 | DEF-04 | Text axis margins layout sweep | **PASSED** | Readability overlap eliminated. |

---

## 9. Final Sign-Off

- **Testing complete:** Yes
- **Critical defects open:** No
- **Ready for delivery: **Yes
