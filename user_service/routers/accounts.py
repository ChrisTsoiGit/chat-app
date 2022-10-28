# router.py
from fastapi import (
    Depends,
    HTTPException,
    status,
    APIRouter,
    Request,
)
from queries.accounts import (
    AccountIn,
    AccountOut,
    DuplicateAccountError,
    AccountStatus,
)
from queries.accounts import AccountQueries
from jwtdown_fastapi.authentication import Token
from routers.auth import auth
from pydantic import BaseModel


class AccountForm(BaseModel):
    username: str
    password: str


class AccountToken(Token):
    account: AccountOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()


# protected/ you have to be logged in for this
# @router.get("/api/protected", response_model=bool)
# async def get_protected(
#     # ex: vacation: VacationsQueries = Depends(),
#     account_data: dict = Depends(auth.get_current_account_data),
# ):
#     return True
# return vacations.get_account_vacations(account_data)


# get token/ to be protected by something
# if the try_get_current_account_data existed, it will return the account
@router.get("/api/token", response_model=AccountToken | None)
async def get_token(
    request: Request, account: AccountOut = Depends(auth.try_get_current_account_data)
) -> AccountToken | None:
    if auth.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[auth.cookie_name],
            "type": "Bearer",
            "account": account,
        }
    else:
        raise Exception("No cookie in request")


@router.post("/api/accounts", response_model=AccountStatus | HttpError)
async def create_account(
    info: AccountIn,  # this is what should be in the body
    accounts: AccountQueries = Depends(),
):
    hashed_password = auth.hash_password(info.password)
    try:
        accounts.create(info, hashed_password)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    AccountForm(username=info.username, password=info.password)
    # token = await auth.login(response, request, form, accounts)
    # return AccountToken(account=account, **token.dict())
    return AccountStatus(successcreated=True)
