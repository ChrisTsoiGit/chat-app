import os
import pymongo
from fastapi import FastAPI

# create a MongoClient to connect to the DDBMS (Distributed Database Management System):
client = pymongo.MongoClient(os.environ["DATABASE_URL"])
dbname = os.environ['DATABASE_NAME']

# connect to a specific database name:
db = client[dbname]
