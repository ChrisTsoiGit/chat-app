import pymongo
import os

# import motor.motor_asyncio
# #connectoin between database.py and mango db
# client = motor.motor_asyncio.AsyncIOMotorClient('mangodb://localhoast:27017')
# database = client.accounts
# collection = database.blog

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


