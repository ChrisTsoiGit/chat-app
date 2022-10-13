from unittest.util import strclass
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
