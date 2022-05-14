#Orginal code:  https://dev.to/james_kinga/simple-twitter-bot-to-retweet-favorite-using-python-tweepy-50bg

import tweepy
import datetime
from datetime import datetime, timedelta
from config import create_api
from time import sleep

#MyGasAndEnergy1
api = create_api()

# assign to favorite and follow
Favorite = True
Follow = True

hashtags = ['#henryhub','#natgas', '#naturalgas']

# the function with the logic on the bot actions
def main():
    for tweet in tweepy.Cursor(
        api.search_tweets, q=hashtags).items():
        try:
            # get time 3 days ago and modify it 
            # so we can compare it to modified tweet_time 
            t=tweet.created_at
            tweet_time=t.strftime("%Y-%m-%d")
            p = datetime.today()- timedelta(days=3)
            past = p.strftime("%Y-%m-%d")

            #check if tweet is too old
            if (tweet_time > past): # <- not yet sure if this is right

                # pass if tweeter is me (simple version) 
                if not tweet.user.screen_name=='MyGasAndEnergy1':
                    print("\nTweet by: @" + tweet.user.screen_name)

                     # check if we have retweeted and retweet if not
                    if not tweet.retweeted:
                        try:
                            tweet.retweet()
                            print("Tweet retweeted!")
                        except Exception as e:
                            #pass
                            print(e)

                    # check if we have favorited and favorite if not
                    if not tweet.favorited:
                        try:
                            tweet.favorite()
                            print("Tweet favorited!")
                        except Exception as e:
                            #pass
                            print(e)

                    # bot sleep time (seconds)
                    sleep(480)

        except tweepy.TweepyException as e:
            print(e.reason)


        except StopIteration:
            break


while True:
    main()
    sleep(240)






