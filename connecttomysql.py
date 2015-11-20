#!/usr/bin/python
import MySQLdb
import csv

# connect
db = MySQLdb.connect(host="localhost", user="web", passwd="atth1132",
db="ML3_mirror")

cursor = db.cursor()

# execute SQL select statement
cursor.execute("SELECT * FROM ML3_mirror.user_rating_pairs where source!='ML4'")

# commit your changes
db.commit()

# get the number of rows in the resultset
numrows = int(cursor.rowcount)
with open("output.csv", "wb") as f:
    writer = csv.writer(f,delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    writer.writerow(['userId', 'movieId', 'rating', 'tstamp', 'source'])
    for x in range(0,numrows):
   		row = cursor.fetchone()
   		writer.writerow([row[0], row[1], row[2], row[3], row[4]])