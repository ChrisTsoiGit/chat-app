from fastapi import (
    Depends,
    HTTPException,
    status,
    APIRouter,
    Request,
    Response,
)

from jwtdown_fastapi.authentication import Token
from routers.authenticator import auth
from pydantic import BaseModel
from typing import Optional

from queries.accounts import (
    DuplicateAccountError,
    AccountIn,
    AccountOut,
    AccountQueries,
)


class AccountForm(BaseModel):
    username: str
    password: str

class AccountToken(Token):
    account: AccountOut

class AccountStatus(BaseModel):
    status: bool

class HttpError(BaseModel):
    detail: str


router = APIRouter()

@router.get("/")
def greet():
    return {"msg": "Hello, welcome to FAstAPI world!"}

# @router.get("/api/protected", response_model=bool)
# async def get_protected(
#     account_data: Optional[dict] = Depends(auth.try_get_current_account_data),
# ):
#     return True

# @router.post("/api/accounts", response_model=AccountToken | HttpError)
@router.post("/api/accounts", response_model=AccountStatus | HttpError)
async def create_account(
    info: AccountIn,
    request: Request,
    response: Response,
    accounts: AccountQueries = Depends(),
):
    # jwtdown_fastapi > authentication.py > class Authenticator > def hash_password():
    hashed_password = auth.hash_password(info.password)
    try:
        account = accounts.create(info, hashed_password)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    form = AccountForm(username=info.username, password=info.password)
    # # jwtdown_fastapi > authenntication.py > class Authenticator > def login():
    # token = await auth.login(response, request, form, accounts)
    # return AccountOut(account=account, **token.dict())
    return  AccountStatus(status=True)

@router.get("/token", response_model=AccountToken | None)
async def get_token(
    request: Request,
    account: AccountOut = Depends(auth.try_get_current_account_data)
) -> AccountToken | None:
    if auth.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[auth.cookie_name],
            "type": "Bearer",
            "account": account,
        }
