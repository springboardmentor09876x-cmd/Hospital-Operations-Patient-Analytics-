#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
# Load the original patient-level healthcare dataset 
df = pd.read_csv(r'C:\Users\pranv\OneDrive\Desktop\Hospital Operations & Patient Analytics\Hospital-Operations-Patient-Analytics-\data\healthcare_dataset.csv')
print(df.shape)
df.head()


# In[6]:


df = df.rename(columns={
    'Name': 'Patient_Name',
    'Medical Condition': 'Diagnosis',                  
    'Date of Admission': 'Admission_Date',
    'Hospital': 'Hospital_Name',
    'Insurance Provider': 'Insurance',
    'Room Number': 'Room_No',
    'Discharge Date': 'Discharge_Date',
    'Admission Type': 'Admission_Type',
    'Test Results': 'Test_Result'
})
# Rename original columns to cleaner, consistent names
df.columns


# In[7]:


# The raw dataset has no 'Department' column, so we derive one
# by mapping each medical condition to a relevant hospital department
condition_to_dept = {
    'Diabetes': 'Endocrinology',
    'Cancer': 'Oncology',
    'Obesity': 'General Medicine',
    'Asthma': 'Pulmonology',
    'Hypertension': 'Cardiology',
    'Arthritis': 'Orthopedics'
}
df['Department'] = df['Diagnosis'].map(condition_to_dept)
df[['Diagnosis','Department']].head()


# In[8]:


np.random.seed(42)                               # Set a random seed so results are reproducible every time we run this

hospitals = df['Hospital_Name'].unique()         # Get list of unique hospitals in the dataset
                                                 # Since our raw data has no hospital location/type info,
                                                 # we simulate realistic hospital-level attributes
cities = ['Mumbai', 'Delhi', 'Bengaluru', 'Hyderabad', 'Chennai', 'Vijayawada']
states = ['Maharashtra', 'Delhi', 'Karnataka', 'Telangana', 'Tamil Nadu', 'Andhra Pradesh']
types = ['Private', 'Government']
                                                 # Build a small reference table: one row per unique hospital
hospital_ref = pd.DataFrame({
    'Hospital_Name': hospitals,
    'Hospital_ID': ['HOSP' + str(1000+i) for i in range(len(hospitals))],
    'Hospital_Type': np.random.choice(types, len(hospitals)),
    'City': np.random.choice(cities, len(hospitals)),
    'State': np.random.choice(states, len(hospitals))
})
                                                  # Merge hospital info into the main dataset using Hospital_Name as the key
df = pd.merge(df, hospital_ref, on='Hospital_Name', how='left')
df.head()  


# In[9]:


departments = df['Department'].dropna().unique()  # Get list of unique departments (excluding any missing/NaN values)
                                                  # Simulate department-level resource data since it's not in the raw dataset
dept_ref = pd.DataFrame({
    'Department': departments,
    'Department_ID': ['DEPT' + str(1+i).zfill(3) for i in range(len(departments))],
    'Nurses': np.random.randint(10, 50, len(departments)),
    'Dept_Staff_Count': np.random.randint(20, 100, len(departments)),
    'Dept_Beds': np.random.randint(20, 100, len(departments)),
    'Dept_ICU_Beds': np.random.randint(5, 30, len(departments))
})
                                                  # Merge department resource info into the main dataset using Department as the key
df = pd.merge(df, dept_ref, on='Department', how='left')
df.head()


# In[11]:


df['Patient_ID'] = ['PAT' + str(1+i).zfill(5) for i in range(len(df))]  # Create a unique Patient ID for every row


# In[12]:


df['Bed_Number'] = np.random.randint(1, 500, len(df))        # Assign a random bed number to each patient
df['ICU_Beds'] = df['Dept_ICU_Beds']                         # ICU beds available comes from the department's total ICU capacity
df['Beds_Available'] = df['Dept_Beds'] - np.random.randint(0, 30, len(df)) # Simulate how many beds are currently available
df['Bed_Occupied'] = np.random.choice(['Yes', 'No'], len(df), p=[0.7, 0.3]) # Randomly flag whether this patient's bed is currently occupied


# In[15]:


# Assign a random equipment ID to each patient record, equipment type and simulate current equipment status.
equipment_types = ['Ventilator', 'MRI Scanner', 'Dialysis Machine', 'Patient Monitor']
df['Equipment_ID'] = ['EQ' + str(np.random.randint(1000,9999)) for _ in range(len(df))]
df['Equipment_Type'] = np.random.choice(equipment_types, len(df))
df['Equipment_Status'] = np.random.choice(['In Use', 'Available', 'Under Maintenance'], len(df), p=[0.4,0.5,0.1])
df['Equipment_InUse_Flag'] = (df['Equipment_Status'] == 'In Use').astype(int)


# In[16]:


df['Admission_Date'] = pd.to_datetime(df['Admission_Date']) # Convert admission/discharge columns from text to actual datetime format
df['Discharge_Date'] = pd.to_datetime(df['Discharge_Date'])
df['Length_of_Stay'] = (df['Discharge_Date'] - df['Admission_Date']).dt.days # Calculate how many days each patient stayed in the hospital

df['Transferred'] = np.random.choice(['Yes', 'No'], len(df), p=[0.15, 0.85])# Simulate whether a patient was transferred between departments/hospitals
df['Number_of_Transfers'] = np.where(df['Transferred']=='Yes', np.random.randint(1,3,len(df)), 0) # If transferred, assign 1-2 transfers; otherwise 0
df['Readmission'] = np.random.choice(['Yes', 'No'], len(df), p=[0.1, 0.9]) #Simulate whether this patient was readmitted after a previous visit


# In[17]:


df['Staff_Utilization'] = (df['Dept_Staff_Count'] / (df['Dept_Staff_Count'] + df['Nurses']) * 100).round(1) # proportion of department staff relative to total staff and nurses
df['Bed_Occupancy_Rate'] = ((df['Dept_Beds'] - df['Beds_Available']) / df['Dept_Beds'] * 100).round(1)  # Bed Occupancy Rate: how full the department's beds are
df['ICU_Occupancy_Rate'] = np.random.uniform(20, 90, len(df)).round(1)    #simulated for now since we don't have real-time ICU tracking


# In[18]:


print("Shape:", df.shape)  # Print final shape and column list to confirm everything was added correctly
print("Columns:", df.columns.tolist())

missing_pct = (df.isnull().sum().sum() / df.size) * 100 # Check overall data completeness
print(f"Missing values: {missing_pct:.2f}%")
# Save the final integrated dataset
path = r'C:\Users\pranv\OneDrive\Desktop\Hospital Operations & Patient Analytics\Hospital-Operations-Patient-Analytics-\data\\'
df.to_csv(path + 'hospital_raw_data.csv', index=False)
print("Saved: hospital_raw_data.csv")


# In[ ]:




