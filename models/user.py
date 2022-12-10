#!/usr/bin/python3
'''
user.py
'''

from .base_model import BaseModel, Base

from sqlalchemy import Column, Integer, String


class User(BaseModel, Base):
    '''defines user class'''
    __tablename__ = 'users'

    username = Column(String(60), nullable=False, unique=True)
    first_name = Column(String(60), nullable=False)
    middle_name = Column(String(60), nullable=True)
    last_name = Column(String(60), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
