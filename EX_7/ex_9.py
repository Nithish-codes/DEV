import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# STEP 2: Load Dataset
df = pd.read_csv("employee_data.csv")

# STEP 3: EDA
print(df.head())
print("\nShape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nSummary:")
print(df.describe())

# Handle Missing Values
df.fillna(df.median(numeric_only=True), inplace=True)
df.fillna(df.mode().iloc[0], inplace=True)

print("\nMissing Values:")
print(df.isnull().sum())

# Explore Categorical Variables
print("\nDepartment:")
print(df["Department"].value_counts())

print("\nGender:")
print(df["Gender"].value_counts())

# STEP 4: Visualizations

# a. Distribution of Age
plt.figure(figsize=(6,4))
sns.histplot(df["Age"], kde=True)
plt.title("Distribution of Age")
plt.show()

# b. Performance Rating by Department
plt.figure(figsize=(6,4))
sns.boxplot(x="Department", y="PerformanceRating", data=df)
plt.title("Performance Ratings by Department")
plt.xticks(rotation=45)
plt.show()

# STEP 5: Analysis Report
print("\n--- Analysis Report ---")
print("Average Age:", round(df["Age"].mean(), 2))
print("Average Performance Rating:",
      round(df["PerformanceRating"].mean(), 2))
print("Average Salary:", round(df["Salary"].mean(), 2))

print("\nEDA and visualization completed successfully.")