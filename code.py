#Install Modules
!pip install tweepy --ignore-installed
#an open source Python package that gives you a very convenient way to access the Twitter API with Python
!pip install flair
#allows you to apply our state-of-the-art natural language processing (NLP) models to your text, 
#such as named entity recognition (NER), part-of-speech tagging (PoS), special support for biomedical data, sense disambiguation and classification, 
#with support for a rapidly growing number of languages

#Configuration , to acccess twitter with tweepy
#Go to your apps page where you will see the app you created. Click on details. Once you're there, click on keys and tokens to get the relevant keys
bearer = "<<KEY>>"
consumer_key = "<<KEY>>"
consumer_secret = "<<KEY>>" 
access_token = "<<KEY>>"
access_token_secret = "<<KEY>>"

import tweepy
import re
import time

from flair.models import TextClassifier
from flair.data import Sentence


## initialize tweepy
api = tweepy.Client(bearer, consumer_key, consumer_secret, access_token, access_token_secret)
api.get_me()


## get tweets in realtime
response = api.search_recent_tweets('#crypto')

tweets = response.data
for tweet in tweets:
    print(tweet.text)
    print('-----------------------------------------------')
    
def preprocess_text(text):
    # convert to lower case
    text = text.lower()
    # remove user handle
    text = re.sub("@[\w]*", "", text)
    # remove http links
    text = re.sub("http\S+", "", text)
    # remove digits and spl characters
    text = re.sub("[^a-zA-Z#]", " ", text)
    # remove rt characters
    text = re.sub("rt", "", text)
    # remove additional spaces
    text = re.sub("\s+", " ", text)

    return text
    
tweet.text


preprocess_text(tweet.text)

## create sentiment analysis function
classifier = TextClassifier.load('en-sentiment')
def get_sentiment(tweet):
    sentence = Sentence(tweet)
    classifier.predict(sentence)
    return str(sentence.labels[0]).split()[0]
    
get_sentiment(tweet.text)


#Realtime Twitter Sentiments
## preprocess the tweets
def preprocess_text(text):
    # convert to lower case
    text = text.lower()
    # remove user handle
    text = re.sub("@[\w]*", "", text)
    # remove http links
    text = re.sub("http\S+", "", text)
    # remove digits and spl characters
    text = re.sub("[^a-zA-Z#]", " ", text)
    # remove rt characters
    text = re.sub("rt", "", text)
    # remove additional spaces
    text = re.sub("\s+", " ", text)

    return text

## create sentiment analysis function
classifier = TextClassifier.load('en-sentiment')
def get_sentiment(tweet):
    sentence = Sentence(tweet)
    classifier.predict(sentence)
    return str(sentence.labels).split("\'")[3] #split sentence into 3 words

## get realtime sentiments
while True:
    # get tweets (10 tweets)
    tweets = api.search_recent_tweets('#crypto').data

    for tweet in tweets:
        original_tweet = tweet.text
        clean_tweet = preprocess_text(original_tweet)
        sentiment = get_sentiment(clean_tweet)

        print('------------------------Tweet-------------------------------')
        print(original_tweet)
        print('------------------------------------------------------------')
        print('Sentiment:', sentiment)
        time.sleep(1)
        print('\n\n')

