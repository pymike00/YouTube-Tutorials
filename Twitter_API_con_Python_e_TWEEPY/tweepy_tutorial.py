import tweepy
from twitter_app_credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# new_tweet = api.update_status("Nuovo video tutorial in fase di registrazione... ;)") # hello world

public_tweets = tweepy.Cursor(api.search, 
                              q="bitcoin", 
                              result_type="mixed", 
                              tweet_mode="extended").items(100)

for tweet in public_tweets:
    print("@" + tweet.user.screen_name)
    tweet_text = tweet.full_text
    print(tweet_text)
    print()