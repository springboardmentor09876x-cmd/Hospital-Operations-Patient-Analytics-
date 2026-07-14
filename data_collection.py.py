import pandas as pd

# Load the datasets
raw_dataset = pd.read_csv("hospital_raw_data.csv")
operations_dataset = pd.read_csv("Hospital_Operations_Dataset.csv")

# Rename the key column so both datasets have the same column name
operations_dataset.rename(columns={"Patient_ID": "Patient ID"}, inplace=True)

# Merge the datasets
updated_dataset = pd.merge(
    raw_dataset,
    operations_dataset,
    on="Patient ID",
    how="left"
)

# Save the merged dataset
updated_dataset.to_excel("Hospital_updated_dataset.xlsx", index=False)

# Preview
print(updated_dataset.head())

# Check dimensions
print("Rows, Columns:", updated_dataset.shape)
