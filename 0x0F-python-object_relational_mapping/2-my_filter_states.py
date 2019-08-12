#!/usr/bin/python3

'''displays all values in the states table of hbtn_0e_0_usa if matches name'''

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
			WHERE BINARY `name` = '{}'
			ORDER BY 'states.id' ASC""".format(sys.argv[4]))
	for i in states:
		print("({}, '{}')".format(i[0], i[1]))
	states.close()
	database.close()
