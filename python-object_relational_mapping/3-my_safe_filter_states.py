#!/usr/bin/python3
"""takes in arguments and displays all values in the states"""
import sys
import MySQLdb

def getStates():
    mydb = MySQLdb.connect(host='localhost',
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states WHERE name = %s \
                      ORDER BY states.id", (sys.argv[4],))
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

if __name__ == '__main__':
    getStates()
