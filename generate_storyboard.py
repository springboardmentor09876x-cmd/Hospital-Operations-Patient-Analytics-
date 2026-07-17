"""Dashboard Storyboard Generation Script (Module 4)

This script programmatically generates a professional, 4-page PDF document 
containing the wireframe layouts and design specifications for the 
four dashboards in the MedTrack_DV Tableau workbook.
"""

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as patches

# Set non-interactive backend
import matplotlib
matplotlib.use("Agg")

OUTPUT_PDF = "dashboard_storyboard.pdf"

def setup_page(title, page_num):
    fig, ax = plt.subplots(figsize=(11, 8.5), dpi=100)
    ax.axis("off")
    
    # Draw page border
    border = patches.Rectangle((0.01, 0.01), 0.98, 0.98, fill=False, edgecolor="#333333", linewidth=1.5)
    ax.add_patch(border)
    
    # Draw header bar
    header = patches.Rectangle((0.01, 0.90), 0.98, 0.09, fill=True, facecolor="#1F4E78", edgecolor="#1F4E78")
    ax.add_patch(header)
    
    # Header Text
    ax.text(0.04, 0.94, "MedTrack DV — Dashboard Storyboard & Layout", color="white", fontsize=14, fontweight="bold")
    ax.text(0.04, 0.915, f"Dashboard {page_num}: {title}", color="#D9E1F2", fontsize=11, fontstyle="italic")
    ax.text(0.92, 0.94, f"Page {page_num}/4", color="white", fontsize=11, fontweight="bold")
    
    return fig, ax

def add_panel(ax, x, y, w, h, title, content_type="chart", bg_color="#F2F4F7"):
    # Draw panel background
    panel = patches.Rectangle((x, y), w, h, fill=True, facecolor=bg_color, edgecolor="#BDD7EE", linewidth=1)
    ax.add_patch(panel)
    
    # Draw panel header
    p_header = patches.Rectangle((x, y + h - 0.03), w, 0.03, fill=True, facecolor="#D9E1F2", edgecolor="#BDD7EE", linewidth=1)
    ax.add_patch(p_header)
    
    # Panel Title
    ax.text(x + 0.01, y + h - 0.022, title, color="#1F4E78", fontsize=8, fontweight="bold")
    
    # Draw placeholder content
    cx, cy = x + w/2, y + (h - 0.03)/2
    if content_type == "chart":
        ax.plot([x + w*0.2, x + w*0.4, x + w*0.6, x + w*0.8], [y + h*0.2, y + h*0.6, y + h*0.3, y + h*0.7], color="#8FAADC", linewidth=1.5)
        ax.scatter([x + w*0.2, x + w*0.4, x + w*0.6, x + w*0.8], [y + h*0.2, y + h*0.6, y + h*0.3, y + h*0.7], color="#1F4E78", s=10)
    elif content_type == "kpi":
        ax.text(cx, cy + 0.01, "0,000", color="#2F5597", fontsize=12, fontweight="bold", ha="center", va="center")
        ax.text(cx, cy - 0.015, "▲ 0.0% vs LY", color="green", fontsize=7, ha="center", va="center")
    elif content_type == "map":
        ax.text(cx, cy, "[India Map View]", color="#7F7F7F", fontsize=9, ha="center", va="center", style="italic")
        # Draw placeholder map outline
        ax.plot([cx-w*0.2, cx, cx+w*0.2, cx, cx-w*0.2], [cy-h*0.2, cy+h*0.2, cy, cy-h*0.2, cy-h*0.2], color="#A6A6A6", linestyle="--", linewidth=1)
    elif content_type == "table":
        ax.text(cx, cy, "[Top List/Table Grid]", color="#7F7F7F", fontsize=9, ha="center", va="center", style="italic")
        for i in range(3):
            yy = y + h*0.2 + i*0.015
            ax.plot([x+w*0.1, x+w*0.9], [yy, yy], color="#D9D9D9", linewidth=0.8)

