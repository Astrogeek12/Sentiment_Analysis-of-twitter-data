import pandas as pd
import spacy
from textblob import TextBlob

# Load spaCy model for English
nlp = spacy.load("en_core_web_sm")

# Load the CSV file containing tweets
df = pd.read_csv("tweets.csv")  # Replace with the path to your CSV file

# Function to perform aspect-based sentiment analysis on a single tweet
def analyze_tweet(tweet):
    if isinstance(tweet, str):  # Check if the tweet is a string
        doc = nlp(tweet)
        aspect_sentiments = {}

        for ent in doc.ents:
            if ent.label_ in ["ORG", "PRODUCT"]:  # Adjust entity labels as needed
                aspect = ent.text
                analysis = TextBlob(tweet)
                aspect_sentiment_polarity = analysis.sentiment.polarity
                aspect_sentiments[aspect] = aspect_sentiment_polarity

        return aspect_sentiments
    else:
        return {}  # Return an empty dictionary for non-string values

# Apply the analyze_tweet function, handling NaN values
df['aspect_sentiments'] = df['text'].apply(lambda tweet: analyze_tweet(tweet) if pd.notna(tweet) else {})

# Print or save the results
print(df[['text', 'aspect_sentiments']])
