#!/usr/bin/python3
'''lists all states with a name starting with N (upper N) from the database'''
import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               password=sys.argv[2],
                               user=sys.argv[1],
                               database=sys.argv[3])
	states = database.cursor()
	states.execute("""SELECT * FROM states 
			WHERE name 
			LIKE BINARY 'N%'
			ORDER BY 'states.id' ASC""")
	for i in states:
		print("({},'{}')".format(i[0], i[1]))
	states.close()
	database.close() 
