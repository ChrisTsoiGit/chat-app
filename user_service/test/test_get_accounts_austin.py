from fastapi.testclient import TestClient
from queries.accounts import AccountQueries
from main import app


client = TestClient(app)


def test_create_blog():
    class fakegetallaccsQuery:
        def fetch_all_accounts(self):
            pass

    app.dependency_overrides[AccountQueries] = fakegetallaccsQuery
    response = client.get("/accounts")
    assert response.status_code == 200
    app.dependency_overrides = {}
