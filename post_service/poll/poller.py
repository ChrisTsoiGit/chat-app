import json
import time
import requests
import sys
from fastapi import FastAPI

# sys.path.appenf('')
# os.environ.setdefault(#??? what goses here and do i need to build an enviournment to pull in fast api)


from post_service.model import UserVO

app = FastAPI()

@app.post("/createuser", response_model = UserVO)
async def create_user(user: UserVO):
    return user

def get_user():
    url = "http://localhost:8000/users"
    responce = requests.get(url)
    content = json.loads(responce.content)
    for user in content["User"]:
        create_user(user)
        
        # UserVO.objects.update_or_create(
        #     # username: str
        #     # full_name: str | None = None
        #     # profile_picture: Optional[str]
        # )


def poll():
    while True:
        print("loading poll....")
        try:
            get_user()
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(60)

            