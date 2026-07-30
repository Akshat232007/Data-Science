import pandas as p

data = {
    "Roll_No" : [1,2,3,4,5],
    "Name" : ["Akshat","Pratik","Tejas","Aditya","Suraj"],
    "Age" : [20,19,21,18,21],
}

Data_frame = p.DataFrame(data)

print(Data_frame)