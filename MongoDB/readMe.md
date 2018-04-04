Phase 2: Database Assignment
=============================
EC500 C1 - MongoDB
-------------------


# Overview
For this assignemnt, the following tasks are performed on top of what I have already accomplished for Project 1 (Twitter API).
- Acesss MongoDB
- Input the information from the Twitter pictures into the database
- Be able to Search and Update the database

# Instructions
The steps in performing this is relatively simple. After Downloading pymongo from the mongodb website, download phase2_mongodb.py. Open two terminal windows, running mongodb on one by writing the code: mongod, and running the python script that you have just downloaded.

**To Input Data** 
When asked for the prompt, username, make sure you enter a valid username for the twitter handle. It will automatically grab 10 photos from the user that you have specified. (NOTE: The default is 10 photos for the purpose of this assignment. Keep in mind that for phase3, there will be no limit for the number of photos because we want all the photos).

**Searching for Data**
The python script will also ask you if you would like to perform a search in the database. For example, if you have 'hayatopia' (my twitter handle) already in the database, by entering hayatopia on the search script, it will show you the descriptions google vision displays. 

The following is an example output:

```
{'_id': ObjectId('5ac50313654e990b28fb5c06'),
 'picture1': 'art',
 'picture10': 'nose',
 'picture2': 'standing',
 'picture3': 'car',
 'picture4': 'music',
 'picture5': 'red',
 'picture6': 'event',
 'picture7': 'pink',
 'picture8': 'wood',
 'picture9': 'pink',
 'username': 'hayatopia'}
```
