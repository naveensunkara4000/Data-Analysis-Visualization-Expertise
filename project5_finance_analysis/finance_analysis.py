import os
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PATH SETUP ----------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "stock_prices.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

REPORT_PATH = os.path.join(OUTPUT_DIR, "stock_analysis_report.txt")
PRICE_PLOT_PATH = os.path.join(OUTPUT_DIR, "closing_price_trend.png")
RETURN_PLOT_PATH = os.path.join(OUTPUT_DIR, "daily_returns.png")

# ---------------- LOAD DATA ----------------

df = pd.read_csv(DATA_PATH)

# ---------------- ANALYSIS ----------------

df["Daily_Return"] = df["Close"].pct_change()

avg_return = df["Daily_Return"].mean()
volatility = df["Daily_Return"].std()
max_close = df["Close"].max()
min_close = df["Close"].min()

# ---------------- SAVE REPORT ----------------

with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write("STOCK MARKET ANALYSIS REPORT\n")
    f.write("============================\n\n")
    f.write(f"Average Daily Return: {avg_return:.4f}\n")
    f.write(f"Volatility (Risk): {volatility:.4f}\n")
    f.write(f"Maximum Closing Price: ₹{max_close}\n")
    f.write(f"Minimum Closing Price: ₹{min_close}\n\n")
    f.write("Daily Price Data:\n")
    f.write(df.to_string(index=False))

# ---------------- PRINT OUTPUT ----------------

print("STOCK MARKET ANALYSIS REPORT")
print("============================")
print(f"Average Daily Return: {avg_return:.4f}")
print(f"Volatility (Risk): {volatility:.4f}")
print(f"Maximum Closing Price: ₹{max_close}")
print(f"Minimum Closing Price: ₹{min_close}")

# ---------------- VISUALIZATIONS ----------------

# Closing price trend
plt.figure(figsize=(8, 5))
plt.plot(df["Date"], df["Close"], marker="o")
plt.title("Closing Price Trend")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(PRICE_PLOT_PATH)
plt.close()

# Daily returns
plt.figure(figsize=(8, 5))
plt.bar(df["Date"], df["Daily_Return"])
plt.title("Daily Returns")
plt.xlabel("Date")
plt.ylabel("Return")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(RETURN_PLOT_PATH)
plt.close()

print("\n Outputs saved successfully!")
print(" Report:", REPORT_PATH)
print(" Price Plot:", PRICE_PLOT_PATH)
print(" Return Plot:", RETURN_PLOT_PATH)
