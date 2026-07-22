"""Tableau Packaged Workbook Generator Script (Milestone 3)

This script programmatically generates the Tableau Packaged Workbook (.twbx) files 
for Milestone 3 (Modules 5 & 6) by compiling a valid Tableau XML workbook (.twb) 
and packaging it with the final Excel dataset into a ZIP-based packaged workbook.
"""

import zipfile
import os

TWB_CONTENT = """<?xml version='1.0' encoding='utf-8' ?>
<workbook source-build='2020.2.0' version='18.1' xmlns:user='http://www.tableausoftware.com/xml/user'>
  <preferences>
  </preferences>
  <datasources>
    <datasource caption='hospital_final_dataset' inline='true' name='federated.excel-direct' version='18.1'>
      <connection class='federated'>
        <named-connections>
          <named-connection caption='hospital_final_dataset' name='excel-direct.connection'>
            <connection class='excel-direct' cleaning='no' compat='no' dataRefreshTime='' filename='hospital_final_dataset.xlsx' validate='no' />
          </named-connection>
        </named-connections>
        <relation connection='excel-direct.connection' name='Sheet1' table='[Sheet1$]' type='table' />
      </connection>
      <layout dim-ordering='alphabetical' dim-percentage='0.5' measure-ordering='alphabetical' measure-percentage='0.5' show-structure='true' />
      <semantic-values>
        <semantic-value key='[Country].[Name]' value='&quot;India&quot;' />
      </semantic-values>
    </datasource>
  </datasources>
  <worksheets>
    <worksheet name='Hospital Overview Sheet'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.excel-direct' />
          </datasources>
          <aggregation value='true' />
        </view>
        <style>
        </style>
        <panes>
          <pane id='0'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Automatic' />
          </pane>
        </panes>
        <rows>[federated.excel-direct].[Sum:Billing Amount]</rows>
        <cols>[federated.excel-direct].[None:Department]</cols>
      </table>
    </worksheet>
    <worksheet name='Patient Flow Sheet'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.excel-direct' />
          </datasources>
          <aggregation value='true' />
        </view>
        <style>
        </style>
        <panes>
          <pane id='0'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Automatic' />
          </pane>
        </panes>
        <rows>[federated.excel-direct].[Sum:Length of Stay]</rows>
        <cols>[federated.excel-direct].[None:Admission Date]</cols>
      </table>
    </worksheet>
    <worksheet name='Department Analytics Sheet'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.excel-direct' />
          </datasources>
          <aggregation value='true' />
        </view>
        <style>
        </style>
        <panes>
          <pane id='0'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Automatic' />
          </pane>
        </panes>
        <rows>[federated.excel-direct].[Avg:Department Efficiency Score]</rows>
        <cols>[federated.excel-direct].[None:Department]</cols>
      </table>
    </worksheet>
    <worksheet name='Resource Utilization Sheet'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.excel-direct' />
          </datasources>
          <aggregation value='true' />
        </view>
        <style>
        </style>
        <panes>
          <pane id='0'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Automatic' />
          </pane>
        </panes>
        <rows>[federated.excel-direct].[Avg:Bed Utilization Rate (%)]</rows>
        <cols>[federated.excel-direct].[None:Hospital Name]</cols>
      </table>
    </worksheet>
  </worksheets>
  <dashboards>
    <dashboard name='Hospital Overview'>
      <style />
      <zones>
        <zone id='1' type-name='layout-basic' x='0' y='0' w='1000' h='1000'>
          <zone id='2' name='Hospital Overview Sheet' type-name='worksheet' x='0' y='0' w='1000' h='1000' />
        </zone>
      </zones>
    </dashboard>
    <dashboard name='Patient Flow'>
      <style />
      <zones>
        <zone id='1' type-name='layout-basic' x='0' y='0' w='1000' h='1000'>
          <zone id='2' name='Patient Flow Sheet' type-name='worksheet' x='0' y='0' w='1000' h='1000' />
        </zone>
      </zones>
    </dashboard>
    <dashboard name='Department Analytics'>
      <style />
      <zones>
        <zone id='1' type-name='layout-basic' x='0' y='0' w='1000' h='1000'>
          <zone id='2' name='Department Analytics Sheet' type-name='worksheet' x='0' y='0' w='1000' h='1000' />
        </zone>
      </zones>
    </dashboard>
    <dashboard name='Resource Utilization'>
      <style />
      <zones>
        <zone id='1' type-name='layout-basic' x='0' y='0' w='1000' h='1000'>
          <zone id='2' name='Resource Utilization Sheet' type-name='worksheet' x='0' y='0' w='1000' h='1000' />
        </zone>
      </zones>
    </dashboard>
  </dashboards>
  <windows>
    <window class='worksheet' name='Hospital Overview Sheet'>
      <active />
    </window>
  </windows>
</workbook>
"""

# Determine directory paths relative to the script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_EXCEL_PATH = os.path.join(SCRIPT_DIR, "..", "data", "hospital_final_dataset.xlsx")

def create_packaged_workbook(output_filename, temp_twb_filename):
    # Construct paths relative to the script
    output_path = os.path.join(SCRIPT_DIR, "..", "dashboard", output_filename)
    temp_twb_path = os.path.join(SCRIPT_DIR, temp_twb_filename)
    
    print(f"Creating {output_path}...")
    
    # 1. Write the temporary .twb XML file
    with open(temp_twb_path, "w", encoding="utf-8") as f:
        f.write(TWB_CONTENT)
    
    # 2. Package into the .twbx (which is a ZIP file)
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as z:
        # Write .twb as the root of the packaged workbook
        z.write(temp_twb_path, arcname=temp_twb_filename)
        # Write excel dataset into the packaged workbook
        z.write(DATA_EXCEL_PATH, arcname="hospital_final_dataset.xlsx")
        
    print(f"Successfully packaged {output_path}!")
    
    # Clean up the temporary .twb file
    if os.path.exists(temp_twb_path):
        os.remove(temp_twb_path)

def main():
    # Generate Module 5 deliverable
    create_packaged_workbook("medtrack_dashboard_v1.twbx", "medtrack_dashboard_v1.twb")
    
    # Generate Module 6 (integrated) deliverable
    create_packaged_workbook("MedTrack_DV.twbx", "MedTrack_DV.twb")
    
    print("\n" + "=" * 50)
    print("TABLEAU PACKAGED WORKBOOKS GENERATED SUCCESSFULLY!")
    print("=" * 50)

if __name__ == "__main__":
    main()
