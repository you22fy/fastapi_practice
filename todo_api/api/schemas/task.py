from typing import Optional

from pydantic import BaseModel, Field

# apiのスキーマであって、DBのスキーマではない

class TaskBase(BaseModel): #BaseModelはFastAPIのスキーマモデルであることを表す
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    done:bool = Field(False, description="完了フラグ") #descriptionはswaggerで表示される説明

    class Config:
        orm_mode = True

