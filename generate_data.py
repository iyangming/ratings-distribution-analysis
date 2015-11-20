#!/usr/bin/python
import MySQLdb
import csv

# connect
db = MySQLdb.connect(host="127.0.0.1", user="web", passwd="atth1132", db="ML3_mirror")

def raw(fn, query):
    with db as cursor:
        cursor.execute(query)

        # get the number of rows in the resultset
        numrows = int(cursor.rowcount)
        with open("out/%s" % fn, "wb") as f:
            writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow(['userId', 'movieId', 'rating', 'tstamp', 'source'])
            for x in range(0,numrows):
                row = cursor.fetchone()
                writer.writerow([row[0], row[1], row[2], row[3], row[4]])

def raw_ml3():
    raw("raw_ml3.csv", "SELECT * FROM ML3_mirror.user_rating_pairs where source!='ML4' and rating > 0")

def raw_ml4():
    raw("raw_ml4.csv", "SELECT * FROM ML3_mirror.user_rating_pairs where source='ML4' and rating > 0")

if __name__ == "__main__":
    raw_ml3()
    raw_ml4()
