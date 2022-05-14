#Code:  https://dev.to/james_kinga/simple-twitter-bot-to-retweet-favorite-using-python-tweepy-50bg

import tweepy

from config import create_api
from time import sleep
#MyGasAndEnergy1
#stream = tweepy.Stream(seacret.KEY, seacret.SECRET, seacret.TOKEN, seacret.TOKEN_SECRET)
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
            if not tweet.user.screen_name=='MyGasAndEnergy1':
                print("\nTweet by: @" + tweet.user.screen_name)

                # check if we have retweeted and retweet if not
                if not tweet.retweeted:
                    try:
                        tweet.retweet()
                        print("Tweet retweeted!")
                    except Exception as e:
                        print(e)

                # check if we have favorited and favorite if not
                if not tweet.favorited:
                    try:
                        tweet.favorite()
                        print("Tweet favorited!")
                    except Exception as e:
                        print(e)

                # bot sleep time (seconds)
                sleep(480)

        except tweepy.TweepyError as e:
            print(e.reason)


        except StopIteration:
            break


while True:
    main()
    sleep(240)






