#!/usr/bin/python3
"""
    The module contains the class definition of
    a City and an instance Base = declarative_base().
"""


from sqlalchemy import (VARCHAR, Column, ForeignKey, ForeignKeyConstraint,
                        Integer, MetaData, PrimaryKeyConstraint,
                        UniqueConstraint)
from sqlalchemy.orm import declarative_base
from model_state import State, Base


class City(Base):
    """
    The class definition of a City table and an instance
    Base = declarative_base()

    Args:
        Base (class): The declarative base class wraps the mapper
        and the MetaData.
    """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True)
    name = Column(VARCHAR(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id, "cities_fk",
                      nullable=False))
    __table_args__ = (
        PrimaryKeyConstraint("id", name="state_pk"),
        UniqueConstraint("id", name="unique_id"),
    )
