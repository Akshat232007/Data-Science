import numpy as np

print('S087 Akshat Halwai')

n = int(input('Enter Number of element : '))

elements = []
for i in range(1, n + 1):
    elements.append(int(input(f"Enter No {i} Element : ")))

arr = np.array(elements)

max_val = arr[0]
min_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print(f"\nArray: {arr}")
print(f"Maximum Element: {max_val}")
print(f"Minimum Element: {min_val}")
