#!/usr/bin/python3
"""
    Change the name of a State object from the database hbtn_0e_6_usa
    where id = 2 to New Mexico.
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
    state_2 = session.get(State, 2)
    state_2.name = "New Mexico"
    session.add(state_2)
    session.commit()
