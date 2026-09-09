import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Amit", "Sneha", "Rahul", "Priya",
             "Neha", "Rohan", "Pooja", "Karan"],
    "Age": [19, 20, 19, 21, 20, 19, 21, 20],
    "Gender": ["Male", "Female", "Male", "Female",
               "Female", "Male", "Female", "Male"],
    "Course": ["BSc CS", "BSc CS", "BSc IT", "BSc CS",
               "BSc IT", "BSc CS", "BSc IT", "BSc CS"],
    "Marks": [78, 85, 67, 92, 88, 74, 81, 69]
}

df = pd.DataFrame(data)

print("Complete Dataset:")
print(df)

print("\nFirst 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

print("\nShape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nStatistical Information:")
print(df.describe())