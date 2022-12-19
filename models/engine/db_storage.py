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

    def all(self, cls=None):
        dict_of_objects = {}

        if cls is None:
            for _class in classes:
                list_of_objs = self.__session.query(_class).all()

                for obj in list_of_objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dict_of_objects[key] = obj

            return dict_of_objects

        cls = eval(cls) if type(cls) is str else cls
        if cls not in classes:
            return None

        obj_list = self.__session.query(cls).all()
        for obj in obj_list:
            key = type(obj).__name__ + '.' + obj.id
            dict_of_objects[key] = obj
        return dict_of_objects

    def get(self, cls, id):
        '''returns object based on the class and its ID or None if not found'''
        cls = eval(cls) if type(cls) is str else cls
        if cls not in classes or cls is None:
            return None
        objects = list(self.all(cls).values())
        for obj in objects:
            if id == obj.id:
                return obj
        return None


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

    def check_user(self, username=None, id=None):
        """
        checks if a user exists.
        returns User object if exists else None
        """
        if username:
            existing_user = self.__session.query(User).filter_by(username=username).first()
            if existing_user:
                return existing_user
            return None

        if id:
            existing_user = self.__session.query(User).filter_by(username=username).first()
            if existing_user:
                return existing_user
            return None

        return None

    def check_email(self, email=None):
        '''validates email'''
        existing_user = self.__session.query(User).filter_by(email=email).first()
        if existing_user:
            return existing_user
        return None

