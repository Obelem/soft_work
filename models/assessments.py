#!/usr/bin/python3
'''assessments.py'''
from .base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Text, PickleType
from sqlalchemy.ext.mutable import MutableList


class Assessment(BaseModel, Base):
    '''
    This class creates an Assesment Object.
    The Assesment object represents an assessment type
    '''
    __tablename__ = "assessments"
    name = Column(String(60), nullable=False, unique=True)
