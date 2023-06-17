#!/usr/bin/python3
"""
lists all cities of a state passed as argumentfrom the database
hbtn_0e_0_usa in ascending order by cities.id
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    searched = sys.argv[4]
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name
            FROM cities INNER JOIN states
            ON cities.state_id = states.id
            WHERE states.name LIKE %s
            ORDER BY cities.id ASC""", (searched,))
    print(", ".join([city[0] for city in cursor.fetchall()]))
    cursor.close()
    db.close()
