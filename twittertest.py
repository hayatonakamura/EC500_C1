#Python Twitter Test
#Hayato Nakamura 



import tweepy
from tweepy import OAuthHandler
import json
import wget

 
consumer_key = 'HXsLvWs59wM1d1XGE7LJQOigJ'
consumer_secret = 'qBeTcrfx4pzUC0EhNdYco0tQkYKVkhIIebdNr4FB6t7pOYMMoT'
access_token = '255953036-hY9jLN886BikD0qOBODFgaJ54xwTuAKFBgwXknLB'
access_secret = 'nXtasuKhZnAcA3djmj5JOrjACa7JsJthuu4amegKn4Eqt'

# @classmethod
# def parse(cls, api, raw):
#     status = cls.first_parse(api, raw)
#     setattr(status, 'json', json.dumps(raw))
#     return status
 
# # Status() is the data model for a tweet
# tweepy.models.Status.first_parse = tweepy.models.Status.parse
# tweepy.models.Status.parse = parse
# # User() is the data model for a user profil
# tweepy.models.User.first_parse = tweepy.models.User.parse
# tweepy.models.User.parse = parse
# # You need to do it for all the models you need

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


#getting the tweet from the user, number of tweets are 200
tweets = api.user_timeline(screen_name='realDonaldTrump',
                           count=200, include_rts=False,
                           exclude_replies=True)

last_id = tweets[-1].id

username = "realDonaldTrump"
 
while (True):
	more_tweets = api.user_timeline(screen_name='realDonaldTrump',
								count=200,
								include_rts=False,
								exclude_replies=True,
								max_id=last_id-1)
# There are no more tweets
	if (len(more_tweets) == 0):
		break
	else:
		last_id = more_tweets[-1].id-1
		tweets = tweets + more_tweets



#Obtaining the full path of the image
media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])


#Downloading the images
for media_file in media_files:
    wget.download(media_file)



