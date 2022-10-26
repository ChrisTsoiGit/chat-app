from queries.accounts import AccountOut
from main import app
from fastapi.testclient import TestClient
from routers.auth import auth

client = TestClient(app)

fakeAccOut = AccountOut(
    id="1",
    email="email@email.com",
    username="username",
    full_name="full name",
)

fakeAccToken_none = None


async def account_out_override():
    return fakeAccOut

app.dependency_overrides[auth.try_get_current_account_data] = account_out_override

def test_get_account():
    response = client.get("/api/token", cookies={"test_token": ""})  
    assert response.status_code == 200
    assert response.json() == fakeAccToken_none 
