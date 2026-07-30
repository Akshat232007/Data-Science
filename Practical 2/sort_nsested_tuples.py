students = (
    ("Rohan", "B", 20),
    ("Ajay", "A", 21),
    ("Karan", "A", 19),
)

def sort_key(student):
    name, grade, age = student
    return (grade, age)


sorted_students = sorted(students, key=sort_key)

print("Sorted by Grade, then Age:")
for student in sorted_students:
    print(student)