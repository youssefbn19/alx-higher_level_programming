#!/usr/bin/python3
"""
    The module lists all 'states' with a name starting with N (upper N)
    from the database 'hbtn_0e_0_usa'
"""
import MySQLdb
import sys


def filter_states(params):
    """
    Filter states table with a name starting with N (upper N).
    Args:
        params (list): list  take 3 arguments: mysql username,
        mysql password and database name
    """
    state_db = MySQLdb.connect(host="localhost", port=3306,
                               user=params[1], passwd=params[2], db=params[3])
    cr = state_db.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
               ORDER BY states.id ASC")
    states = cr.fetchall()
    for state in states:
        print(state)
    cr.close()
    state_db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        filter_states(sys.argv)
