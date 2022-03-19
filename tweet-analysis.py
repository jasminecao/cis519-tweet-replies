import nltk
from textblob import TextBlob
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from preprocessing import *

nltk.download("vader_lexicon")


def extract_features(tweets_df):
    sid = SentimentIntensityAnalyzer()
    tweets_df["polarity"] = tweets_df["tweet"].apply(
        lambda x: sid.polarity_scores(x).get("compound")
    )
    tweets_df["subjectivity"] = tweets_df["tweet"].apply(
        lambda x: TextBlob(x).sentiment.subjectivity
    )
    tweets_df["num_tokens"] = tweets_df["tweet"].apply(lambda x: len(x.split(" ")))

    return tweets_df


def train_model(tweets_df):
    labels_df = tweets_df["label"]
    features_df = tweets_df.drop(["label", "tweet"], axis=1)
    train_features, test_features, train_labels, test_labels = train_test_split(
        features_df, labels_df, test_size=0.2
    )
    rf = RandomForestRegressor(n_estimators=1000)
    rf.fit(train_features, train_labels)


processed_tweets_df = preprocess_tweets("final_tweets_test.txt")
tweets_df = extract_features(processed_tweets_df)
