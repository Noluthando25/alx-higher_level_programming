import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=noluthando25, passwd=freestate, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
