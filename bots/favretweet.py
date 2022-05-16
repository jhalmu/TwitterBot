# Orginal code:  https://dev.to/james_kinga/simple-twitter-bot-to-retweet-favorite-using-python-tweepy-50bg

import tweepy
import datetime
from datetime import datetime, timedelta
from config import create_api
from time import sleep

# MyGasAndEnergy1
api = create_api()

# assign to favorite and follow
Favorite = True
Follow = True

search_term = "#henryhub OR #natgas OR #lng -filter:retweets"

# the function with the logic on the bot actions
def main():
    for tweet in tweepy.Cursor(
        api.search_tweets, 
        q=search_term
        ).items():
        try:
            # get time 3 days ago and modify it
            t = tweet.created_at
            tweet_time = t.strftime("%Y-%m-%d %H:%M")
            #p = datetime.today() - timedelta(days=3)
            #past = p.strftime("%Y-%m-%d")

            # check if tweet is too old
            # well, found out when reading docs that there is inbuild method for this.
            #while tweet_time >= past:  # <- not yet sure if this is right
                #print('only oldies not goldies')
                #continue
                # pass if tweeter is me (simple version)
            if not tweet.user.screen_name == "MyGasAndEnergy1":
                print("\nThanks to: @" + tweet.user.screen_name + ' at ' + tweet_time)
                # check if we have retweeted and retweet if not
                if not tweet.retweeted:
                    try:
                        tweet.retweet()
                        print("Tweet retweeted")
                    except Exception as e:
                        print('but old news, not prosessed')
                        #print(e)

                # check if we have favorited and favorite if not
                if not tweet.favorited:
                    try:
                        tweet.favorite()
                        print("...and favorited!")
                    except Exception as e:
                        pass
                        #print(e)

                # bot sleep time (seconds)
                sleep(480)
                print("waiting for sunny day...")

        except tweepy.TweepyException as e:
            print(e.reason)

        except StopIteration:
            break


while True:
    main()
    sleep(240)
