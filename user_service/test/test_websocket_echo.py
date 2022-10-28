from fastapi.testclient import TestClient
from main import app
from routers.websocket import get_jwt
from routers.accounts import AccountToken
from queries.accounts import AccountOut

token = "access_token"

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


class FakeJwt:
    def decode(token, signing_key, algorithms):
        return fakeAccToken.dict()


async def fake_jwt():
    return FakeJwt


def test_websocket():
    app.dependency_overrides[get_jwt] = fake_jwt
    client = TestClient(app)
    with client.websocket_connect("/chat" + "?token=" + token) as websocket:
        data = websocket.receive_json()
        assert data["content"] == "Welcome!"
        assert data["username"] == "username"
