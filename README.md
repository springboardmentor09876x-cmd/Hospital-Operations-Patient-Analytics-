# MedTrack_DV (Hospital Operations & Patient Analytics Dashboard)

MedTrack_DV is a comprehensive healthcare operational analytics suite. It processes raw patient admission records and hospital metrics, engineers key performance indicators (KPIs), and structures interactive Tableau dashboards to provide actionable insights for hospital administrators.

---

## 📂 Project Directory Structure

Following the project delivery guidelines, the repository is organized into distinct functional folders:

```text
Hospital-Operations-Patient-Analytics/
│
├── data/                      # Contains all raw and generated datasets
│   ├── Hospital_Dataset.xlsx
│   ├── Patient_Dataset.xlsx
│   ├── Hospital_RawDataset_Updated.xlsx
│   ├── hospital_raw_data.csv  # Merged raw datasets (Milestone 1)
│   ├── hospital_cleaned.csv   # Cleaned data (Milestone 1)
│   ├── hospital_final_dataset.csv
│   └── hospital_final_dataset.xlsx # Tableau-ready dataset with KPIs (Milestone 2)
│
├── scripts/                   # Data pipeline, cleaning & compiling scripts
│   ├── data_collection.py     # Script to load raw data
│   ├── data_collection.ipynb
│   ├── hospital_cleaning.ipynb # Notebook for cleaning & normalization
│   ├── generate_hospital_kpis.py # Script to calculate KPIs
│   ├── generate_storyboard.py  # Script to build layout PDF
│   └── build_tableau_workbook.py # Script to package twbx workbooks
│
├── dashboard/                 # Tableau packaged workbooks and layout assets
│   ├── medtrack_dashboard_v1.twbx # Tableau dashboard (Milestone 3 Module 5)
│   ├── MedTrack_DV.twbx       # Integrated Tableau dashboard (Milestone 3 Module 6)
│   └── dashboard_storyboard.pdf # Visual wireframe design storyboard
│
├── docs/                      # Technical guides, testing reports & QA checklists
│   ├── tableau_guide.md       # Interactive dashboard setup guide
│   ├── QA_Checklist.md        # QA test cases (Milestone 4 Module 7)
│   ├── Dashboard_Testing_Report.md # QA test results (Milestone 4 Module 7)
│   └── Final_Documentation.md  # Final documentation (Milestone 4 Module 8)
│
└── README.md                  # Project landing page
```

---

## 🛠️ Data Pipeline & Execution Guide

To run the pipeline and regenerate the project deliverables from scratch, execute the following commands in order:

### 1. Data Collection
Verify raw data load and column mapping:
```bash
python scripts/data_collection.py
```

### 2. KPI Engineering
Calculate admissions counts, occupancy, bed utilization, and department efficiency scores:
```bash
python scripts/generate_hospital_kpis.py
```

### 3. Generate Visual Storyboard
Compile layout wireframes into a multi-page PDF:
```bash
python scripts/generate_storyboard.py
```

### 4. Compile Tableau packaged workbooks (.twbx)
Pack the Tableau workbooks and link them to the Excel dataset:
```bash
python scripts/build_tableau_workbook.py
```

---

## 📊 Tableau Dashboard Suite

The generated dashboard package **[MedTrack_DV.twbx](file:///C:/Users/shrut/.gemini/antigravity/scratch/Hospital-Operations-Patient-Analytics-/dashboard/MedTrack_DV.twbx)** includes four interactive dashboards:
1. **Hospital Overview**: High-level trends on patient volume and occupancy rates.
2. **Patient Flow**: Tracking of admissions, discharges, stay categories, and peak load hours.
3. **Department Analytics**: Benchmarking clinical departments by composite Efficiency Scores.
4. **Resource Utilization**: Bed utilization heatmaps and staff allocation grids.

*Refer to the [Tableau Construction Guide](docs/tableau_guide.md) for detailed sheet-by-sheet configuration.*