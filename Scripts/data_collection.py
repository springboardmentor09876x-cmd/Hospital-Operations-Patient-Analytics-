import pandas as pd


# Read dataset
df = pd.read_csv(
    "Data/hospital_raw_data.csv"
)


# Add Patient_ID column at first position
df.insert(
    0,
    "Patient_ID",
    range(1, len(df) + 1)
)


# Save updated dataset
df.to_csv(
    "Data/hospital_raw_data.csv",
    index=False
)


print("Patient_ID added successfully")

print(df.head())