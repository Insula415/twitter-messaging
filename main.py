import tweepy
import sys
import time

consumer_key = "" #your consumer key
consumer_secret = "" #your consumer secret key
access_token = "" #your access token
access_token_secret = "" #your secret access token


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


f = open("handles.txt", "r")
h = f.readlines()
f.close()

text = sys.argv[1]
print("")
print("'" + text + "'")
print("")
confirm = input("Are you sure you want to send the following? ")
opt = ["y", "yes"]

if confirm.lower() in opt:
    for i in h:
        try:
            direct_message = api.send_direct_message(i.strip(), text) #sending message
            print("Sent to",i)
        except:
            print("Failed to send to",i)
else:
    print("Cancelled")
    exit()
