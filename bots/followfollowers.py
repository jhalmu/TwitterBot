# twitterbot/bots/followfollowers.py 

import tweepy
import logging
from config import create_api
import pause

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

print('visiting here')

def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.get_followers).items():

        # if no followers ---
        if follower.following == False:
            if not follower.following:
                logger.info(f"Following {follower.name}")
                follower.follow()
        else:

            # -- lets check tomorrow again
            logger.info("No followers, going to sleep for 24h")
            pause.days(1)

def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        pause.minutes(1)

if __name__ == "__main__":
    main()