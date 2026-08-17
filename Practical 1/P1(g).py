students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent Details:")

total = 0
highest_name = ""
highest_marks = 0

for name in students:
    print(name, ":", students[name])

    total += students[name]

    if students[name] > highest_marks:
        highest_marks = students[name]
        highest_name = name

average = total / 5

print("\nClass Average:", average)
print("Student with Highest Marks:", highest_name)
print("Highest Marks:", highest_marks)
