import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.random.uniform(5, 12, 60)
y = 115 - 3 * x + np.random.normal(0, 4, 60)

plt.scatter(x, y, color='green', s=100)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.show()