# from fastapi import FastAPI
import pymongo
import os

MONGO_URL = os.environ.get("DATABASE_URL")
# MONGO_URL = os.environ.get("MONGODB_URI")
client = pymongo.MongoClient(MONGO_URL)


class Queries:
    @property
    def collection(self):
        db = client[self.DB_NAME]
        return db[self.COLLECTION]
