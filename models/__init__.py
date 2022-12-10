#!/usr/bin/python3
'''defines storage instance'''
from models.engine.db_storage import DBStorage

storage = DBStorage()

storage.reload()
