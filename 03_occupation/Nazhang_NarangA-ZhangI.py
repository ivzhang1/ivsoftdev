# Nazhang - Amit Narang and Ivan Zhang
# SoftDev1 pd07
# K #06: StI/O: Divine your Destiny!
# 2018-09-13

from random import random, choices

# Returns a dictionary in the following manner: {"OCCUPATION_1":PERCENTAGE_1,"OCCUPATION_2":PERCENTAGE_2,...}
def makeOccupationDict():
	new_dict = {}

	f = open("occupations.csv", "r") # Opens file for reading

	for line in f.readlines(): # f.readlines() returns a list of lines

		line = line.replace('"', "") # Removes the unnecessary extra quotes

		line = line.strip() # Removes all extra new lines
		occupation_percentage = line.rsplit(",", 1) # Splits line in the format ["OCCUPATION", "PERCENTAGE"]

		if occupation_percentage[0] in "Job Class Total": # If the 1st value of the line is "Job Class" or "Total" skip it
			continue

		new_dict[occupation_percentage[0]] = float(occupation_percentage[1])/100 # Creates a new value in the form {"OCCUPATION": PERCENTAGE}

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
		
		x -= occupation_dict[key] # Subtract the decimal from x

		if x <= 0: # If x is less than or equal to zero, then x has been "subtracted enough"
			return key # Return the occupation


# In this case, we pass the function weightedAverageOccupation the dictionary of occupations from Function 1
# def weightedAverageOccupation(dictOfOccupations): 
#     # makes a list of the keys of the input dictionary
#     listOcc = list(dictOfOccupations.keys())
#     # makes a list of the values of the input dictionary
#     listWeight = list(dictOfOccupations.values())

#     # When given two parameters, random.choices uses the first as the 'population' and the second as the 'weight'.
#     # Since we pass the random.choices function the keys and the values (respectively), it uses the values,
#     # which were the percentage of total jobs each respective key is 'worth,' as the weight and picks from 
#     # the job descriptions.
#     return choices(listOcc,listWeight)[0]

print(selectRandom())

#print(weightedAverageOccupation(occupation_dict))
