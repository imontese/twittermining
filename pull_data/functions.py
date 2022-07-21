# import modules
import os
import tweepy
from pull_data import *

import pull_data as pull_data

# env module
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class TweeterMining:

    api = 0
    search = ''

    def __init__(self, _search_term = 0, _search_name = 0, _tweets_amount=200):
        self.search_term = _search_term
        self.search_name = _search_name
        self.tweets_amount = _tweets_amount
        TweeterMining.authentication()


    def authentication():
        # set online authentication
        auth = tweepy.OAuth1UserHandler(os.getenv('consumer_key'), os.getenv('consumer_secret'))
        auth.set_access_token (os.getenv('access_token'), os.getenv('access_token_secret'))

        # seting up Oauth 2.0 Bearer Token
        #auth = tweepy.OAuth2BearerHandler(os.getenv('bearer_token'))

        # calling the API
        TweeterMining.api = tweepy.API(auth)

    def mining(self):
        # use lowercases for search term
        screen_name = self.search_name
        search_term = self.search_term
        tweet_amount = self.tweets_amount
        tweets_raw = []
        likes = []
        time = []


        if screen_name != 0:
            # return most recent status posted
            # search by user name
            data = tweepy.Cursor(TweeterMining.api.user_timeline,
                                screen_name = screen_name,
                                tweet_mode='extended',
                                ).items(tweet_amount)
            
            TweeterMining.search = screen_name

        elif search_term != 0:
            # return most recent search word
            # search by topic
            data = tweepy.Cursor(TweeterMining.api.search_tweets,
                                q = search_term,
                                lang='en',
                                tweet_mode='extended',
                                ).items(tweet_amount)

            TweeterMining.search = search_term


        # getting data into a lists
        for tweet in data:
            #print(tweet.text)
            tweets_raw.append(tweet.full_text)
            likes.append(tweet.favorite_count)
            time.append(tweet.created_at)
        
        return tweets_raw


