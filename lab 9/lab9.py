import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
print(iris.head())

plt.plot(iris["sepal_length"])
plt.title("Line Plot: Sepal Length")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.show()

plt.scatter(iris["sepal_length"], iris["petal_length"])
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()

avg_petal = iris.groupby("species")["petal_length"].mean()
plt.bar(avg_petal.index, avg_petal.values)
plt.title("Bar Chart: Avg Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Avg Petal Length")
plt.show()

plt.hist(iris["sepal_width"], bins=10)
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
plt.show()

species_counts = iris["species"].value_counts()
plt.pie(species_counts, labels=species_counts.index, autopct="%1.1f%%")
plt.title("Pie Chart: Species Proportion")
plt.show()

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].hist(iris["sepal_length"])
ax[0].set_title("Sepal Length Histogram")

ax[1].pie(species_counts, labels=species_counts.index, autopct="%1.1f%%")
ax[1].set_title("Species Pie Chart")

plt.show()