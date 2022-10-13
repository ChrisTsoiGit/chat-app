from fastapi import FastAPI
import pymongo
import os

# client = pymongo.MongoClient(os.environ["DATABASE_URL"])
# dbname = os.environ['DATABASE_NAME']
# db = client[dbname]

MONGO_URL = os.environ["DATABASE_URL"]
client = pymongo.MongoClient(MONGO_URL)


class Queries:
    @property
    def collection(self):
        db = client[self.DB_NAME]
        return db[self.COLLECTION]
