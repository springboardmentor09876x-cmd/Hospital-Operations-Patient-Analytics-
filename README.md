# Hospital-Operations-Patient-Analytics-


# MedTrack_DV — Hospital Analytics & Operations Dashboard

## 📊 Project Overview

**MedTrack_DV** is an interactive hospital analytics project developed during the **Internship** to transform hospital data into meaningful operational insights.

The project uses **Microsoft Power BI** to analyze patient admissions, hospital performance, department-level activity, bed utilization, readmissions, patient flow, and resource usage through a collection of interconnected dashboards.

The dashboard is designed to help hospital administrators and healthcare managers monitor key performance indicators, identify operational patterns, compare departments, and support data-driven decision-making.

---

## 🎯 Project Goals

The primary objective of **MedTrack_DV** is to convert raw hospital records into an easy-to-understand analytical solution.

The project focuses on:

* Monitoring overall hospital performance through key metrics.
* Understanding patient admission and discharge patterns.
* Comparing performance across hospital departments.
* Analyzing bed and staff utilization.
* Identifying readmission patterns.
* Evaluating patient flow and treatment activity.
* Providing interactive filtering and navigation for easier analysis.
* Presenting operational information through a centralized dashboard environment.

---

## 🏥 Dashboard Suite

The final Power BI workbook contains four major analytical pages, with each page focusing on a different aspect of hospital operations.

### 1. Hospital Overview

The **Hospital Overview** page provides an executive-level summary of hospital performance.

#### Analysis Includes

* Admissions Overview
* Occupancy monitoring
* Readmission analysis 
* Hospital Performance KPIs
* Monthly Operational Trends

#### Key Metrics

* Total Admissions
* Avg Length of Stay
* Bed Occupancy %
* Avg Billing Amount
* Equipment in Use

This page acts as the primary entry point for understanding the overall hospital situation.

---

### 2. Patient Flow Analysis

The **Patient Flow** page focuses on how patients move through the hospital and provides insights into admission, discharge, transfer, and stay patterns.

#### Analysis Includes

* Admission trends
* Discharge Tracking
* Patient Movement Analysis
* Average Stay Analysis
* Peak Patient Load Monitoring

#### Key Metrics

* Total Admissions
* Total Discharges
* Total Transfers
* Readmission Rate %
* Avg Length of Stay

The page provides a clearer view of patient movement and helps identify patterns in hospital workload.

---

### 3. Department Analytics

The **Department Analytics** page enables detailed comparison between hospital departments.

#### Analysis Includes

* Treatment Capacity Analysis
* Readmission by Department
* Department Efficiency Comparison
* Patient Volume by Department
* Department Performance Analysis

#### Key Metrics

* Total Admissions
* Avg Length of Stay
* Readmission Rate %
* Bed Occupancy %
* Total Transfers

Interactive comparisons make it possible to identify departments with higher patient loads, different readmission patterns, and variations in operational efficiency.

This page is particularly useful for **department managers and hospital administrators** who need to compare performance across different units.

---

### 4. Resource Utilization

The **Resource Utilization** page focuses on the effective use of hospital resources.

#### Analysis Includes

* Bed Utilization Analysis
* Staff Allocation Monitoring
* Equipment Utilization Tracking
* Capacity Planning Insgiths
* Resource Availability Analysis

#### Key Metrics

* Beds Available
* Bed Occupancy %
* ICU Beds
* Staff Utilization %
* Equipment in Use
  
This dashboard provides a broader view of how available hospital resources are being utilized and where capacity may require closer monitoring.

---
## 📌 Key Performance Indicators

The project incorporates several KPIs to measure hospital operations.

| KPI | Purpose |
| --- | --- |
| **Total Admissions** | Measures the overall number of patient records handled by the hospital. |
| **Occupancy Rate** | Indicates the level of hospital bed usage. |
| **Average Length of Stay** | Measures the average duration of patient stays. |
| **Readmission Rate** | Tracks the proportion of patients marked as readmitted. |
| **Bed Utilization Rate** | Examines utilization of available bed capacity. |
| **Department Efficiency Score** | Provides a comparative measure of departmental performance. |
| **Avg Billing Amount** | Tracks financial volume and average revenue per patient admission. |
| **Total Discharges** | Tracks completed patient discharges handled by the hospital. |
| **Total Transfers** | Measures patient transfers within the hospital. |
| **Available Beds** | Tracks available bed capacity. |
| **ICU Beds** | Monitors dedicated intensive care bed capacity across departments. |
| **Staff Utilization** | Helps monitor staff usage across departments. |
| **Equipment Utilization** | Provides insight into equipment usage. |
---

## 🔄 From Raw Data to Dashboard

The project follows a complete analytics workflow:

