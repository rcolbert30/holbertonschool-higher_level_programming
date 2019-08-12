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
    ret = ""
    cities = database.cursor()
    a = cities.execute("SELECT * FROM `cities`\
                   INNER JOIN `states` \
                   ON states.id = cities.state_id \
                   WHERE states.name = %s\
                   ORDER BY cities.id \
                   ASC", (sys.argv[4],))
    for i in cities:
        ret += str(city[2]) + ","
    retstring = ret.strip(" , ")
    print(retstring)
    cities.close()
    database.close()
