import pandas as pd

df = pd.read_csv("Operations and Visualization using Dataset\\Resource\\vgsales.csv")

print("Number of Games in Each Genre:")
print(df.groupby("Genre")["Name"].count())

print("\nAverage Global Sales by Genre:")
print(df.groupby("Genre")["Global_Sales"].mean())

print("\nMaximum Global Sales by Genre:")
print(df.groupby("Genre")["Global_Sales"].max())

print("\nAverage North American Sales by Genre:")
print(df.groupby("Genre")["NA_Sales"].mean())