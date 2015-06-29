import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
   
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)
    picture = Column(String(250))

    @property
    def serialize(self):
        ''' return object data in easily serializeable format '''
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'picture': self.picture
        }


class Categories(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)
    vehicle_type = Column(String(250), nullable=False)
    description = Column(String(500))

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
            'id': self.id,
            'user_id': self.user_id,
            'vehicle_type': self.vehicle_type,
            'description': self.description
       }


class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    categories = relationship(Categories)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)
    make = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    description = Column(String(2000))
    picture1 = Column(String(250))
    picture2 = Column(String(250))
    picture3 = Column(String(250))
    displacement = Column(String(20))
    engine = Column(String(50))
    cylinders = Column(String(20))
    power = Column(String(20))
    speed = Column(String(20))
    seats = Column(String(20))
    weight = Column(String(20))
    year = Column(String(20))
    price = Column(String(20))


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'category_id': self.category_id,
            'user_id': self.user_id,
            'make': self.make,
            'model': self.model,
            'description': self.description,
            'picture1': self.picture1,
            'picture2': self.picture2,
            'picture3': self.picture3,
            'displacement': self.displacement,
            'engine': self.engine,
            'cylinders': self.cylinders,
            'power': self.power,
            'speed': self.speed,
            'seats': self.seats,
            'weight': self.weight,
            'year': self.weight,
            'price': self.price
        }


if __name__ == '__main__':
    engine = create_engine('postgresql:///catalog')

    # drops all table's rows
    Base.metadata.drop_all(engine)

    # creates all tables
    Base.metadata.create_all(engine)

