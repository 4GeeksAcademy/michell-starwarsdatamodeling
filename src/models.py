import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    lastName = Column(String(200), nullable=False)
    user_name = Column(String(200))
    email= Column(String(200))
    password= Column(String(200))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name= Column(String(80))
    description= Column(String(250))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    climate = Column(String(80))
    terrain = Column(String(80))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(String(60), primary_key=True)
    name= Column(String(60))
    description= Column(String(250))
    gender= Column(String(60))
    mass= Column(Integer)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'))
    character_id= Column(Integer, ForeignKey('characters.id'))
    planet_id= Column(Integer, ForeignKey('planets.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
