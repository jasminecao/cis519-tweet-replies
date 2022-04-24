import re
import pandas as pd
import nltk
import string
from plotly import graph_objects as go
import plotly.express as px
import numpy as np

nltk.download("stopwords")
stopword_list = nltk.corpus.stopwords.words("english")


def read_file(filename):
    """
    Converts given text file into dataframe with cols of label and
    (positive, negative, neutral)
    """
    tweet_df = pd.read_csv(filename, sep="\t", lineterminator="\n")
    tweet_df.columns = ["label", "tweet"]
    return tweet_df


def clean_tweet(tweet):
    """
    tweet: string
    returns: cleaned tweet (string)
    """
    tweet = tweet.lower()
    # remove punctuation
    tweet = "".join([c for c in tweet if c not in string.punctuation])
    # remove stop words
    tweet = "".join([(c + " ") for c in tweet.split(" ") if c not in stopword_list])
    # remove all @mentions
    tweet = re.sub(r"(@.*?)[\s]", " ", tweet)
    # remove twitter URL at end of tweet (https://t.co/...)
    tweet = re.sub("http[s]?://\S+", "", tweet)
    return tweet


def visualize_tweets(tweet_df):
    """
    tweet_df: dataframe
    """
    index = ["negative", "neutral", "positive"]

    tweet_u, tweet_counts = np.unique(tweet_df["label"], return_counts=True)
    text = [round(x / len(tweet_df), 3) for x in tweet_counts]
    fig = go.Figure(
        data=[
            go.Bar(
                name="Tweets",
                x=index,
                y=tweet_counts / len(tweet_df),
                text=text,
            ),
        ],
        layout=go.Layout(
            title="Proportion of Tweets by Sentiment",
            yaxis_title="Proportion of Total Tweets",
        ),
    )
    fig.show()


def preprocess_tweets(filename):
    tweet_df = read_file(filename)
    tweet_df["tweet"] = tweet_df["tweet"].apply(clean_tweet)
    return tweet_df
