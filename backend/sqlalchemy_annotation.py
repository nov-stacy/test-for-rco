from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name_u = Column(String, unique=True)

    def __init__(self, name):
        self.name_u = name


class Parameter(Base):

    __tablename__ = 'parameters'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name_p = Column(String)
    type_p = Column(String)
    value_p = Column(String)

    def __init__(self, user_id, name, type_, value):
        self.user_id = user_id
        self.name_p = name,
        self.type_p = type_
        self.value_p = value
