import pymongo
import pandas as pd 
import json
from dataclasses import dataclass
import os

#The @dataclass decorator is a decorator from the Python dataclasses module that is used to create classes that store data. 
#When you apply the @dataclass decorator to a class, 
#it automatically generates special methods for the class based on the variables defined in the class body.
@dataclass
class EnvironmentVariable:
        #Getting MongoDB URL from .env file
        mongo_db_url:str = os.getenv("mongo_sensor_url")

#Using __init__ and using @dataclass does the same thing
#class EnvironmentVariable:
#    def __init__(self,mongo_db_url):
#        mongo_db_url = os.getenv("mongo_sensor_url")


env_var = EnvironmentVariable()
#MongoDB URL
client = pymongo.MongoClient(env_var.mongo_db_url)