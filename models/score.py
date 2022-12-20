'''user.py'''
from .base_model import BaseModel, Base
from sqlalchemy import Boolean, Column, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship


class Score(BaseModel, Base):
    '''stores scores'''
    __tablename__ = 'scores'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    listening_skills = Column(Float)
    communication_skills = Column(Float)
    critical_thinking = Column(Float)

    user = relationship('User', back_populates='score')
