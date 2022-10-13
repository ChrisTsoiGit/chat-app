from pydantic import BaseModel, EmailStr
from queries.mongoclient import Queries

class DuplicatedAccountError(ValueError):
    pass

class AccountIn(BaseModel):
    username : str
    email: EmailStr
    password: str
    full_name: str

class AccountOut(BaseModel):
    id: str
    username : str
    email: EmailStr
    full_name: str

class AccountPasswordDB(AccountOut):
    hashed_password: str

# this queries should be DB
class AccountQueries(Queries):
    def get(self, email:str) -> AccountPasswordDB:
        pass
    def create(self, info:AccountIn, hashed_password:str) -> AccountPasswordDB:
        pass