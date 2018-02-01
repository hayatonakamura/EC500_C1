#Python Twitter Test
#Hayato Nakamura 



import tweepy
from tweepy import OAuthHandler
import json
import wget
import os

 
 #My Twitter Information
consumer_key = ''
consumer_secret = ''
access_token = '-'
access_secret = ''


#using the tweety library
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)



#api search

#getting the tweet from the user, number of tweets are 200
tweets = api.user_timeline(screen_name='Hayatopia',
                           count=2, include_rts=False,
                           exclude_replies=True)

last_id = tweets[-1].id

username = "Hayatopia"


while (True):
	more_tweets = api.user_timeline(screen_name=username,
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



#---------------------Converting the pictures to Video--------------------------
#     Using ffmpeg

os.system("ffmpeg -framerate 10 -pattern_type glob -i '*.jpg' out.mp4")

#-------------------------------------------------------------------------------












