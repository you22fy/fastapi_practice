from fastapi import FastAPI

from api.routers import tweet, user

app = FastAPI()
app.include_router(tweet.router)
app.include_router(user.router)
