# Pandas - Alex Liu and Ivan Zhang
# SoftDev1 pd07
# K #10: Jinja Tuning ...
# 2018-09-21

from flask import Flask, render_template
from random import random

app = Flask(__name__)

# Returns a dictionary in the following manner: {"OCCUPATION_1":PERCENTAGE_1,"OCCUPATION_2":PERCENTAGE_2,...}
def makeOccupationDict():
	new_dict = {}

	f = open("data/occupations.csv", "r") # Opens file for reading

	for line in f.readlines(): # f.readlines() returns a list of lines

		line = line.replace('"', "") # Removes the unnecessary extra quotes

		line = line.strip() # Removes all extra new lines
		occupation_percentage = line.rsplit(",", 2) # Splits line in the format ["OCCUPATION", "PERCENTAGE"]

		if occupation_percentage[0] in "Job Class Total": # If the 1st value of the line is "Job Class" or "Total" skip it
			continue

		new_dict[occupation_percentage[0]] = (float(occupation_percentage[1])/100,occupation_percentage[2]) # Creates a new value in the form {"OCCUPATION": (PERCENTAGE, LINK) }

		#print(new_dict.keys(), new_dict[occupation_percentage[0]], new_dict.values())

	f.close()

	return new_dict

occupation_dict = makeOccupationDict() # Gets an dictionary occupation and their respective percentages

# Selects a random occupation
def selectRandom():
	x = random() # Random decimals from 0 to 1

	while(x >= .998): # x CANNOT BE .998 because occupational percentages add up to 99.8 rather than 100 (see 'occupations.csv')
		x = random() # Keep randomizing until x is less than .998

	for key in occupation_dict.keys():
		
		x -= occupation_dict[key][0] # Subtract the decimal from x

		if x <= 0: # If x is less than or equal to zero, then x has been "subtracted enough"
			return key # Return the occupation


@app.route("/")
@app.route("/occupations")
def occupations():
	 return render_template("occupations.html", random_occ = selectRandom(), occ_dictionary = occupation_dict)

if __name__ == "__main__":
	app.debug = True
	app.run()