# import modules
import constants as c
from pull_data.functions import *
from roberta_sa.functions import roberta_sa 


# Triggering the entire project
# Do this by python run.py

def run():
    tweets_raw = tweeter_data(c.SEARCH_TERM, c.TWEETS_AMOUNT)
    roberta_sa(tweets_raw)


# runs only if the file was executed directly
if __name__ == '__main__':
    run()