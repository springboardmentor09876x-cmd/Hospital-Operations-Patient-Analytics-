# 🏥 MedTrack_DV - Hospital Operations & Patient Analytics Dashboard

A comprehensive **Hospital Operations & Patient Analytics Dashboard** built using **Tableau, Python, Pandas, NumPy, Jupyter Notebook, and Microsoft Excel** to analyze hospital performance, patient flow, departmental efficiency, and resource utilization.

The project transforms raw healthcare datasets into a structured analytical dataset through data collection, data cleaning, KPI engineering, and Tableau visualization. The final solution consists of **four interactive Tableau dashboards** designed for hospital management and operational analysis.

---

# 📌 Project Overview

**MedTrack_DV** is an interactive healthcare analytics project designed to help hospital administrators and decision-makers monitor important operational metrics and identify patterns in:

* Hospital performance
* Patient admissions and flow
* Department workload
* Patient outcomes
* Staffing efficiency
* Bed utilization
* ICU utilization
* Equipment distribution
* Resource availability

The project follows a complete data analytics workflow:

**Raw Data → Data Cleaning → Data Transformation → KPI Engineering → Visualization → Interactive Dashboard**

The final Tableau workbook contains four major analytical modules:

1. **Hospital Overview**
2. **Patient Flow**
3. **Department Analytics**
4. **Resource Utilization**

---

# 🎯 Problem Statement

Hospitals generate large amounts of operational and patient-related data. Without an effective analytical system, it can be difficult to monitor hospital performance, understand patient demand, evaluate departmental workload, and identify resource-utilization patterns.

The objective of this project is to transform hospital data into an interactive visual analytics solution that enables users to:

* Monitor overall hospital performance
* Analyze admission patterns
* Understand patient flow
* Evaluate departmental efficiency
* Analyze patient outcomes
* Monitor bed and ICU utilization
* Compare hospital resource availability
* Analyze staffing levels
* Support data-driven operational decisions

---

# 🎯 Project Objectives

The major objectives of the project are:

* Analyze hospital admissions
* Monitor hospital occupancy
* Evaluate ICU utilization
* Analyze patient flow
* Understand patient outcomes
* Identify common medical conditions
* Evaluate departmental workload
* Analyze staffing efficiency
* Monitor bed availability
* Compare ICU capacity across hospitals
* Analyze equipment distribution
* Build interactive dashboards for hospital management
* Provide a centralized analytical view of hospital operations

---

# 📊 Dashboard Modules

## 1️⃣ Hospital Overview

The **Hospital Overview** dashboard provides a high-level summary of hospital performance.

It is designed to answer:

> **How are the hospitals performing overall?**

### KPIs

* Total Hospitals
* Total Admissions
* Occupancy Rate
* Average Length of Stay
* Readmission Rate
* ICU Utilization

### Visualizations

* Admissions by Hospital
* Monthly Admission Trend
* State-wise Admissions
* Hospital Type Distribution
* Occupancy Rate by Hospital

---

## 2️⃣ Patient Flow

The **Patient Flow** dashboard focuses on patient characteristics, admission patterns, length of stay, medical conditions, and patient outcomes.

It is designed to answer:

> **Who are the patients, how are they being admitted, and what are their outcomes?**

### KPIs

* Total Patients
* Average Length of Stay
* Emergency Admissions
* Weekend Admissions
* High Risk Patients
* Recovery Rate

### Visualizations

* Age Group Distribution
* Length of Stay Category
* Top Medical Conditions
* Admissions by Day of Week
* Patient Outcome

---

## 3️⃣ Department Analytics

The **Department Analytics** dashboard evaluates departmental workload, staffing, productivity, length of stay, and readmission performance.

It is designed to answer:

> **Which departments handle the greatest workload and how efficiently are their resources being utilized?**

### KPIs

* Total Departments
* Department Admissions
* Patients per Nurse
* Patients per Staff
* Average Length of Stay
* Total Doctors

### Visualizations

* Admissions by Department
* Patients per Nurse by Department
* Doctor Productivity
* Average Length of Stay by Department
* Readmission Rate by Department

---

## 4️⃣ Resource Utilization

The **Resource Utilization** dashboard focuses on hospital infrastructure and resource capacity.

It is designed to answer:

> **Are hospital resources being utilized efficiently, and where is additional capacity required?**

### KPIs

* Total Beds
* ICU Beds
* Bed Utilization
* ICU Utilization
* Beds Available
* Equipment Types

### Visualizations

* Beds Available vs Occupied by Hospital
* ICU Beds by Hospital
* ICU Utilization by Hospital
* Staff Count by Department
* Equipment Distribution

