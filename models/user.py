#!/usr/bin/python3
'''user.py'''
from .base_model import BaseModel, Base
from sqlalchemy import Boolean, Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

metadata = Base.metadata

userAssessment = Table(
    'userAssessment',
    metadata,
    Column('users', ForeignKey('users.id'), primary_key=True),
    Column('assessments', ForeignKey('assessments.id'), primary_key=True)
)


class User(BaseModel, Base):
    '''defines user class'''
    __tablename__ = 'users'

    username = Column(String(60), nullable=False, unique=True)
    first_name = Column(String(60), nullable=False)
    middle_name = Column(String(60))
    last_name = Column(String(60), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    authenticated = Column(Boolean, default=False)
    profile_pic = Column(String(128), default="")

    assessments = relationship('Assessment', secondary='userAssessment', back_populates='users')

    status = relationship('Status', uselist=False, back_populates='user', cascade='all, delete, delete-orphan')
    score = relationship('Score', uselist=False, back_populates='user', cascade='all, delete, delete-orphan')
    certificate = relationship('Certificate', uselist=False, back_populates='user', cascade='all, delete, delete-orphan')

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.username

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
