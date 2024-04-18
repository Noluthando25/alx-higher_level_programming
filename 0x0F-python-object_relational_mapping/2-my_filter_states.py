#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], 
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    match = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    cursor = cursor.fetchall()

    for row in cursor:
        print(row)
    cursor.close()
    db.close()
