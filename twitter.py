from credentials import *

import tweepy
 
import pandas as pd
import csv
import re 
import string
import preprocessor as p
import analysis
import emoji

consumer_key = "eWDIfDxXrYCfIcZmrnyqDa8MF"
consumer_secret =  "rK86MTAtzC8mVcZfs4ximI2TXcZGCQub7q3GnlGQtgIvJiXdn7"
access_key= "1465826212861943809-JKsYmTnPRKN2UEuzO1gZhLph0mmdqA"
access_secret = "Jhl8q3suY45Avrm2SgchC8BsqNzoVvkB8enAukuXFTRu9"
 
# Remove Emojis
def give_emoji_free_text(text):
    allchars = [str for str in text]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])

    return clean_text

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True)
 
 
search_words = "#wildfires"      # enter your words
new_search = search_words + " -filter:retweets"

for tweets in api.search_tweets(q=new_search, lang="en", count=100, since_id=0):
    print(tweets.text)
    text = give_emoji_free_text(text=tweets.text)
    analysis.overall_sentiment(text)