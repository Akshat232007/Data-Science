import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Operations and Visualization using Dataset\\Resource\\Indias_Electricity_Consumption_Dataset.csv")

df["Dates"] = pd.to_datetime(df["Dates"])
first_10 = df.head(10)

plt.figure(figsize=(10, 5))
plt.bar(first_10["Dates"].dt.strftime("%d-%m"), 
        first_10["Total Consumption"])

plt.xlabel("Date")
plt.ylabel("Total Consumption")
plt.title("Electricity Consumption")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(df["Dates"], df["Maharashtra"])

plt.xlabel("Date")
plt.ylabel("Electricity Consumption")
plt.title("Maharashtra Electricity Consumption")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["Total Consumption"], bins=10)

plt.xlabel("Total Consumption")
plt.ylabel("Number of Days")
plt.title("Distribution of Electricity Consumption")
plt.show()


states = ["Maharashtra", "Gujarat", "Karnataka", "Tamil Nadu"]

values = [
    df["Maharashtra"].sum(),
    df["Gujarat"].sum(),
    df["Karnataka"].sum(),
    df["Tamil Nadu"].sum()
]

plt.figure(figsize=(7, 7))
plt.pie(values, labels=states, autopct="%1.1f%%")

plt.title("Electricity Consumption by State")
plt.show()