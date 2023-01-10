#!/usr/bin/python3
'''stores completion status of user assessments'''
from .base_model import BaseModel, Base
from sqlalchemy import Boolean, Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


class Status(BaseModel, Base):
    '''stores assessment status of user'''
    __tablename__ = 'status'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    listening_skills = Column(Boolean, default=False)
    communication_skills = Column(Boolean, default=False)
    critical_thinking = Column(Boolean, default=False)

    user = relationship('User', back_populates='status')
