#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
import datetime
import models


Base = declarative_base()


class BaseModel:
    id = Column(String(60), nullable=False, primary_key=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)
        if self.id is None:
            self.id = str(uuid.uuid4())
        if self.created_at is None:
            self.created_at = datetime.datetime.utcnow()
        if self.updated_at is None:
            self.updated_at = datetime.datetime.utcnow()


    def __str__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        models.storage.delete(self)

    def to_dict(self):
        data = dict(self.__dict__)
        data.pop('_sa_instance_state', None)
        if 'created_at' in data:
            data['created_at'] = data['created_at'].isoformat()
        if 'updated_at' in data:
            data['updated_at'] = data['updated_at'].isoformat()
        return data

