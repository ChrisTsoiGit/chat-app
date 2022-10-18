import json
import time
# import requests
import sys
import requests



def get_user():
    url = "http://user_service:8000/users"
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


# import requests
# from time import sleep
# from db import AutoVOQueries

# queries = AutoVOQueries() 

# def poll():
#     while True:
#         print("the poller is running" )
#         try:
#             url = "http://inventory:8000/api/inventory" 
#             response = requests.get(url) 
#             if response.status_code ==  200:
#                 print("data from inventory:" , response)
#                 autos = response.json() 
#                 for auto in autos:
#                     queries.create_autovo(auto) 

#         except Exception as ex:
#             print("Exception caught in poller" , ex)

#         sleep(30)

# if __name__ == "__main__":
#     poll()
