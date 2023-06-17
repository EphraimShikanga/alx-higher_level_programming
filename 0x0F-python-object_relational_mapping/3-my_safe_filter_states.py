#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
Safe from MySQL injections
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Retrieve MySQL connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the query to retrieve all states
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the states
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

