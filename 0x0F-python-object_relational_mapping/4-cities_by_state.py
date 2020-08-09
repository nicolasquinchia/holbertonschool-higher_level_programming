#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa
    """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    str_q = "SELECT cities.id, cities.name, states.name FROM cities"
    str_q += " LEFT JOIN states ON cities.state_id = states.id;"
    cur.execute(str_q)
    rows = cur.fetchall()
    for row in rows:
        print(row)
