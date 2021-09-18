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


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')