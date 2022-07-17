# import modules
import tweepy
from pull_data import *

import pull_data as pull_data


def tweeter_data(_search_term, _tweets_amount):
    # use lowercases for search term
    screen_name = 'elonmusk'
    search_term = _search_term
    tweet_amount = _tweets_amount
    tweets_raw = []
    likes = []
    time = []

    # return most recent status posted
    # search by user name
    '''
    data = tweepy.Cursor(api.user_timeline,
                        screen_name = screen_name,
                        tweet_mode='extended',
                        ).items(tweet_amount)


    # return most recent search word
    '''
    # search by topic
    data = tweepy.Cursor(pull_data.api.search_tweets,
                        q = search_term,
                        lang='en',
                        tweet_mode='extended',
                        ).items(tweet_amount)


    # getting data into a lists
    for tweet in data:
        #print(tweet.text)
        tweets_raw.append(tweet.full_text)
        likes.append(tweet.favorite_count)
        time.append(tweet.created_at)
    
    return tweets_raw
