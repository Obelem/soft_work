#!/usr/bin/python3
from os import getenv, environ
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from models.base_model import Base
from models.user import User
from models.assessments import Assessment
from models.question_bank import QuestionBank

classes = [User, Assessment, QuestionBank]

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        S_USER, S_PWD = environ['S_USER'], environ['S_PWD']
        S_HOST, S_DB = environ['S_HOST'], environ['S_DB']

        url = f'mysql+mysqldb://{S_USER}:{S_PWD}@{S_HOST}/{S_DB}'

        self.__engine = create_engine(url, pool_pre_ping=True)


    def new(self, obj):
        self.__session.add(obj)


    def save(self):
        self.__session.commit()


    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def check_user(self, username):
        """
        checks if a user exists.
        returns User object if exists else None
        """
        existing_user = self.__session.query(User).filter_by(username=username).first()
        if existing_user:
            return existing_user
        return None
