import pandas as pd

df=pd.read_csv("hospital_cleaned_less2_missing.csv")

total_admissions=len(df)
occupancy_rate=df["Bed_Occupancy_Rate_%"].mean()
average_length_of_stay=df["Length of Stay"].mean()

if "Readmission" in df.columns:
    readmission_rate=(df["Readmission"].astype(str).str.lower().isin(["yes","1","true"])).mean()*100
else:
    readmission_rate=0

if "Total_Beds" in df.columns:
    bed_utilization_rate=(df["Beds_Occupied_Count"].sum()/df["Total_Beds"].sum())*100
else:
    bed_utilization_rate=df["Bed_Occupancy_Rate_%"].mean()

eff=df.groupby("Department")[["Staff_Utilization_%_Derived","Admissions_Rate_%_Derived"]].mean()
eff["Department_Efficiency_Score"]=(eff["Staff_Utilization_%_Derived"]+eff["Admissions_Rate_%_Derived"])/2
df=df.merge(eff["Department_Efficiency_Score"],on="Department",how="left")

df["Total_Admissions"]=total_admissions
df["Occupancy_Rate"]=occupancy_rate
df["Average_Length_of_Stay"]=average_length_of_stay
df["Readmission_Rate"]=readmission_rate
df["Bed_Utilization_Rate"]=bed_utilization_rate

df.to_excel("hospital_final_dataset.xlsx",index=False)
print("Done")
