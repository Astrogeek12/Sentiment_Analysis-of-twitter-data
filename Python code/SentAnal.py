import numpy as np
import pandas as pd
# plotting
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# nltk
from nltk.stem import WordNetLemmatizer
# sklearn
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report

# DATASET_COLUMNS=['ids','ids','text']
# DATASET_ENCODING = "ISO-8859-1"
# df = pd.read_csv('Tweets.csv', encoding=DATASET_ENCODING, names=DATASET_COLUMNS)
# # df.shape
# # df.info
# print(df)
# # print(np.sum(df.isnull().any(axis=1)))
# # print('Count of columns in the data is:  ', len(df.columns))
# # print('Count of rows in the data is:  ', len(df))

# # Plotting the distribution for dataset.
# # ax = df.groupby('target').count().plot(kind='bar', title='Distribution of data',legend=False)
# # ax.set_xticklabels(['Negative','Positive'], rotation=0)
# # # Storing data in lists.
# # text, sentiment = list(df['text']), list(df['target'])

# # sns.countplot(x='target', data=df)

from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import nltk

df = pd.read_csv('Tweets.csv')
df.head()

#Convert text to lowercase
df['text'] = df['text'].str.lower()

df['text'] = df['text'].astype(str)  # Convert 'text' column to string data type

df['tokens'] = df['text'].apply(nltk.word_tokenize)  # Tokenization


# Remove stopwords
stopwords = nltk.corpus.stopwords.words('english')
df['tokens'] = df['tokens'].apply(lambda x: [word for word in x if word not in stopwords])

X = df['text']
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

model = SVC()
model.fit(X_train_vectors, y_train)

y_pred = model.predict(X_test_vectors)

# print("Classification Report:")
# print(classification_report(y_test, y_pred))

# print("Accuracy Score:", accuracy_score(y_test, y_pred))





# Extract the text from positive sentiment tweets
positive_tweets = df[df['sentiment'] == 'positive']['text']

# Concatenate all the positive sentiment tweets into a single string
positive_text = ' '.join(positive_tweets)

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positive_text)

# Plot the WordCloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud - Positive Sentiment')
plt.show()
