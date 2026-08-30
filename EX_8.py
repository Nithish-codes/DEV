import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


file_path = "wine_quality_dataset.csv"
df = pd.read_csv(file_path)

# 2. Data Inspection & Summary Statistics
print("--- Dataset Shape ---")
print(df.shape)

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Summary Statistics ---")
print(df.describe().T)

print("\n--- Correlation with Quality ---")
corr = df.corr(numeric_only=True)["quality"].drop("quality").sort_values(ascending=False)
print(corr)

# 3. Feature Engineering (Adding Extra Features)
# Feature 1: Bound SO2 (Total SO2 minus Free SO2)
df["bound_so2"] = df["total sulfur dioxide"] - df["free sulfur dioxide"]

# Feature 2: Free-to-Total SO2 Ratio
df["so2_ratio"] = df["free sulfur dioxide"] / df["total sulfur dioxide"]

# Feature 3: Quality Category Grouping
df["quality_group"] = df["quality"].apply(
    lambda x: "High (>=7)" if x >= 7 else "Low/Avg (<7)"
)

# Set global Seaborn theme
sns.set_theme(style="whitegrid")


# FIGURE 1: Core EDA Summary Dashboard
fig1, axes1 = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1.1: Quality Rating Distribution
sns.countplot(
    data=df, x="quality", hue="quality", palette="viridis", ax=axes1[0, 0]
)
if axes1[0, 0].get_legend() is not None:
    axes1[0, 0].get_legend().remove()
axes1[0, 0].set_title("Distribution of Wine Quality Ratings", fontsize=12)
axes1[0, 0].set_xlabel("Quality Score")
axes1[0, 0].set_ylabel("Count")

# Add count annotations above bars
for p in axes1[0, 0].patches:
    if p.get_height() > 0:
        axes1[0, 0].annotate(
            f"{int(p.get_height())}",
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 5),
            textcoords="offset points",
        )

# Plot 1.2: Alcohol vs. Quality Boxplot
sns.boxplot(
    data=df, x="quality", y="alcohol", hue="quality", palette="Blues", ax=axes1[0, 1]
)
if axes1[0, 1].get_legend() is not None:
    axes1[0, 1].get_legend().remove()
axes1[0, 1].set_title("Alcohol Content by Wine Quality", fontsize=12)
axes1[0, 1].set_ylabel("Alcohol (% ABV)")

# Plot 1.3: Density vs. Residual Sugar Scatter Plot
sns.scatterplot(
    data=df,
    x="residual sugar",
    y="density",
    hue="quality",
    palette="coolwarm",
    alpha=0.6,
    ax=axes1[1, 0],
)
axes1[1, 0].set_title("Density vs Residual Sugar", fontsize=12)
axes1[1, 0].set_xlabel("Residual Sugar (g/dm³)")
axes1[1, 0].set_ylabel("Density (g/cm³)")
axes1[1, 0].set_xlim(0, 30)

# Plot 1.4: Feature Correlation Bar Chart
original_features = [col for col in df.columns if col not in ["bound_so2", "so2_ratio", "quality_group"]]
corr_sorted = df[original_features].corr()["quality"].drop("quality").sort_values()
colors = np.where(corr_sorted > 0, "skyblue", "salmon")
corr_sorted.plot(kind="barh", color=colors, ax=axes1[1, 1])
axes1[1, 1].set_title("Feature Correlation with Quality Score", fontsize=12)
axes1[1, 1].set_xlabel("Pearson Correlation Coefficient")

plt.tight_layout()
plt.savefig("wine_eda_summary.png", dpi=300)


# FIGURE 2: 5 Key Distributions & Engineered Features (3x2)
fig2, axes2 = plt.subplots(3, 2, figsize=(14, 12))

# 1. Distribution: Alcohol
sns.histplot(df["alcohol"], kde=True, color="purple", ax=axes2[0, 0])
axes2[0, 0].set_title("1. Distribution of Alcohol Content", fontsize=12)
axes2[0, 0].set_xlabel("Alcohol (% ABV)")

# 2. Residual Sugar
sns.histplot(df["residual sugar"], kde=True, color="teal", ax=axes2[0, 1])
axes2[0, 1].set_title("2. Distribution of Residual Sugar", fontsize=12)
axes2[0, 1].set_xlabel("Residual Sugar (g/dm³)")

# 3. Volatile Acidity
sns.histplot(df["volatile acidity"], kde=True, color="crimson", ax=axes2[1, 0])
axes2[1, 0].set_title("3. Distribution of Volatile Acidity", fontsize=12)
axes2[1, 0].set_xlabel("Volatile Acidity (g/dm³)")

# 4. Total Sulfur Dioxide
sns.histplot(df["total sulfur dioxide"], kde=True, color="darkorange", ax=axes2[1, 1])
axes2[1, 1].set_title("4. Distribution of Total Sulfur Dioxide", fontsize=12)
axes2[1, 1].set_xlabel("Total SO2 (mg/dm³)")

# 5. pH
sns.histplot(df["pH"], kde=True, color="forestgreen", ax=axes2[2, 0])
axes2[2, 0].set_title("5. Distribution of pH Levels", fontsize=12)
axes2[2, 0].set_xlabel("pH")

# 6. Bound SO2 by Quality Group
sns.boxplot(
    data=df,
    x="quality_group",
    y="bound_so2",
    hue="quality_group",
    palette="Set2",
    ax=axes2[2, 1],
)
if axes2[2, 1].get_legend() is not None:
    axes2[2, 1].get_legend().remove()
axes2[2, 1].set_title("6. Bound SO2 by Quality Group", fontsize=12)
axes2[2, 1].set_xlabel("Quality Category")
axes2[2, 1].set_ylabel("Bound SO2 (mg/dm³)")

plt.tight_layout()
plt.savefig("wine_distributions_and_features.png", dpi=300)
plt.show()
