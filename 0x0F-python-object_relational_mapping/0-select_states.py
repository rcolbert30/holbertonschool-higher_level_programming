#!/usr/bin/python3
'''lists all states sform the database hbtn_0e_0_usa'''
import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               password=sys.argv[2],
                               user=sys.argv[1],
                               database=sys.argv[3])
    states = database.cursor()
    states.execute("SELECT * FROM states ORDER BY 'states.id' ASC")
    for i in states:
        print("({}, '{}')".format(i[0], i[1]))
