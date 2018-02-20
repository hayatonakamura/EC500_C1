# EC500 Code Analysis

   ### Part 1
    
The file, CodeAnalysis.md, analyses my partner's code in depth, going over syntax, error handling, API call, cleanliness, and the accuracy of execution.
testcases.py will run the python script (re-named testtwitter2.py) with three test cases: 
  1. Non-existent Twitter Handle
  2. Twitter Handle with no photos
  3. Unrecognisable .json file or twitter credentials
  
Finally, I have suggested improvements, on my partner's github, labeled as issues for each missing section that I was able to discover. To view this, go to: https://github.com/WeiXinqiao/EC500_C1/tree/master/HW1_API


   ### Part 2:
    
In order to create a local website, I used the library *flask*, and displayed the necessary information on http://localhost:5000/ .

The following cases were tested:
1. Time it takes to execute the file
2. The google cloud vision labels
3. Invalid Username Case



### Aside:

The file **flasktest.py** is simply to test if the flask library works. Refer to **flask.py** for the actual main code. 
Make sure the name of the python scripts are consistent, and all in the same file. 
modified.py is specifically for returning the time, while newtwittertest.py is for printing out the labels. Both are modified so that they take in certain input arguments as a function, and delete the original video itself as well. Compare the original twitter.py in the main API folder for details.
