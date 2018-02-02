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
	if (counter < 5):
		counter = counter + 1
		wget.download(media_file)



#---------------------Converting the pictures to Video--------------------------
#     Using ffmpeg

os.system("ffmpeg -framerate .5 -pattern_type glob -i '*.jpg' out.mp4")

#-------------------------------------------------------------------------------



# ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
# RESULTS_DIR = 'jsons'
# makedirs(RESULTS_DIR, exist_ok=True)

# def make_image_data_list(image_filenames):
#     """
#     image_filenames is a list of filename strings
#     Returns a list of dicts formatted as the Vision API
#         needs them to be
#     """
#     img_requests = []
#     for imgname in image_filenames:
#         with open(imgname, 'rb') as f:
#             ctxt = b64encode(f.read()).decode()
#             img_requests.append({
#                     'image': {'content': ctxt},
#                     'features': [{
#                         'type': 'TEXT_DETECTION',
#                         'maxResults': 1
#                     }]
#             })
#     return img_requests

# def make_image_data(image_filenames):
#     """Returns the image data lists as bytes"""
#     imgdict = make_image_data_list(image_filenames)
#     return json.dumps({"requests": imgdict }).encode()


# def request_ocr(api_key, image_filenames):
#     response = requests.post(ENDPOINT_URL,
#                              data=make_image_data(image_filenames),
#                              params={'key': api_key},
#                              headers={'Content-Type': 'application/json'})
#     return response


# if __name__ == '__main__':
#     api_key, *image_filenames = argv[1:]
#     if not api_key or not image_filenames:
#         print("""
#             Please supply an api key, then one or more image filenames
#             $ python cloudvisreq.py api_key image1.jpg image2.png""")
#     else:
#         response = request_ocr(api_key, image_filenames)
#         if response.status_code != 200 or response.json().get('error'):
#             print(response.text)
#         else:
#             for idx, resp in enumerate(response.json()['responses']):
#                 # save to JSON file
#                 imgname = image_filenames[idx]
#                 jpath = join(RESULTS_DIR, basename(imgname) + '.json')
#                 with open(jpath, 'w') as f:
#                     datatxt = json.dumps(resp, indent=2)
#                     print("Wrote", len(datatxt), "bytes to", jpath)
#                     f.write(datatxt)

#                 # print the plaintext to screen for convenience
#                 print("---------------------------------------------")
#                 t = resp['textAnnotations'][0]
#                 print("    Bounding Polygon:")
#                 print(t['boundingPoly'])
#                 print("    Text:")
#                 print(t['description'])





