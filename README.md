# MedTrack_DV — Hospital Operations & Patient Analytics Dashboard

## Project Overview

**MedTrack_DV** is a hospital operations and patient analytics dashboard project developed to transform hospital operational and patient-related data into interactive Tableau dashboards.

The project focuses on hospital performance, patient admissions, patient flow, department efficiency, and healthcare resource utilization. The final solution brings the analysis together in a unified Tableau workbook for exploring operational trends and supporting data-driven decision-making.

## Project Objectives

- Analyze hospital admissions and patient activity.
- Monitor hospital performance using healthcare KPIs.
- Analyze patient admission, discharge, movement, and stay patterns.
- Compare department-level performance.
- Analyze hospital resource utilization.
- Provide interactive filters and dashboard navigation.
- Integrate four related Tableau dashboards into a single workbook.
- Provide a structured data-processing and dashboard workflow.

## Project Workflow

```text
Hospital Data Collection
        ↓
Data Cleaning & Transformation
        ↓
KPI Engineering
        ↓
Dashboard Planning & Prototyping
        ↓
Dashboard Development
        ↓
Dashboard Integration
        ↓
Testing & Validation
        ↓
Documentation & Delivery
```

# Milestone 1 — Data Collection & Preparation

## Module 1: Hospital Data Collection

Publicly available hospital-related datasets were collected and integrated for hospital operations analysis.

### Deliverables

```text
data/neelima-hospital_raw_data.csv
scripts/neelima-data_collection.py
```

The source datasets used during preparation were used as working/reference inputs and are not part of the milestone deliverables.

## Module 2: Data Cleaning & Transformation

The collected data was cleaned and transformed into a Tableau-ready dataset.

### Deliverables

```text
data/neelima-hospital_cleaned.csv
notebooks/neelima-hospital_cleaning.ipynb
```

The cleaning workflow prepares the data for KPI engineering and dashboard development.

# Milestone 2 — KPI Engineering & Dashboard Planning

## Module 3: Hospital KPI Engineering

KPI generation is implemented in:

```text
scripts/neelima-generate_hospital_kpis.py
```

Final Tableau-ready dataset:

```text
data/neelima-hospital_final_dataset.xlsx
```

### KPIs

1. Total Admissions
2. Occupancy Rate
3. Average Length of Stay
4. Readmission Rate
5. Bed Utilization Rate
6. Department Efficiency Score

An additional **Staff Utilization Rate** KPI was also generated and used in the project.

## Module 4: Dashboard Planning & Prototyping

The dashboard planning stage defined the layout and interaction approach for:

1. Hospital Overview
2. Patient Flow
3. Department Analytics
4. Resource Utilization

### Deliverables

```text
dashboard/module4/
├── dashboard_storyboard.pdf
└── medtrack_prototype.twbx
```

The planning covers layouts, filters, navigation, dashboard actions, parameter interaction, and department comparisons.

# Milestone 3 — Dashboard Development

## Module 5: Hospital Overview & Patient Flow

### Hospital Overview

Includes:

- Admissions overview
- Hospital performance KPIs
- Occupancy monitoring
- Readmission analysis
- Monthly operational/patient trends
- Patient-load analysis
- State-based analysis
- Department-based analysis

### Patient Flow

Includes:

- Admission trends
- Discharge tracking
- Patient movement analysis
- Patient transfer analysis
- Average stay analysis
- Patient-load/peak-load analysis

### Deliverable

```text
dashboard/module5/
└── medtrack_dashboard_v1.twbx
```

## Module 6: Department Analytics & Resource Utilization

### Department Analytics

Includes:

- Department performance analysis
- Patient volume by department
- Readmission by department
- Department efficiency comparison
- Treatment capacity analysis
- Department-level stay and transfer analysis

### Resource Utilization

Includes:

- Bed utilization analysis
- Staff utilization/allocation analysis
- Equipment utilization tracking
- Capacity planning insights
- Resource availability analysis

### Dashboard Integration

The final dashboard suite includes:

- Global State filtering
- Global Department filtering
- Dashboard navigation
- Dashboard actions
- Department parameter action
- Dashboard linking

### Deliverable

```text
dashboard/module6/
└── MedTrack_DV.twbx
```

# Dashboard Suite

```text
Hospital Overview
       │
       ├── Patient Flow
       ├── Department Analytics
       └── Resource Utilization
```

## Interactive Features

### Global Filters

**State:** Allows analysis to be viewed for different states.

**Department:** Allows analysis to be focused on individual departments.

### Navigation

Navigation controls allow users to move between dashboard views within the final workbook.

### Parameter Action

A Department Parameter Action is implemented. A department selection is passed into a Tableau parameter and used for dashboard interaction.

# KPI Definitions

| KPI | Description |
|---|---|
| Total Admissions | Total number of admissions represented in the hospital dataset. |
| Occupancy Rate | Measures hospital occupancy based on the available patient and bed information. |
| Average Length of Stay | Average duration of patient stay. |
| Readmission Rate | Measures the proportion of patients represented as readmissions. |
| Bed Utilization Rate | Measures the utilization of available hospital beds. |
| Department Efficiency Score | Measures department-level operational efficiency using the project KPI calculation. |
| Staff Utilization Rate | Additional KPI used to analyze staff utilization. |

