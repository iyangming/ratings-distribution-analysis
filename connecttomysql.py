#!/usr/bin/python
import MySQLdb
import csv

# connect
db = MySQLdb.connect(host="127.0.0.1", user="web", passwd="atth1132", db="ML3_mirror")

def raw_ml3_ml4():
    with db as cursor:
        cursor.execute("SELECT * FROM ML3_mirror.user_rating_pairs where source!='ML4' limit 10")

        # get the number of rows in the resultset
        numrows = int(cursor.rowcount)
        with open("output.csv", "wb") as f:
            writer = csv.writer(f,delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow(['userId', 'movieId', 'rating', 'tstamp', 'source'])
            for x in range(0,numrows):
                row = cursor.fetchone()
                writer.writerow([row[0], row[1], row[2], row[3], row[4]])

if __name__ == "__main__":
    raw_ml3_ml4()
