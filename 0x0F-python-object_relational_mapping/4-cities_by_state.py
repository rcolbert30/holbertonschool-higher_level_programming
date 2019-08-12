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
    cities = database.cursor()
    cities.execute("""SELECT * FROM `cities`\
                   FROM cities JOIN states \
                   ON states.id - cities.state_id \
                   ORDER BY cities.id \
                   ASC""")
    for i in cities:
        print("({}, '{}', '{}')".format(i[0], i[2], i[4]))
    cities.close
    database.close
