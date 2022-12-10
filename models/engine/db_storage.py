#!/usr/bin/python3
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from models.base_model import Base
from models.user import User


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user, password = getenv('user'), getenv('password')
        host, db = getenv('host'), getenv('db')

        url = f'mysql+mysqldb://{user}:{password}@{host}/{db}'

        self.__engine = create_engine(url, pool_pre_ping=True)


    def reload(self):
        ''' reload engine '''
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def new(self, obj):
        '''adds a new record (object) to session'''
        self.__session.add(obj)

    def save(self):
        ''' saves a new record (object) to table '''
        self.__session.commit()
