#!/usr/bin/python3
"""
    The module contains the class definition of
    a State and an instance Base = declarative_base().
"""
from sqlalchemy import (VARCHAR, Column,
                        Integer, MetaData, PrimaryKeyConstraint,
                        UniqueConstraint)
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    """
    The class definition of a State table and an instance
    Base = declarative_base()

    Args:
        Base (class): The declarative base class wraps the mapper
        and the MetaData.
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True)
    name = Column(VARCHAR(128), nullable=False)
    __table_args__ = (
        PrimaryKeyConstraint("id", name="state_pk"),
        UniqueConstraint("id", name="unique_id")
    )
