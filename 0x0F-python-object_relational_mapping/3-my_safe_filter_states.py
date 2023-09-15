#!/usr/bin/python3
"""
    The module takes in arguments and displays all values in
    the 'states' table of 'hbtn_0e_0_usa' where name matches the argument.
    But this time, write one that is safe from MySQL injections.
"""
import MySQLdb
import sys


def filter_states_safe_by_name(params):
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
    query = "SELECT * FROM states WHERE name LIKE BINARY %s\
            ORDER BY states.id ASC"
    cr.execute(query, (params[4],))
    states = cr.fetchall()
    for state in states:
        print(state)
    cr.close()
    state_db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        filter_states_safe_by_name(sys.argv)
