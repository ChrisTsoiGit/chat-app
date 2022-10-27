from fastapi.testclient import TestClient
from main import app
from queries.accounts import AccountIn

client = TestClient(app)

fakeAcc = {
    'username': "username",
    'email': "user@email.com",
    'password': "password",
    "full_name": "string",
}

fakeAccStatus = {
    'successcreated': True
}


def test_create_account():
    class fakeAccQuery:
        def create(self, item, item2):
            
             pass
    app.dependency_overrides[AccountIn] = fakeAccQuery 
    response = client.post("/api/accounts", json=fakeAcc)
    assert response.status_code == 200
    assert response.json() == fakeAccStatus
