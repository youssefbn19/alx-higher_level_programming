#!/usr/bin/python3
"""
    Lists all State objects from the database hbtn_0e_6_usa.
"""
import sys


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State

if __name__ == "__main__":
    engine = create_engine(
             f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}'
             )
    Session = sessionmaker(engine)
    session = Session()
    states_data = session.query(State).all()
    for state in states_data:
        print(f'{state.id}: {state.name}')
