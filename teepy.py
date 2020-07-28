import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("QJNw1zQDxW17NBPH5alSS07GM", 
    "fNxbFPeszmgX0xJZiiR6dI1d8ijtdqhM8gWaLBoKoFBvVmAuhb")
auth.set_access_token("1266663205843107840-Bgc2VgrOSNo3jm3HEUarP1HepfionH", 
    "nxMMPk1JCljbuHJ7nJYqx8Pcd9nDDGOpPnRgTTELpfMdc")

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
#=============================================================
#to print last 20 tweets from my feed

# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")
#==============================================================

#to tweet something at my feed
# api.update_status("Test tweet from Tweepy Python")    
#==============================================================
#search any word find # on tweet
for tweet in api.search(q={"Premier League","premier league"}, lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")

#=======================================================
#trending # in india
# trends_result = api.trends_place(2282863)
trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
    print(trend["name"])
#========================================================
'''
CODED BY-:
             __              ___          __
|   | _|_   |__) /\  |      |   _   |  | |__)  _|_    /\ 
|___|  |__  |   /~~\ |___   |__| |  |__| |      |__  /~~\ 

'''
