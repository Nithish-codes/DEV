import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re

df = pd.read_csv("emails.csv")
df['Email_Length'] = df['Body'].astype(str).apply(len)

# 1. Length Distribution
sns.histplot(df['Email_Length'], bins=50)
plt.show()

# 2. Word Cloud
text = " ".join(df['Body'].dropna())
wordcloud = WordCloud(background_color='white').generate(text)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

# 3. Top 20 Words
words = re.findall(r'\w+', text.lower())
freq_df = pd.DataFrame(Counter(words).most_common(20), columns=['Word', 'Frequency'])
sns.barplot(data=freq_df, x='Frequency', y='Word')
plt.show()
