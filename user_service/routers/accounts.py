# router.py
from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from jwtdown_fastapi.authentication import Token
from routers.auth import auth

from pydantic import BaseModel

from queries.accounts import (
    AccountIn,
    AccountOut,
    AccountPasswordDB,
    DuplicateAccountError,
    AccountStatus,
)
from queries.accounts import AccountQueries

class AccountForm(BaseModel):
    username: str
    password: str

class AccountToken(Token):
    account: AccountOut

class HttpError(BaseModel):
    detail: str

router = APIRouter()


@router.post("/api/accounts", response_model=AccountStatus | HttpError)
async def create_account(
    info: AccountIn,  #this is what should be in the body
    request: Request,
    response: Response,
    accounts: AccountQueries = Depends(),
):
    hashed_password = auth.hash_password(info.password)
    try:
        account = accounts.create(info, hashed_password)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    form = AccountForm(username=info.username, password=info.password)
    # token = await auth.login(response, request, form, accounts)
    # return AccountToken(account=account, **token.dict())
    return AccountStatus(successcreated = True)

# @router.get("/api/accounts", response_model=AccountToken | HttpError)
# async def get_user():
#     return AccountOut