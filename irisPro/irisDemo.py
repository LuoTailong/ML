import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

sns.set(style="ticks")

df = sns.load_dataset("iris")
sns.pairplot(df, hue="species")

plt.show()

iris = load_iris()
df = pd.read_csv("./iris.csv")
print(df)
