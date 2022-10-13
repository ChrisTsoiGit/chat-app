from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class BlogPost(BaseModel):
    user: int
    pic: str
    location: str
    time: str
    likes: int
    user: int
    desc: str

class BlogComment(BaseModel):
    blog: BlogPost
    user: int
    comment: str
    time: int


