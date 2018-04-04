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

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

#mongodb libraries
import pymongo
from pymongo import MongoClient
import pprint


def Twitter(username):
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

		#directory = input('Enter the directory for the saved photos (eg: /Users/Hayato/Desktop/Media/): ')
		#cwd = os.getcwd()
		cwd = "/Users/Hayato/"

		#Downloading the images
		counter = 0
		for media_file in media_files:
			if (counter < 10):
				counter = counter + 1
				#change your directory here
				address = cwd + str(counter) + '.jpg'
				wget.download(media_file, address)
				filename = str(counter) + '.jpg'





	#--------------------------------------------Google Cloud Vision API-------------------------------------------



	# Instantiates a client
		client = vision.ImageAnnotatorClient()





	 
	#This counter is to name the 10 images 1.jpg, 2.jpg, ... , 10.jpg
		newcounter = 0
		count = 0
		twitterlabels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

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
		    



		    #increments for mongodb category name
		    newname = "picture" + str(x)

		    z = 0            #This is a counter to ONLY download the first description label
		    marker = '*************************************************************'

		    for label in labels:
		        if (z == 0):
		            z = z + 1
		            y = label.description           #This is the output text when run though google cloud vision
		            print(marker)
		            print(' ')
		            print(y)
		            print(' ')
		            twitterlabels[count] = y
		            #newdata = {"username": username, "picture1": y, "picture2": "blank", "picture3": "blank", "picture4": "blank", "picture5": "blank", "picture6": "blank", "picture7": "blank", "picture8": "blank", "picture9": "blank", "picture10": "blank"}
		            
		            #newdata = {"username": username, newname: y}
		            #db.twitter.update_one(newdata)
		            #twitterlabels[count] = y
		    count = count + 1


		    newcommand = "rm " + name
		    os.system(newcommand)

		return twitterlabels






def twitterbase(twitterinfo, username):
	# Instantiates mongodb client
	try:
		client = MongoClient()
		print("connection successful")
	except:
		print("could not connect to MongoDB")
	db = client.twittermongo
	post = json.load(open('/Users/Hayato/Desktop/twitter.json'))
	db.twittermongo.insert(post)
	#newdata = {"username": username}
	newdata = {"username": username, "picture1": "blank", "picture2": "blank", "picture3": "blank", "picture4": "blank", "picture5": "blank", "picture6": "blank", "picture7": "blank", "picture8": "blank", "picture9": "blank", "picture10": "blank"}
	db.twittermongo.insert(newdata)
	count = 1
	for x in range(1,11):
		newone = "picture" + str(count)
		count = count + 1
		db.twittermongo.update_one({"username": username}, { "$set": {newone: twitterinfo[count - 2]}})





def findinfo():
	client = pymongo.MongoClient()
	db = client.twittermongo
	u = input("Enter the  username:")
	category = "username"
	data = db.twittermongo.find_one({"username": u})
	print("Information about the username: \n")
	pprint.pprint(data)
	print("\n")





if __name__ == '__main__':
	 #My Twitter Information (enter your credentials here)
	consumer_key = 'HXsLvWs59wM1d1XGE7LJQOigJ'
	consumer_secret = 'qBeTcrfx4pzUC0EhNdYco0tQkYKVkhIIebdNr4FB6t7pOYMMoT'
	access_token = '255953036-hY9jLN886BikD0qOBODFgaJ54xwTuAKFBgwXknLB'
	access_secret = 'nXtasuKhZnAcA3djmj5JOrjACa7JsJthuu4amegKn4Eqt'


	#Authorizing using your information
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)


	#Keyboard input for the twitter username
	username=input('Twitter Username:')
	twitterinfo = Twitter(username)
	twitterbase(twitterinfo, username)
	check = input("Would you like to find data in your database? (y/n): ")
	if (check == "yes" or check == "y" or check == "Y"):
		findinfo()