KPI calculations are implemented in:

```text
scripts/neelima-generate_hospital_kpis.py
```

# Healthcare Operations Methodology

1. **Data Collection** — Hospital operational and patient-related datasets were collected and integrated.
2. **Data Cleaning** — The collected data was cleaned and transformed into a consistent structure.
3. **KPI Engineering** — Healthcare operational KPIs were calculated using Python and stored in the final dataset.
4. **Dashboard Planning** — Dashboard layouts, filters, navigation, and actions were planned.
5. **Dashboard Development** — Four analytical dashboard areas were developed in Tableau.
6. **Dashboard Integration** — The dashboards were combined into one workbook with filters, navigation, parameter actions, and linking.
7. **Testing & Validation** — The final workbook was reviewed for KPI calculations, dashboard functionality, filters, navigation, parameter actions, patient-flow analytics, and integration.
8. **Documentation & Delivery** — Final project files and documentation were organized for delivery.

# Module 7 — Testing & Validation

Module 7 documentation is available in:

```text
docs/
└── testing/
    ├── QA_Checklist.pdf
    └── Dashboard_Testing_Report.pdf
```

Testing covered:

- KPI calculations
- Healthcare operational metrics
- Hospital Overview
- Patient Flow
- Department Analytics
- Resource Utilization
- Global filters
- Dashboard navigation
- Parameter actions
- Dashboard integration
- Visual and usability review

The final testing review identified no major dashboard functionality issue.

# Project Structure

```text
Hospital-Operations-Patient-Analytics-
│
├── README.md
│
├── data/
│   ├── neelima-hospital_raw_data.csv
│   ├── neelima-hospital_cleaned.csv
│   └── neelima-hospital_final_dataset.xlsx
│
├── dashboard/
│   ├── module4/
│   │   ├── dashboard_storyboard.pdf
│   │   └── medtrack_prototype.twbx
│   │
│   ├── module5/
│   │   └── medtrack_dashboard_v1.twbx
│   │
│   └── module6/
│       └── MedTrack_DV.twbx
│
├── docs/
│   └── testing/
│       ├── QA_Checklist.pdf
│       └── Dashboard_Testing_Report.pdf
│
├── notebooks/
│   └── neelima-hospital_cleaning.ipynb
│
└── scripts/
    ├── neelima-data_collection.py
    └── neelima-generate_hospital_kpis.py
```

The `data/raw_sources/` and `data/reference/` directories contain working/source/reference files used during project preparation and are not listed as milestone deliverables.

# Tools & Technologies

| Area | Technology |
|---|---|
| Data Collection | Python |
| Data Processing | Pandas, NumPy |
| Data Cleaning | Python, Jupyter Notebook |
| KPI Engineering | Python |
| Visualization | Tableau |
| Dashboard Integration | Tableau Filters, Parameters, Actions |
| Documentation | Markdown, PDF |
| Version Control | Git & GitHub |

# Final Deliverables

## Module 4

```text
dashboard/module4/
├── dashboard_storyboard.pdf
└── medtrack_prototype.twbx
```

## Module 5

```text
dashboard/module5/
└── medtrack_dashboard_v1.twbx
```

## Module 6

```text
dashboard/module6/
└── MedTrack_DV.twbx
```

## Module 7

```text
docs/testing/
├── QA_Checklist.pdf
└── Dashboard_Testing_Report.pdf
```

## Module 8

```text
README.md
```

The README serves as the final project documentation covering dataset sources, KPI definitions, dashboard guide, healthcare operations methodology, project structure, tools, workflow, and delivery information.

# Final Tableau Workbook

The final integrated Tableau workbook is:

```text
dashboard/module6/MedTrack_DV.twbx
```

It contains the complete four-dashboard MedTrack_DV suite and its implemented integration features.

# GitHub Repository

**Repository:**  
https://github.com/springboardmentor09876x-cmd/Hospital-Operations-Patient-Analytics-

**Development/Submission Branch:** `neelima`

The project deliverables are maintained in the `neelima` branch of the repository.

# Tableau Public

Tableau Public deployment is **optional** for this project. The final workbook is provided as the required `.twbx` deliverable.

# Project Completion Status

| Milestone | Modules | Status |
|---|---|---|
| Milestone 1 — Data Collection & Preparation | Modules 1–2 | Completed |
| Milestone 2 — KPI Engineering & Dashboard Planning | Modules 3–4 | Completed |
| Milestone 3 — Dashboard Development | Modules 5–6 | Completed |
| Milestone 4 — Testing, Documentation & Delivery | Modules 7–8 | Completed |

# Final Project Outcome

The completed MedTrack_DV project provides a unified Tableau dashboard suite for hospital operations and patient analytics. It combines hospital performance KPIs, patient-flow analysis, department analytics, and resource utilization into an integrated interactive dashboard solution.
