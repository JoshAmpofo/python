#!/usr/bin/python3
"""This script details how to use sqlalchemy as an ORM"""

# connecting to database
from sqlalchemy import create_engine
# using an in-memory-only SQLite db
engine = create_engine('sqlite:///:memory:', echo=True)
# declaring a Mapping
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Now we create tables
from sqlalchemy import Column, Integer, String
class User(Base):  # inheriting from Base
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):  # optional but needed for beautiful repr'
        """canonical representation of string"""
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)