def add_sidebar_specs(ax, title, specs):
    # Draw specifications panel container
    container = patches.Rectangle((0.74, 0.03), 0.23, 0.85, fill=True, facecolor="#F8F9FA", edgecolor="#A6A6A6", linewidth=1)
    ax.add_patch(container)
    
    # Specs Header
    ax.text(0.75, 0.85, "Specifications", color="#1F4E78", fontsize=11, fontweight="bold")
    ax.plot([0.75, 0.95], [0.84, 0.84], color="#1F4E78", linewidth=1)
    
    # Subtitle
    ax.text(0.75, 0.82, title, color="#333333", fontsize=9, fontweight="bold")
    
    # List specs
    y_pos = 0.77
    for spec in specs:
        if spec.startswith("- "):
            ax.text(0.75, y_pos, "• " + spec[2:], color="#595959", fontsize=8, wrap=True)
            y_pos -= 0.035
        else:
            y_pos -= 0.01
            ax.text(0.75, y_pos, spec, color="#1F4E78", fontsize=8, fontweight="bold")
            y_pos -= 0.025

def generate_pdf():
    print(f"Generating storyboard PDF at {OUTPUT_PDF}...")
    
    with PdfPages(OUTPUT_PDF) as pdf:
        # -------------------------------------------------------------
        # PAGE 1: Hospital Overview
        # -------------------------------------------------------------
        fig, ax = setup_page("Hospital Overview Dashboard", 1)
        
        # Draw KPI Scorecards (Top)
        add_panel(ax, 0.03, 0.76, 0.10, 0.11, "Total Admissions", "kpi")
        add_panel(ax, 0.15, 0.76, 0.10, 0.11, "Occupancy Rate", "kpi")
        add_panel(ax, 0.27, 0.76, 0.10, 0.11, "Avg Stay (LOS)", "kpi")
        add_panel(ax, 0.39, 0.76, 0.10, 0.11, "Readmission Rate", "kpi")
        add_panel(ax, 0.51, 0.76, 0.10, 0.11, "Bed Util. Rate", "kpi")
        add_panel(ax, 0.63, 0.76, 0.09, 0.11, "Discharges", "kpi")
        
        # Row 2 Panels
        add_panel(ax, 0.03, 0.50, 0.22, 0.22, "Admissions Trend", "chart")
        add_panel(ax, 0.27, 0.50, 0.22, 0.22, "Occupancy Rate Trend", "chart")
        add_panel(ax, 0.51, 0.50, 0.21, 0.22, "Readmission Rate Trend", "chart")
        
        # Row 3 Panels
        add_panel(ax, 0.03, 0.24, 0.22, 0.22, "Admissions by Patient Type", "chart")
        add_panel(ax, 0.27, 0.24, 0.22, 0.22, "Admissions by Department", "chart")
        add_panel(ax, 0.51, 0.24, 0.21, 0.22, "ALOS by Department", "chart")
        
        # Row 4 Panels
        add_panel(ax, 0.03, 0.03, 0.32, 0.18, "Admissions by Region Map", "map")
        add_panel(ax, 0.38, 0.03, 0.34, 0.18, "Top 5 Hospitals by Occupancy", "table")
        
        # Sidebar specs
        specs_p1 = [
            "Filters & Slicers",
            "- Date Range Selector",
            "- Hospital Filter",
            "- Department Filter",
            "- Region Filter",
            "Key Focus Areas",
            "- Overall operational health",
            "- Admissions and occupancy trends",
            "- Readmission alert tracking",
            "Target Audience",
            "- Hospital Administrators",
            "- Healthcare Managers"
        ]
        add_sidebar_specs(ax, "Overall KPIs & Trends", specs_p1)
        
        pdf.savefig(fig)
        plt.close(fig)

        # -------------------------------------------------------------
        # PAGE 2: Patient Flow
        # -------------------------------------------------------------
        fig, ax = setup_page("Patient Flow Dashboard", 2)
        
        # Top KPI bar
        add_panel(ax, 0.03, 0.76, 0.15, 0.11, "Total Admissions", "kpi")
        add_panel(ax, 0.20, 0.76, 0.15, 0.11, "Discharge Count", "kpi")
        add_panel(ax, 0.37, 0.76, 0.15, 0.11, "Avg Length of Stay", "kpi")
        add_panel(ax, 0.54, 0.76, 0.18, 0.11, "Net Flow (In vs Out)", "kpi")
        
        # Main charts
        add_panel(ax, 0.03, 0.40, 0.33, 0.32, "Daily Admissions vs Discharges", "chart")
        add_panel(ax, 0.39, 0.40, 0.33, 0.32, "Peak Load Hours Tracker", "chart")
        
        add_panel(ax, 0.03, 0.03, 0.33, 0.33, "Department Transfer Flow", "chart")
        add_panel(ax, 0.39, 0.03, 0.33, 0.33, "Stay Category Breakdown", "chart")
        
        # Sidebar specs
        specs_p2 = [
            "Filters & Slicers",
            "- Month/Quarter Select",
            "- Admission Type",
            "- Patient Age/Gender",
            "Key Focus Areas",
            "- Discharge tracking speed",
            "- Hourly load bottlenecks",
            "- Stay Category distribution",
            "Target Audience",
            "- Operations Staff",
            "- Emergency Coordinators"
        ]
        add_sidebar_specs(ax, "Admissions & Discharges", specs_p2)
        
        pdf.savefig(fig)
        plt.close(fig)

        # -------------------------------------------------------------
        # PAGE 3: Department Analytics
        # -------------------------------------------------------------
        fig, ax = setup_page("Department Analytics Dashboard", 3)
        
        # Top KPI bar
        add_panel(ax, 0.03, 0.76, 0.15, 0.11, "Dept Admissions", "kpi")
        add_panel(ax, 0.20, 0.76, 0.15, 0.11, "Avg ALOS per Dept", "kpi")
        add_panel(ax, 0.37, 0.76, 0.15, 0.11, "Readmit Rate per Dept", "kpi")
        add_panel(ax, 0.54, 0.18, 0.18, 0.11, "Efficiency Score", "kpi")
        
        # Layout panels
        add_panel(ax, 0.03, 0.40, 0.48, 0.32, "Department Efficiency Rankings", "chart")
        add_panel(ax, 0.54, 0.40, 0.18, 0.32, "Billing vs ALOS", "chart")
        
        add_panel(ax, 0.03, 0.03, 0.33, 0.33, "Treatment Capacity Index", "chart")
        add_panel(ax, 0.39, 0.03, 0.33, 0.33, "Top Diagnoses per Department", "table")
        
        # Sidebar specs
        specs_p3 = [
            "Filters & Slicers",
            "- Department Selector",
            "- Doctor In Charge",
            "- Billing Bracket",
            "Key Focus Areas",
            "- Efficiency Score calculation",
            "- Diagnosis volumes per dept",
            "- Performance benchmarking",
            "Target Audience",
            "- Clinical Chiefs",
            "- Quality Review Board"
        ]
        add_sidebar_specs(ax, "Department Benchmarking", specs_p3)
        
        pdf.savefig(fig)
        plt.close(fig)

        # -------------------------------------------------------------
        # PAGE 4: Resource Utilization
        # -------------------------------------------------------------
        fig, ax = setup_page("Resource Utilization Dashboard", 4)
        
        # Top KPI bar
        add_panel(ax, 0.03, 0.76, 0.15, 0.11, "Beds Available", "kpi")
        add_panel(ax, 0.20, 0.76, 0.15, 0.11, "ICU Bed Count", "kpi")
        add_panel(ax, 0.37, 0.76, 0.15, 0.11, "Staff Count", "kpi")
        add_panel(ax, 0.54, 0.76, 0.18, 0.11, "Bed Utilization %", "kpi")
        
        # Main charts
        add_panel(ax, 0.03, 0.40, 0.33, 0.32, "Bed Occupancy Forecast", "chart")
        add_panel(ax, 0.39, 0.40, 0.33, 0.32, "Staff to Patient Ratio Trends", "chart")
        
        add_panel(ax, 0.03, 0.03, 0.33, 0.33, "Equipment Usage Tracker", "chart")
        add_panel(ax, 0.39, 0.03, 0.33, 0.33, "Staff Workload Distribution", "chart")
        
        # Sidebar specs
        specs_p4 = [
            "Filters & Slicers",
            "- Resource Category",
            "- Staff shift / Department",
            "- Equipment status filter",
            "Key Focus Areas",
            "- Underutilized bed capacity",
            "- Nurse/Doctor allocation rates",
            "- Equipment wear & usage hours",
            "Target Audience",
            "- Resource Planners",
            "- Operations Directors"
        ]
        add_sidebar_specs(ax, "Resources & Logistics", specs_p4)
        
        pdf.savefig(fig)
        plt.close(fig)
        
    print(f"PDF successfully generated: {OUTPUT_PDF}")

if __name__ == "__main__":
    generate_pdf()
