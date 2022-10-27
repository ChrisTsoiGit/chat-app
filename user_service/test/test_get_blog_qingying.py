from fastapi import FastAPI
from fastapi.testclient import TestClient


app = FastAPI()
# we supposed to have a blog page in the stretch goal
@app.get("/me")
async def get_blog():
    return {"msg": "This is my blog."}


def test_get_blog():
    client = TestClient(app)
    response = client.get("/me")
    assert response.status_code == 200
    assert response.json() == {"msg": "This is my blog."}
