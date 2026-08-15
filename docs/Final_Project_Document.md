# 🏥 MedTrack_DV: Enterprise Hospital Operations Analytics
> **Module 8 Capstone Project Portfolio Asset: Comprehensive Data Engineering & Dashboard Integration Master Documentation**  
> Deployed on Windows 11 Framework | Built via Power BI Desktop & Jupyter Notebook ,python 3.11.5


![OS: Windows 11](https://shields.io)
![Platform: Power BI](https://shields.io)
![Engine: Python 3.11.5](https://shields.io)
![IDE: Jupyter Notebook](https://shields.io)
![Project Status: Completed](https://shields.io)

---

## 📂 1. Directory Tree & Delivery Architecture

To comply with standard enterprise deployment guidelines, all project assets must be structured into the following reproducible folder format on your local machine before deployment to GitHub:

```text
MedTrack_DV/
├── 📁 dashboard/
    |__medtrack_dashboard_v1.pbix 
    |__medtrack_prototype.pbix
│   └── 📊 MedTrack_DV_Dashboard.pbix    #Polished Power BI Desktop UI dashboard
├── 📁 data/
│   ├── 📄 hospital_raw_data.csv            # Uncleaned baseline transactional feed
│   ├── 📄 hospital_cleaned.csv             # Cleaned intermediate data sheet
│   └── 📁 hospital_final_dataset.xlsx      # Aligned analytics data layer for Power BI
├── 📁 docs/
│   ├── 📝 Final_Project_Documentation.md   # Core portfolio asset
│   └── 📋 MedTrack_DV_QA_Checklist.md      # Full 18-point verification matrix
     |__📋 Dashboard_Testing_Report.md
     |__dashboard_storyboard.pdf
└── 📁 scripts/
    ├── 📓 data_collection.py    # Initial data profhiling and quality scan
    |__📓 hospital_cleaning.ipynb
    └── 📓 generate_hospital_kpis.py      # Automated pandas calculation engine
```

---

## 🛠️ 2. Step 1: Data Ingestion & Data Cleansing Workflow

The raw dataset `hospital_raw_data.csv` initially contained several data anomalies, duplicate entries, and raw data parameters that would have caused layout distortion on the canvas. I resolved these inside **Jupyter Notebook using Python 3.11.5** via the following data cleaning pipeline:

### 2.1 Deduplication & Row Alignment
* **The Problem:** The raw data stream contained broken row formatting and record duplication.
* **How I Worked On It:** I isolated accidental separator breaks (`df = df[df["Hospital Name"].astype(str).str.strip() != "======="]`) and ran a programmatic deduplication scan: `df.drop_duplicates(keep='first', inplace=True)`. This locked our dataset footprint to exactly **10,000 unique patient encounters**.

### 2.2 Missing Value Strategy
* **The Problem:** Key analytics fields were fragmented, risking broken filtering loops.
* **How I Worked On It:** I computed the missing threshold weights across all variables: `missing_frac = df.isna().mean()`. Any sparse structural data columns containing **greater than 50% missing metrics were systematically dropped** (such as the raw text-based `Transfer_Date`). Continuous variables were imputed using the median value (`df[c].fillna(df[c].median())`) to ensure our model remained completely error-free.

### 2.3 Structural Standardization
* **How I Worked On It:** Standardized raw department names (`'Cardio'` converted to `'Cardiology'`, and `'Neuro'` to `'Neurology'`) to ensure that slicers map cleanly. I engineered a script-driven string formatter (`PAT00001`, `HOS001`) to auto-generate crisp Primary Keys (`Patient_ID`) and ForeignKey pointers (`Hospital_ID`) across rows.

---

## 📐 3. Step 2: Metric Calculations & KPI Engineering

Once the data schema was fully sanitized, I calculated the **8 core business performance metrics** required by the project specifications. To ensure the math inside Power BI matched our control records exactly, I pre-computed all metrics programmatically in Python:

### 📊 Deployed Project KPIs

#### 1. Total Admissions
* **Clinical Operation Basis:** Measures the baseline operational volume traffic flowing through the hospital network.
* **Calculation Workflow:** Engineered via `len(df)`. Tied this directly into a card component on the canvas and utilized the clear **`COUNT`** function to confirm a true total of **10K** admissions.

#### 2. Average Length of Stay (LOS)
* **Clinical Operation Basis:** Tracks the operational velocity of inpatient throughput. Lower stay averages highlight optimized discharge workflows.
* **Mathematical Formula:** 
  \[\text{Length of Stay (LOS)} = \text{Discharge Date} - \text{Admission Date}\]
  \[\text{Average Length of Stay} = \text{Round}(\text{Mean}(\text{LOS}), 2)\]
* **How I Worked On It:** Formatted admission and discharge strings into datetime components. To protect the dataset mean from extreme clinical outliers, I bounded the column via clipping constraints: `df["Length of Stay"].clip(lower=1, upper=30)`. Calculated the exact average mean at **20.40 days**.

#### 3. Readmission Rate
* **Clinical Operation Basis:** Monitors clinical outcome safety and quality control parameters post-discharge.
* **How I Worked On It:** Extracted values from the string-based field `Readmission` and translated them into binary integers (`Readmission_Flag` = `1` or `0`). Computed the true rate across the dataset via `df["Readmission_Flag"].mean()`, validating a core baseline of **50.0%** readmissions.

#### 4. Bed Occupancy Rate (Occupancy Rate)
* **Clinical Operation Basis:** Evaluates overall inpatient bed traffic loads to prevent emergency capacity overruns.
* **How I Worked On It:** Extracted row-level bed census columns and cross-references filled parameters against overall bed inventories, confirming a baseline average occupancy rate of **37.0%**.

#### 5. Utilization Rate
* **Clinical Operation Basis:** Provides a high-level operational view of global facility resource utilization.
* **How I Worked On It:** Summarized general hospital resource metrics across different facilities to isolate under-utilized sectors.

#### 6. Department Efficiency Score
* **Clinical Operation Basis:** Ranks healthcare delivery velocity across clinical wings.
* **Mathematical Formula:** 
  \[\text{Department Efficiency Score} = \text{Max}(100 - (\text{Mean}(\text{LOS}_{\text{Dept}}) / 60), 0)\]
  *An inverse relationship where a lower average stay duration corresponds directly to an elevated operational efficiency rating.*
* **How I Worked On It:** Processed department-level stay distributions in Pandas, handling outlier cases safely before embedding the structured inverse metrics into the final exported dataset (`hospital_final_dataset.xlsx`) with an engineered score of **99.66**.

#### 7. Equipment Utilization Rate
* **Clinical Operation Basis:** Tracks machine asset allocation states to ensure advanced clinical hardware remains optimally deployed.
* **How I Worked On It (UI Optimization Fix):** Dragging this parameter into its card visual initially caused Power BI to output a raw database title reading `"Max of Equipment_InUse_Flag"`. I manually opened the visual field component inside the canvas pane, applied a **visual-level rename to "Equipment Utilization"**, and toggled the default category label to **`OFF`** to achieve a clean presentation-grade format.

#### 8. Staff Utilization Rate
* **Clinical Operation Basis:** Measures clinical personnel assignment balances to ensure clinician shifts are optimized efficiently without causing fatigue.
* **How I Worked On It (UI Optimization Fix):** Similar to the equipment metric, this visual card initially displayed an ugly default tag (`Max of Staff_Utilization_Calc`). I opened the **Format Visual properties (Paintbrush Icon 🖌️)**, navigated to the **Category Label** toggle switch, turned it completely **`OFF`**, and placed a custom text box above the metric to serve as a clean business header.

---

## 🎨 4. Step 3: Architecture of Deployed Dashboard Views & Visual Layouts

The frontend data application contains **4 dedicated analytics sheets** mapped out inside the final `MedTrack_DV_Dashboard.pbix` workbook. Each layout enforces a strict **Unified Page Grid Model** featuring a balanced combination of exactly **6 KPI summary cards, 5 core data visualizations, 4 interactive dynamic filters, and 1 integrated Q&A intelligence button** to eliminate workspace crowding and prioritize high-density enterprise scannability.

```text
+------------------------------------------------------------------------------------------------------------------------+

|  MedTrack Dashboard App                                    [ FILTER 1 ]  [ FILTER 2 ]  [ FILTER 3 ]  [ FILTER 4 ]      |
+------------------------------------------------------------------------------------------------------------------------+

|  [📄 CARD 1]   [📄 CARD 2]   [📄 CARD 3]   [📄 CARD 4]   [📄 CARD 5]   [📄 CARD 6]                 [ ❓ ASK A QUESTION ] |
+------------------------------------------------------------------------------------------------------------------------+

|                                                       |                                                                |
|       📊 [ VISUAL CONTAINER 1 ]                        |       📊 [ VISUAL CONTAINER 2 ]                                |
