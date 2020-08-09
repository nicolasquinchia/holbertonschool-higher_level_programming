#!/usr/bin/python3
"""Takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
    """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    str_q = "SELECT cities.name FROM cities LEFT JOIN states"
    str_q += " ON cities.state_id = states.id WHERE states.name LIKE BINARY %s"
    cur.execute(str_q, (argv[4], ))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        cities.append(row[0])
    str_cities = ", ".join(cities)
    print(str_cities)
    cur.close()
    db.close()