---

# 📌 Why These KPIs Were Used

The KPIs were selected to provide an immediate summary of the most important operational indicators for each analytical area.

## Hospital Overview KPIs

### Total Hospitals

Shows the number of hospitals included in the analysis. It establishes the scope of the hospital network being evaluated.

### Total Admissions

Measures the overall number of patient admissions and provides an indication of the scale of patient activity.

### Occupancy Rate

Measures how effectively hospital bed capacity is being utilized. It helps identify whether hospitals are operating with relatively low, moderate, or high bed utilization.

### Average Length of Stay

Measures the average number of days patients remain hospitalized. It helps evaluate patient throughput and operational efficiency.

### Readmission Rate

Measures the proportion of patients who return for another admission. It can help identify departments or hospitals that may require further investigation into treatment outcomes and post-discharge care.

### ICU Utilization

Measures the utilization of intensive-care resources and provides an indication of critical-care demand.

---

# 📌 Patient Flow KPI Rationale

### Total Patients

Shows the overall patient population represented in the dataset and provides the foundation for patient-flow analysis.

### Average Length of Stay

Helps understand how long patients typically remain in the hospital and provides an indication of patient throughput.

### Emergency Admissions

Measures emergency admission volume and helps identify the demand placed on emergency-care services.

### Weekend Admissions

Shows the number of admissions occurring during weekends and helps identify differences in admission patterns across the week.

### High Risk Patients

Shows the number of patients classified as high risk and provides an indication of patients who may require greater monitoring or clinical attention.

### Recovery Rate

Provides a high-level view of successful patient recovery and helps evaluate overall patient outcomes.

---

# 📌 Department Analytics KPI Rationale

### Total Departments

Shows the number of departments included in the analysis and establishes the scope of departmental comparison.

### Department Admissions

Measures the number of admissions handled by departments and identifies departments with higher patient workloads.

### Patients per Nurse

Measures the average patient workload associated with nursing resources. It helps identify departments with relatively higher or lower nursing workloads.

### Patients per Staff

Measures the patient workload relative to available staff and provides an indication of staffing pressure.

### Average Length of Stay

Shows the average duration of hospitalization for patients within departments and helps identify departments with longer patient stays.

### Total Doctors

Shows the number of doctors across departments and provides an overview of medical staffing capacity.

---

# 📌 Resource Utilization KPI Rationale

### Total Beds

Shows the overall hospital bed capacity available across the hospitals.

### ICU Beds

Shows the total number of ICU beds and provides an indication of critical-care capacity.

### Bed Utilization

Measures how much of the available bed capacity is being utilized.

### ICU Utilization

Measures ICU resource utilization and helps identify differences in critical-care demand.

### Beds Available

Shows the available bed capacity and provides an indication of remaining hospital capacity.

### Equipment Types

Shows the number of equipment categories represented in the analysis and provides an overview of the equipment resources being tracked.

---

# 📈 Why These Charts Were Used

Different visualization types were selected according to the analytical purpose of each chart.

The goal was not simply to display the data, but to choose a chart that makes the intended comparison, trend, distribution, or relationship easy to understand.

---

## 🏥 Hospital Overview Visualizations

### Admissions by Hospital — Horizontal Bar Chart

A horizontal bar chart is used because multiple hospitals need to be compared.

It allows users to:

* Rank hospitals by admission volume
* Identify hospitals with the highest admissions
* Compare hospitals quickly
* Read long hospital names more easily

Horizontal bars are particularly suitable because hospital names can be lengthy.

### Monthly Admission Trend — Line Chart

A line chart is used to represent admissions over time.

It allows users to identify:

* Increasing admission trends
* Decreasing admission trends
* Monthly fluctuations
* Possible seasonal patterns
* Changes in patient demand over time

A line chart is appropriate because time is continuous and trends are more important than individual category comparisons.

### State-wise Admissions — Map

A geographic map is used because the visualization involves state-level admission data.

The map provides geographical context and allows users to identify areas with relatively higher or lower admission activity.

### Hospital Type Distribution — Donut Chart

A donut chart is used to show the composition of hospital types.

For example, it allows users to quickly compare:

* Government hospitals
* Private hospitals

The visualization is appropriate for a simple part-to-whole relationship.

### Occupancy Rate by Hospital — Horizontal Bar Chart

A horizontal bar chart is used to compare occupancy rates across hospitals.

It allows users to quickly identify:

* Hospitals with higher occupancy
* Hospitals with lower occupancy
* Differences in bed utilization between hospitals

---

# 👥 Patient Flow Visualizations

