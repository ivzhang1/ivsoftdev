# Ivan Zhang
# SoftDev1 pd07
# K #08: Fill Yer Flask
# 2018-09-18   

from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def home():
	return '''Cool Home Page: 
		<ul>
		<li> <a href = '/'> Home </a>  </li>
		<li> <a href = '/random'> Random Saying </a> </li> 
		<li> <a href = '/animals'> Random Animal </a> </li> 
		</ul>'''

@app.route("/random")
def random_page():

	sayings = ["Visit the Dojo", "Something will happen today", "A beautiful, smart, and loving person will be coming into your life.", 
				"A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.", "All the troubles you have will pass away very quickly."]
	return sayings[randint(0,len(sayings)-1)] + ''' <ul>
		<li> <a href = '/'> Home </a>  </li>
		<li> <a href = '/random'> Random Saying </a> </li> 
		<li> <a href = '/animals'> Random Animal </a> </li> 
		</ul>'''

@app.route("/animals")
def animals():
	list_animals = ["https://mbtskoudsalg.com/images/cute-animal-png-1.png", "http://pngimg.com/uploads/leopard/leopard_PNG14821.png", "https://png.pngtree.com/element_origin_min_pic/16/06/19/1457663edebbfc2.jpg",
					"http://pngimg.com/uploads/hippo/hippo_PNG16.png"]
	return '''<ul>
		<li> <a href = '/'> Home </a>  </li>
		<li> <a href = '/random'> Random Saying </a> </li> 
		<li> <a href = '/animals'> Random Animal </a> </li> 
		</ul>''' + "<img src = " + list_animals[randint(0,len(list_animals)-1)] + ">"


if __name__ == "__main__":
	app.debug = True
	app.run()