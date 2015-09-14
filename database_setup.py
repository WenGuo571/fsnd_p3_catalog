import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Catagory(Base):
    __tablename__ = 'catagory'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return catagory in serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
        }


class CatagoryItem(Base):
    __tablename__ = 'catagory_item'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    edit_time = Column(DateTime, nullable=False)
    catagory_name = Column(Integer, ForeignKey('catagory.name'))
    catagory = relationship(Catagory)

    @property
    def serialize(self):
        """Return item in serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'catagory_name': self.catagory_name,
            'description': self.description,
        }


engine = create_engine('sqlite:///catalog.db')


Base.metadata.create_all(engine)
