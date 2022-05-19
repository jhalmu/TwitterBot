# twitterbot/bots/config.py
# thanks to realpython.com

import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret= os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_seacret = os.getenv("ACCESS_TOKEN_SECRET")

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_seacret)

    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
