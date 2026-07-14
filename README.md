# Hospital Management Dataset Integration

## 📌 Project Overview

This project combines two hospital datasets into a single, comprehensive dataset using Python and Pandas.

The merged dataset can be used for:
- Data Analysis
- Machine Learning
- Dashboard Development (Power BI/Tableau)
- Healthcare Research
- Academic Projects

---

## 📂 Project Structure

```
Hospital_Project/
│
├── hospital_raw_data.csv
├── Hospital_Operations_Dataset.csv
├── merge_hospital_datasets.py
├── Hospital_updated_dataset.xlsx
└── README.md
```

---

## 📊 Datasets Used

### 1. hospital_raw_data.csv

Contains patient demographic and medical information such as:

- Patient ID
- Name
- Age
- Gender
- Department
- Diagnosis
- Admission Date
- Discharge Date
- Doctor
- Billing Amount
- Insurance Provider
- Hospital
- City
- State
- and other patient-related details.

---

### 2. Hospital_Operations_Dataset.csv

Contains hospital operational information such as:

- Patient_ID
- Bed Number
- Ward
- Floor
- Admission Type
- Operation Theatre
- Surgery Duration
- Nurse Assigned
- Room Charges
- Medication Charges
- Lab Charges
- Doctor Fees
- Total Hospital Charges
- Payment Status
- Discharge Summary
- Follow-up Date
- Satisfaction Rating
- and other operational details.

---

## 🔄 Dataset Integration

The datasets are merged using the common patient identifier.

Before merging,

```
Patient_ID
```

is renamed to

```
Patient ID
```

to match the column name in the raw dataset.

The merge operation uses a **Left Join**, ensuring that all records from the raw dataset are retained.

```python
updated_dataset = pd.merge(
    raw_dataset,
    operations_dataset,
    on="Patient ID",
    how="left"
)
```

---

## ⚙️ Requirements

Install the required Python libraries.

```bash
pip install pandas openpyxl
```

---

## ▶️ How to Run

1. Place all files in the same folder.

```
hospital_raw_data.csv
Hospital_Operations_Dataset.csv
merge_hospital_datasets.py
```

2. Open Terminal or Command Prompt.

3. Run

```bash
python merge_hospital_datasets.py
```

---

## 📄 Output

The script generates:

```
Hospital_updated_dataset.xlsx
```

This file contains the merged information from both datasets.

---

## 📚 Technologies Used

- Python
- Pandas
- OpenPyXL
- CSV
- Excel

---

## 🎯 Applications

The merged dataset can be used for:

- Hospital Performance Analysis
- Patient Record Analysis
- Healthcare Dashboard Development
- Machine Learning Projects
- Data Visualization
- Predictive Analytics
- Academic Research

---

## 👩‍💻 Author

**Vainavi Sidagam**

B.Tech – Computer Science and Engineering (Data Science)

Vignan Institute of Information Technology

---

## 📜 License

This project is created for educational and academic purposes.
