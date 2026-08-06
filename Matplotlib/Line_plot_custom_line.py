import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', linestyle='-', color='b')

plt.title("Simple Line Plot")
plt.xlabel("Numbers")
plt.ylabel("Doubles")
plt.grid(True)

plt.show()