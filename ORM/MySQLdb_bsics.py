#!/usr/bin/env python3
"""This script contains basic commands used in establishing a db connection
using MySQLdb and python"""

import MySQLdb
# To establish a connection to an MySQL database
db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_db)

# Getting a cursor [allows to extablish multiple separate working environments through the same connection to the database
cur = db.cursor() 
# note that this is the default cursor class multiple cursor classes exists. To access them you specify the 'cursorclass' parameter to the class you desire.E.g. 'DictCursor' sets results returned as python dictionaries.

# Executing queries in Python
cur.execute("CREATE TABLE song ( id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL )") # creating a table

# Executing an insertion query (single substitution query)
songs = ('Purple Haze', 'All Along the Watch Tower', 'Foxy Lady')
for song in songs:
    cur.execute("INSERT INTO song (title) VALUE (%s)", song)
    print 'Auto Increment ID: %s' % cur.lastrowid # autogenerate an id

# Executing multiple substitution query
cur.execute("SELECT * FROM song WHERE id = %s or id = %s", (1, 2)) # always use a tuple to specify multiple vals

# Execute Select
numrows = cur.execute("SELECT * FROM song")
print "Selected %s rows" % numrows
print "Selected %s rows" % cur.rowcount # most preferred way to access num or rows

# Obtaining query results
# After executing any SELECT statement, you will need to use one of two methods to obtain results

# METHOD_1: Fetch all at once
# print results in comma delimited format
cur.execute("SELECT * FROM song")
rows = cur.fetchall()
for row in rows:
    for col in row:
        print "%s, " % col
    print "\n"


# METHOD_2: Fetch One-at-a-time
cur.execute("SELECT * FROM song WHERE id = 1")
print("Id: %s -- Title: %s" % cur.fetchone())


# Exceptions and Errors
""" Every execute statement has the potential to raise an exception error.
It is good practice to surround every query statement in a try/except block
"""

# Get data from db
try:
    cur.execute("SELECT * FROM song")
    rows = cur.fetchall()
except MySQLdb.Error, e: # most commonly used module error
    try:
        print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
    except IndexError:
        print "MySQL Error: %s" % str(e)

# Print results in a comma delimited format
for row in rows:
    for col in row:
        print "%s, " % col
    print "\n"

# After executing each connection, we close the cursor and db connection as clean up

# close all cursors
cur.close()

# close all databases
db.close()
