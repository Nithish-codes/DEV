import matplotlib.pyplot as plt
import pandas as pd

# 1. Load the dataset
# Replace 'Gold.csv' with your actual file path if needed
df = pd.read_csv("Gold.csv")

# 2. Convert 'DATE' to datetime and set as index
df["DATE"] = pd.to_datetime(df["DATE"])
df = df.set_index("DATE")
df = df.sort_index()

# 3. Calculate a Simple Moving Average (e.g., 30-day window)
df["SMA"] = df["VALUE"].rolling(window=30).mean()

# 4. Plot the time series data
plt.figure(figsize=(12, 6))
plt.plot(df.index, df["VALUE"], label="Gold Price", color="goldenrod", alpha=0.6)
plt.plot(
    df.index, df["SMA"], label="30-Day SMA", color="darkred", linewidth=1.5
)

plt.title("Gold Price Time Series Analysis")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.tight_layout()
plt.show()

# 5. Print basic statistics
print(df["VALUE"].describe())