### Age Group Distribution — Horizontal Bar Chart

A horizontal bar chart is used to compare patient counts across age groups.

It helps identify which age groups represent the largest patient populations.

### Length of Stay Category — Horizontal Bar Chart

The chart compares patients across different length-of-stay categories:

* Short Stay
* Medium Stay
* Long Stay
* Extended Stay

This makes it easier to understand how hospitalization duration is distributed across the patient population.

### Top Medical Conditions — Horizontal Bar Chart

A horizontal bar chart is used to rank medical conditions according to patient count.

It helps identify the medical conditions contributing most significantly to the patient workload.

### Admissions by Day of Week — Column Chart

A column chart is used to compare admission volumes across the days of the week.

It makes differences between individual days easy to identify and helps reveal weekday and weekend admission patterns.

### Patient Outcome — Bar Chart

A bar chart is used to compare patient outcomes such as:

* Discharge
* Expiry
* Dama

The difference in bar lengths allows users to quickly understand the relative frequency of each outcome.

---

# 🏢 Department Analytics Visualizations

### Admissions by Department — Horizontal Bar Chart

A horizontal bar chart ranks departments according to admission volume.

It helps identify departments with the highest patient workload and allows quick comparison between departments.

### Patients per Nurse by Department — Horizontal Bar Chart

This chart compares the patient-to-nurse workload across departments.

It helps identify departments where nurses are managing relatively higher patient loads.

### Doctor Productivity — Scatter Plot

A scatter plot is used to examine relationships between doctor-related productivity measures and patient workload.

It helps identify:

* Patterns
* Clusters
* Variations
* Departments that behave differently from the overall distribution

A scatter plot is useful when the objective is to examine relationships rather than simply rank categories.

### Average Length of Stay by Department — Horizontal Bar Chart

A horizontal bar chart is used to compare average length of stay between departments.

It helps identify departments where patients tend to remain hospitalized for longer periods.

### Readmission Rate by Department — Horizontal Bar Chart

A horizontal bar chart allows readmission rates to be compared across departments.

It helps identify departments with relatively higher or lower readmission rates.

---

# 🛏️ Resource Utilization Visualizations

### Beds Available vs Occupied by Hospital — Stacked Bar Chart

A stacked bar chart is used to compare occupied and available beds for each hospital.

This visualization allows users to see:

* Total bed capacity
* Occupied beds
* Available beds
* Differences in capacity between hospitals

The stacked structure allows multiple components of total capacity to be viewed together.

### ICU Beds by Hospital — Horizontal Bar Chart

A horizontal bar chart ranks hospitals based on ICU bed capacity.

It helps identify hospitals with greater critical-care infrastructure.

### ICU Utilization by Hospital — Horizontal Bar Chart

This chart compares ICU utilization across hospitals.

It helps identify hospitals experiencing relatively higher or lower demand for ICU resources.

### Staff Count by Department — Horizontal Bar Chart

A horizontal bar chart compares staffing levels across departments.

It helps identify departments with larger or smaller staffing capacity.

### Equipment Distribution — Horizontal Bar Chart

The chart ranks equipment categories according to their quantity.

It provides a clear overview of equipment distribution and helps identify resources that are available in relatively larger or smaller quantities.

---

# 📊 Overall Visualization Design Rationale

| Visualization            | Purpose                                                           |
| ------------------------ | ----------------------------------------------------------------- |
| **KPI Cards**            | Provide an immediate summary of important performance indicators  |
| **Horizontal Bar Chart** | Compare and rank hospitals, departments, conditions, or resources |
| **Line Chart**           | Analyze trends and changes over time                              |
| **Map**                  | Show geographic distribution                                      |
| **Donut Chart**          | Show simple part-to-whole distributions                           |
| **Column Chart**         | Compare values across discrete categories                         |
| **Scatter Plot**         | Examine relationships, patterns, and variations between measures  |
| **Stacked Bar Chart**    | Compare multiple components within a total                        |

The combination of these visualization types provides both **high-level monitoring** through KPI cards and **detailed analytical exploration** through charts.

---

# 🛠️ Technologies Used

### Data Processing

* Python
* Pandas
* NumPy

### Data Analysis

* Jupyter Notebook
* Python-based KPI engineering
* Excel

### Data Visualization

* Tableau Desktop

### Data Storage

* Microsoft Excel

---

# 📂 Dataset Information

The project uses multiple healthcare datasets covering hospital, patient, and departmental information.

### Raw Datasets

* `patient_admissions.xlsx`
* `hospital_info.xlsx`
* `department_resources.xlsx`

