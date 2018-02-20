Code Review: Xinqiao Wei

By Hayato Nakamura


https://github.com/WeiXinqiao/EC500_C1/blob/master/HW1_API/hw1_api.py

Flow Analysis:  
Read Twitter credentials, checks the authorization and the twitter handle
Goes through the twitter timeline, downloads a photo
Converts the photo into video using FFMPEG
Repeat step 2 with more photos (10)
Output a .txt file with 50 different captions made by cloud vision

API Calls:
	The API calls to twitter as well as google cloud vision is simple and satisfies the necessary requirements. The twitter call uses tweepy, the required library for accessing twitter, while the cloud vision call uses google.cloud. Both API will need a developers key (cloud vision being the .json file) to fully access the network, which the user will need to manually input. 

Readability/Syntax Convention:
	Overall, the syntax of the code is easy to understand. The coder does a fairly good job writing understandable code, as well as commenting out almost all the actions in his code. However, there are areas where I would not include, such as line 34-40, where the user parses twitter data. Although it was used in the specific model this coder used online, it’s not necessary to include in this assignment. I would suggest either commenting that this is optional, or delete this section entirely. 

Performance of API (Error Handling):
	The following test cases were passed through the code:

Non-existent Twitter Handle
No Photos on the Twitter Page
Bad Access Token
Twitter
JSON

	For better convention, the following modifications were made in the code:
Username parses through as an input argument

Analysis: 
1.	
When a non-existent twitter handle was passed through, the following error message was thrown back:

 raise TweepError(error_msg, resp, api_code=api_error_code)
tweepy.error.TweepError: [{'code': 34, 'message': 'Sorry, that page does not exist.'}]

This was an error call directly from tweepy (terminal) which immediately terminates the program. It would be best if there was an error call directly by the coder, that may ask for a valid twitter handle and reruns the program. 


2.
	When a twitter handle with 0 photos were passed, the following output would be displayed:

...1 tweets downloaded so far
set()
set()

The program did terminate without failure, but did not perform the task it was meant to do since there were no pictures. A friendly error message is suggested here, which can be done through a print statement such as the one below:

if (numoftweets == 1):
	print(‘There were no photos available by this user’)


3. 
An invalid twitter credential is entered
The tweepy library terminated itself as it did not recognise the necessary information required to use the twitter API. 
An invalid JSON file is specified
Terminal did not like it when a non-existing .JSON file was specified for the google cloud vision API.
	

Accuracy of Execution:
	Although the necessary API calls were handled correctly, the coder failed to execute the assignment requirements. Instead of making a collective video collage, the code would generate a video per image. In the end, there were 10 images downloaded, then 10 videos, one second each, would be created. Additionally, it would spit out ~50 different captions created by google cloud vision. Here is what the student should have done for the best code:
Instead of hardcoding, ask the user a set of questions such as:
Twitter Handle
Number of photos you would like to download
Make a video collage of the combined images, not a one second video collage of a single picture.
Automatically delete the pictures that you downloaded, making the only outputs the .txt file and the video.
(optional but recommended) Have the caption ON the video, not linked separately as a .txt file. The captions in this file were also combined and very difficult to tell which captions were for which photo. 


Overall Analysis:

Category
Grade: (A ~ F)
API Call
A
Performance
C+
Cleanliness / Explanation
A
Syntax Convention
A-
Accuracy of Execution
C

Average:

B/B+
