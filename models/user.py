#!/usr/bin/python3
'''
user.py
'''

from .base_model import BaseModel, Base

from sqlalchemy import Column, Integer, String


class User(BaseModel, Base):
    '''defines user class'''
    email = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, primary_key=True, unique=True)
    password = Column(String(50), nullable=False)