These datasets contain information used to analyze:

* Patient admissions
* Hospital information
* Hospital resources
* Departments
* Staffing
* Beds
* ICU capacity
* Equipment
* Patient outcomes

---

# 🔄 Data Processing Workflow

The project follows the following analytical workflow:

```text
Raw Healthcare Data
        ↓
Data Collection
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
Dataset Integration
        ↓
KPI Engineering
        ↓
Final Analytical Dataset
        ↓
Tableau Visualization
        ↓
Interactive Dashboards
```

### Step 1 — Data Collection

The required healthcare datasets were collected and organized into separate Excel files.

### Step 2 — Data Cleaning

The datasets were inspected and cleaned to improve consistency and prepare them for analysis.

Typical preparation activities included:

* Handling inconsistent values
* Standardizing fields
* Preparing categorical variables
* Validating numerical fields
* Preparing datasets for integration

### Step 3 — Data Transformation

Relevant datasets were transformed into an analytical structure suitable for Tableau.

### Step 4 — KPI Engineering

Important operational KPIs were calculated to support hospital, patient, department, and resource analysis.

### Step 5 — Tableau Visualization

The final analytical dataset was connected to Tableau and used to create individual worksheets and dashboards.

### Step 6 — Dashboard Development

The worksheets were arranged into four interactive dashboards with:

* Navigation buttons
* KPI cards
* Filters
* Charts
* Dashboard-level interactions

---

# 📈 KPIs Created

The project includes the following major KPIs:

* Total Hospitals
* Total Patients
* Total Admissions
* Total Departments
* Total Doctors
* Total Beds
* ICU Beds
* Occupancy Rate
* ICU Utilization
* Recovery Rate
* Readmission Rate
* Average Length of Stay
* Patients per Nurse
* Patients per Staff
* Bed Availability

---

# 🎛️ Dashboard Interactivity

The dashboards include interactive features to support data exploration.

### Navigation

Users can navigate between the four analytical modules:

**Hospital Overview → Patient Flow → Department Analytics → Resource Utilization**

### Filters

Depending on the dashboard, users can filter the analysis using dimensions such as:

* Date Range
* Hospital
* State
* Department
* Gender
* Age Group
* Hospital Type

Filters allow users to move from an overall view to a more focused analysis.

---

# 📊 Dashboard Navigation Structure

```text
                    MedTrack_DV
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
Hospital Overview   Patient Flow   Department Analytics
        │                │                │
        └────────────────┼────────────────┘
                         │
                         ▼
                Resource Utilization
```

The navigation design allows users to move between different operational perspectives without leaving the Tableau workbook.

---

# 📁 Project Structure

```text
MedTrack_DV/
│
├── dashboard/
│   ├── dashboard_storyboard.pdf
│   └── medtrack_prototype.twb
│
├── data/
│   ├── hospital_cleaned.xlsx
│   ├── hospital_final_dataset.xlsx
│   └── hospital_raw_data.xlsx
│
├── docs/
│   └── README.md
│
├── notebooks/
│   ├── data_collection.ipynb
│   ├── hospital_cleaning.ipynb
│   └── kpi_engineering.ipynb
│
├── raw-dataset/
│   ├── department_resources.xlsx
│   ├── hospital_info.xlsx
│   └── patient_admissions.xlsx
│
├── scripts/
│   └── generate_hospital_kpis.py
│
└── screenshots/
    ├── dashboard1.png
    ├── dashboard2.png
    ├── dashboard3.png
    └── dashboard4.png
```

---

# 📷 Dashboard Screenshots

## 🏥 Hospital Overview

![Hospital Overview](screenshots/dashboard1.png)

The Hospital Overview dashboard provides a consolidated view of hospital admissions, occupancy, hospital type, geographic distribution, and admission trends.

---

## 👥 Patient Flow

![Patient Flow](screenshots/dashboard2.png)

The Patient Flow dashboard focuses on patient demographics, length of stay, medical conditions, admission patterns, and patient outcomes.

---

## 🏢 Department Analytics

![Department Analytics](screenshots/dashboard3.png)

The Department Analytics dashboard evaluates department-level admissions, staffing ratios, doctor productivity, length of stay, and readmission rates.

---

## 🛏️ Resource Utilization

![Resource Utilization](screenshots/dashboard4.png)

The Resource Utilization dashboard analyzes beds, ICU capacity, ICU utilization, staffing, and equipment distribution.

---

# 🔍 Key Insights

The dashboards provide several operational insights, including:

