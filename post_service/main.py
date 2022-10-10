from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class BlogPost(BaseModel):
    pic: str
    location: str
    time: str
    likes: int

class BlogComment(BaseModel):
    blog: BlogPost
    user: int
    comment: str
    time: int

# class subcomment(BaseModel):
#     comentorigin: BlogComment


post = {
    1: {
        'pic': 'str',
        'location': 'str',
        'time': 'str',
        'likes': 'int'
    
    }
}



@app.post('/create-post')
def create_blogpost(item: BlogPost):
    return {}

    @app.post('/create-post')
def create_blogpost(item: BlogPost):
    return {}



