# impor modules 
import pandas as pd
import numpy as np
import re
from constants import SEARCH_TERM
from pull_data.functions import tweeter_data


# roBERTa-base for Sentiment Analysis
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
from scipy.special import softmax

# load model and tokenizet
MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
# PT
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

import matplotlib.pyplot as plt; plt.rcdefaults()


def roberta_sa(tweets_raw):   

    # cleaning tweets, removing mentioned users (@)
    tweets_final = []
    new_tweets = tweets_raw

    for tweet in new_tweets:
        final_text = tweet.replace('&amp;', 'and')
        #final_text = re.sub('^RT ', '', final_text)      # this remove only RT letters
        final_text = re.sub('htt.*', 'http', final_text)
        final_text = re.sub(r'@.\w+', '@user ', final_text)
        tweets_final.append(final_text)


    # create data frame
    df = pd.DataFrame({'tweets':tweets_final})

    # removing retweets (all the line)
    df = df[~df.tweets.str.contains("RT")]

    # removing links
    #df = df[~df.tweets.str.contains("http")]

    # reset index
    df = df.reset_index(drop=True)

    # fb to a list
    list_of_sentences = [sentence for sentence in df.tweets]

    score_Negative = []
    score_Neutral = []
    score_Positive = []

    # sentiment analysis per tweet
    for tweets in list_of_sentences:

        # sentiment analysis
        encoded_tweet = tokenizer(tweets, return_tensors='pt')
        #output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
        output = model(**encoded_tweet)

        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        score_Negative.append(scores[0]) 
        score_Neutral.append(scores[1]) 
        score_Positive.append(scores[2]) 

    
    df =pd.DataFrame({'tweets': list_of_sentences, 'negative': score_Negative, 'neutral': score_Neutral, 'positive': score_Positive,})

    # Define Data 
    lables = ['Negative', 'Neutral', 'Positive']
    score_means = [df["negative"].mean(), df["neutral"].mean(), df["positive"].mean()]

    # Plot bar chart
    plt.bar(lables, score_means, color=['red', 'yellow', 'green'])
    plt.xticks()
    plt.xlabel("Sentiment", fontweight='bold')
    plt.ylabel("Mean", fontweight='bold')
    plt.title(SEARCH_TERM)

    plt.show()
