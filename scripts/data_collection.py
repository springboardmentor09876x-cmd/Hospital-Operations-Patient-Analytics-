#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os      # Import the os module to interact with the operating system
print(os.getcwd()) # Display the current working directory
print(os.listdir()) # Display all files and folders in the current directory


# In[ ]:


import pandas as pd

df = pd.read_csv('../data/healthcare_dataset.csv') # Load the healthcare dataset
print(df.shape)
df.head()


# In[ ]:


condition_to_dept = {
    'Diabetes': 'Endocrinology',
    'Cancer': 'Oncology',                        
    'Obesity': 'General Medicine',
    'Asthma': 'Pulmonology',
    'Hypertension': 'Cardiology',
    'Arthritis': 'Orthopedics'
}# Map each medical condition to its corresponding department
 # Create a new Department column
df['Department'] = df['Medical Condition'].map(condition_to_dept)  
df[['Medical Condition', 'Department']].head(10)


# In[ ]:


departments = df['Department'].unique()
print(departments)
                                       # Create hospital resource data and merge it with the dataset
resource_data = pd.DataFrame({
    'Department': departments,
    'total_beds': [50, 60, 30, 40, 20, 35][:len(departments)],
    'staff_count': [20, 25, 15, 22, 30, 18][:len(departments)]
})
        # Merge patient data with department resource information
hospital_raw_data = pd.merge(df, resource_data, on='Department', how='left')
print(hospital_raw_data.shape)
hospital_raw_data.head()


# In[ ]:


print(len(hospital_raw_data))  # Display the total number of records in the dataset


# In[ ]:


completeness = (1 - hospital_raw_data.isnull().sum().sum() / hospital_raw_data.size) * 100
print(f"Dataset completeness: {completeness:.2f}%")     # Calculate the percentage of complete (non-missing) data


# In[ ]:


hospital_raw_data.to_csv('../data/hospital_raw_data.csv', index=False) # Save the processed dataset as a CSV file
print("Saved successfully: hospital_raw_data.csv") # Display a confirmation message after saving the file


# In[ ]:


import pandas as pd

def load_data():
    df = pd.read_csv('../data/healthcare_dataset.csv')
    return df

def add_department(df):
    condition_to_dept = {
        'Diabetes': 'Endocrinology',
        'Cancer': 'Oncology',
        'Obesity': 'General Medicine',
        'Asthma': 'Pulmonology',
        'Hypertension': 'Cardiology',
        'Arthritis': 'Orthopedics'
    }
    df['Department'] = df['Medical Condition'].map(condition_to_dept)
    return df

def add_resources(df):
    departments = df['Department'].unique()
    resource_data = pd.DataFrame({
        'Department': departments,
        'total_beds': [50, 60, 30, 40, 20, 35][:len(departments)],
        'staff_count': [20, 25, 15, 22, 30, 18][:len(departments)]
    })
    merged = pd.merge(df, resource_data, on='Department', how='left')
    return merged

def main():
    df = load_data()
    df = add_department(df)
    df = add_resources(df)
    df.to_csv('../data/hospital_raw_data.csv', index=False)
    completeness = (1 - df.isnull().sum().sum() / df.size) * 100
    print(f"Saved: hospital_raw_data.csv | Shape: {df.shape} | Completeness: {completeness:.2f}%")

if __name__ == "__main__":
    main()


# In[ ]:




