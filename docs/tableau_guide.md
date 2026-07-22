# Tableau Dashboard Construction Guide (Milestone 3)

This guide provides step-by-step instructions on how to build the four dashboards for **Milestone 3 (Modules 5 & 6)** in Tableau using the calculated dataset `hospital_final_dataset.xlsx`.

---

## Part 1: Connecting the Data

1. Open **Tableau Desktop** or **Tableau Public**.
2. Click **Microsoft Excel** under *Connect* on the left sidebar.
3. Browse and select your dataset:
   `C:\Users\shrut\.gemini\antigravity\scratch\Hospital-Operations-Patient-Analytics-\hospital_final_dataset.xlsx`
4. Drag the sheet into the canvas area.
5. Click **Sheet 1** at the bottom to go to your worksheet workspace.

---

## Part 2: Building the 4 Dashboards (Worksheet by Worksheet)

### Dashboard 1: Hospital Overview
Configure the following worksheets and place them in the layout matching page 1 of `dashboard_storyboard.pdf`:

1. **Admissions Trend (Line Chart)**:
   - Columns: `Date of Admission` (aggregated to Month/Year)
   - Rows: `Total Admissions (Overall)`
   - Marks: Line
2. **Occupancy Rate Trend (Line Chart)**:
   - Columns: `Date of Admission` (Month/Year)
   - Rows: `Occupancy Rate (%)` (Average)
3. **Readmission Rate Trend (Line Chart)**:
   - Columns: `Date of Admission` (Month/Year)
   - Rows: `Readmission Rate (%)` (Average)
4. **Admissions by Department (Horizontal Bar)**:
   - Columns: `Total Admissions (Dept)`
   - Rows: `Department` (Sorted descending)
5. **ALOS by Department (Bar Chart)**:
   - Columns: `Department`
   - Rows: `Average Length of Stay (Dept)` (Average)
6. **Top 5 Hospitals by Occupancy (Row Chart)**:
   - Columns: `Occupancy Rate (Hospital) (%)` (Average)
   - Rows: `Hospital Name`
   - Filter: Top 5 by Occupancy Rate.

---

### Dashboard 2: Patient Flow
Configure these worksheets to track admission kinetics and discharge flow (matching page 2 of `dashboard_storyboard.pdf`):

1. **Daily Admissions vs. Discharges (Dual Axis Line)**:
   - Columns: `Date of Admission` (Day)
   - Rows: Count of `Patient ID` (Admissions) and Count of `Discharge Date` (Discharges)
   - Right-click one of the Row pills and choose **Dual Axis**, then right-click the axis and select **Synchronize Axis**.
2. **Stay Category Distribution (Pie/Donut Chart)**:
   - Colors: `Stay Category` (Short, Medium, Long, Extended)
   - Size/Angle: Count of `Patient ID`
3. **Peak Load Hours (Area Chart)**:
   - Columns: `Admission_Time` (Hour of Day)
   - Rows: Count of `Patient ID`
   - Marks: Area (Color: Orange)

---

### Dashboard 3: Department Analytics
Configure these sheets to benchmark clinical department performance (matching page 3 of `dashboard_storyboard.pdf`):

1. **Department Efficiency Rankings (Sorted Bar Chart)**:
   - Columns: `Department Efficiency Score` (Average)
   - Rows: `Department`
   - Sort: `Department` descending by `Department Efficiency Score`.
   - Color: Map `Department Efficiency Score` to Color (diverging palette).
2. **Billing vs. ALOS (Scatter Plot)**:
   - Columns: `Billing Amount` (Average)
   - Rows: `Length of Stay` (Average)
   - Detail: `Department`

---

### Dashboard 4: Resource Utilization
Configure these sheets to monitor bed capacity and staff allocation (matching page 4 of `dashboard_storyboard.pdf`):

1. **Bed Utilization Heatmap (Highlight Table)**:
   - Rows: `Hospital Name`
   - Columns: `Department`
   - Label & Color: `Bed Utilization Rate (%)` (Average)
2. **Staff Workload Distribution (Packed Bubbles)**:
   - Label: `Department`
   - Color: `Hospital Name`
   - Size: `Staff Count` (Average)

---

## Part 3: Dashboard Integration & Interactions

Once your worksheets are built, create the dashboards and configure the interactions:

1. **Global Filters**:
   - Add the filters (`Hospital Name`, `Department`, `Admission Type`, and `Admission Date` as a range slider) to the top of your dashboards.
   - Click the dropdown arrow on each filter card -> **Apply to Worksheets** -> **All Using This Data Source**.
2. **Dashboard Actions (Linking)**:
   - Go to **Dashboard -> Actions** from the top menu.
   - Click **Add Action -> Filter**.
   - Set the *Source Sheets* to your **Hospital Overview** dashboard, and the *Target Sheets* to the **Department Analytics** dashboard.
   - Select **Run action on: Select**. This allows you to click a department bar on the overview dashboard to automatically navigate and filter the department analytics dashboard.

---

## Part 4: Saving and Submitting

1. When finished, save your Tableau workbook.
2. Select **File -> Save As...**
3. Choose the type: **Tableau Packaged Workbook (*.twbx)**.
4. Save it in the repository folder as:
   `C:\Users\shrut\.gemini\antigravity\scratch\Hospital-Operations-Patient-Analytics-\MedTrack_DV.twbx`
5. Once saved, let me know, and I will push the file to your GitHub branch to complete Milestone 3!
