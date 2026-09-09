import pandas as pd

df = pd.read_csv("Operations and Visualization using Dataset\\Resource\\nba.csv")

print("Player Name and Salary:")
print(df[["Name", "Salary"]])

print("\nPlayers older than 30:")
print(df[df["Age"] > 30])

print("\nPlayers with salary more than 5 million:")
print(df[df["Salary"] > 5000000])

print("\nPoint Guards:")
print(df[df["Position"] == "PG"])

print("\nBoston Celtics Players:")
print(df[df["Team"] == "Boston Celtics"])

print("\nPlayers older than 25 with salary above 5 million:")
print(df[(df["Age"] > 25) & (df["Salary"] > 5000000)])