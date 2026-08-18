# MedTrack_DV - Hospital Operations & Patient Analytics Dashboard

MedTrack_DV is an end-to-end healthcare analytics and operational intelligence solution designed to transform complex hospital and patient data into actionable insights. The project integrates data engineering workflows with interactive Power BI dashboards to monitor hospital performance, analyze patient flow, track department efficiency, and optimize resource allocation.

---

## 📌 Project Overview

Modern healthcare facilities generate vast amounts of operational data across admissions, department transfers, resource allocations, and patient management. MedTrack_DV unifies these disparate data points into a cohesive analytical dataset of ~10,000 patient records and delivers a multi-dashboard monitoring suite for hospital administrators, department heads, and clinical planners.

### Key Focus Areas
- **Admissions & Patient Flow:** Tracking intake volumes, discharge dynamics, transfer rates, and length of stay (LOS).
- **Hospital Performance Monitoring:** High-level executive KPIs across admissions, readmissions, and bed occupancy.
- **Department Analytics:** Department-level patient load, efficiency scores, and capacity utilization.
- **Resource Utilization:** Bed occupancy, ICU bed availability, medical equipment status, and staff allocation.

---

## 📊 Dashboard Suite Architecture

The Power BI dashboard suite consists of four interconnected dashboards with cross-filtering, global slicing, and seamless inter-dashboard navigation:

| Dashboard | Core Focus & Analytical Scope |
| :--- | :--- |
| **1. Hospital Overview** | Macro-level operational metrics, Top 5 hospitals by volume, Bed Occupancy Rate, Readmission Rates, and Monthly Admission/Discharge trends. |
| **2. Patient Flow** | Micro-level patient movement, Average Length of Stay (overall & by department), peak daily admission monitoring, and transfer rate analysis. |
| **3. Department Analytics** | Department-level efficiency scores, patient volume distributions, department readmission rates, and treatment capacity analysis. |
| **4. Resource Utilization** | Bed and ICU occupancy, staff allocation vs. utilization, equipment operational status (available, in-use, maintenance), and capacity forecasting. |

---

## 🛠️ Tech Stack & Tools

- **Data Processing & KPI Engineering:** Python, Pandas, Jupyter Notebook
- **Business Intelligence & Visualization:** Power BI Desktop
- **Version Control & Collaboration:** Git & GitHub

---

## 📁 Repository Structure

```text
├── dashboard/               # Power BI report files (.pbix) and dashboard assets
├── data/                    # Raw, cleaned, and processed analytical datasets
├── docs/                    # Final Dashboard Report, Testing & QA Documentation
├── scripts/                 # Python/Jupyter scripts for data cleaning, ETL, and KPI validation
└── README.md                # Project documentation and summary
