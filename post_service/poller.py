import json
import time
# import requests
import sys
import requests



def get_user():
    url = "http://localhost:8000/users"
    print("the poller is running")
    responce = requests.get(url)
    content = json.loads(responce.content)
    for user in content["User"]:
        print(user)
        
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


if __name__ == "__main__":
    poll()