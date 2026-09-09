import pandas as pd

df = pd.read_csv("Operations and Visualization using Dataset\\Resource\\Data_mobile_usage_among_youngsters.csv")

print("Original Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull())

print("\nCount of Missing Values:")
print(df.isnull().sum())

df["age"] = df["age"].fillna(df["age"].mean())

df["device_hours_per_day"] = df["device_hours_per_day"].fillna(
    df["device_hours_per_day"].mean()
)

df["study_mins"] = df["study_mins"].fillna(
    df["study_mins"].mean()
)

df["sleep_hours"] = df["sleep_hours"].fillna(
    df["sleep_hours"].mean()
)

print("\nCleaned Dataset:")
print(df)