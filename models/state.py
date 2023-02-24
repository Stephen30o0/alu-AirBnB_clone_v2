#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if storage_type == 'db':
        cities = relationship('City', cascade='all, delete-orphan', backref='state')
    else:
        @property
        def cities(self):
            from models import storage
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list

