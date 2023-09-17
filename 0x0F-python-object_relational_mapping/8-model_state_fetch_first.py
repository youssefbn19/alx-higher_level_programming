#!/usr/bin/python3
"""
    Prints the first State object from the database hbtn_0e_6_usa.
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
    state = session.query(State).first()
    if state:
        print(f'{state.id}: {state.name}')
    else:
        print("Nothing")
