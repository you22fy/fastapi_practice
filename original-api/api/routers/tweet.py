from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.tweet as tweet_crud
from api.db import get_db
import api.schemas.tweet as tweet_schema


router = APIRouter()


@router.get("/tweets", response_model=List[tweet_schema.Tweet])
async def list_tweets():
    return [tweet_schema.Tweet(id=1, body="今、何してる？")]


@router.post("/tweets", response_model=tweet_schema.TweetCreateResponse)
async def create_tweet(tweet_body: tweet_schema.TweetCreate, db: AsyncSession = Depends(get_db)):
    return await tweet_crud.create_tweet(db, tweet_body)


@router.put("/tweets/{tweet_id}")
async def update_tweet(tweet_id: int):
    pass


@router.delete("/tweets/{tweet_id}")
async def delete_tweet(tweet_id: int):
    pass
