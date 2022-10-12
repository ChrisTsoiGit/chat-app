from fastapi import APIRouter
from models.user import User
from config.database import connection
from schemas.user import userEntity, listOfUserEntity
from bson import ObjectId

user_router = APIRouter()

@user_router.get('/hello')
async def hello_world():
    return "Hello, world!"

# create a user:
@user_router.post('/users')
async def create_user(user: User):
    connection.local.user.insert_one(dict(user))
    return listOfUserEntity(connection.local.user.find()) # return all users

# get all users:
@user_router.get('/users')
async def find_all_users():
    return listOfUserEntity(connection.local.user.find())

#  get a user by id:
@user_router.get('/users/{userId}')
async def find_user_by_id(userId):
    return userEntity(connection.local.user.find_one({"_id": ObjectId(userId)}))

# update a user:
@user_router.put('/users/{userId}')
async def update_user(userId, user: User):
    # find and update:
    connection.local.user.find_one_and_update(
        {"_id": ObjectId(userId)},
        {"$set": dict(user)}
    )
    # return the updated:
    return userEntity(connection.local.user.find_one({"_id": ObjectId(userId)}))

# delete a user:
@user_router.delete('/users/{userId}')
async def delete_user(userId):
    return userEntity(connection.local.user.find_one_and_delete({"_id": ObjectId(userId)}))
