#Python Twitter API
#Hayato Nakamura 

#Libraries    :    note -- Some libraries may not be necessary
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

 
 #My Twitter Information (enter your credentials here)
consumer_key = ''
consumer_secret = ''
access_token = '-'
access_secret = ''


#Authorizing using your information
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


#Keyboard input for the twitter username
username=input('Twitter Username:')


#getting the tweet from the user, number of tweets are 200
invalid = 0
try:
	tweets = api.user_timeline(screen_name=username,
	                           count=200, include_rts=False,
    	                       exclude_replies=True)
	last_id = tweets[-1].id
except:
	print('\nInvalid Username!\n')
	invalid = 1


if (invalid == 0):
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

	directory = input('Enter the directory for the saved photos (eg: /Users/Hayato/Desktop/Media/): ')

	#Downloading the images
	counter = 0
	for media_file in media_files:
		if (counter < 10):
			counter = counter + 1
			#change your directory here
			address = directory + str(counter) + '.jpg'
			wget.download(media_file, address)
			filename = str(counter) + '.jpg'
			# image = Image.open(filename)
			# new_image = image.resize((500, 500))						#for resizing the image (optional)
			# hello = counter * 10
			# newname = str(counter) + '.jpg'
			# new_image.save(newname)





#--------------------------------------------Google Cloud Vision API-------------------------------------------



# Instantiates a client
	client = vision.ImageAnnotatorClient()
 
#This counter is to name the 10 images 1.jpg, 2.jpg, ... , 10.jpg
	newcounter = 0

	for x in range(1, 11):
	    newcounter = newcounter + 1                  
	    name = str(newcounter) + '.jpg'                    #names the image names differently

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

	    x = 0            #This is a counter to ONLY download the first description label
	    marker = '*************************************************************'

	    for label in labels:
	        if (x == 0):
	            x = x + 1
	            y = label.description           #This is the output text when run though google cloud vision
	            print(marker)
	            print(' ')
	            print(y)
	            print(' ')
	    new = 'new' + str(newcounter) + '.jpg'     #The new file is called new1.jpg, new2.jpg, ... , new10.jpg
	    image = Image.open(name)
	    font_type = ImageFont.truetype('arial.ttf', 35)                     # if you want to change the font
	    draw = ImageDraw.Draw(image)
	    draw.text(xy=(0, 0), text = y, font = font_type, fill=(255, 69, 0))
	    #Saves the new image, then deletes the old one
	    image.save(new)
	    newcommand = "rm " + name
	    os.system(newcommand)
	    #image.show()






#---------------------Converting the pictures to Video--------------------------
#     Using ffmpeg

	os.system("ffmpeg -framerate .5 -pattern_type glob -i '*.jpg' out.mp4")

#-------------------------------------------------------------------------------



#Aditionally, if you would like to delete the new pictures as well, include the following

	count = 0

	for z in range(1, 11):
		count = count + 1 
		file = 'new' + str(count) + '.jpg'
		deletepic = "rm " + file
		os.system(deletepic)


	#automatically open the video:
	video_out = 'open ' + directory + 'out.mp4'
	os.system(directory)



