# EC500 Twitter API & Google Cloud Vision API 

## Objective: 
twittertest.py will download 10 pictures from your selected twitter handl. Then it will run those 10 photos through google cloud vision, override the picture with a word that describes each photo, and outputs a video in a mp4 format for the audience.

The Twitter API credentials are left for the user to input.

Some things to set up before you can have this running: 
  1. Download the google cloud vision (through pip)
  2. Set up the API page for google cloud vision, and rename the JSON file (ex: filename.json)
  3. type the following on the terminal command
  
  >export GOOGLE_APPLICATION_CREDENTIALS=filename.json
     
     
**Make sure that you change filename.json depending on what you actually name it**


## Code Flow:
The following shows the basic flow of the code:

 1. Checks your twitter credentials
 2. Checks if it is a valid twitter handle
 3. Downloads the pictures (.jpg)
 4. Runs the pictures through the google vision API
 5. Creates new pictures with the label written over it, while deleting the original photos
 6. Runs the new photos through FFMPEG and deletes the old pictures


Enjoy!
