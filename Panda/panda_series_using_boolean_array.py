import pandas as pd

data = pd.Series([10, 25, 30, 45, 50], index=["a", "b", "c", "d", "e"])

mask = [True, False, True, False, True]

filtered_series = data[mask]

print("Original Series:")
print(data)

print("\nFiltered Series (using Boolean array):")
print(filtered_series)