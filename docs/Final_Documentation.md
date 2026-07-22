# MedTrack_DV - Final Project Documentation

This document provides a comprehensive summary of the MedTrack_DV project, including data sources, KPI definitions, dashboard functionality, and operational methodologies.

---

## 1. Dataset Sources & Collection Methodology
The analysis integrates data from two primary transactional exports:
1. **Hospital Information System (HIS) Export (`Hospital_Dataset.xlsx`)**: Contains 10,000 records tracking hospital facilities, staff count, geographic location, bed capacity, clinical diagnoses, and patient details.
2. **Clinical Patient Admission Records (`Patient_Dataset.xlsx`)**: Tracks clinical information including length of stay, medical conditions, medication, billing amounts, and patient movement patterns.
3. **Derived Hospital Metrics (`Hospital_RawDataset_Updated.xlsx`)**: Provides pre-derived variables for bed capacities, staff utilization, and occupancy rates used to validate raw transactional data.

---

## 2. KPI Definitions & Mathematical Formulas

The following metrics are engineered to drive operational decision-making:

### 1. Total Admissions
- **Definition**: The total volume of patient admissions over a given period.
- **Formula**:
  $$TotalAdmissions = Count(PatientID)$$

### 2. Bed Occupancy Rate
- **Definition**: The percentage of hospital beds occupied by patients at any given time.
- **Formula**:
  $$OccupancyRate = \frac{BedsOccupiedCount}{BedsAvailable} \times 100$$

### 3. Average Length of Stay (ALOS)
- **Definition**: The average number of days a patient spends in the hospital during a single admission.
- **Formula**:
  $$ALOS = \frac{\sum LengthOfStay}{TotalAdmissions}$$

### 4. Patient Readmission Rate
- **Definition**: The percentage of patients readmitted to the hospital within a 30-day period.
- **Formula**:
  $$ReadmissionRate = \frac{Count(Readmissions = 'Yes')}{TotalAdmissions} \times 100$$

### 5. Bed Utilization Rate
- **Definition**: The utilization percentage of inpatient bed capacity.
- **Formula**:
  $$BedUtilization = \frac{BedsOccupiedCount}{BedsAvailable} \times 100$$

### 6. Department Efficiency Score
- **Definition**: A composite score (0-100%) reflecting clinical quality and resource efficiency.
- **Formula**:
  $$EfficiencyScore = 100 - (ReadmissionRate \times 0.4) - (NormalizedALOS \times 0.3) + (BedUtilizationRate \times 0.3)$$
  *Where:*
  $$NormalizedALOS = \frac{DeptALOS}{MaxDeptALOS} \times 100$$

---

## 3. Dashboard Guide & Navigation

The packaged workbook `MedTrack_DV.twbx` contains four interconnected dashboards:

1. **Hospital Overview Dashboard**:
   - *Purpose*: Provides hospital executives with high-level operational performance metrics (Total Admissions, ALOS, Readmission Rate).
   - *Key Viz*: Monthly Admissions Trend, Top 5 Hospitals by Occupancy.
2. **Patient Flow Dashboard**:
   - *Purpose*: Tracks patient volume kinetics from admission through discharge.
   - *Key Viz*: Daily Admissions vs. Discharges, Peak Load Hours.
3. **Department Analytics Dashboard**:
   - *Purpose*: Enables clinical chiefs to compare efficiency and diagnoses across departments.
   - *Key Viz*: Department Efficiency rankings, ALOS vs. Billing Scatter Plot.
4. **Resource Utilization Dashboard**:
   - *Purpose*: Monitors hospital bed capacity, staff workloads, and equipment availability.
   - *Key Viz*: Bed utilization highlight table, Staff Workload Bubble chart.

---

## 4. Healthcare Operations Methodology
- **Operational Efficiency**: By identifying peak admission hours (e.g. 10:00 AM to 2:00 PM), resource planners can align nurse shifts to handle higher workloads.
- **Quality of Care**: High readmission rates point to potential gaps in discharge protocols. Tracking readmission rates per department helps target quality improvement audits.
- **Resource Allocation**: High bed utilization rates coupled with high patient-to-staff ratios indicate bottleneck risks. The resource dashboard helps identify departments requiring staff reallocation.
