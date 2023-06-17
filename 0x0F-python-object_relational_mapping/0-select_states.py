#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
in Ascending order
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
    # Create a cursor object to execute SQL queries
    cursor_object = db.cursor()
    # Execute the query to retrieve all states
    cursor_object.execute("SELECT * FROM states ORDER BY id ASC")
    #fetch all rows and prints the states
    rows = cursor_object.fetchall()
    for row in rows:
        state_id, state_name = row
        print(f"({state_id}, '{state_name}')")
    #close db 
    cursor_object.close()
    db.close()

