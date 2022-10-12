from pydantic import BaseModel

class User(BaseModel):
    user_name: str
    user_email: str
    user_pw: str
    user_avatar_url: str
