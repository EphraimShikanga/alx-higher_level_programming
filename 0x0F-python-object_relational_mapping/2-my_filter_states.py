#!/usr/bin/python3
"""
displays the value inthe states table of hbtn_0e_0_usa 
where name matches the argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    searched = sys.argv[4].strip("'")
    cursor = db.cursor()
    cursor.execute(
            """SELECT * FROM states
            WHERE name LIKE BINARY '{}'
            ORDER BY id ASC""".format(searched))
    [print(state) for state in cursor.fetchall()]
    cursor.close()
    db.close()
