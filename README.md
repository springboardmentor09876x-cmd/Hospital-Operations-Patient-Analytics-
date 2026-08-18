# MedTrack – Hospital Operations & Patient Analytics

MedTrack is a hospital operations and patient analytics project developed to analyze healthcare operational data through Python-based data processing and interactive Tableau dashboards.

The project provides insights into patient admissions, patient flow, department performance, hospital occupancy, readmissions, capacity, and resource utilization.

## Project Objectives

The main objectives of MedTrack are to:

* Analyze hospital admission patterns
* Monitor patient flow and discharge activity
* Compare department-level performance
* Analyze hospital occupancy and capacity
* Monitor readmission rates
* Analyze staff and equipment utilization
* Provide interactive dashboards for healthcare operations analysis

## Dashboard Suite

The project contains four integrated Tableau dashboards.

### 1. Hospital Overview

Provides a high-level view of hospital operations.

Key views include:

* Total Admissions
* Occupancy Rate
* Average Length of Stay
* Readmission Rate
* Admissions Trend
* Patients by Gender
* Admissions by Department
* Occupancy Monitoring by Department
* Readmission Analysis

### 2. Patient Flow

Focuses on patient movement and admission patterns.

Key views include:

* Admission Type Distribution
* Peak Patient Load
* Average LOS by Admission Type
* Patient Transfers by Department
* Monthly Discharges

### 3. Department Analytics

Provides department-level operational analysis.

Key views include:

* Patient Volume by Department
* Readmission by Department
* Department Efficiency Comparison
* Treatment Capacity Analysis
* Department Occupancy

### 4. Resource Utilization

Focuses on hospital resource management.

Key views include:

* Bed Utilization
* Staff Allocation
* Equipment Utilization
* Capacity Planning
* Resource Availability

## Key KPIs

The dashboard suite includes important healthcare operational metrics such as:

* Total Admissions
* Occupancy Rate
* Average Length of Stay
* Readmission Rate
* Bed Utilization
* Department Efficiency
* Resource Availability

## Data Processing

The data processing workflow follows these stages:

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

The processed data was then used to develop the Tableau dashboards.

## Technology Stack

| Area                  | Technology                              |
| --------------------- | --------------------------------------- |
| Data Collection       | Python                                  |
| Data Processing       | Pandas, NumPy                           |
| Data Cleaning         | Python                                  |
| Visualization         | Tableau Desktop                         |
| Dashboard Integration | Tableau Filters, Parameters and Actions |
| Documentation         | Markdown                                |
| Version Control       | GitHub                                  |

## Project Structure

```text
Hospital-Operations-Patient-Analytics/
│
├── data/
│   ├── hospital_cleaned.csv
│   ├── hospital_final_dataset.xlsx
│   └── hospital_raw_data.csv
│
├── scripts/
│   ├── data_collection.py
│   ├── generate_hospital_kpis.py
│   ├── hospital_cleaning.py
│   └── hospital_cleaning.ipynb
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

## Dashboard Integration

The dashboards are integrated using Tableau navigation controls.

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

Interactive filters are provided for relevant dashboards, including:

* Month
* Hospital
* Department
* Gender where applicable

Dashboard interactions and filters were tested during the validation stage.

## Testing and Validation

The dashboard suite was tested for:

* KPI calculations
* Healthcare metrics
* Dashboard filters
* Dashboard navigation
* Patient flow analytics
* Department analytics
* Resource utilization

The overall dashboard testing status is:

**PASS**

Detailed testing information is available in:

```text
docs/QA_Checklist.md
docs/Dashboard_Testing_Report.md
```

## Documentation

Detailed project documentation is available in the `docs` directory.

* `Final_Documentation.md` – Complete project documentation
* `QA_Checklist.md` – Quality assurance checklist
* `Dashboard_Testing_Report.md` – Dashboard testing and validation report

## Tableau Workbooks

The final Tableau workbooks are available in the `dashboard/` directory.

The primary integrated dashboard workbook is:

```text
MedTrack_DV.twbx
```

The Module 5 dashboard workbook is:

```text
medtrack_dashboard_v1.twbx
```

## Final Deliverables

The project includes:

* Cleaned hospital dataset
* Python data processing scripts
* KPI preparation workflow
* Hospital Overview dashboard
* Patient Flow dashboard
* Department Analytics dashboard
* Resource Utilization dashboard
* QA Checklist
* Dashboard Testing Report
* Final Documentation
* GitHub repository
* Final Tableau workbook

## Conclusion

MedTrack provides an integrated hospital operations analytics solution covering patient admissions, patient flow, departmental performance, hospital capacity, and resource utilization.

The four interactive dashboards provide a consolidated environment for exploring hospital operational data and supporting data-driven healthcare analysis.
