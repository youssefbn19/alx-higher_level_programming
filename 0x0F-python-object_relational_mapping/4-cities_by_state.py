#!/usr/bin/python3
"""
    The module lists all 'cities' from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


def cities_by_state(params):
    """
    List all 'cities' from the database hbtn_0e_4_usa.
    Args:
        params (list): list  take 3 arguments: mysql username,
        mysql password, database name.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=params[0], passwd=params[1], db=params[2])
    cr = db.cursor()
    query = "SELECT c.id, c.name, s.name FROM cities c\
            JOIN states s ON c.state_id = s.id\
            ORDER BY c.id"
    cr.execute(query)
    cities = cr.fetchall()
    for city in cities:
        print(city)
    cr.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        cities_by_state(sys.argv[1:])
