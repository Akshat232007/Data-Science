import pandas as pd


df = pd.read_csv("Cleaned_NSUT.csv")


print("--- STATISTICAL SUMMARY ---")
print(df.describe())


print("\n--- SPECIFIC CALCULATIONS FOR AQI ---")
print("Average AQI (Mean):", df["AQI"].mean())
print("Middle Value (Median):", df["AQI"].median())
print("Lowest AQI (Min):", df["AQI"].min())
print("Highest AQI (Max):", df["AQI"].max())
print("Standard Deviation:", df["AQI"].std())

print("\n--- CORRELATION WITH AQI ---")
print(df[["PM2.5", "PM10", "NO2", "SO2", "CO", "Ozone", "AQI"]].corr())