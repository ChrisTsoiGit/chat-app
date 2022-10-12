from fastapi import FastAPI
from routes.user import user_router

# create app:
app = FastAPI()

# register router:
app.include_router(user_router)
