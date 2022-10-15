import os
import pymongo

# create a Mongo client to connect to the DDBMS (Distributed Database Management System):
MONGO_URL = os.environ["DATABASE_URL"]
client = pymongo.MongoClient(MONGO_URL)

class Queries:
    @property
    def collection(self):
        db = client[self.DB_NAME] # accountQueries
        return db[self.COLLECTION]
