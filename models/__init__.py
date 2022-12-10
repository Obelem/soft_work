#!/usr/bin/python3
'''defines storage instance'''
from dotenv import load_dotenv

if not load_dotenv("./.env"):
    print("No evironment variables set")
    exit()


from models.engine.db_storage import DBStorage

storage = DBStorage()

storage.reload()
