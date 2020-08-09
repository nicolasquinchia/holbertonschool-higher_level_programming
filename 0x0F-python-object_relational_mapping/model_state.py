#!/usr/bin/python3
"""Module that holds the State Class
    """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class to link to a Sql table states
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
