from model import BlogPost, UserVO
import os
#mango db driver
import motor.motor_asyncio

from fastapi import FastAPI
import pymongo
import os


# #connectoin between database.py and mango 
# MONGO_URL = os.environ["DATABASE_URL"]
# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
# database = client.BlogPost
# collection = database.blog

MONGO_URL = os.environ["DATABASE_URL"]
client = pymongo.MongoClient(MONGO_URL)


class Queries:
    @property
    def collection(self):
        db = client[self.DB_NAME]
        return db[self.COLLECTION]

async def create_a_uservo(user):
    document = user
    result = await collection.insert_one(document)
    return document
    
async def fetch_all_users():
    users = []
    cursor = collection.find({})
    async for document in cursor:
        users.append(UserVO(**document))
    return users

async def fetch_a_blog_post(user):
    document = await collection.find_one({"user":user})
    return document

async def fetch_all_blogs():
    blogs = []
    cursor = collection.find({})
    async for document in cursor:
        blogs.append(BlogPost(**document))
    return blogs

async def create_a_blog(blog):
    document = blog
    result = await collection.insert_one(document)
    return document

async def update_blog(id, desc):
    await collection.update_one({'desc':desc},)


class AccountQueries(Queries):
    DB_NAME = "BlogsPosts"
    COLLECTION = "Blogs"

#     def get(self, username:str) -> AccountPasswordDB:
#         props = self.collection.find_one({"username": username})
#         if not props:
#             return None
#         props["id"] = str(props["_id"])
#         return AccountPasswordDB(**props)

    def create(self, info:UserVO):
        props = info.dict()
        self.collection.insert_one(props)
        props["id"] = str(props["_id"])
        return props

    def fetch_all_accounts(self):
        accounts = []
        props = self.collection.find({})
        for document in props:
            document['id'] = str(document['_id'])
            accounts.append(AccountOut(**document))
            print(document)
        return accounts

    def create_a_uservo(self, info:UserVO, ):
        document = self
        props = self.collection.insert_one(document)
        return document
