import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("emails.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Hour'] = df['Date'].dt.hour
df['Weekday'] = df['Date'].dt.day_name()

# 1. Monthly Volume
df.groupby('Month').size().plot(kind='bar')
plt.title("Emails Per Month")
plt.show()

# 2. Weekday Distribution
sns.countplot(data=df, x='Weekday', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title("Day-wise Activity")
plt.show()

# 3. Hourly Pattern
hourly = df['Hour'].value_counts().sort_index()
sns.lineplot(x=hourly.index, y=hourly.values)
plt.title("Hourly Pattern")
plt.show()
