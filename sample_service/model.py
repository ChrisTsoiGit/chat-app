from unittest.util import strclass
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from datetime import date
from typing import Optional

class User(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    profile_img: Optional[EmailStr]

class UserIn(User):
    password: str

class UserOut(User):
    pass

class UserInDB(User):
    _id: int
    date_created: date





# **user_in.dict() - pedantic method that will convert your object into a dictionary
# ** means passing in the dict into matching those model attricute.