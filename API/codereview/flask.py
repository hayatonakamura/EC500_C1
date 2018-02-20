from flask import Flask

app = Flask(__name__)

first = '<!DOCTYPE html> <html lang="en"> <head> <meta charset = "UTF-8"> <title>Title</title> </head> <body> <h1> EC500 LOCAL WEBSITE: HAYATO NAKAMURA </h1> <p>'
second = "</p> </body> </html>"

imageurl = "https://pbs.twimg.com/media/DVJ7JaAVMAAESdw.jpg"
complete1 = '<img src="' + imageurl + '" width="20%" height="20%">'

run = first + complete1 + second


@app.route("/")
def hello():
	return """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset = "UTF-8">
	<title>Title</title>

</head>

	<body>
	<h1> EC500 LOCAL WEBSITE: HAYATO NAKAMURA </h1>

		<p>
        <img src="https://pbs.twimg.com/media/DVJ7JaAVMAAESdw.jpg" width="20%" height="20%">
		</p>

	<video controls>
  <source src="out.mp4" type="video/mp4">
  <source src="out.ogg" type="video/ogg">
Your browser does not support the video tag.
</video>

	</body>
</html>
	"""




if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

