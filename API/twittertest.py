#Python Twitter Test
#Hayato Nakamura 



import tweepy
from tweepy import OAuthHandler
import json
import wget
import os

from base64 import b64encode
from os import makedirs
from os.path import join, basename
from sys import argv
import requests

import io

import PIL
from PIL import Image, ImageDraw, ImageFont

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

 
 #My Twitter Information
consumer_key = 'HXsLvWs59wM1d1XGE7LJQOigJ'
consumer_secret = 'qBeTcrfx4pzUC0EhNdYco0tQkYKVkhIIebdNr4FB6t7pOYMMoT'
access_token = '255953036-hY9jLN886BikD0qOBODFgaJ54xwTuAKFBgwXknLB'
access_secret = 'nXtasuKhZnAcA3djmj5JOrjACa7JsJthuu4amegKn4Eqt'


#using the tweety library
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)



#api search

#getting the tweet from the user, number of tweets are 200
tweets = api.user_timeline(screen_name='Hayatopia',
                           count=200, include_rts=False,
                           exclude_replies=True)

last_id = tweets[-1].id

username = 'Hayatopia'


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
counter = 0
for media_file in media_files:
	if (counter < 10):
		counter = counter + 1
		address = '/Users/Hayato/Desktop/Media/' + str(counter) + '.jpg'
		wget.download(media_file, address)





#---------------------------------------------------------------------------------------------------

newcounter = 0
# Instantiates a client
client = vision.ImageAnnotatorClient()



for x in range(1, 11):
    newcounter = newcounter + 1
    name = str(newcounter) + '.jpg'

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        name)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    x = 0

    for label in labels:
        if (x == 0):
            x = x + 1
            y = label.description
            # print(y)
    new = 'new' + str(newcounter) + '.jpg'
    image = Image.open(name)
    # font_type = ImageFont.truetype('Arial.tff', 20)                     // if you want to change the font
    draw = ImageDraw.Draw(image)
    draw.text(xy=(100, 50), text = y, fill=(255, 69, 0))
    image.save(new) # save it
    newcommand = "rm " + name;
    os.system(newcommand)
    #image.show()






#---------------------Converting the pictures to Video--------------------------
#     Using ffmpeg

os.system("ffmpeg -framerate .5 -pattern_type glob -i '*.jpg' out.mp4")

#-------------------------------------------------------------------------------














