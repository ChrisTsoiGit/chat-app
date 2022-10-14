from pydantic import BaseModel
from queries.mongoclient import Queries
from pymongo.errors import DuplicateKeyError

class DuplicateAccountError(ValueError):
    pass

class AccountIn(BaseModel):
    email: str
    full_name: str
    username : str
    password: str

class AccountOut(BaseModel):
    id: str
    email: str
    full_name: str
    username : str

class AccountOutWithPw(AccountIn):
    hashed_password: str

# this queries should be DB:
class AccountQueries(Queries):
    DB_NAME = "user"
    COLLECTION = "accounts"

    def get(self, username: str) -> AccountOutWithPw:
        props = self.collection.find_one({"username": username})
        if not props:
            return None
        props["id"] = str(props["_id"])
        return AccountOutWithPw(**props)

    def create(self, info:AccountIn, hashed_password:str) -> AccountOutWithPw:
        props = info.dict()
        props["password"] = hashed_password
        try:
            self.collection.insert_one(props)
        except DuplicateKeyError:
            raise DuplicateAccountError()
        props["id"] = str(props["_id"])  # ObjectId -> str
        return AccountOutWithPw(**props)
