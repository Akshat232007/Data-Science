import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 40]
y2 = [50, 40, 30, 20, 10]

plt.subplot(1, 2, 1)
plt.plot(x, y1, color='blue')

plt.subplot(1, 2, 2)
plt.scatter(x, y2, color='red')

plt.tight_layout()
plt.show()