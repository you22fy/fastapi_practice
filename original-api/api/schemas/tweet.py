from typing import Optional

from pydantic import BaseModel, Field


class TweetBase(BaseModel):
    body: Optional[str] = Field(None, example="今、何してる？")

class TweetCreate(TweetBase):
    pass

class TweetCreateResponse(TweetBase):
    id: int
    class Config:
        orm_mode = True

class Tweet(TweetBase):
    id: int

    class Config:
        orm_mode = True