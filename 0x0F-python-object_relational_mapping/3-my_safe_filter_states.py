#!/usr/bin/python3
'''displays all values where name matches arg,but safe from mqsql injections'''

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
                   WHERE `name` = %s
                   ORDER BY 'states.id' ASC""", (sys.argv[4],))
    for i in states:
        print("({}, '{}')".format(i[0], i[1]))
    states.close
    database.close
