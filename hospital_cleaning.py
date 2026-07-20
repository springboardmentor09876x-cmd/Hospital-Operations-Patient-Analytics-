
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# ==========================
# Load Dataset
# ==========================
input_file = "Hospital_RawDataset_Updated(1).xlsx"
df = pd.read_excel(input_file)

# ==========================
# Remove Duplicate Records
# ==========================
clean = df.drop_duplicates().copy()

# ==========================
# Handle Missing Values
# ==========================

# Fill categorical columns with mode
for col in clean.select_dtypes(include="object").columns:
    if clean[col].isna().any():
        if "date" in col.lower():
            continue
        mode = clean[col].mode(dropna=True)
        fill_value = mode.iloc[0] if not mode.empty else "Unknown"
        clean[col] = clean[col].fillna(fill_value)

# Fill numeric columns with median
for col in clean.select_dtypes(include="number").columns:
    if clean[col].isna().any():
        clean[col] = clean[col].fillna(clean[col].median())

# Fill missing Transfer_Date values
if "Transfer_Date" in clean.columns:
    transfer = pd.to_datetime(clean["Transfer_Date"], errors="coerce")

    if "Admission Date" in clean.columns:
        admission = pd.to_datetime(clean["Admission Date"], errors="coerce")
        transfer = transfer.fillna(admission)
    else:
        transfer = transfer.fillna(pd.Timestamp("2024-01-01"))

    clean["Transfer_Date"] = transfer.dt.strftime("%Y-%m-%d")

# ==========================
# Standardize Department Names
# ==========================
department_cols = [
    "Department",
    "Transfer_From_Department",
    "Transfer_To_Department"
]

for col in department_cols:
    if col in clean.columns:
        clean[col] = (
            clean[col]
            .astype(str)
            .str.strip()
            .str.title()
        )

# ==========================
# Normalize Healthcare Indicators
# ==========================
indicator_cols = [
    "Admissions_Rate_%_Derived",
    "Staff_Utilization_%_Derived",
    "Bed_Occupancy_Rate_%",
    "Beds_Occupied_Count",
    "Length of Stay",
    "Billing Amount"
]

indicator_cols = [c for c in indicator_cols if c in clean.columns]

if indicator_cols:
    scaler = MinMaxScaler()
    clean[[c + "_Normalized" for c in indicator_cols]] = scaler.fit_transform(
        clean[indicator_cols]
    )

# ==========================
# Save Cleaned Dataset
# ==========================
output_file = "hospital_cleaned_less2_missing.csv"
clean.to_csv(output_file, index=False)

print("=" * 50)
print("Cleaning Completed Successfully!")
print(f"Output File: {output_file}")
print("\nMissing Values (%)")
print((clean.isna().mean() * 100).sort_values(ascending=False).head())
print("=" * 50)
