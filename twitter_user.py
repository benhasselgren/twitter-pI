import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'tTjtLioa2jf4n2rMhbuLDJaFe'
CONSUMER_SECRET = 'v85AnwRJfSt3sKXVIdY5t0naQI95MMpprSSmLN5vQo9WK53vi9'
OAUTH_TOKEN = '3931416802-odGr30SEFcceYxzZiptvSAmaQjbRQvGAgQSYcCA'
OAUTH_TOKEN_SECRET = 'y1q2oJnxb8Jans21f4zkbS99174rd05bw8FfPB6IXSXHb'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

user = api.get_user('@ben_hasselgren')

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a tweet
    print(status.text)