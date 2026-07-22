import pandas as pd
from pathlib import Path

# File Paths
input_file = Path("data") / "hospital_cleaned.csv"
output_file = Path("data") / "hospital_cleaned.csv"

print("Loading Dataset...")

df = pd.read_csv(input_file)

print("Dataset Loaded Successfully!")

print("\nTotal Records:", len(df))
print("Total Columns:", len(df.columns))

df.to_csv(output_file, index=False)

print("\nDataset Ready.")
print(f"Saved to: {output_file}")