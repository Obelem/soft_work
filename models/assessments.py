#!/usr/bin/python3
'''assessments.py'''
from .base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship
import models


class Assessment(BaseModel, Base):
    '''
    This class creates an Assesment Object.
    The Assesment object represents an assessment type
    '''
    __tablename__ = "assessments"
    name = Column(String(60), nullable=False)

    questions = relationship('QuestionBank', back_populates='assessment', cascade='all, delete, delete-orphan')

    users = relationship('User', secondary='userAssessment', back_populates='assessments')
