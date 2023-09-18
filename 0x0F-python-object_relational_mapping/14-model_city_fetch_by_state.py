#!/usr/bin/python3
"""
    Change the name of a State object from the database hbtn_0e_6_usa
    where id = 2 to New Mexico.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State, Base
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
             f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}'
             )
    Session = sessionmaker(engine)
    session = Session()
    cities = session.query(State.name, City.id, City.name).join(State).all()
    if cities:
        for city in cities:
            print(f"{city[0]}: ({city[1]}) {city[2]}")
