# MedTrack DV

## Hospital Operations & Patient Analytics Dashboard

MedTrack DV is an interactive **Hospital Operations & Patient Analytics Dashboard** developed using Microsoft Power BI. It provides a consolidated view of hospital operations, patient flow, department performance, and resource utilization.

The dashboard transforms patient-level hospital data into meaningful analytical insights to support monitoring, comparison, and operational decision-making.

---

## 1. Project Overview

MedTrack DV consists of four interactive dashboards:

* **Hospital Overview** – Overall hospital performance and key trends.
* **Patient Flow** – Admissions, discharges, transfers, and patient stay analysis.
* **Department Analytics** – Department-level performance and comparison.
* **Resource Utilization** – Bed, staff, equipment, and resource utilization analysis.

The dashboards use interactive filters, cross-filtering, KPI cards, charts, and navigation controls to provide a consistent analytical experience.

---

## 2. Project Objectives

The main objectives of MedTrack DV are to:

* Monitor key hospital performance indicators.
* Analyze patient admissions, discharges, transfers, and length of stay.
* Compare performance across hospital departments.
* Analyze readmission patterns.
* Monitor bed, staff, and equipment utilization.
* Identify operational trends and differences between departments.
* Provide an interactive and user-friendly hospital analytics solution.

---

## 3. Dataset Sources & Description

### Dataset

The project uses a cleaned hospital patient analytics dataset containing **10,000 patient records**.

The dataset contains information related to patients, admissions, discharges, departments, transfers, readmissions, beds, staff, and equipment.

### Dataset Summary

| Attribute              |      Value |
| ---------------------- | ---------: |
| Patient Records        |     10,000 |
| Unique Patients        |     10,000 |
| Hospitals              |         20 |
| Departments            |         10 |
| Minimum Length of Stay |      1 day |
| Maximum Length of Stay |   338 days |
| Average Length of Stay | 78.78 days |
| Transferred Patients   |      1,760 |
| Readmitted Patients    |      4,987 |

### Data Preparation

Before dashboard development, the dataset was checked and prepared by:

* Checking missing values.
* Checking duplicate patient records.
* Validating Patient IDs.
* Validating admission and discharge dates.
* Checking Length of Stay values.
* Validating readmission information.
* Validating transfer information.
* Preparing fields required for dashboard calculations.

---

## 4. Healthcare Operations Methodology

The dashboard converts patient-level records into operational and department-level healthcare metrics.

### Patient Flow

Patient movement is analyzed through:

**Admissions → Department Activity → Transfers → Discharges**

This provides an overview of patient movement through the hospital.

### Length of Stay

Average Length of Stay is used to measure the average number of days patients remain in the hospital and to compare stay patterns across departments.

### Readmission

Readmission analysis measures the proportion of patients identified as readmitted and allows comparison of readmission patterns between departments.

### Resource Utilization

Hospital resource utilization is analyzed through:

* Bed utilization
* Occupancy
* Staff utilization
* Equipment utilization
* Resource availability
* Department-level resource analysis

### Department Performance

Departments are compared using:

* Patient volume
* Average Length of Stay
* Readmission Rate
* Department Efficiency Score
* Resource utilization

---

## 5. KPI Definitions

| KPI                             | Definition                                                         |
| ------------------------------- | ------------------------------------------------------------------ |
| **Total Admissions**            | Total number of patient admission records.                         |
| **Occupancy Rate**              | Percentage representing hospital bed occupancy.                    |
| **Average Length of Stay**      | Average number of days patients stay in the hospital.              |
| **Readmission Rate**            | Percentage of patients identified as readmitted.                   |
| **Bed Utilization Rate**        | Percentage representing the utilization of available beds.         |
| **Transfer Rate**               | Percentage of patients who were transferred.                       |
| **Staff Utilization**           | Measure of staff utilization across hospital operations.           |
| **Equipment Utilization**       | Measure of hospital equipment usage.                               |
| **Department Efficiency Score** | Measure used to compare operational efficiency across departments. |
| **Resource Availability Rate**  | Measure representing the availability of hospital resources.       |

### Validated KPI Values

