#Ivan Zhang
#SoftDev1 pd7
#K25: Getting More REST
#2018-11-14

from flask import Flask, render_template
import urllib.request
import json
import ssl
import random


context = ssl._create_unverified_context()

app = Flask(__name__)

@app.route("/")
def got():
	url = "https://api.got.show/api/characters/" # URL
	cri = urllib.request.Request(url) # SETS UP REQUEST
	stuff = urllib.request.urlopen(cri, context=context) # GETS STUFF 
	js = stuff.read() # gets info from urlopen
	jason = json.loads(js) # loads into JSON
	#print(jason)

	return render_template("nasa.html", characters = jason)

@app.route("/poke")
def poke():
	url = "http://swapi.co/api/planets/{}/".format(str(r)) # URL WITH RANDOM INT
	cri = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # SETS UP REQUEST
	stuff = urllib.request.urlopen(cri, context=context) # GETS STUFF 
	js = stuff.read() # gets info from urlopen
	jason = json.loads(js) # loads into JSON
	#print(jason)

	return render_template("nasa.html", _d = jason)
https://docs.google.com/document/d/1Dzcwh8tSxYQiXnEhezSDOa-iyqOWOfg-3iW45IiSvDo/edit#

@app.route("/memey")
def ():
	url = "http://swapi.co/api/planets/{}/".format(str(r)) # URL WITH RANDOM INT
	cri = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # SETS UP REQUEST
	stuff = urllib.request.urlopen(cri, context=context) # GETS STUFF 
	js = stuff.read() # gets info from urlopen
	jason = json.loads(js) # loads into JSON
	#print(jason)

	return render_template("nasa.html", _d = jason)

https://docs.google.com/document/d/14C5iN-B-43ie3FoU4T3A1yThAA99MXyzcJTU7skDo98/edit
if __name__ == "__main__":
	app.debug = True
	app.run()
