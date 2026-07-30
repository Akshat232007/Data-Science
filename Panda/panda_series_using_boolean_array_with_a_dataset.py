import pandas as pd

df = pd.read_csv('Cleaned_NSUT.csv')

pm25_series = df['PM2.5']

boolean_mask = pm25_series > 150

filtered_pm25 = pm25_series[boolean_mask]

print("Boolean Mask (First 5 entries):")
print(boolean_mask.head())
print("-" * 40)

print(f"Filtered PM2.5 Series (Values > 150, total count: {len(filtered_pm25)}):")
print(filtered_pm25.head(10))