#Ivan Zhang
#SoftDev1 pd7
#K24 - A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template
import urllib.request
import json
import ssl


context = ssl._create_unverified_context()

app = Flask(__name__)

@app.route("/")
def stars():
    url = "https://api.nasa.gov/planetary/apod?api_key=wv7X1ZwzclmKH1VSh8sqjgoYeip2bc6rl2tAXtJS" # NASA link with API KEY
    stuff = urllib.request.urlopen(url, context=context) # GETS NASA API stuff
    js = stuff.read() # gets info from urlopen
    jason = json.loads(js) # loads into JSON
    img_u = jason['url'] #gets img url
    return render_template("nasa.html", url = img_u, desc = jason['explanation'])



if __name__ == "__main__":
	app.debug = True
	app.run()
