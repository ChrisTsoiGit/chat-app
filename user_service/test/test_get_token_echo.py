from queries.accounts import AccountOut
from main import app
from fastapi.testclient import TestClient
from routers.auth import auth
from routers.accounts import AccountToken

client = TestClient(app)

fakeAccOut = AccountOut(
    id="1",
    email="email@email.com",
    username="username",
    full_name="full name",
)

fakeAccToken = AccountToken(
    access_token="abcd123orsomethinglikethat",
    token_type="Bearer",
    account=fakeAccOut,
)


async def account_out_override():
    return fakeAccOut


app.dependency_overrides[
    auth.try_get_current_account_data
] = account_out_override


def test_get_account():
    response = client.get(
        "/api/token", cookies={"fastapi_token": "abcd123orsomethinglikethat"}
    )
    assert response.status_code == 200
    print(response.json())
    assert response.json() == fakeAccToken

