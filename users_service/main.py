from fastapi import FastAPI

# create fastAPI application:
users_api = FastAPI()

@users_api.get("/")
async def hello():
    return {"msg": "Hello!"}
