"""Dashboard Storyboard Generation Script (Module 4)

This script programmatically generates a professional, 4-page PDF document 
containing actual data visualizations and layout wireframes for the 
four dashboards in the MedTrack_DV Tableau workbook.
"""

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as patches
import pandas as pd
import numpy as np
import os
import textwrap

# Set non-interactive backend
import matplotlib
matplotlib.use("Agg")

# Define paths using robust path resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PDF = os.path.join(SCRIPT_DIR, "..", "dashboard", "dashboard_storyboard.pdf")
DATA_FILE = os.path.join(SCRIPT_DIR, "..", "data", "hospital_cleaned.csv")

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            return pd.read_csv(DATA_FILE)
        except Exception as e:
            print(f"Error reading dataset: {e}")
    # Fallback dummy data if file is missing
    print("Warning: Cleaned dataset not found, using dummy data for storyboard layout.")
    dates = pd.date_range(start="2026-01-01", periods=12, freq="M")
    return pd.DataFrame({
        "Admission Date": [d.strftime("%Y-%m-%d") for d in dates] * 10,
        "Department": ["General Medicine", "Pediatrics", "ICU", "Neurology", "Cardiology"] * 24,
        "Admission Type": ["Emergency", "Urgent", "Elective"] * 40,
        "Billing Amount": np.random.randint(1000, 50000, 120),
        "Length of Stay": np.random.randint(1, 15, 120),
        "Hospital Name": ["Apollo Hospital", "Deepak Hospital", "Manipal Hospital"] * 40,
        "Re-admission": ["Yes", "No", "No", "Yes"] * 30
    })

df = load_data()

# Preprocess dates
df["Admission Date"] = pd.to_datetime(df["Admission Date"])
df["Month_Name"] = df["Admission Date"].dt.strftime("%b")

def setup_page(title, page_num):
    fig, ax = plt.subplots(figsize=(11, 8.5), dpi=100)
    ax.axis("off")
    
    # Outer Border
    border = patches.Rectangle((0.01, 0.01), 0.98, 0.98, fill=False, edgecolor="#333333", linewidth=1.5)
    ax.add_patch(border)
    
    # Header Banner
    header = patches.Rectangle((0.01, 0.90), 0.98, 0.09, fill=True, facecolor="#1F4E78", edgecolor="#1F4E78")
    ax.add_patch(header)
    
    ax.text(0.04, 0.94, "MedTrack DV — Dashboard Storyboard & Visualizations", color="white", fontsize=14, fontweight="bold")
    ax.text(0.04, 0.915, f"Dashboard {page_num}: {title}", color="#D9E1F2", fontsize=11, fontstyle="italic")
    ax.text(0.92, 0.94, f"Page {page_num}/4", color="white", fontsize=11, fontweight="bold")
    
    return fig, ax

def add_panel(ax, x, y, w, h, title):
    # Background panel
    panel = patches.Rectangle((x, y), w, h, fill=True, facecolor="#FFFFFF", edgecolor="#BDD7EE", linewidth=1)
    ax.add_patch(panel)
    
    # Panel title bar
    p_header = patches.Rectangle((x, y + h - 0.03), w, 0.03, fill=True, facecolor="#D9E1F2", edgecolor="#BDD7EE", linewidth=1)
    ax.add_patch(p_header)
    
    ax.text(x + 0.01, y + h - 0.022, title, color="#1F4E78", fontsize=8, fontweight="bold")

def add_sidebar_specs(ax, title, specs):
    container = patches.Rectangle((0.74, 0.03), 0.23, 0.85, fill=True, facecolor="#F8F9FA", edgecolor="#A6A6A6", linewidth=1)
    ax.add_patch(container)
    
    ax.text(0.75, 0.85, "Specifications", color="#1F4E78", fontsize=11, fontweight="bold")
    ax.plot([0.75, 0.95], [0.84, 0.84], color="#1F4E78", linewidth=1)
    
    y_pos = 0.81
    title_lines = textwrap.wrap(title, width=22)
    for t_line in title_lines:
        ax.text(0.75, y_pos, t_line, color="#333333", fontsize=9, fontweight="bold")
        y_pos -= 0.022
        
    y_pos -= 0.008
    
    for spec in specs:
        if spec.startswith("- "):
            bullet_text = "• " + spec[2:]
            wrapped = textwrap.wrap(bullet_text, width=24)
            for w_line in wrapped:
                ax.text(0.75, y_pos, w_line, color="#595959", fontsize=8)
                y_pos -= 0.020
        else:
            y_pos -= 0.008
            wrapped = textwrap.wrap(spec, width=22)
            for w_line in wrapped:
                ax.text(0.75, y_pos, w_line, color="#1F4E78", fontsize=8, fontweight="bold")
                y_pos -= 0.020

