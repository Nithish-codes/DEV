import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("emails.csv")
df['Email_Length'] = df['Body'].astype(str).apply(len)
df['Subject_Length'] = df['Subject'].astype(str).apply(len)
df['Hour'] = pd.to_datetime(df['Date']).dt.hour

numerical_df = df[['Email_Length', 'Subject_Length', 'Attachments', 'Hour']]
sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Matrix")
plt.show()
