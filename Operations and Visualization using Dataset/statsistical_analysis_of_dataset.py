import pandas as pd

df = pd.read_csv("Operations and Visualization using Dataset\\Resource\\plant_growth_data.csv")

print("Average Growth Milestone:")
print(df["Growth_Milestone"].mean())

print("\nMaximum Growth Milestone:")
print(df["Growth_Milestone"].max())

print("\nMinimum Growth Milestone:")
print(df["Growth_Milestone"].min())

print("\nMedian Growth Milestone:")
print(df["Growth_Milestone"].median())

print("\nStandard Deviation:")
print(df["Growth_Milestone"].std())

print("\nAverage Sunlight Hours:")
print(df["Sunlight_Hours"].mean())

print("\nNumber of Plants:")
print(len(df))

print("\nPlants with Growth Milestone greater than 0:")
print((df["Growth_Milestone"] > 0).sum())