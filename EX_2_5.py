import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("emails.csv")

df['Attachments'].value_counts().plot(kind='bar')
plt.title("Attachment Count Distribution")
plt.xlabel("Number of Attachments")
plt.ylabel("Email Count")
plt.show()
