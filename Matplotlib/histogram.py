import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(size=100)
plt.hist(data, bins=20)
plt.grid()
plt.show()