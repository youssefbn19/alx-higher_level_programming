#!/usr/bin/python3
"""
    The module lists all 'cities' of that 'state',
    using the database 'hbtn_0e_4_usa'.
"""
import MySQLdb
import sys


def filter_cities_by_state(params):
    """
    takes in the name of a state as an argument and lists all 'cities' of
    that 'state', using the database 'hbtn_0e_4_usa'.
    Args:
        params (list): list  take 4 arguments: mysql username,
        mysql password, database name and state name.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=params[0], passwd=params[1], db=params[2])
    cr = db.cursor()
    query = "SELECT c.name FROM cities c\
            JOIN states s ON c.state_id = s.id\
            WHERE s.name = %s\
            ORDER BY c.id"
    cr.execute(query, (params[3],))
    cities = cr.fetchall()
    num_cities = len(cities)
    if (num_cities > 0):
        for index in range(0, num_cities - 1):
            print(cities[index][0], end=", ")
        print(cities[num_cities - 1][0])
    else:
        print()
    cr.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        filter_cities_by_state(sys.argv[1:])
