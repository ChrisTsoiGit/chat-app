from pydantic import BaseModel, EmailStr
from queries.mongoclient import Queries
from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()

class UserVO(BaseModel):
    id: str
    username : str
    email: EmailStr
    full_name: str

class BlogPost(BaseModel):
    user: UserVO
    pic: str
    location: str
    time: str
    likes: int
    user: int
    desc: str

class BlogComment(BaseModel):
    blog: BlogPost
    user: UserVO
    comment: str
    time: int

# this queries should be DB
class BlogQueries(Queries):
    DB_NAME = "posts"
    COLLECTION = "blogs"

    def create_a_uservo(self, user):
        document = user
        # print('document:', document)
        result = self.collection.insert_one(document)
        # print('results:', result)
        return result

    
    def fetch_all_users(self):
        users = []
        props = self.collection.find({})
        for document in props:
            document['id'] = str(document['_id'])
            users.append(UserVO(**document))
            print(document)
        return users

    def create_a_Blog(self, blog):
        document = blog
        print('document :', document)
        # print('document:', document)
        result = self.collection.insert_one(document)
        print('results:', result)
        # print('results:', result)
        return result

    
    def fetch_all_blogs(self):
        blogs = []
        props = self.collection.find({})
        for document in props:
            document['id'] = str(document['_id'])
            blogs.append(BlogPost(**document))
            print(document)
        return blogs


    #    def get(self, username:str) -> AccountPasswordDB:
    #     props = self.collection.find_one({"username": username})
    #     if not props:
    #         return None
    #     props["id"] = str(props["_id"])
    #     return AccountPasswordDB(**props)

    # def create(self, info:AccountIn, hashed_password:str) -> AccountPasswordDB:
    #     props = info.dict()
    #     props["password"] = hashed_password
    #     # props["roles"] = roles
    #     try:
    #         self.collection.insert_one(props)
    #     except DuplicateKeyError:
    #         raise DuplicateAccountError()
    #     props["id"] = str(props["_id"])
    #     return AccountPasswordDB(**props)