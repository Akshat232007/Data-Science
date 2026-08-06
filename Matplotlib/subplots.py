import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 4]
data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7]

plt.subplot(2, 2, 1)
plt.plot(x, y, color='blue')
plt.title('Line Plot')

plt.subplot(2, 2, 2)
plt.bar(categories, values, color='orange')
plt.title('Bar Chart')

plt.subplot(2, 2, 3)
plt.scatter(x, values, color='green')
plt.title('Scatter Plot')

plt.subplot(2, 2, 4)
plt.hist(data, color='purple')
plt.title('Histogram')

plt.tight_layout()
plt.show()