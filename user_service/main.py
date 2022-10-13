import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter
from routers import users, websocket, authenticator
from routers.authenticator import authenticator
# from fastapi.security import OAuth2PasswordBearer

# create app:
app = FastAPI()

# register router:
app.include_router(users.router)
app.include_router(websocket.router)
app.include_router(authenticator.router)
# app.include_router(user_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get("CORS_HOST", "http://localhost:3000")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# @app.get("/items/")
# async def read_items(token: str = Depends(oauth2_scheme)):
#     return {"token": token}
