import os
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PATH SETUP ----------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "weather.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

REPORT_PATH = os.path.join(OUTPUT_DIR, "weather_analysis_report.txt")
TEMP_PLOT_PATH = os.path.join(OUTPUT_DIR, "temperature_trend.png")
RAIN_PLOT_PATH = os.path.join(OUTPUT_DIR, "rainfall_distribution.png")

# ---------------- LOAD DATA ----------------

df = pd.read_csv(DATA_PATH)

# ---------------- ANALYSIS ----------------

avg_temp = df["Temperature"].mean()
max_temp = df["Temperature"].max()
min_temp = df["Temperature"].min()
total_rainfall = df["Rainfall"].sum()

# ---------------- SAVE REPORT ----------------

with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write("WEATHER DATA ANALYSIS REPORT\n")
    f.write("===========================\n\n")
    f.write(f"Average Temperature: {avg_temp:.2f} °C\n")
    f.write(f"Maximum Temperature: {max_temp:.2f} °C\n")
    f.write(f"Minimum Temperature: {min_temp:.2f} °C\n")
    f.write(f"Total Rainfall: {total_rainfall:.2f} mm\n\n")
    f.write("Daily Weather Data:\n")
    f.write(df.to_string(index=False))

# ---------------- PRINT OUTPUT ----------------

print("WEATHER DATA ANALYSIS REPORT")
print("===========================")
print(f"Average Temperature: {avg_temp:.2f} °C")
print(f"Maximum Temperature: {max_temp:.2f} °C")
print(f"Minimum Temperature: {min_temp:.2f} °C")
print(f"Total Rainfall: {total_rainfall:.2f} mm")

# ---------------- VISUALIZATIONS ----------------

# Temperature trend
plt.figure(figsize=(8, 5))
plt.plot(df["Date"], df["Temperature"], marker="o")
plt.title("Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(TEMP_PLOT_PATH)
plt.close()

# Rainfall distribution
plt.figure(figsize=(6, 4))
plt.bar(df["Date"], df["Rainfall"])
plt.title("Daily Rainfall")
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(RAIN_PLOT_PATH)
plt.close()

print("\n✅ Outputs saved successfully!")
print("📄 Report:", REPORT_PATH)
print("📊 Temperature Plot:", TEMP_PLOT_PATH)
print("🌧️ Rainfall Plot:", RAIN_PLOT_PATH)
