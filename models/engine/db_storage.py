#!/usr/bin/python3
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        USER = getenv("USER")
        PWD = getenv("PWD")
        HOST = getenv("HOST")
        DB = getenv("DB")
        ENV = getenv("ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(USER,
                                             PWD,
                                             HOST,
                                             DB))
        if ENV == "test":
            Base.metadata.drop_all(self.__engine)


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
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