| Metric                      |      Value |
| --------------------------- | ---------: |
| Total Admissions            |     10,000 |
| Average Length of Stay      | 78.78 days |
| Occupancy Rate              |     36.76% |
| Readmission Rate            |     49.87% |
| Bed Utilization Rate        |     36.76% |
| Transfer Rate               |     17.60% |
| Staff Utilization           |     57.92% |
| Equipment Utilization       |     33.55% |
| Department Efficiency Score |       27.9 |
| Resource Availability Rate  |      99.3% |

---

## 6. Dashboard Guide

### 6.1 Hospital Overview

The Hospital Overview dashboard provides a high-level view of hospital performance.

**Key KPIs:**

* Total Admissions
* Occupancy Rate
* Average Length of Stay
* Readmission Rate
* Bed Utilization
* Department Efficiency Score

**Key Visuals:**

* Admission Trends
* Occupancy Rate Trend
* Readmission Rate Trend
* Admissions by Patient Type
* Admissions by Department
* Average LOS by Department
* Readmission Rate by Department
* Total Admissions by Date
* Monthly Admissions vs Discharges
* Department Efficiency Score by Department

**Purpose:** Provides an overall view of hospital activity, trends, and departmental performance.

---

### 6.2 Patient Flow

The Patient Flow dashboard focuses on patient movement through the hospital.

**Key KPIs:**

* Total Admissions
* Average Length of Stay
* Total Discharges
* Transfer Rate

**Key Visuals:**

* Admission Trends
* Discharge Tracking
* Transfer Rate by Department
* Average Stay Analysis
* Monthly Patient Load Trend
* Admissions by Patient Type
* Admissions by Age Group
* Patient Flow by Day of Week

**Purpose:** Helps analyze admissions, discharges, transfers, patient load, and length-of-stay patterns.

---

### 6.3 Department Analytics

The Department Analytics dashboard focuses on comparing hospital departments.

**Key KPIs:**

* Total Admissions
* Average Length of Stay
* Total Discharges
* Readmission Rate
* Department Efficiency Score

**Key Visuals:**

* Department Efficiency Score
* Patient Volume by Department
* Readmission Rate by Department
* Department Efficiency Comparison
* Average LOS by Department
* Utilization Capacity by Department

**Purpose:** Enables comparison of patient activity, performance, and utilization across departments.

---

### 6.4 Resource Utilization

The Resource Utilization dashboard focuses on hospital resource management.

**Key KPIs:**

* Occupancy Rate
* Bed Utilization
* Staff Utilization
* Equipment Utilization
* Resource Availability Rate

**Key Visuals:**

* Bed Utilization by Department
* Resource Availability by Department
* Equipment Utilization by Equipment Type
* Staff Allocation by Department
* Capacity Planning by Department

**Purpose:** Provides insights into resource usage, availability, and departmental capacity.

---

## 7. Dashboard Interactions & Navigation

The dashboards support interactive analysis through:

* Date Range filtering
* Hospital filtering
* Department filtering
* Patient Type filtering
* Age filtering
* Gender filtering
* Visual cross-filtering
* Reset Filters
* Dashboard navigation

### Navigation Flow

**Home → Hospital Overview → Patient Flow → Department Analytics → Resource Utilization**

Users can select filters or chart elements to dynamically update related visuals.

The **Reset** function returns the dashboard to its default filter state.

The **About** page provides information about the project and dashboard.

---

## 8. Testing & Validation

The dashboard was tested as part of **Module 7: Testing and Validation**.

Testing covered:

* Data validation
* KPI validation
* Healthcare metric validation
* Dashboard visual validation
* Filter testing
* Cross-filtering
* Navigation
* Reset Filters
* Patient flow validation
* Department analytics
* Resource utilization

The dashboard was manually tested and all major dashboard components, filters, interactions, and navigation functions operated as expected.

### Testing Result

**Overall QA Result: PASS**

Detailed testing records are available in:

* [QA Checklist](docs/QA_Checklist.md)
* [Dashboard Testing Report](docs/Dashboard_Testing_Report.md)

---

## 9. Conclusion

MedTrack DV provides an interactive analytical view of hospital operations and patient activity by combining patient flow analysis, department performance monitoring, healthcare KPI tracking, and resource utilization analysis.

The dashboard has completed data validation, KPI validation, functional testing, interaction testing, and navigation testing.

