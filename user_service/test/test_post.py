from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

local_data = None
app = FastAPI()

class Blog(BaseModel):
    content: str

@app.post("/blog/")
async def create_blog(blog: Blog):
    return blog

fake_blog = {'content':'It is a fake blog'}

def test_get_blog():
    client = TestClient(app)
    response = client.post("/blog/", json=fake_blog)
    assert response.status_code == 200
    assert response.json() == fake_blog
