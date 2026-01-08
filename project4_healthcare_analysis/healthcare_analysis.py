import os
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PATH SETUP ----------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "covid_data.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

REPORT_PATH = os.path.join(OUTPUT_DIR, "covid_analysis_report.txt")
CASE_PLOT_PATH = os.path.join(OUTPUT_DIR, "covid_cases_trend.png")
DEATH_PLOT_PATH = os.path.join(OUTPUT_DIR, "covid_deaths_trend.png")

# ---------------- LOAD DATA ----------------

df = pd.read_csv(DATA_PATH)

# ---------------- ANALYSIS ----------------

total_cases = df["Confirmed"].sum()
total_recoveries = df["Recovered"].sum()
total_deaths = df["Deaths"].sum()

mortality_rate = (total_deaths / total_cases) * 100
recovery_rate = (total_recoveries / total_cases) * 100

# ---------------- SAVE REPORT ----------------

with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write("COVID-19 HEALTHCARE ANALYSIS REPORT\n")
    f.write("=================================\n\n")
    f.write(f"Total Confirmed Cases: {total_cases}\n")
    f.write(f"Total Recovered Cases: {total_recoveries}\n")
    f.write(f"Total Deaths: {total_deaths}\n\n")
    f.write(f"Mortality Rate: {mortality_rate:.2f}%\n")
    f.write(f"Recovery Rate: {recovery_rate:.2f}%\n\n")
    f.write("Daily Data:\n")
    f.write(df.to_string(index=False))

# ---------------- PRINT OUTPUT ----------------

print("COVID-19 HEALTHCARE ANALYSIS REPORT")
print("=================================")
print(f"Total Confirmed Cases: {total_cases}")
print(f"Total Recovered Cases: {total_recoveries}")
print(f"Total Deaths: {total_deaths}")
print(f"Mortality Rate: {mortality_rate:.2f}%")
print(f"Recovery Rate: {recovery_rate:.2f}%")

# ---------------- VISUALIZATIONS ----------------

# Confirmed cases trend
plt.figure(figsize=(8, 5))
plt.plot(df["Date"], df["Confirmed"], marker="o", label="Confirmed")
plt.plot(df["Date"], df["Recovered"], marker="o", label="Recovered")
plt.title("COVID-19 Confirmed vs Recovered Cases")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(CASE_PLOT_PATH)
plt.close()

# Deaths trend
plt.figure(figsize=(8, 5))
plt.plot(df["Date"], df["Deaths"], color="red", marker="o")
plt.title("COVID-19 Deaths Trend")
plt.xlabel("Date")
plt.ylabel("Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(DEATH_PLOT_PATH)
plt.close()

print("\n Outputs saved successfully!")
print(" Report:", REPORT_PATH)
print(" Cases Plot:", CASE_PLOT_PATH)
print(" Deaths Plot:", DEATH_PLOT_PATH)
