from flask import Flask

app = Flask(__name__)

first = '<!DOCTYPE html> <html lang="en"> <head> <meta charset = "UTF-8"> <title>Title</title> </head> <body> <h1> EC500 LOCAL WEBSITE: HAYATO NAKAMURA </h1> <p>'
second = "</p> </body> </html>"

imageurl = "https://pbs.twimg.com/media/DVJ7JaAVMAAESdw.jpg"
complete = '<img src="' + imageurl + '" width="20%" height="20%">'

run = first + complete + second

@app.route("/")
def hello():
	return (run)




if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)


	