* Cardiology recorded the highest number of patient admissions among the analyzed departments.
* Occupancy rates remained relatively high across most hospitals.
* Readmission rates varied between departments.
* ICU utilization differed across hospitals, highlighting differences in critical-care demand.
* Patient workload varied significantly between departments.
* Bed availability differed between hospitals.
* Hospital resources such as beds, staff, ICU capacity, and equipment were distributed differently across facilities.
* Patient admission volumes varied across days and over time.
* Medical conditions contributed differently to overall patient workload.
* Patient length of stay varied across departments and patient categories.

> **Note:** These insights are descriptive observations from the analyzed dataset and should not be interpreted as clinical recommendations.

---

# 🚀 Future Enhancements

The project can be extended with additional analytical capabilities.

### Real-Time Data Integration

Integrate live hospital information systems to provide continuously updated dashboards.

### Predictive Analytics

Use machine learning models to predict future hospital demand and patient outcomes.

### Patient Readmission Prediction

Develop a machine learning model to identify patients who may have a higher probability of readmission.

### Doctor Performance Forecasting

Analyze historical workload and productivity patterns to support future staffing and resource planning.

### Bed Demand Forecasting

Predict future bed requirements using historical admission and occupancy trends.

### Automated Reporting

Generate automated hospital performance reports at regular intervals.

### Advanced Alerts

Introduce alerts for:

* High occupancy
* High ICU utilization
* Low bed availability
* High departmental workload
* Unusual admission patterns

---

# ▶️ How to Open the Project

## Prerequisites

The following software is required:

* Tableau Desktop
* Python
* Jupyter Notebook
* Microsoft Excel

## Opening the Tableau Workbook

1. Clone or download the project repository.
2. Open the `dashboard` folder.
3. Open the Tableau workbook:
   `medtrack_prototype.twb`
4. Allow Tableau to access the required Excel data sources if prompted.
5. Navigate through the four dashboards using the built-in navigation buttons.
6. Use the available filters to explore the data.

---

# 🐍 Running the Python Components

The Python components are included for data processing and KPI engineering.

The notebooks can be opened using Jupyter Notebook or JupyterLab.

### Notebook Workflow

```text
data_collection.ipynb
        ↓
hospital_cleaning.ipynb
        ↓
kpi_engineering.ipynb
        ↓
Final Analytical Dataset
        ↓
Tableau Dashboard
```

The Python script is available under:

```text
scripts/generate_hospital_kpis.py
```

---

# 📚 Documentation

The project includes a Tableau dashboard storyboard:

```text
dashboard/dashboard_storyboard.pdf
```

The storyboard provides the planned dashboard structure and visualization layout used during dashboard development.

---

# 📌 Project Highlights

### Data Analytics

* Healthcare data analysis
* Data cleaning
* Data transformation
* KPI engineering
* Descriptive analytics

### Tableau

* Four interactive dashboards
* KPI cards
* Interactive filters
* Dashboard navigation
* Multiple visualization techniques
* Hospital-level analysis
* Department-level analysis
* Patient-level analysis
* Resource-level analysis

### Python

* Data processing
* Data cleaning
* KPI calculations
* Analytical dataset preparation

---

# 🎓 Skills Demonstrated

This project demonstrates practical experience in:

* Data Cleaning
* Data Transformation
* Exploratory Data Analysis
* KPI Engineering
* Data Visualization
* Tableau Dashboard Development
* Dashboard Design
* Interactive Filtering
* Data Storytelling
* Healthcare Analytics
* Python
* Pandas
* NumPy
* Excel
* Jupyter Notebook

---

# 👨‍💻 Author

**Hariharan A**

B.Tech Computer Science Engineering
**AI & Data Science**

**Areas of Interest**

* Data Analytics
* Tableau
* Python
* SQL
* Excel
* Data Visualization
* Business Intelligence

---

# ⭐ Project Summary

**MedTrack_DV** demonstrates an end-to-end data analytics workflow for hospital operations, beginning with raw healthcare datasets and progressing through data cleaning, transformation, KPI engineering, and interactive Tableau visualization.

The four dashboards provide complementary perspectives:

| Dashboard                | Primary Focus                                     |
| ------------------------ | ------------------------------------------------- |
| **Hospital Overview**    | Overall hospital performance                      |
| **Patient Flow**         | Patient characteristics, admissions, and outcomes |
| **Department Analytics** | Department workload and efficiency                |
| **Resource Utilization** | Beds, ICU, staff, and equipment                   |

Together, these dashboards provide a centralized analytical view of hospital operations and demonstrate how healthcare data can be transformed into meaningful visual insights for operational analysis and decision support.

---

# ⭐ If you found this project useful, consider giving it a star!
