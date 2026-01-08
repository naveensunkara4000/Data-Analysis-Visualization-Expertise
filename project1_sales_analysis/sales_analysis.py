import os
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PATH SETUP ----------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "supermarket_sales.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

# Create outputs folder if not exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

REPORT_PATH = os.path.join(OUTPUT_DIR, "sales_analysis_report.txt")
PLOT_PATH = os.path.join(OUTPUT_DIR, "daily_sales_trend.png")

# ---------------- LOAD DATA ----------------

df = pd.read_csv(DATA_PATH)

# ---------------- ANALYSIS ----------------

total_sales = df["Total"].sum()

best_products = (
    df.groupby("Product_Line")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

daily_sales = df.groupby("Date")["Total"].sum()

# ---------------- SAVE TEXT OUTPUT ----------------

with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write("SUPERMARKET SALES ANALYSIS REPORT\n")
    f.write("================================\n\n")
    f.write(f"Total Sales: ₹{total_sales:,.2f}\n\n")
    f.write("Top Product Lines (by Quantity Sold):\n")
    f.write(best_products.to_string())
    f.write("\n")

# Also print to terminal
print("SUPERMARKET SALES ANALYSIS REPORT")
print("================================")
print(f"Total Sales: ₹{total_sales:,.2f}")
print("\nTop Product Lines:")
print(best_products)

# ---------------- SAVE PLOT ----------------

plt.figure(figsize=(10, 5))
daily_sales.plot(marker="o")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(PLOT_PATH)
plt.close()

print("\n Output files saved successfully!")
print(" Report:", REPORT_PATH)
print(" Plot:", PLOT_PATH)
