#dataset cleaning 

import pandas as pd

# Load your dataset
df = pd.read_csv("hospital_raw_data.csv")

# 🔍 Check for missing values
print("Missing values per column:")
print(df.isnull().sum())

# 🔍 Check for duplicate rows
duplicate_count = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicate_count}")

# ✅ If you want to drop duplicates and missing values:
df_cleaned = df.drop_duplicates().dropna()

# Save the cleaned dataset
df_cleaned.to_csv("hospital_cleaned_data.csv", index=False)

print("\nCleaned dataset saved as 'hospital_cleaned_data.csv'")
