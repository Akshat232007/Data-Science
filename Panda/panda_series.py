import pandas as pd

student_scores = {"Akshat": 85, "Pratik": 92, "Tejas": 78, "Aditya": 88}

series = pd.Series(student_scores)

print("Pandas Series created from dictionary:")
print(series)