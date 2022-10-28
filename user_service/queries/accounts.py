from pydantic import BaseModel, EmailStr
from queries.mongoclient import Queries
from pymongo.errors import DuplicateKeyError
from model import PydanticObjectId
class DuplicateAccountError(ValueError):
    pass

class AccountStatus(BaseModel):
    successcreated: bool

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

class AccountPasswordDB(AccountIn):
    id: PydanticObjectId
    # hashed_password: str

# this queries should be DB
class AccountQueries(Queries):
    DB_NAME = "user"
    COLLECTION = "accounts"

    def get(self, username:str) -> AccountPasswordDB:
        props = self.collection.find_one({"username": username})
        if not props:
            return None
        props["id"] = str(props["_id"])
        return AccountPasswordDB(**props)

    def create(self, info:AccountIn, hashed_password:str) -> AccountPasswordDB:
        props = info.dict()
        props["password"] = hashed_password
        
        try:
            self.collection.insert_one(props)
        except DuplicateKeyError:
            raise DuplicateAccountError()
        props["id"] = str(props["_id"])
        return AccountPasswordDB(**props)

    def fetch_all_accounts(self):
        accounts = []
        props = self.collection.find({})
        for document in props:
            document['id'] = str(document['_id'])
            accounts.append(AccountOut(**document))
            print(document)
        return accounts
