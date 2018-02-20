import twitter
import os

# Error Unit Testing 
# Capitals have no effect

# CASE 1
# Directory must be in same location as code, else will exit because image not found.

twitter.twitterdownloader("Hayatopia", "/Users/jleong/Desktop/EC500/HayatoCode/EC500_C1-master/API/")

try:
	twitter.twitterdownloader("HAYATOPIA", "/Users/jleong/Desktop/EC500/HayatoCode/EC500_C1-master/hellohello/")

# CASE 2
# Speed of program (UNIX only)
except:
	print("\ncase 1 error\n")

	try:
		os.system("time python twitter.py")

# CASE 3
# No Photos. Program will break and throw an error at Google Cloud Vision Step
	
		twitter.twitterdownloader("hellomyname000", "/Users/jleong/Desktop/EC500/HayatoCode/EC500_C1-master/API/")
	except:
		print("case 3 error")

