from credentials import *

import tweepy
 
import pandas as pd
import csv
import re 
import string
import preprocessor as p
 

 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True)
 
 
search_words = "#wildfires"      # enter your words
new_search = search_words + " -filter:retweets"

for tweets in api.search_tweets(q="iphone", lang="en", count=100, since_id=0):
    print(tweets.text.encode('utf-8'))
# #for tweet in tweepy.Cursor(api.search_tweets,q=new_search,count=100,
#                            lang="en",
#                            since_id=0).items():
#                            print(tweet.text.encode('utf-8'))