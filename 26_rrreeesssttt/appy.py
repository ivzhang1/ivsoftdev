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
	url = "https://api.pokemontcg.io/v1/cards/"
	cri = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # SETS UP REQUEST
	stuff = urllib.request.urlopen(cri, context=context) # GETS STUFF 
	js = stuff.read() # gets info from urlopen
	jason = json.loads(js) # loads into JSON
	#print(jason)

	return render_template("poke.html", characters = jason["cards"])

@app.route("/memey")
def meme():
	url = "http://xkcd.com/{}/info.0.json".format(random.randrange(0,800))
	stuff = urllib.request.urlopen(url, context=context) # GETS STUFF 
	js = stuff.read() # gets info from urlopen
	jason = json.loads(js) # loads into JSON
	print(jason)

	return render_template("meme.html", _d = jason)

if __name__ == "__main__":
	app.debug = True
	app.run()
