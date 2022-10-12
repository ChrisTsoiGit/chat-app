from urllib import response
from fastapi import APIRouter
from model import User, UserIn
from queries import mongoclient


router = APIRouter()

# homepage
@router.get("/")
def index():
    return {"message": "Welcome To FastAPI World"}


# get all users
@router.get("/users", response_model = User)
def get_user(user:User):
    return user

# get a user
@router.get("/users/{id}", response_model = User)
def get_user(user:User):
    return user

# post user
@router.post("/createuser", response_model = User)
async def create_user(user: UserIn):
    return user




