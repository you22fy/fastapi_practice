from fastapi import FastAPI

from api.routers import tweet

app = FastAPI()
app.include_router(tweet.router)
