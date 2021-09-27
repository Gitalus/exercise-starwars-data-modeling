from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

from eralchemy import render_er

Base = declarative_base()

class FavPlanets(Base):
    __tablename__ = 'fav_planets'
    
    user_id = Column(Integer, db.ForeignKey('users.id'), primary_key=True)
    planet_id = Column(Integer, db.ForeignKey('planets.id'), primary_key=True)
)

class FavCharacters(Base):
    __tablename__ = 'fav_characters'

    user_id = Column(Integer, db.ForeignKey('users.id'), primary_key=True),
    char_id = Column(Integer, db.ForeignKey('characters.id'), primary_key=True)
)

class Residents(Base):
    __tablename__ = 'residents'

    planet_id = Column(Integer, ForeignKey('planets.planet_id'))
    character = Column(Integer, ForeignKey('characters.character_id'), primary_key=True)

class Pilots(Base):
    __tablename__ = 'pilots'

    starship_id = Column(Integer, ForeignKey('starships.starship_id'), primary_key=True)
    pilot = Column(Integer, ForeignKey('characters.character_id'), primary_key=True)

class User(Base):
    __tablename__ = 'users'
    id = Column(db.Integer, primary_key=True)
    email = Column(String(200), unique=True, nullable=False)
    password = Column(String(200), unique=False, nullable=False)

    favorite_planets = Column(Integer, ForeignKey('fav_planets.planet_id'))
    favorite_characters = Column(Integer, ForeignKey('fav_characters.char_id'))

class Character(Base):
    __tablename__ = 'characters'

    character_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    heigth = Column(Float)
    mass = Column(Float)
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(20))
    birth_year = Column(String(20))
    gender = Column(String(20))
    homeworld = Column(Integer, ForeignKey('planets.planet_id'))
    starships = Column(Integer, ForeignKey('pilots.starship_id'))


class Planet(Base):
    __tablename__ = 'planets'

    planet_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    rotation_period = Column(Float)
    orbital_period = Column(Float)
    diameter = Column(Float)
    climate = Column(String(20))
    gravity = Column(String(20))
    terrain = Column(String(20))
    surface_water = Column(Float)
    population = Column(Integer)


class Starship(Base):
    __tablename__ = 'starships'

    starship_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    model = Column(String(20))
    manufacturer = Column(String(20))
    cost_in_credits = Column(Integer)
    length = Column(Float)
    max_atmosphering_speed = Column(Float)
    crew = Column(String(20))
    passengers = Column(Integer)
    cargo_capacity = Column(Float)
    consumables = Column(String(20))
    hyperdrive_rating = Column(Float)
    MGLT = Column(Integer)
    starship_class = Column(String(20))



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')