import pandas as pd

df = pd.read_csv('Cleaned_NSUT.csv')

avg_aqi_dict = df.groupby('Month')['AQI'].mean().to_dict()

print("Original Dictionary:")
print(avg_aqi_dict)
print("-" * 40)


aqi_series = pd.Series(avg_aqi_dict)

print("Pandas Series created from Dictionary:")
print(aqi_series)