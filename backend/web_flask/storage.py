#!/usr/bin/python3
"""store everything in a database"""
import os
import json
import requests
import time
from PIL import Image
from io import BytesIO
from rich.console import Console
from rich.text import Text
from dotenv import load_dotenv
# import sqlite3 as sql # this is the database
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
db = create_engine('sqlite:///food.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=db)
session = Session()
session = scoped_session(sessionmaker(bind=db))  # this is the session
Base.metadata.create_all(db) # this is the base metadata
Base.metadata.bind = db # this is the base metadata
storage_type = os.get_env("STORAGE_TYPE", "db")

class Filestorage:
    def __init__(self):
        pass
    def create_db(self):
        """create the database"""
        try:
            with db.connect("food.db") as con: # this is the database
                cur = con.cursor() # this is the cursor
                cur.execute("CREATE TABLE IF NOT EXISTS food (id INTEGER PRIMARY KEY, name TEXT, cuisine TEXT, image TEXT, instructions TEXT, ingredients TEXT, nutrition TEXT, summary TEXT)")
                con.commit() # this is the commit command to save the changes
        except Exception as e:
            print(e)
    def storage():
        """use the database or json file to store the data from the API"""
        if storage_type == "db":
            return Filestorage()