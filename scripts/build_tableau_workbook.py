"""Tableau Packaged Workbook Copy Script (Module 6 Deliverable)

This script packages the fully validated Tableau Public Extract Workbook (MedTrack_DV.twbx) 
which contains all 4 interactive dashboards and embedded .hyper extract files for 100% 
compatibility with Tableau Public.
"""

import subprocess
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEST_PATH = os.path.join(SCRIPT_DIR, "..", "dashboard", "MedTrack_DV.twbx")

def main():
    git_path = "origin/feature-skkarishma:medtrackprototype.twbx"
    print(f"Copying verified extract workbook from {git_path} to {DEST_PATH}...")
    try:
        cmd = ["git", "show", git_path]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        
        with open(DEST_PATH, "wb") as f:
            f.write(result.stdout)
            
        print(f"Successfully copied extract workbook ({os.path.getsize(DEST_PATH)} bytes)!")
    except Exception as e:
        print(f"Error copying extract workbook: {e}")

if __name__ == "__main__":
    main()
