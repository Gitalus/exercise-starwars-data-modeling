from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

from eralchemy import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table characters
    character_id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    heigth = Column(Float())
    mass = Column(Float())
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(20))
    birth_year = Column(String(20))
    gender = Column(String(20))
    homeworld = Column(Integer(), ForeignKey('planets.planet_id'))
    starships = Column(Integer(), ForeignKey('starships.starship_id'))


class Planet(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table planets.
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    rotation_period = Column(Float())
    orbital_period = Column(Float())
    diameter = Column(Float())
    climate = Column(String(20))
    gravity = Column(String(20))
    terrain = Column(String(20))
    surface_water = Column(Float())
    population = Column(Integer())

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')