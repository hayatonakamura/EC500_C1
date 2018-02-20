from newtwittertest import apicall
import os

def lab():
	# Output time
	ret = ''
	ret += '<body bgcolor="#88B8F8">'
	ret += "<h1> <b>Script Successful </b> </h1>"
	ret += ("<b>The following are the labels that are generated from the code: </b>")
	var = apicall('Hayatopia')
	ret += '<h1><p>' + str(var) + '</p></h1>'
	ret += '</body>'


	return ret


if __name__ == '__main__':
	lab()
