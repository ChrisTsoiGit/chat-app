from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi import FastAPI
from routes.user import user_router

# create app:
app = FastAPI()

# register router:
app.include_router(user_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get("CORS_HOST", "http://localhost:3000")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
