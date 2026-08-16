# Hospital-Operations-Patient-Analytics-
# MedTrack_DV — Hospital Analytics & Operations Dashboard

## Project Overview

**MedTrack_DV** is an interactive hospital analytics project developed to transform hospital data into meaningful operational insights using **Microsoft Power BI**.

The project analyzes patient admissions, patient flow, department performance, bed utilization, readmissions, and hospital resource usage through four interconnected analytical dashboard pages.

The dashboard is designed to help hospital administrators and healthcare managers monitor operational performance, identify trends, compare departments, and support data-driven decision-making.

---

# 1. Dataset Sources

The project uses hospital patient and operational data containing information required for analyzing admissions, patient flow, department activity, resource utilization, bed occupancy, and readmissions.

### Dataset Files

The repository contains the following stages of the dataset:

| Dataset                       | Description                                                       |
| ----------------------------- | ----------------------------------------------------------------- |
| `hospital_raw_data.xlsx`      | Original hospital dataset used as the starting point for analysis |
| `hospital_cleaned.xlsx`       | Dataset after cleaning and preparation                            |
| `hospital_final_dataset.xlsx` | Final dataset prepared for Power BI dashboard development         |

The final prepared dataset contains **10,000 patient records**.

### Dataset Source

**Source:** Kaggle, Global Hospital Flow Dynamics Dataset

The dataset was processed and prepared before being used for dashboard development.

### Data Preparation

The preparation process included:

* Handling inconsistent data
* Standardizing relevant fields
* Preparing categorical and numerical attributes
* Creating derived analytical fields
* Preparing KPI-related information
* Structuring the final dataset for Power BI analysis

### Data Processing Workflow

```text
Raw Hospital Data
        ↓
Data Collection
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
Final Dataset
        ↓
Dashboard Creation
        ↓
Power BI Analysis
```

---

# 2. KPI Definitions

The dashboard uses six primary KPIs to evaluate hospital operations.

| KPI                             | Definition                                                            | Purpose                                                           |
| ------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Total Admissions**            | Measures the total number of patient records handled by the hospital. | Helps monitor patient demand and overall hospital activity.       |
| **Occupancy Rate**              | Indicates the level of hospital bed usage.                            | Helps monitor hospital capacity and bed availability.             |
| **Average Length of Stay**      | Measures the average duration of patient stays.                       | Helps evaluate patient throughput and bed utilization.            |
| **Readmission Rate**            | Tracks the proportion of patients marked as readmitted.               | Helps identify readmission patterns and monitor patient outcomes. |
| **Bed Utilization Rate**        | Examines the utilization of available bed capacity.                   | Helps evaluate how effectively hospital beds are being used.      |
| **Department Efficiency Score** | Provides a comparative measure of departmental performance.           | Helps compare operational efficiency across departments.          |

### Additional Operational Metrics

The dashboard also tracks:

* Average Billing Amount
* Total Discharges
* Total Transfers
* Available Beds
* ICU Beds
* Staff Utilization
* Equipment Utilization

These supporting metrics provide additional context for understanding hospital workload, capacity, and resource usage.

---

# 3. Dashboard Guide

The final Power BI solution consists of **four integrated analytical pages**.

## 3.1 Hospital Overview

The **Hospital Overview** page provides an executive-level summary of overall hospital performance.

### Main Analysis

* Admissions Overview
* Occupancy Monitoring
* Readmission Analysis
* Hospital Performance KPIs
* Monthly Operational Trends

### Key Metrics

* Total Admissions
* Average Length of Stay
* Bed Occupancy %
* Average Billing Amount
* Equipment in Use

This page acts as the main entry point for understanding the current operational situation of the hospital.

---

## 3.2 Patient Flow Analysis

The **Patient Flow Analysis** page focuses on how patients move through the hospital.

### Main Analysis

* Admission Trends
* Discharge Tracking
* Patient Movement
* Average Stay Analysis
* Peak Patient Load Monitoring

### Key Metrics

* Total Admissions
* Total Discharges
* Total Transfers
* Readmission Rate %
* Average Length of Stay

This page helps identify patient movement patterns and periods of higher hospital workload.

---

## 3.3 Department Analytics

The **Department Analytics** page provides detailed comparison between hospital departments.

### Main Analysis

* Treatment Capacity
* Readmission by Department
* Department Efficiency
* Patient Volume by Department
* Department Performance

### Key Metrics

* Total Admissions
* Average Length of Stay
* Readmission Rate %
* Bed Occupancy %
* Total Transfers

This page helps administrators identify departments with higher workloads, different readmission patterns, and variations in operational performance.

---

## 3.4 Resource Utilization

The **Resource Utilization** page focuses on how hospital resources are being utilized.

### Main Analysis

* Bed Utilization
* Staff Allocation
* Equipment Utilization
* Capacity Planning
* Resource Availability

### Key Metrics

* Beds Available
* Bed Occupancy %
* ICU Beds
* Staff Utilization %
* Equipment in Use

This page supports analysis of hospital capacity and resource utilization.

---

## Dashboard Navigation & Interaction

The dashboard is designed as an integrated Power BI report.

### Synced Filters

The following filters are synchronized across dashboard pages:

