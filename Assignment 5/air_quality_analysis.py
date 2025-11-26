
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Task 1: Data Loading
# ------------------------------
df = pd.read_csv("air_quality_raw.csv")
print(df.head())
print(df.info())
print(df.describe())

# ------------------------------
# Task 2: Data Cleaning
# ------------------------------
df["Date"] = pd.to_datetime(df["Date"])
df = df.dropna()
df = df[["Date", "PM2.5", "PM10", "AQI", "NO2", "SO2"]]

# ------------------------------
# Task 3: Statistical Analysis
# ------------------------------
# Daily Data Already Given
daily_avg = df[["PM2.5", "PM10"]].mean()

# Monthly Aggregation
df.set_index("Date", inplace=True)
monthly_avg = df.resample("ME")[["PM2.5", "PM10"]].mean()

aqi_min = df["AQI"].min()
aqi_max = df["AQI"].max()
aqi_std = df["AQI"].std()

print("Monthly Average:")
print(monthly_avg)
print("AQI Min:", aqi_min)
print("AQI Max:", aqi_max)
print("AQI Std Dev:", aqi_std)

# ------------------------------
# Task 4: Visualizations
# ------------------------------
plt.figure()
plt.plot(df.index, df["AQI"])
plt.title("Daily AQI Trend")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("daily_aqi.png")

plt.figure()
monthly_avg["PM2.5"].plot(kind="bar")
plt.title("Monthly Avg PM2.5")
plt.xlabel("Month")
plt.ylabel("PM2.5")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_pm25.png")

plt.figure()
plt.scatter(df["PM2.5"], df["PM10"])
plt.title("PM2.5 vs PM10 Scatter Plot")
plt.xlabel("PM2.5")
plt.ylabel("PM10")
plt.tight_layout()
plt.savefig("pm_scatter.png")

# Subplot
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(df.index, df["PM2.5"])
ax[0].set_title("Daily PM2.5")
ax[0].tick_params(axis="x", rotation=45)

ax[1].plot(df.index, df["PM10"])
ax[1].set_title("Daily PM10")
ax[1].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.savefig("subplot_pm.png")

# ------------------------------
# Task 5: Grouping
# ------------------------------
df["Month"] = df.index.month
month_group = df.groupby("Month")[["PM2.5", "PM10", "AQI"]].mean()
print(month_group)

# ------------------------------
# Task 6: Exporting
# ------------------------------
df.to_csv("cleaned_air_quality.csv")
