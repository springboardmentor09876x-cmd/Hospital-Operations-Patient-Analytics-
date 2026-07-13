"""
MedTrack_DV: Module 1 - Hospital Data Collection
This script documents the structural layout and integration of the core features
required for the Hospital Operations and Patient Analytics Dashboard.
"""
import pandas as pd

def check_raw_data():
    try:
        df = pd.read_csv('data/hospital_raw_data.csv')
        print("--- Module 1: Data Integration Evaluation ---")
        print(f"Dataset successfully loaded. Row count: {len(df)}")
        print(f"Total attributes collected: {len(df.columns)}")
        
        # Verify completeness is above 95%
        completeness = (1 - (df.isnull().sum().sum() / df.size)) * 100
        print(f"Dataset Completeness: {completeness:.2f}%")
        if completeness >= 95:
            print("Evaluation Status: PASSED (>95% completeness achieved)")
        else:
            print("Evaluation Status: FAILED (<95% completeness)")
            
    except FileNotFoundError:
        print("Error: Please place 'hospital_raw_data.csv' inside the 'data/' folder.")

if __name__ == "__main__":
    check_raw_data()