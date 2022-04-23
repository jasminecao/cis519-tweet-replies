import requests
import re
import time


def read_file(filename):
    """
    Converts given text file into dictionary with key tweet ID and value label
    (positive, negative, neutral)
    """
    with open(filename, "r") as f:
        lines = f.readlines()

    lines = lines[1:]

    # tab-delimited text file (e.g. "negative	1222226229446750214")
    # split by tab, strip trailing newline characters
    tweet_dict = {line.split("\t")[1].rstrip(): line.split("\t")[0] for line in lines}

    return tweet_dict


def get_tweet(tweet_dict, filename):
    """
    tweet_dict: dictionary with key tweet ID and value label
    Requests tweet from Twitter API using tweet ID. Writes tweet to file.
    returns: list of tuples (tweet text, label)
    """
    tweet_list = list()
    with open(filename, "a") as text_file:
        for (tweet_id, label) in tweet_dict.items():
            url = "https://api.twitter.com/2/tweets/" + tweet_id
            headers = {
                "Authorization": "Bearer " + BEARER_TOKEN,
                "Content-Type": "application/json",
            }
            response = requests.get(url, headers=headers)
            tweet_res = response.json()

            if "data" in tweet_res:
                tweet = tweet_res["data"]["text"]
                print(tweet_id)
                print(tweet)
                # remove all tabs and newlines from tweet content
                tweet = re.sub("\s+", " ", tweet)
                tweet_list.append((tweet, label))
                text_file.write(label + "\t" + tweet + "\n")
            elif "title" in tweet_res and tweet_res["title"] == "Too Many Requests":
                print("===================== Too Many Requests =====================")
                print(tweet_id)
                print(tweet_res)
                # wait 17 minutes before requesting again
                time.sleep(60 * 17)
                response = requests.get(url, headers=headers)
                tweet_res = response.json()
                # continue where we left off
                if "data" in tweet_res:
                    tweet = tweet_res["data"]["text"]
                    print(tweet)
                    tweet = re.sub("\s+", " ", tweet)
                    tweet_list.append((tweet, label))
                    text_file.write(label + "\t" + tweet + "\n")
    return tweet_list


labeled_tweet_id = read_file("train_final_label.txt")
get_tweet(labeled_tweet_id, "final_tweets_training.txt")
