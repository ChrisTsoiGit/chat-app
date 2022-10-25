import json
import time
# import requests
import sys
import requests
from queries.blogs import BlogQueries



def get_user():
    queries = BlogQueries()
    url = "http://user:8000/accounts"
    print("the poller is running")
    responce = requests.get(url)
    if responce.status_code == 200:
        # print("responce :", responce)
        content = json.loads(responce.content)
        # print("content :", content)
        for user in content:
            # print(user)
            queries.create_a_uservo(user)
        
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


