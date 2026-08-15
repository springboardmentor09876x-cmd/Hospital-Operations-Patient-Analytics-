
MedTrack_DV/
├── 📁 dashboard/
    |__medtrack_dashboard_v1.pbix 
    |__medtrack_prototype.pbix
│   └── 📊 MedTrack_DV_Dashboard.pbix    #Polished Power BI Desktop UI dashboard
├── 📁 data/
│   ├── 📄 hospital_raw_data.csv            # Uncleaned baseline transactional feed
│   ├── 📄 hospital_cleaned.csv             # Cleaned intermediate data sheet
│   └── 📁 hospital_final_dataset.xlsx      # Aligned analytics data layer for Power BI
├── 📁 docs/
│   ├── 📝 Final_Project_Documentation.md   # Core portfolio asset
│   └── 📋 MedTrack_DV_QA_Checklist.md      # Full 18-point verification matrix
     |__📋 Dashboard_Testing_Report.md
     |__dashboard_storyboard.pdf
└── 📁 scripts/
    ├── 📓 data_collection.py    # Initial data profhiling and quality scan
    |__📓 hospital_cleaning.ipynb
    └── 📓 generate_hospital_kpis.py      # Automated pandas calculation engine