from fastapi import APIRouter, Depends, Response
from pydantic import BaseModel
from typing import Union, List
from queries.blogs import UserVO , BlogPost, BlogQueries
from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)


# from queries.tasks import (
#   DifficultyOut,
#   DifficultyRepository,
# )
# from queries.users import (
#   UserRepository
# )

router = APIRouter()

#get all users
@router.get("/Users")
def get_accounts(
    response: Response,
    users: BlogQueries = Depends()
):
    response = users.fetch_all_users()
    print(response)
    return response

#get all users
@router.get("/Blogs")
def get_blogs(
    response: Response,
    blogs: BlogQueries = Depends()
):
    response = blogs.fetch_all_blogs()
    print(response)
    return response

# Tasks: Create single task 
@router.post("/createblog", response_model=BlogPost)
def create_blog(
  blogpost: BlogPost,
  queries: BlogQueries = Depends()
):
  print('task', blogpost)
  # response.status_code = 400
  
  return queries.create_a_Blog(blogpost)



# # user: POST/create single user
# @router.post("/Create-Blog/", response_model=UserOut)
# def create_user(
#     user_in: UserIn,
#     queries: UserRepository = Depends()):
#     return queries.create_user(user_in)
#     # introduce error handling here

# # user: POST/create single user
# @router.post("/api/users/", response_model=UserOut)
# def create_user(
#     user_in: UserIn,
#     queries: UserRepository = Depends()):
#     return queries.create_user(user_in)
#     # introduce error handling here





# # user: PUT single user
# @router.put("/api/users/{user_id}", response_model=UserOut)
# def update_user(
#     user_id: int,
#     user_in: UserIn, # coming from body, w UserIn shape
#     response: Response,
#     queries: UserRepository = Depends(), # dependency injection
# ):
#     record = queries.update_user(user_id, user_in)
#     if record is None:
#         response.status_code = 404
#     else:
#         return record



# # # user: GET single user
# @router.get("/Users2", response_model=UserVO)
# def get_user(
#     response: Response,
#     queries: BlogQueries = Depends(),
# ):
#     record = queries.fetch_all_users()
#     if record is None:
#         response.status_code = 404
#     else:
#         return record