* Admission Type
* Department
* Month
* City
* Hospital Name

This allows users to maintain the same filtering context while moving between pages.

### Navigation

A **Power BI Page Navigator** connects the four dashboard pages:

```text
Hospital Overview
        ↓
Patient Flow Analysis
        ↓
Department Analytics
        ↓
Resource Utilization
```

### Interactive Features

* KPI Cards
* Synchronized Slicers
* Page Navigator
* Drill-Through
* Interactive Charts
* Department Filtering
* Consistent Dashboard Layout

---

# 4. Healthcare Operations Methodology

The project applies a data-driven methodology to understand and monitor hospital operations.

The methodology converts raw hospital records into operational indicators that can support hospital administrators and department managers.

## Patient Demand Analysis

Admission volumes and trends are analyzed to understand patient demand and overall hospital workload.

## Patient Flow Analysis

Admissions, discharges, transfers, and average length of stay are examined to understand patient movement and hospital throughput.

## Bed & Capacity Management

Occupancy rate and bed utilization are used to monitor available hospital capacity and identify areas where bed demand may require attention.

## Department Performance Analysis

Department-level admission volumes, occupancy, readmission rates, length of stay, and efficiency measures are compared to identify differences in operational performance.

## Resource Utilization

Staff, equipment, ICU beds, and other hospital resources are monitored to understand utilization and support better resource planning.

## Operational Analytics Flow

```text
Hospital Data
      ↓
Data Cleaning & Preparation
      ↓
KPI Development
      ↓
Patient & Operational Analysis
      ↓
Department Comparison
      ↓
Resource Utilization Analysis
      ↓
Operational Insights
      ↓
Data-Driven Decision Support
```

The overall methodology connects patient-level data with hospital-level operational indicators to provide a centralized view of healthcare performance.

---

# 5. Project Structure

The project is organized into separate folders for dashboard files, datasets, documentation, and analysis notebooks.

```text
Hospital-Operations-Patient-Analytics-/
│
├── Dashboard/
│   ├── MedTrack_DV.pbix
│   ├── medtrack_dashboard_v1.pbix
│   └── medtrack_prototype.pbix
│
├── Data/
│   ├── hospital_cleaned.xlsx
│   ├── hospital_final_dataset.xlsx
│   └── hospital_raw_data.xlsx
│
├── Docs/
│   ├── Dashboard Testing Report.pdf
│   ├── QA Checklist.pdf
│   └── dashboard_storyboard.pdf
│
├── Scripts/
│   ├── data_collection.ipynb
│   ├── generate_hospital_kpis.ipynb
│   └── hospital_cleaning.ipynb
│
└── README.md
```

### Folder Responsibilities

**Dashboard/**
Contains Power BI dashboard and prototype files.

**Data/**
Contains raw, cleaned, and final datasets used throughout the project.

**Docs/**
Contains testing, quality assurance, dashboard planning and final documentation.

**Scripts/**
Contains Jupyter notebooks used for data collection, cleaning, and KPI preparation.

---

# 6. Deployment

## GitHub Repository

The project is organized and maintained in a GitHub repository containing the dashboard files, datasets, analysis notebooks, and project documentation.

The repository provides a centralized location for accessing the complete project and its supporting resources.

## Power BI

For the final implementation the dashboard was developed using **Microsoft Power BI**.

The final visualization and dashboard delivery are therefore provided through Power BI files in the `Dashboard/` folder.

---

# 7. Testing & Validation

The dashboard was tested as an integrated report to verify that the analytical calculations and interactive features behaved as expected.

Testing included:

* KPI calculation validation
* Filter interaction testing
* Slicer synchronization testing
* Page navigation testing
* Visual responsiveness testing
* Department-level filtering
* Data consistency checks

Detailed testing documents are available in the `Docs/` folder:

* `Dashboard Testing Report.pdf`
* `QA Checklist.pdf`

---

# 8. Technology Stack

| Area                    | Technology                                  |
| ----------------------- | ------------------------------------------- |
| Data Collection         | Python                                      |
| Data Processing         | Pandas, NumPy                               |
| Data Cleaning           | Python                                      |
| Data Storage            | Microsoft Excel                             |
| Data Analysis           | Python, Jupyter Notebook                    |
| Business Intelligence   | Microsoft Power BI                          |
| Visualization           | Power BI                                    |
| Dashboard Interaction   | Sync Slicers, Page Navigator, Drill-Through |
| Documentation           | Markdown                                    |
| Version Control         | Git & GitHub                                |

---

# 9. Module 8 Deliverables

The completed project provides the required outcomes:

* Dataset source documentation
* KPI definitions
* Dashboard guide
* Healthcare operations methodology
* Organized project structure
* GitHub repository
* Final Power BI dashboard
* QA Checklist
* Dashboard Testing Report
* Supporting datasets
* Data processing scripts

---

# Project Outcome

MedTrack_DV demonstrates how raw hospital data can be transformed into meaningful operational insights using Power BI.

By integrating patient admissions, patient flow, department performance, bed utilization, readmissions, and resource utilization into a unified dashboard environment, the project provides a portfolio-ready analytical solution for understanding and monitoring hospital operations.
