#!/usr/bin/python3
"""The module lists all 'states' from the database 'hbtn_0e_0_usa'
"""

import MySQLdb
import sys

params = sys.argv
if (len(params) == 4):
    state_db = MySQLdb.connect(host="localhost", port=3306,
                               user=params[1], passwd=params[2], db=params[3])
    cr = state_db.cursor()
    cr.execute("SELECT * FROM states")

    states = cr.fetchall()
    for state in states:
        print(state)

    cr.close()
    state_db.close()
