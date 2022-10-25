# router.py
from urllib import response
from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from queries.accounts import (
    AccountIn,
    AccountOut,
    AccountPasswordDB,
    DuplicateAccountError,
    AccountStatus,
)
from queries.accounts import AccountQueries
from jwtdown_fastapi.authentication import Token
from routers.auth import auth
from pydantic import BaseModel
from queries.mongoclient import Queries


class AccountForm(BaseModel):
    username: str
    password: str

class AccountToken(Token):
    account: AccountOut

class HttpError(BaseModel):
    detail: str


router = APIRouter()


# protected/ you have to be logged in for this
@router.get("/api/protected", response_model=bool)
async def get_protected(
    #ex: vacation: VacationsQueries = Depends(),
    account_data: dict = Depends(auth.get_current_account_data),
):
    return True  
    # return vacations.get_account_vacations(account_data)


# get token/ to be protected by something
# if the try_get_current_account_data existed, it will return the account
@router.get("/api/token", response_model=AccountToken | None)
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



#get all users
@router.get("/accounts")
def get_accounts(
    request: Request,
    response: Response,
    accounts: AccountQueries = Depends()
):
    response = accounts.fetch_all_accounts()
    print(response)
    return response



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