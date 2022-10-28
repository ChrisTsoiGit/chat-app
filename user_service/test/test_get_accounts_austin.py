from fastapi import FastAPI
from fastapi.testclient import TestClient
from queries.accounts import AccountOut
from main import app



client = TestClient(app)

fakeblog = {
    'id': "string",
    'username': "username",
    'email': "user@email.com",
    "full_name": "string"
}



def test_create_blog():
    class fakegetallaccsQuery:
        def create(self, item):
            pass

    app.dependency_overrides[AccountOut] = fakegetallaccsQuery 

    response = client.post("/accounts", json=fakeblog)

    assert response.status_code == 200
