from fastapi.testclient import TestClient
from queries.accounts import AccountQueries
from main import app


client = TestClient(app)

fakeblog = {
    "id": "string",
    "username": "username",
    "email": "user@email.com",
    "full_name": "string",
}


def test_create_blog():
    class fakegetallaccsQuery:
        def create(self, item):
            pass

    app.dependency_overrides[AccountQueries] = fakegetallaccsQuery

    response = client.post("/accounts", json=fakeblog)

    assert response.status_code == 200
