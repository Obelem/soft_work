#!/usr/bin/python3
'''
    defines the BaseModel class from which all
    other classes would inherit common attributes and
    methods from
'''
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    '''BaseModel class definition'''
    id = Column(String(60), nullable=False,
                primary_key=True, default=str(uuid4()))
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))


    def __init__(self, *args, **kwargs):
        '''
            all classes inherit the following attributes:
                id, created_at and updated_at
        '''
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()

        if kwargs == {}:
            return

        for key, value in kwargs.items():
            if key in ['created_at', 'updated_at']:
                value = datetime.fromisoformat(value)
            if key != '__class__':
                self.__dict__[key] = value

    def __str__(self):
        ''' defines custom string representation of object '''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
