#!/usr/bin/env python
# coding: utf-8

# In[1]:


#  LOAD THE CLEANED DATASET
# Import pandas for data handling
import pandas as pd

# Define the data folder path
path = r'C:\Users\pranv\OneDrive\Desktop\Hospital Operations & Patient Analytics\Hospital-Operations-Patient-Analytics-\data\\'

# Load Module 2's output dataset 
df_cleaned = pd.read_csv(path + 'hospital_cleaned.csv')

# Work on a COPY of the data
df = df_cleaned.copy()

# Display 
print("Shape of the dataset:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
df.head()


# In[2]:


#  CALCULATE TOTAL ADMISSIONS


# Total Admissions = count of unique patient records in the dataset
total_admissions = df['Patient_ID'].nunique()
print("Total Admissions:", total_admissions)

# Add as a new column — same overall value repeated for every row

df['Total_Admissions'] = total_admissions


# In[3]:


# CALCULATE OCCUPANCY RATE


# Occupancy Rate = (Occupied beds / Total department beds) * 100
# Count how many patient records have their bed marked as occupied
occupied_beds = (df['Bed_Occupied'] == 'Yes').sum()

# Sum up total beds across all department records
total_dept_beds = df['Dept_Beds'].sum()

# Calculate the overall occupancy rate as a percentage
overall_occupancy_rate = round((occupied_beds / total_dept_beds) * 100, 2)
print("Overall Occupancy Rate:", overall_occupancy_rate)

# Add as a new column — same overall value repeated for every row
df['Overall_Occupancy_Rate'] = overall_occupancy_rate


# In[4]:


#  CALCULATE AVERAGE LENGTH OF STAY

# Average Length of Stay = mean of the Length_of_Stay column (in days)
avg_length_of_stay = round(df['Length_of_Stay'].mean(), 2)
print("Average Length of Stay (days):", avg_length_of_stay)

# Add as a new column  
df['Average_Length_of_Stay'] = avg_length_of_stay


# In[5]:


#  CALCULATE READMISSION RATE

# Readmission Rate = (Patients readmitted / Total patients) * 100
readmitted_count = (df['Readmission'] == 'Yes').sum()
total_patients = len(df)

readmission_rate = round((readmitted_count / total_patients) * 100, 2)
print("Readmission Rate (%):", readmission_rate)

# Add as a new column 
df['Readmission_Rate'] = readmission_rate


# In[6]:


#  CALCULATE BED UTILIZATION RATE

# Bed Utilization Rate = (Occupied beds in department / Total department beds) * 100

df['Bed_Utilization_Rate'] = (
    (df['Dept_Beds'] - df['Beds_Available']) / df['Dept_Beds'] * 100
).round(2)

# Preview to confirm it varies sensibly by department
df[['Department', 'Dept_Beds', 'Beds_Available', 'Bed_Utilization_Rate']].head(10)


# In[7]:


# CALCULATE DEPARTMENT EFFICIENCY SCORE


# Department Efficiency Score
# 1. Staff Utilization (40% weight) - how efficiently staff are being used
# 2. Bed Occupancy Rate (40% weight) - how well beds are being utilized
# 3. Readmission penalty (20% weight) - lower readmissions = higher efficiency

# Formula: weighted sum of normalised (0-1 scale) components
df['Department_Efficiency_Score'] = (
    (df['Staff_Utilization'] / 100) * 0.4 +
    (df['Bed_Occupancy_Rate'] / 100) * 0.4 +
    (1 - (df['Readmission'] == 'Yes').astype(int)) * 0.2
).round(4)

# Preview the result
df[['Department', 'Staff_Utilization', 'Bed_Occupancy_Rate', 
    'Readmission', 'Department_Efficiency_Score']].head(10)


# In[8]:


# Print final shape to confirm all new KPI columns were added
print("Final dataset shape:", df.shape)

# Print a summary of all calculated KPIs for a final check
print("\nKPI Summary:")
print(df[['Total_Admissions', 'Overall_Occupancy_Rate', 'Average_Length_of_Stay',
           'Readmission_Rate', 'Bed_Utilization_Rate', 'Department_Efficiency_Score']].describe())

# Save the final dataset 
save_path = path + 'hospital_final_dataset.xlsx'
df.to_excel(save_path, index=False, engine='openpyxl')

print("\nhospital_final_dataset.xlsx saved successfully.")
print("Saved to:", save_path)


# In[10]:


print(df['Bed_Utilization_Rate'].describe())


# In[11]:


# Fix: Bed_Utilization_Rate should never exceed 100% or go below 0%
df['Bed_Utilization_Rate'] = df['Bed_Utilization_Rate'].clip(lower=0, upper=100)

print("Bed_Utilization_Rate range after fix:")
print(df['Bed_Utilization_Rate'].describe())


# In[12]:


save_path = path + 'hospital_final_dataset.xlsx'
df.to_excel(save_path, index=False, engine='openpyxl')

import os
print("Re-saved with fix. File size (bytes):", os.path.getsize(save_path))


# In[13]:


# Fix: Department_Efficiency_Score should stay within 0 to 1 range
df['Department_Efficiency_Score'] = df['Department_Efficiency_Score'].clip(lower=0, upper=1)

print("Department_Efficiency_Score range after fix:")
print(df['Department_Efficiency_Score'].describe())


# In[14]:


save_path = path + 'hospital_final_dataset.xlsx'
df.to_excel(save_path, index=False, engine='openpyxl')

import os
print("Re-saved. File size (bytes):", os.path.getsize(save_path))


# In[ ]:




