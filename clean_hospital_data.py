
import pandas as pd
import numpy as np
def clean_hospital_data(in_path='hospital_cleaned.csv', out_path='hospital_cleaned_v2.csv'):
    df = pd.read_csv(in_path)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed', na=False)]
    for c in df.select_dtypes(include=['object']).columns:
        df[c] = df[c].where(df[c].isna(), df[c].str.strip())
    for c in ['Hospital Name','City','State','Department','Doctor','Patient Name','Admission Type','Insurance Provider']:
        if c in df.columns:
            df[c] = df[c].astype(str).str.title().replace({'Nan': np.nan})
    for c in df.columns:
        if c.lower().endswith('id') or ' id' in c.lower() or c.lower().startswith('hospital id'):
            df[c] = df[c].astype(str).str.upper()
    for c in ['Admission Date','Discharge Date']:
        if c in df.columns:
            df[c] = pd.to_datetime(df[c], errors='coerce')
    for c in ['Admission Time','Discharge Time']:
        if c in df.columns:
            df[c] = pd.to_datetime(df[c], errors='coerce').dt.strftime('%H:%M').fillna('')
    for c in ['Age','Beds Available','ICU Beds','Staff Count','Billing Amount','Length of Stay']:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')
    if 'Insurance Provider' in df.columns:
        df['Insurance Provider'] = df['Insurance Provider'].replace({'': np.nan}).fillna('Self-Pay')
    if 'Admission Date' in df.columns and 'Discharge Date' in df.columns:
        mask = (df['Discharge Date'].notna()) & (df['Admission Date'].notna()) & (df['Discharge Date'] < df['Admission Date'])
        df.loc[mask, 'Discharge Date'] = df.loc[mask, 'Admission Date']
    if 'Patient ID' in df.columns and 'Admission Date' in df.columns:
        df = df.drop_duplicates(subset=['Patient ID','Admission Date'], keep='first')
    df = df.dropna(axis=1, how='all')
    df.to_csv(out_path, index=False)
    print(f'Wrote cleaned file: {out_path}')
