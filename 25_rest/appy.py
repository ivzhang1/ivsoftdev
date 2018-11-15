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
def stars():
	r = random.randrange(0, 50)
	url = "http://swapi.co/api/planets/{}/".format(str(r)) # URL WITH RANDOM INT
	cri = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # SETS UP REQUEST
	stuff = urllib.request.urlopen(cri, context=context) # GETS STUFF 
	js = stuff.read() # gets info from urlopen
	jason = json.loads(js) # loads into JSON
	#print(jason)

	return render_template("nasa.html", _d = jason)



if __name__ == "__main__":
	app.debug = True
	app.run()
