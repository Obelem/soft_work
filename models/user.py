#!/usr/bin/python3
'''user.py'''
from .base_model import BaseModel, Base
from flask_login import UserMixin
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

metadata = Base.metadata

userAssessment = Table(
    'userAssessment',
    metadata,
    Column('users', ForeignKey('users.id'), primary_key=True),
    Column('assessments', ForeignKey('assessments.id'), primary_key=True)
)


class User(UserMixin, BaseModel, Base):
    '''defines user class'''
    __tablename__ = 'users'

    username = Column(String(60), nullable=False, unique=True)
    first_name = Column(String(60), nullable=False)
    middle_name = Column(String(60))
    last_name = Column(String(60), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    assessments = relationship('Assessment', secondary='userAssessment', back_populates='users')
