from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class UserVO(BaseModel):
    username: str
    full_name: str | None = None
    profile_picture: Optional[str]

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


