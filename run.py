# import modules
import constants as c
from pull_data.functions import *
from roberta_sa.functions import roberta_sa 


# Triggering the entire project
# Do this by python run.py

def run():
    tmining = TweeterMining(search_term = c.SEARCH_TERM, search_name=None, tweets_amount= c.TWEETS_AMOUNT)

    tweets_raw = tmining.get_tweets()
    roberta_sa(tweets_raw)





# runs only if the file was executed directly
if __name__ == '__main__':
    run()   