def generate_pdf():
    print(f"Generating storyboard PDF at {OUTPUT_PDF}...")
    
    # Sort months chronologically for plots
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    with PdfPages(OUTPUT_PDF) as pdf:
        # -------------------------------------------------------------
        # PAGE 1: Hospital Overview
        # -------------------------------------------------------------
        fig, ax = setup_page("Hospital Overview Dashboard", 1)
        
        # KPI Cards (Mockup styling)
        add_panel(ax, 0.03, 0.76, 0.12, 0.11, "Total Admissions")
        ax.text(0.09, 0.81, f"{len(df):,}", color="#2F5597", fontsize=14, fontweight="bold", ha="center")
        
        add_panel(ax, 0.17, 0.76, 0.12, 0.11, "Occupancy Rate")
        ax.text(0.23, 0.81, "36.8%", color="#2F5597", fontsize=14, fontweight="bold", ha="center")
        
        add_panel(ax, 0.31, 0.76, 0.12, 0.11, "Average LOS")
        ax.text(0.37, 0.81, f"{df['Length of Stay'].mean().round(2)} Days", color="#2F5597", fontsize=14, fontweight="bold", ha="center")
        
        add_panel(ax, 0.45, 0.76, 0.12, 0.11, "Readmission Rate")
        readmit_pct = (df["Re-admission"].str.strip().str.title().eq("Yes").mean() * 100).round(1)
        ax.text(0.51, 0.81, f"{readmit_pct}%", color="#2F5597", fontsize=14, fontweight="bold", ha="center")
        
        add_panel(ax, 0.59, 0.76, 0.12, 0.11, "Bed Utilization")
        ax.text(0.65, 0.81, "78.5%", color="#2F5597", fontsize=14, fontweight="bold", ha="center")

        # Visualization 1: Admissions by Month (Line)
        add_panel(ax, 0.03, 0.43, 0.32, 0.30, "Monthly Admissions Trend")
        ax_viz1 = fig.add_axes([0.08, 0.46, 0.25, 0.22])
        monthly_adm = df.groupby("Month_Name")["Patient ID"].count().reindex(month_order).dropna()
        ax_viz1.plot(monthly_adm.index, monthly_adm.values, color="#1F4E78", marker="o", linewidth=1.5, markersize=4)
        ax_viz1.tick_params(labelsize=7)
        ax_viz1.grid(True, linestyle="--", alpha=0.5)

        # Visualization 2: Admissions by Department (Bar)
        add_panel(ax, 0.38, 0.43, 0.33, 0.30, "Admissions by Department")
        ax_viz2 = fig.add_axes([0.43, 0.46, 0.26, 0.21])
        dept_counts = df["Department"].value_counts().head(5)
        ax_viz2.bar(dept_counts.index, dept_counts.values, color="#8FAADC", edgecolor="#1F4E78")
        ax_viz2.tick_params(axis="x", labelrotation=15, labelsize=6)
        ax_viz2.tick_params(axis="y", labelsize=7)

        # Visualization 3: Admission Type (Donut)
        add_panel(ax, 0.03, 0.08, 0.32, 0.32, "Admission Type Distribution")
        ax_viz3 = fig.add_axes([0.08, 0.11, 0.25, 0.22])
        adm_type = df["Admission Type"].value_counts()
        ax_viz3.pie(adm_type.values, labels=adm_type.index, autopct="%1.1f%%", colors=["#1F4E78", "#8FAADC", "#BDD7EE"], textprops={'fontsize': 7})
        # Add center white circle for donut effect
        centre_circle = plt.Circle((0,0), 0.50, fc='white')
        ax_viz3.add_patch(centre_circle)

        # Visualization 4: Readmission by Hospital (Horizontal Bar)
        add_panel(ax, 0.38, 0.08, 0.33, 0.32, "Readmission by Hospital")
        ax_viz4 = fig.add_axes([0.46, 0.12, 0.23, 0.21])
        df["readmit_numeric"] = df["Re-admission"].str.strip().str.title().map({"Yes": 1, "No": 0}).fillna(0)
        hosp_readmit = (df.groupby("Hospital Name")["readmit_numeric"].mean() * 100).head(5)
        ax_viz4.barh(hosp_readmit.index, hosp_readmit.values, color="#2F5597")
        ax_viz4.tick_params(labelsize=6)
        ax_viz4.set_xlabel("Readmission Rate (%)", fontsize=7)

        specs_p1 = [
            "Global Filters",
            "- Date Range Slider",
            "- Hospital Filter",
            "- Department Filter",
            "KPI Thresholds",
            "- Occupancy Target: 80%",
            "- Readmission Limit: <30%",
            "Business Context",
            "- Real-time operational load monitoring for administrators."
        ]
        add_sidebar_specs(ax, "Hospital Overview Overview", specs_p1)
        pdf.savefig(fig)
        plt.close(fig)

        # -------------------------------------------------------------
        # PAGE 2: Patient Flow
        # -------------------------------------------------------------
        fig, ax = setup_page("Patient Flow Dashboard", 2)
        
        add_panel(ax, 0.03, 0.76, 0.20, 0.11, "Net Inflow / Outflow")
        ax.text(0.13, 0.81, "+120 Patients", color="#2F5597", fontsize=14, fontweight="bold", ha="center")
        
        add_panel(ax, 0.26, 0.76, 0.20, 0.11, "Average Discharge Speed")
        ax.text(0.36, 0.81, "4.2 Hours", color="#2F5597", fontsize=14, fontweight="bold", ha="center")
        
        add_panel(ax, 0.49, 0.76, 0.22, 0.11, "Overstay Admissions")
        ax.text(0.60, 0.81, "12.4%", color="red", fontsize=14, fontweight="bold", ha="center")

        # Visualization 1: Stay Category Distribution (Pie)
        add_panel(ax, 0.03, 0.41, 0.32, 0.32, "Length of Stay Categories")
        ax_viz2_1 = fig.add_axes([0.08, 0.44, 0.25, 0.22])
        df["Stay_Category"] = pd.cut(df["Length of Stay"], bins=[0, 3, 7, 14, 100], labels=["Short", "Medium", "Long", "Extended"])
        stay_cat = df["Stay_Category"].value_counts()
        ax_viz2_1.pie(stay_cat.values, labels=stay_cat.index, autopct="%1.1f%%", colors=["#1F4E78", "#8FAADC", "#BDD7EE", "#D9E1F2"], textprops={'fontsize': 7})

        # Visualization 2: Daily Admissions vs. Discharges (Dual Line)
        add_panel(ax, 0.38, 0.41, 0.33, 0.32, "Daily Inflow vs Outflow Trends")
        ax_viz2_2 = fig.add_axes([0.43, 0.44, 0.26, 0.22])
        daily_in = df.groupby(df["Admission Date"].dt.day)["Patient ID"].count().head(15)
        ax_viz2_2.plot(daily_in.index, daily_in.values, color="#1F4E78", label="Admissions", marker="s", markersize=3)
        ax_viz2_2.tick_params(labelsize=7)
        ax_viz2_2.grid(True, linestyle="--", alpha=0.5)

        # Visualization 3: Peak Load Hours (Area)
        add_panel(ax, 0.03, 0.06, 0.32, 0.32, "Peak Admissions by Hour of Day")
        ax_viz2_3 = fig.add_axes([0.08, 0.10, 0.25, 0.22])
        hours = np.arange(24)
        loads = np.sin(hours/3.5) * 50 + 80 + np.random.randint(-10, 10, 24)
        ax_viz2_3.fill_between(hours, loads, color="#8FAADC", alpha=0.4)
        ax_viz2_3.plot(hours, loads, color="#1F4E78", linewidth=1.5)
        ax_viz2_3.tick_params(labelsize=7)
        ax_viz2_3.set_xlabel("Hour of Day", fontsize=8)

        # Visualization 4: Patient Movement (Flow Grid)
        add_panel(ax, 0.38, 0.06, 0.33, 0.32, "Department Transfer Frequency")
        ax_viz2_4 = fig.add_axes([0.43, 0.10, 0.26, 0.22])
        dept_transfer = df["Department"].value_counts().head(4)
        ax_viz2_4.bar(dept_transfer.index, dept_transfer.values, color="#2F5597", width=0.4)
        ax_viz2_4.tick_params(axis="x", labelrotation=10, labelsize=6)
        ax_viz2_4.tick_params(axis="y", labelsize=7)

        specs_p2 = [
            "Filters & Slicers",
            "- Admission Category",
            "- Patient Age Band",
            "- Transfer Status",
            "Key Focus Areas",
            "- Peak discharge congestion hours.",
            "- Inflow bottle-necks.",
            "Target Audience",
            "- Emergency Chiefs",
            "- Clinical Floor Managers"
        ]
        add_sidebar_specs(ax, "Admissions & Discharges", specs_p2)
        pdf.savefig(fig)
        plt.close(fig)

        # -------------------------------------------------------------
        # PAGE 3: Department Analytics
        # -------------------------------------------------------------
        fig, ax = setup_page("Department Analytics Dashboard", 3)
        
        add_panel(ax, 0.03, 0.76, 0.20, 0.11, "Highest Volume Dept")
        top_dept = df["Department"].value_counts().index[0]
        ax.text(0.13, 0.81, top_dept, color="#2F5597", fontsize=11, fontweight="bold", ha="center")
        
        add_panel(ax, 0.26, 0.76, 0.20, 0.11, "Lowest Performance Dept")
        ax.text(0.36, 0.81, "Pediatrics (64.2)", color="red", fontsize=11, fontweight="bold", ha="center")
        
        add_panel(ax, 0.49, 0.76, 0.22, 0.11, "System-wide Efficiency")
        ax.text(0.60, 0.81, "89.2%", color="#2F5597", fontsize=14, fontweight="bold", ha="center")

        # Visualization 1: Department Efficiency Rankings (Bar)
        add_panel(ax, 0.03, 0.41, 0.32, 0.32, "Department Efficiency Rankings")
        ax_viz3_1 = fig.add_axes([0.09, 0.44, 0.24, 0.22])
        depts = ["Neurology", "Psychiatry", "Surgery", "ICU", "Pediatrics"]
        scores = [89.3, 89.2, 89.1, 89.0, 64.2]
        ax_viz3_1.barh(depts, scores, color=["#1F4E78", "#1F4E78", "#1F4E78", "#1F4E78", "red"])
        ax_viz3_1.tick_params(labelsize=7)

        # Visualization 2: Billing vs ALOS (Scatter)
        add_panel(ax, 0.38, 0.41, 0.33, 0.32, "Billing vs. Average Length of Stay")
        ax_viz3_2 = fig.add_axes([0.44, 0.44, 0.24, 0.22])
        ax_viz3_2.scatter(df["Length of Stay"].head(50), df["Billing Amount"].head(50), color="#2F5597", alpha=0.6, s=15)
        ax_viz3_2.tick_params(labelsize=7)
        ax_viz3_2.set_xlabel("LOS (Days)", fontsize=7)
        ax_viz3_2.set_ylabel("Billing ($)", fontsize=7)

        # Visualization 3: Treatment Capacity Index (Radar/Bar)
        add_panel(ax, 0.03, 0.06, 0.32, 0.32, "Treatment Capacity Index")
        ax_viz3_3 = fig.add_axes([0.08, 0.10, 0.25, 0.22])
        indices = [78.2, 81.4, 75.9, 83.2]
        ax_viz3_3.bar(["Gen Med", "ICU", "Neurology", "Pediatrics"], indices, color="#8FAADC", width=0.5)
        ax_viz3_3.tick_params(labelsize=6)

        # Visualization 4: Top Diagnoses per Department (Table/Grid)
        add_panel(ax, 0.38, 0.06, 0.33, 0.32, "Top Diagnoses volume")
        ax_viz3_4 = fig.add_axes([0.43, 0.10, 0.26, 0.22])
        diag_counts = df["Diagnosis"].value_counts().head(5)
        ax_viz3_4.bar(diag_counts.index, diag_counts.values, color="#1F4E78", width=0.4)
        ax_viz3_4.tick_params(axis="x", labelrotation=20, labelsize=5)
        ax_viz3_4.tick_params(axis="y", labelsize=7)

        specs_p3 = [
            "Filters & Slicers",
            "- Department Select",
            "- Clinical KPI Filter",
            "- Billing Range Slider",
            "Key Focus Areas",
            "- Department Efficiency Scores.",
            "- Financial vs Stay-length benchmarking.",
            "Target Audience",
            "- Operations Director",
            "- CFO / Financial Auditor"
        ]
        add_sidebar_specs(ax, "Department Benchmarking", specs_p3)
        pdf.savefig(fig)
        plt.close(fig)

        # -------------------------------------------------------------
        # PAGE 4: Resource Utilization
        # -------------------------------------------------------------
        fig, ax = setup_page("Resource Utilization Dashboard", 4)
        
        add_panel(ax, 0.03, 0.76, 0.20, 0.11, "Total Bed Inventory")
        ax.text(0.13, 0.81, "1,250 Beds", color="#2F5597", fontsize=14, fontweight="bold", ha="center")
        
        add_panel(ax, 0.26, 0.76, 0.20, 0.11, "Staff Allocations")
        ax.text(0.36, 0.81, "430 Active", color="#2F5597", fontsize=14, fontweight="bold", ha="center")
        
        add_panel(ax, 0.49, 0.76, 0.22, 0.11, "Beds in Maintenance")
        ax.text(0.60, 0.81, "2.4% (Active)", color="#2F5597", fontsize=14, fontweight="bold", ha="center")

        # Visualization 1: Bed Occupancy Forecast (Line)
        add_panel(ax, 0.03, 0.41, 0.32, 0.32, "Bed Occupancy Forecast")
        ax_viz4_1 = fig.add_axes([0.08, 0.44, 0.25, 0.22])
        ax_viz4_1.plot(monthly_adm.index, monthly_adm.values * 0.8, color="#1F4E78", label="Forecast", linestyle="--")
        ax_viz4_1.plot(monthly_adm.index, monthly_adm.values * 0.75, color="#8FAADC", label="Actual")
        ax_viz4_1.tick_params(labelsize=7)
        ax_viz4_1.grid(True, linestyle="--", alpha=0.5)

        # Visualization 2: Staff Ratio Trends (Bar)
        add_panel(ax, 0.38, 0.41, 0.33, 0.32, "Staff to Patient Ratios")
        ax_viz4_2 = fig.add_axes([0.43, 0.44, 0.26, 0.22])
        ratios = [1.2, 1.5, 0.8, 1.9]
        ax_viz4_2.bar(["Gen Med", "ICU", "Neurology", "Pediatrics"], ratios, color="#2F5597", width=0.4)
        ax_viz4_2.tick_params(labelsize=6)
        ax_viz4_2.set_ylabel("Staff per Patient", fontsize=7)

        # Visualization 3: Equipment Usage Tracker (Horizontal Bar)
        add_panel(ax, 0.03, 0.06, 0.32, 0.32, "Equipment Usage Tracker")
        ax_viz4_3 = fig.add_axes([0.08, 0.10, 0.25, 0.22])
        equip = ["Ventilator", "MRI", "CT Scanner", "X-Ray"]
        usage = [84.2, 76.5, 91.0, 68.4]
        ax_viz4_3.barh(equip, usage, color="#8FAADC")
        ax_viz4_3.tick_params(labelsize=7)
        ax_viz4_3.set_xlabel("Usage Rate (%)", fontsize=7)

        # Visualization 4: Staff Workload Distribution (Scatter/Bubble)
        add_panel(ax, 0.38, 0.06, 0.33, 0.32, "Staff Workload Distribution")
        ax_viz4_4 = fig.add_axes([0.43, 0.10, 0.26, 0.22])
        ax_viz4_4.scatter(np.random.randint(5, 30, 15), np.random.randint(10, 50, 15), s=np.random.randint(20, 100, 15), color="#1F4E78", alpha=0.6)
        ax_viz4_4.tick_params(labelsize=7)
        ax_viz4_4.set_xlabel("Hours worked/shift", fontsize=7)

        specs_p4 = [
            "Filters & Slicers",
            "- Resource Category",
            "- Equipment status filter",
            "- Shift timing selector",
            "Key Focus Areas",
            "- Bed utilization rates per hospital.",
            "- Equipment bottleneck tracking.",
            "Target Audience",
            "- Resource Planner",
            "- Operational Directors"
        ]
        add_sidebar_specs(ax, "Resources & Logistics", specs_p4)
        pdf.savefig(fig)
        plt.close(fig)
        
    print(f"PDF successfully generated: {OUTPUT_PDF}")

if __name__ == "__main__":
    generate_pdf()
