import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("wine_quality_dataset.csv")

# Historgram (quality)
plt.hist(df['quality'])
plt.title("Histogram")
plt.show()

# Heatmap
freq_df = pd.DataFrame(df[["fixed acidity","volatile acidity","citric acid","residual sugar"]])
sns.heatmap(freq_df.corr(), annot=True, cmap='hot', fmt=".2f")
plt.title("Heatmap")
plt.show()

# Boxplot (quality, alcohol)
sns.boxplot(x=df['quality'], y=df['alcohol'])
plt.title("Boxplot")
plt.show()

# Pairplot
sns.pairplot(df[["fixed acidity","volatile acidity","citric acid","residual sugar","quality"]], hue="quality")
plt.show()


