#!/usr/bin/python3
'''certificates model'''
from .base_model import BaseModel, Base
from sqlalchemy import Boolean, Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


class Certificate(BaseModel, Base):
    '''implement certificates table'''
    __tablename__ = 'certificates'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    listening_skills = Column(String(240))
    communication_skills = Column(String(240))
    critical_thinking = Column(String(240))

    user = relationship('User', back_populates='certificate')
