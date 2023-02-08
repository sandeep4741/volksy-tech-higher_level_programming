#!/usr/bin/python3
"""lists all cities from state"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    sql = "select cities.name from cities left join states on states.id=cities.state_id where states.id=3;"
    num_rows = cur.execute(sql)
    for i in range(num_rows):
        print(cur.fetchone())
    cur.close()
    db.close()
