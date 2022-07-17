
# set online authentication
auth = tweepy.OAuth1UserHandler(os.getenv('consumer_key'), os.getenv('consumer_secret'))
auth.set_access_token (os.getenv('access_token'), os.getenv('access_token_secret'))

# seting up Oauth 2.0 Bearer Token
#auth = tweepy.OAuth2BearerHandler(os.getenv('bearer_token'))

# calling the API
api = tweepy.API(auth)