**Raw Hospital Data → Data Collection → Data Cleaning → Transformation → KPI Development → Data Modeling → Dashboard Development → Testing → Final Visualization**

### Data Preparation

The hospital dataset was processed before being used for visualization.

The preparation workflow included:

* Removing or handling inconsistent data.
* Standardizing relevant fields.
* Preparing categorical and numerical attributes.
* Creating derived analytical fields.
* Preparing KPI-related information.
* Structuring the dataset for Power BI analysis.

The final dataset contains **10,000 patient records**.

---

## 🖱️ Interactive Dashboard Experience

One of the main goals of the project was to make the dashboard interactive rather than simply presenting static charts.

### 🔹 Synced Filters

Common filters such as:

* Admission Type
* Department
* Month
* City
* Hospital Name

are synchronized across dashboard pages.

This allows users to maintain the same filtering context while moving between different analytical views.

### 🔹 Page Navigation

A **Power BI Page Navigator** provides navigation between the four dashboard pages.

Users can move between:

**Hospital Overview → Patient Flow → Department Analytics → Resource Utilization**

without manually searching through report pages.

### 🔹 Consistent Dashboard Design

The pages follow a consistent visual structure, including:

* KPI cards
* Interactive filters
* Consistent navigation
* Charts and analytical visuals
* Structured layouts
* Unified dashboard styling

This provides a seamless experience when moving across the report.

---

## 🧪 Testing & Validation

The dashboard was tested to ensure that the implemented visuals and analytical calculations behaved as expected.

Validation included checking:

* KPI calculations
* Filter interactions
* Slicer synchronization
* Page navigation
* Visual responsiveness
* Department-level filtering
* Data consistency between source data and dashboard outputs

The final dashboard was reviewed as an integrated Power BI report rather than as four independent pages.

---

## 🛠️ Technology Stack

| Category                          | Technology                                  |
| --------------------------------- | ------------------------------------------- |
| **Programming & Data Processing** | Python                                      |
| **Data Manipulation**             | Pandas, NumPy                               |
| **Data Cleaning**                 | Python                                      |
| **Business Intelligence**         | Microsoft Power BI Desktop                  |
| **Data Visualization**            | Power BI                                    |
| **Dashboard Interaction**         | Sync Slicers, Page Navigator, Drill-Through |
| **Analytical Calculations**       | DAX                                         |
| **Notebook Environment**          | Jupyter Notebook                            |
| **Data Storage**                  | Microsoft Excel                             |
| **Documentation**                 | Markdown                                    |
| **Version Control**               | Git & GitHub                                |

---

## 📁 Project Structure

The project is maintained as a **flat repository structure**. All Power BI reports, Jupyter notebooks, Excel datasets, documentation, and supporting project files are stored directly inside the main **MedTrack_DV** repository.

```text
MedTrack_DV/
│
├── 📄 MedTrack_DV.pbix
├── 📄 README.md
├── 📄 dashboard_storyboard.pdf
│
├── 📓 data_collection.ipynb
├── 📓 generate_hospital_kpis.ipynb
├── 📓 hospital_cleaning.ipynb
│
├── 📊 hospital_raw_data.xlsx
├── 📊 hospital_cleaned.xlsx
├── 📊 hospital_final_dataset.xlsx
│
├── 📄 medtrack_dashboard_v1.pbix
└── 📄 medtrack_prototype.pbix
```

## 📄 File Description

| File                             | Description                                                                                                                             |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **MedTrack_DV.pbix**             | Main and final Power BI dashboard/report file.                                                                                          |
| **README.md**                    | Project documentation containing the project overview, objectives, workflow, dashboard details, technologies, and repository structure. |
| **dashboard_storyboard.pdf**     | Dashboard planning and storyboard document used to define the intended dashboard structure and visual flow.                             |
| **data_collection.ipynb**        | Jupyter Notebook used during the hospital data collection and preparation stage.                                                        |
| **generate_hospital_kpis.ipynb** | Jupyter Notebook used for generating and preparing hospital KPI-related information.                                                    |
| **hospital_cleaning.ipynb**      | Jupyter Notebook used for cleaning and preparing the hospital dataset.                                                                  |
| **hospital_raw_data.xlsx**       | Raw hospital dataset before the cleaning and transformation process.                                                                    |
| **hospital_cleaned.xlsx**        | Cleaned version of the hospital dataset after data preparation.                                                                         |
| **hospital_final_dataset.xlsx**  | Final dataset prepared for analytical and dashboard development.                                                                        |
| **medtrack_dashboard_v1.pbix**   | Earlier/versioned Power BI dashboard implementation.                                                                                    |
| **medtrack_prototype.pbix**      | Prototype Power BI dashboard created during the development stage.                                                                      |

