#!usr/bin/python3

"""
displays all states from the database
hbtn_0e_0_usa in ascending order by states.id
where name matches the argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    searched = sys.argv[4]
    cursor = db.cursor()
    cursor.execute(
            """SELECT * FROM 'states'
            WHERE name LIKE %s ORDER BY id ASC""",
            (searched,))
    [print(state) for state in cursor.fetchall()]
    cursor.close()
    db.close()
