import tweepy
import sys
import time

consumer_key = "v6D3BItAfNQ8XznIzgUU4Hy3Q"
consumer_secret = "7dIJvXYvDLTQIpoJSS32pgXuXuvjzOvWUYE7rE9ivpg4tqNPE6"
access_token = "1213570521712848896-1RjY9BoPHfUbq3nsBcmmLP2q3eiBX1"
access_token_secret = "GgtpcCilr2L7UUHpQ6IxMvY43R4wmQHtR0st2jQgsrlVt"


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
