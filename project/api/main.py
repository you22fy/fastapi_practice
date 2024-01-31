from fastapi import FastAPI

from api.routers import task, done
app = FastAPI() #fastAPIのインスタンス


app.include_router(task.router)
app.include_router(done.router)