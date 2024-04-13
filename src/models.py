import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

   

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birthday_year = Column(String(250))
    eye_color = Column(String(250))
    films = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    height = Column(Integer)
    homeworld = Column(String(250))
    mass = Column(Integer)
    skin_color = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    species = Column(String(250))
    starships = Column(String(250))
    url = Column(String(250))
    vehicles = Column(String(250))
    


class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    climate = Column(String(250))
    created = Column(String(250))
    diameter = Column(Integer)
    edited = Column(String(250))
    films = Column(String(250))
    gravity = Column(Integer)
    name = Column(String(250))
    orbital_period = Column(Integer)
    population = Column(Integer)
    residents = Column(String(250))
    rotation_period = Column(Integer)
    surface_water = Column(Integer)
    terrain = Column(String(250))
    url = Column(String(250))

    
    
class Favorites_People(Base):
    __tablename__ = 'favorites_people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People)

class Favorites_Planet(Base):
    __tablename__ = 'favorites_planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)







# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     test = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
