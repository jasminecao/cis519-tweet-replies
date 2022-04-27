# Predicting the Sentiment of Tweet Replies

## CIS519 Spring 2022 - Eileen Deng, Richard Yeh, Jasmine Cao

This project investigates the sentiment of tweet replies given a source tweet.
The project uses data from
[this dataset](https://www.kaggle.com/soroosharasteh/retweet/), which contains
Tweet IDs and their corresponding reply sentiment. The data is contained in the
files `data/test_gold.txt` and `data/train_final_label.txt`. The file
`tweet-scraper.py` contains code used to scrape these tweets from the Twitter
API. To use the file, one will need a TwitterAPI key and access token. The final
labeled source tweets are stored in the file `data/final_tweets_test.txt` and
`data/final_tweets_training.txt`.

The code for the baseline classifier, random forest classifier, and TextCNN
model is included in the notebook `predictor.ipynb`. The code for the BERT model
and variants of the BERT model are included in `BERT_model.ipynb`.
