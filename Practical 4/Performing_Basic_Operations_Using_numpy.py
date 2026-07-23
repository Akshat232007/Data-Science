import numpy as np

print('S087 Akshat Halwai')

arr = np.array([10, 20, 30, 40, 50])
print(f"Original Array: {arr}")

print(f"First element: {arr[0]},\n Last element: {arr[-1]}")

arr = np.append(arr, 60)
print(f"Append(60): {arr}")

arr = np.insert(arr, 2, 25)
print(f"Insert at index 2 (25): {arr}")

arr[1] = 15
print(f"Updating index 1 to 15: {arr}")
