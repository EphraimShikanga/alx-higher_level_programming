#!/usr/bin/python3
"""
lists all states in the database
"""

import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
            host = "localhost",
            port = 3306,
            user = username,
            passwd = password,
            db = db_name
        )
    cursor_object = db.cursor()
    cursor_object.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor_object.fetchall()

    for row in rows:
        state_id, state_name = row
        print(f"({state_id}, {state_name})")

    cursor_object.close()
    db.close()

