import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("emails.csv")

# Top 10 Senders
df['Sender'].value_counts().head(10).plot(kind='barh')
plt.title("Top 10 Senders")
plt.show()

# Domain Analysis
df['Domain'] = df['Sender'].str.split('@').str[1]
df['Domain'].value_counts().head(10).plot(kind='pie', autopct='%1.1f%%')
plt.title("Domain Distribution")
plt.show()
