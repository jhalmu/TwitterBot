# twitterbot/bots/config.py
# thanks to realpython.com

import tweepy
import logging
import seacret

logger = logging.getLogger()

def create_api():
    KEY = seacret.KEY
    SECRET= seacret.SECRET
    TOKEN = seacret.TOKEN
    TOKEN_SECRET = seacret.TOKEN_SECRET

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(KEY, SECRET)
    auth.set_access_token(TOKEN, TOKEN_SECRET)

    api = tweepy.API(auth)
    #streamapi = tweepy.Stream(seacret.KEY, seacret.SECRET, seacret.TOKEN, seacret.TOKEN_SECRET)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api