
import seaborn as sns
import matplotlib.pyplot as plt


iris = sns.load_dataset("iris")
print(iris.head())

sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=iris)

plt.title("Iris Petal Length vs Width")
plt.show()
