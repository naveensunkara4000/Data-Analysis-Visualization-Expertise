import os
import sys
import pandas as pd

# Allow importing from src folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from data_utils import load_data, clean_data
from visualization_utils import bar_plot

# ---------------- PATHS ----------------

DATA_PATH = os.path.join(BASE_DIR, "data", "student_performance.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

REPORT_PATH = os.path.join(OUTPUT_DIR, "student_performance_report.txt")
PLOT_PATH = os.path.join(OUTPUT_DIR, "student_scores_bar.png")

# ---------------- LOAD & CLEAN DATA ----------------

df = load_data(DATA_PATH)
df = clean_data(df)

# ---------------- ANALYSIS ----------------

pass_mark = 40
df["Result"] = df["Score"].apply(lambda x: "Pass" if x >= pass_mark else "Fail")

pass_rate = (df["Result"] == "Pass").mean() * 100
attendance_corr = df["Attendance"].corr(df["Score"])

# ---------------- SAVE REPORT ----------------

with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write("STUDENT PERFORMANCE ANALYSIS REPORT\n")
    f.write("=================================\n\n")
    f.write(f"Pass Rate: {pass_rate:.2f}%\n")
    f.write(f"Attendance vs Score Correlation: {attendance_corr:.2f}\n\n")
    f.write(df.to_string(index=False))

# ---------------- VISUALIZATION ----------------

bar_plot(
    df=df,
    x="Name",
    y="Score",
    title="Student Score Distribution",
    save_path=PLOT_PATH
)

print("\n Project 2 executed using src utilities!")
print(" Report:", REPORT_PATH)
print(" Plot:", PLOT_PATH)
