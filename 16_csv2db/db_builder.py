#HYPERS - Ivan Zhang and Jerry Ye
#SoftDev1 pd7
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


name = filename.split(".")[0]
DB_FILE= "pepes.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
command = "CREATE TABLE {table_name}(name TEXT, age INTEGER, id INTEGER)".format(table_name = "pepes")
c.execute(command)

with open("peeps.csv", newline = "") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        command = 'INSERT INTO pepes VALUES ("{name}", {age}, {id}) '.format(name=row['name'],age=row['age'],id=row['id'])
        c.execute(command)

#command = ""          #build SQL stmt, save as string
#c.execute(command)    #run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database



