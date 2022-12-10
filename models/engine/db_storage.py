#!/usr/bin/python3
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from models.base_model import Base
from models.user import User
from models.assessments import Assessment
from models.question_bank import QuestionBank
# from models.user_assessment import UserAssessment


classes = [User, Assessment, QuestionBank]

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        USER, PWD = getenv('USER'), getenv('PWD')
        HOST, DB = getenv('HOST'), getenv('DB')
        ENV = getenv("ENV")

        url = f'mysql+mysqldb://{USER}:{PWD}@{HOST}/{DB}'

        self.__engine = create_engine(url, pool_pre_ping=True)

    def all(self, cls):
        dict_of_objects = {}

        cls = eval(cls) if type(cls) is str else cls
        if cls not in classes:
            return None

        obj_list = self.__session.query(cls).all()
        for obj in obj_list:
            key = type(obj).__name__ + '.' + obj.id
            dict_of_objects[key] = obj
        return dict_of_objects


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
