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

# cars 
class Categories(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)
    
    vehicle_type = Column(String(250), nullable=False)
    #picture = Column(String(250))
    description = Column(String(500))

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
           # 'picture'      : self.picture,
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
    displacement = Column(String(250))
    engine = Column(String(15))
    cylinders = Column(String(250))
    power = Column(String(250))
    speed = Column(String(250))
    seats = Column(String(250))
    weight = Column(String(250))
    year = Column(String(250))
    price = Column(String(12))


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'make'           : self.make,
           'model'           : self.model,
           'description'    : self.description,
           'id'             : self.id,
       }


if __name__ == '__main__':
    engine = create_engine('postgresql:///catalog')

    # drops all table's rows
    Base.metadata.drop_all(engine)

    # creates all tables
    Base.metadata.create_all(engine)

