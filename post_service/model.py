from fastapi import FastAPI, Path
from pydantic import BaseModel, Field, HttpUrl, EmailStr
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