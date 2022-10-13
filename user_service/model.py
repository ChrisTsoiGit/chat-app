from pydantic import BaseModel, Field, HttpUrl, EmailStr
from datetime import date
from typing import Optional

class User(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    profile_picture: Optional[str]

class UserIn(User):
    password: str

class UserOut(User):
    pass

class UserInDB(User):
    _id: int
    date_created: date
# **user_in.dict() - pedantic method that will convert your object into a dictionary
# ** means passing in the dict into matching those model attricute.

# accounts for login
class DuplicatedAccountError(ValueError):
    pass

class AccountIn(BaseModel):
    email: EmailStr
    password: str
    full_name: str

class AccountOut(BaseModel):
    id: str
    email: EmailStr
    full_name: str

