import tweepy
import credentials

KEY = credentials.KEY
SECRET= credentials.SECRET
TOKEN = credentials.TOKEN
TOKEN_SECRET = credentials.TOKEN_SECRET


# Authenticate to Twitter
auth = tweepy.OAuthHandler(KEY, SECRET)
auth.set_access_token(TOKEN, TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")