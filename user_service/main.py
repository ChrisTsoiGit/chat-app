import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import accounts, authenticator, websocket

# create app:
app = FastAPI()
# register router:
app.include_router(accounts.router)
app.include_router(authenticator.auth.router)
app.include_router(websocket.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get("CORS_HOST", "http://localhost:3000")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
