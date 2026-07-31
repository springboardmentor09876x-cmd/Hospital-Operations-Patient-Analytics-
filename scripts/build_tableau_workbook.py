"""Tableau Packaged Workbook Generator Script (Milestone 3)

This script programmatically generates the Tableau Packaged Workbook (.twbx) files 
for Milestone 3 (Modules 5 & 6) by extracting the reference XML schema (which includes 
interactive navigation buttons and dashboard actions) and packaging it with the 
final Excel dataset.
"""

import subprocess
import zipfile
import io
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_SRC_PATH = os.path.join(SCRIPT_DIR, "..", "data", "hospital_final_dataset.xlsx")

def extract_reference_xml():
    git_path = "origin/vaishnavi-kruthi:medtrack_prototype.twbx"
    print(f"Extracting reference XML from {git_path}...")
    try:
        cmd = ["git", "show", git_path]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        
        with zipfile.ZipFile(io.BytesIO(result.stdout)) as z:
            for name in z.namelist():
                if name.endswith(".twb"):
                    return z.read(name)
    except Exception as e:
        print(f"Error extracting reference XML: {e}")
        return None

def package_workbook(output_filename, xml_bytes):
    output_path = os.path.join(SCRIPT_DIR, "..", "dashboard", output_filename)
    print(f"Packaging {output_path}...")
    
    # We will create a zip file (.twbx) and add:
    # 1. The .twb XML file at the root of the ZIP
    # 2. The Excel dataset at the relative path expected by the XML connection: 'Data/data/hospital_final_dataset.xlsx'
    inner_twb_name = output_filename.replace(".twbx", ".twb")
    
    try:
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as z:
            # Write XML bytes directly
            z.writestr(inner_twb_name, xml_bytes)
            # Write Excel dataset under the expected subfolder
            z.write(EXCEL_SRC_PATH, arcname="Data/data/hospital_final_dataset.xlsx")
        print(f"Successfully packaged {output_path}!")
    except Exception as e:
        print(f"Error packaging {output_path}: {e}")

def main():
    xml_bytes = extract_reference_xml()
    if xml_bytes is None:
        print("Failed to obtain reference XML, compilation aborted.")
        return
        
    # Generate Module 5 deliverable
    package_workbook("medtrack_dashboard_v1.twbx", xml_bytes)
    
    # Generate Module 6 (integrated) deliverable
    package_workbook("MedTrack_DV.twbx", xml_bytes)
    
    print("\n" + "=" * 50)
    print("TABLEAU PACKAGED WORKBOOKS GENERATED SUCCESSFULLY!")
    print("=" * 50)

if __name__ == "__main__":
    main()
