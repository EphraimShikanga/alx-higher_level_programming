#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
in Ascending order
"""
import sys
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    cursor_object = db.cursor()
    cursor_object.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor_object.fetchall():
        state_id, state_name = row
        print(f"({state_id}, '{state_name}')")
    cursor_object.close()
    db.close()
