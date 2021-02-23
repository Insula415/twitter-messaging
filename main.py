import tweepy
import sys
from time import sleep
from collections import Counter, defaultdict

consumer_key = "" #your consumer key
consumer_secret = "" #your consumer secret key
access_token = "" #your access token
access_token_secret = "" #your secret access token


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print("Checking for duplicates")
print("")
count = defaultdict(int)
d = 0
with open('handles.txt') as f:
    l = Counter(l.strip() for l in f if l.strip())
    for line in l:
        if l[line]>1:
            print(line)

with open('handles.txt') as f:
    for lineno, line in enumerate(f):
        c = line.strip()
        if c:
            if c in count:
                print("Line:",lineno)
                d += 1
            count[c] += 1

if d >= 1:
    print("Duplicates found:",d)
    exit()
else:
    print("No duplicates found, all ready to go!")


f = open("handles.txt", "r")
h = f.readlines()
f.close()

text = sys.argv[1]
print("")
print("'" + text + "'")
print("")
confirm = input("Are you sure you want to send the following? ")
opt = ["y", "yes"]


x = 0
if confirm.lower() in opt:
    print("Sending in 3")
    sleep(1)
    print("Sending in 2")
    sleep(1)
    print("Sending in 1")
    sleep(1)
    print("Blast off")
    for i in h:
        try:
            user = api.get_user(i)
            id = user.id_str
            direct_message = api.send_direct_message(id.strip(), text) #sending message
            u = api.get_user(id)
            print("Sent to",u.screen_name)
            x += 1

        except:
            print("Failed to send to",u.screen_name)
else:
    print("Cancelled")
    exit()

print("Successfully sent to",x,"people")
