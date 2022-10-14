from pydantic import BaseModel, Field, HttpUrl, EmailStr
from datetime import date
from typing import Optional, List
from bson.objectid import ObjectId

# class User(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None
#     profile_picture: Optional[str]

# class UserIn(User):
#     password: str

# class UserOut(User):
#     pass

# class UserInDB(User):
#     _id: int
#     date_created: date
# **user_in.dict() - pedantic method that will convert your object into a dictionary
# ** means passing in the dict into matching those model attricute.

class PydanticObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value: ObjectId | str) -> ObjectId:
        if value:
            try:
                ObjectId(value)
            except:
                raise ValueError(f"Not a valid object id: {value}")
        return value
