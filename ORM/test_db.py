#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
# take input from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

# connect to database
    try:
        db = MySQLdb.connect(
                host="localhost", user=mysql_username,
                passwd=mysql_password,
                db=database_name,
                port=3306)

        cur = db.cursor()

    except MySQLdb.Error as e:
        print(f"MySQL Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)

# execute query selection 
    try:
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        states = cur.fetchall()
    except MySQLdb.Error as e:
        print(f"MySQL Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)
# print data 
    for state in states:
        print(state)
# close all connections (cursor and database)
    cur.close()
    db.close()
