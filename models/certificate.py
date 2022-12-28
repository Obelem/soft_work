#!/usr/bin/python3
'''certificates model'''
from .base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class Certificate(BaseModel, Base):
    '''implement certificates table'''
    __tablename__ = 'certificates'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    listening_skills = Column(Boolean, default=False)
    communication_skills = Column(Boolean, default=False)
    critical_thinking = Column(Boolean, default=False)

    user = relationship('User', back_populates='certificate')
