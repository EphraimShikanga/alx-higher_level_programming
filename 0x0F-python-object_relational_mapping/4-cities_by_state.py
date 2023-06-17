#!/usr/bin/python3
"""
lists all cities from the database
hbtn_0e_0_usa in ascending order by cities.id
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
            FROM cities INNER JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC""")
    rows = cursor.fetchall()
    for row in rows:
        print(tuple(row))
    cursor.close()
    db.close()
