# MedTrack – Hospital Operations & Patient Analytics

## 1. Project Overview

MedTrack is a hospital operations and patient analytics project designed to support healthcare operational monitoring through data analysis and interactive Tableau dashboards.

The project analyzes hospital admissions, patient flow, department performance, occupancy, readmissions, and resource utilization.

The final solution provides four integrated dashboards:

1. Hospital Overview
2. Patient Flow
3. Department Analytics
4. Resource Utilization

---

## 2. Dataset Sources

The project uses hospital patient and operational data containing information related to:

* Patient admissions
* Admission dates
* Discharge dates
* Admission types
* Departments
* Patient demographics
* Bed occupancy
* Readmission information
* Staff allocation
* Equipment usage
* Hospital resources
* Capacity-related metrics

The project uses processed hospital data for the development of the Tableau dashboards. Raw and cleaned data files are maintained as part of the project data-processing workflow.

---

## 3. Data Processing Methodology

The data processing workflow consists of the following stages:

```text
Data Collection
      ↓
Data Cleaning
      ↓
Data Transformation
      ↓
KPI Generation
      ↓
Tableau Visualization
      ↓
Dashboard Testing
```

Python and Pandas were used for data collection, cleaning, transformation, and KPI preparation.

The processed data was then used to build the Tableau dashboards.

---

## 4. KPI Definitions

### Total Admissions

Represents the total number of patient admissions recorded in the dataset.

### Occupancy Rate

Represents the proportion of available hospital bed capacity that is occupied.

### Average Length of Stay

Represents the average duration of patient hospitalization.

### Readmission Rate

Represents the percentage of patient records associated with readmission.

### Bed Utilization

Represents the utilization of hospital beds across departments.

### Department Efficiency

Provides a comparative view of departmental operational efficiency using relevant patient, staffing, and capacity metrics.

### Resource Availability

Represents the availability of hospital resources across departments.

---

## 5. Dashboard Guide

### 5.1 Hospital Overview

The Hospital Overview dashboard provides a high-level view of hospital operations.

It includes:

* Total Admissions
* Occupancy Rate
* Average Length of Stay
* Readmission Rate
* Admissions Trend
* Patients by Gender
* Admissions by Department
* Occupancy Monitoring by Department
* Readmission Analysis

This dashboard is intended for overall hospital performance monitoring.

---

### 5.2 Patient Flow

The Patient Flow dashboard focuses on the movement of patients through the hospital.

It includes:

* Admission Type Distribution
* Peak Patient Load
* Average LOS by Admission Type
* Patient Transfers by Department
* Monthly Discharges

This dashboard helps analyze admission patterns, patient movement, length of stay, discharge activity, and peak patient load.

---

### 5.3 Department Analytics

The Department Analytics dashboard provides department-level operational analysis.

It includes:

* Patient Volume by Department
* Readmission by Department
* Department Efficiency Comparison
* Treatment Capacity Analysis
* Department Occupancy

This dashboard supports comparison of departmental workload, efficiency, readmission levels, capacity, and occupancy.

---

### 5.4 Resource Utilization

The Resource Utilization dashboard focuses on hospital resource management.

It includes:

* Bed Utilization
* Staff Allocation
* Equipment Utilization
* Capacity Planning
* Resource Availability

This dashboard supports analysis of resource usage, staffing, equipment utilization, capacity, and available resources.

---

## 6. Dashboard Integration

The four dashboards are integrated using Tableau navigation controls.

Users can navigate between:

```text
Hospital Overview
       ↕
Patient Flow
       ↕
Department Analytics
       ↕
Resource Utilization
```

Global filters are provided for relevant dashboards, including:

* Month
* Hospital
* Department
* Gender where applicable

The filters were tested to ensure that the dashboard visualizations respond correctly to user selections.

---

## 7. Healthcare Operations Methodology

The dashboard suite supports healthcare operational analysis through four major areas.

### Patient Flow Monitoring

Admission patterns, patient transfers, discharge activity, length of stay, and peak patient load are monitored to understand patient movement.

### Capacity Management

Occupancy, treatment capacity, bed utilization, and capacity planning metrics provide visibility into hospital capacity.

### Department Performance

Department-level patient volume, readmission rates, efficiency, and occupancy provide a basis for operational comparison between departments.

### Resource Management

Staff allocation, equipment utilization, bed utilization, and resource availability provide insights for hospital resource planning.

---

## 8. Testing and Validation

The dashboard suite was tested as part of Module 7.

Testing covered:

* KPI calculations
* Healthcare metrics
* Dashboard filters
* Dashboard navigation
* Patient flow analytics
* Department analytics
* Resource utilization

The following dashboards were tested:

* Hospital Overview
* Patient Flow
* Department Analytics
* Resource Utilization

The detailed QA checklist and Dashboard Testing Report are maintained in the `docs` directory.

### KPI Validation

The main Hospital Overview KPIs were checked during dashboard validation:

| KPI                    | Dashboard Value | Status |
| ---------------------- | --------------: | ------ |
| Total Admissions       |           5,099 | PASS   |
| Occupancy Rate         |          37.26% | PASS   |
| Average Length of Stay |           79.55 | PASS   |
| Readmission Rate       |          50.07% | PASS   |

### Final Testing Result

The dashboard filters, navigation controls, KPI displays, patient flow analytics, department analytics, and resource utilization dashboards were tested successfully.

**Overall Testing Status: PASS**

---

## 9. Project Structure

The final project is organized into the following logical structure:

```text
Hospital-Operations-Patient-Analytics/
│
├── data/
│   ├── Raw and cleaned hospital datasets
│   └── Processed datasets used for analysis
│
├── scripts/
│   ├── Data collection scripts
│   ├── Data cleaning scripts
│   └── KPI preparation scripts
│
├── dashboard/
│   ├── medtrack_dashboard_v1.twbx
│   └── MedTrack_DV.twbx
│
├── docs/
│   ├── QA_Checklist.md
│   ├── Dashboard_Testing_Report.md
│   └── Final_Documentation.md
│
└── README.md
```

---

## 10. Technology Stack

| Area                  | Technology                              |
| --------------------- | --------------------------------------- |
| Data Collection       | Python                                  |
| Data Processing       | Pandas, NumPy                           |
| Data Cleaning         | Python                                  |
| Visualization         | Tableau Desktop                         |
| Dashboard Integration | Tableau Filters, Parameters and Actions |
| Documentation         | Markdown                                |
| Version Control       | GitHub                                  |

---

## 11. Final Deliverables

The completed project includes:

* Cleaned hospital dataset
* Python data processing scripts
* KPI preparation and calculation workflow
* Hospital Overview dashboard
* Patient Flow dashboard
* Department Analytics dashboard
* Resource Utilization dashboard
* QA Checklist
* Dashboard Testing Report
* Final Documentation
* GitHub repository
* Final Tableau workbook

The primary integrated Tableau workbook for the final dashboard solution is:

`MedTrack_DV.twbx`

The Module 5 dashboard workbook is:

`medtrack_dashboard_v1.twbx`

---

## 12. Conclusion

MedTrack provides an integrated hospital operations analytics solution covering patient admissions, patient flow, departmental performance, hospital capacity, and resource utilization.

The four dashboards provide interactive views for monitoring operational metrics and supporting data-driven healthcare management.

The project was tested for dashboard functionality, KPI display, filters, navigation, patient flow analytics, department analytics, and resource utilization.

The final solution provides a structured and interactive Tableau-based environment for exploring hospital operational data and supporting healthcare resource and performance analysis.
