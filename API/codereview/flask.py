from flask import Flask
#from testtwitter2 import get_all_tweets
from twittertest import apicall
from newtwittertest import apicall

import t1
import output
import labels

app = Flask(__name__)



@app.route("/")
def hello():
	return """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset = "UTF-8">
	<title>Title</title>

</head>

	<body bgcolor="#F89C88">
	<h1> EC500 LOCAL WEBSITE: HAYATO NAKAMURA </h1>

		
        <img src="http://make.bu.edu/img/makebu-head.png" width="20%" height="20%">

		<p> To execute the code and see the runtime : add <b>/output</b> to the url </p>
		<p> To check the label output of the script, add this: <b> /labels </p>
		<p> To test error cases: </p>
		<p> Invalid Username: <b>/test1</b> <p>


<br>
<br>

		<p> OUTPUT VIDEO: (in .mp4 format) <p>
	<video controls>
  <source src="out.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

	</body>
</html>
	"""

@app.route("/output")
def out():
    ret = output.out()
    return str(ret)

@app.route("/labels")
def lab():
	ret = labels.lab()
	return str(ret)

@app.route("/test1")
def test1():
    ret = t1.test1()
    return str(ret)







if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

