# Pandas - Alex Liu and Ivan Zhang
# SoftDev1 pd07
# K #10: Jinja Tuning ...
# 2018-09-21

from flask import Flask, render_template
from util import random_occ # Imports the random occupation generator from util

app = Flask(__name__)

@app.route("/")
@app.route("/occupations")
def occupations():
	occupation_dict = random_occ.makeOccupationDict("data/occupations.csv") # returns an occupations dictionary
	random_occupation  = random_occ.selectRandom("data/occupations.csv") # returns a random occupation
	return render_template("occupations.html", random_occ = random_occupation, occ_dictionary = occupation_dict)

if __name__ == "__main__":
	app.debug = True
	app.run()
