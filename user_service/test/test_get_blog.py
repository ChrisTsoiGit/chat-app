from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/me")
async def get_blog():
    return {"msg": "This is my blog."}

def test_get_blog():
    client = TestClient(app)
    print(client.post("/post_test"))
    response = client.get("/me")
    assert response.status_code == 200
    assert response.json() == {"msg": "This is my blog."}
