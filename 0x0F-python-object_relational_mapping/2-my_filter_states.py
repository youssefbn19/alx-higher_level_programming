#!/usr/bin/python3
"""
    The module takes in an argument and displays all values in
    the 'states' table of 'hbtn_0e_0_usa' where name matches the argument.
"""
import MySQLdb
import sys


def filter_states_by_name(params):
    """
    Filter states table with a state name given as an argument
    to the module.
    Args:
        params (list): list  take 4 arguments: mysql username,
        mysql password, database name and state name searched.
    """
    state_db = MySQLdb.connect(host="localhost", port=3306,
                               user=params[1], passwd=params[2], db=params[3])
    cr = state_db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
               ORDER BY states.id ASC".format(params[4])
    cr.execute(query)
    states = cr.fetchall()
    for state in states:
        print(state)
    cr.close()
    state_db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        filter_states_by_name(sys.argv)
