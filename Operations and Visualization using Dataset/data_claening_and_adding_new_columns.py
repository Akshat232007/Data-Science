import pandas as pd

df = pd.read_csv("Operations and Visualization using Dataset\\Resource\\StudentsPerformance.csv")

df["Average"] = (
    df["math score"] +
    df["reading score"] +
    df["writing score"]
) / 3

df["Result"] = df["Average"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

def calculate_grade(marks):

    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(calculate_grade)

print("Updated Dataset:")
print(df)