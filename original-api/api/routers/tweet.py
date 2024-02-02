from fastapi import APIRouter
from typing import List

import api.schemas.tweet as tweet_schema


router = APIRouter()


@router.get("/tweets", response_model=List[tweet_schema.Tweet])
async def list_tweets():
    return [tweet_schema.Tweet(id=1, body="今、何してる？")]


@router.post("/tweets", response_model=tweet_schema.TweetCreateResponse)
async def create_tweet(tweet_body: tweet_schema.TweetCreate):
    return tweet_schema.TweetCreateResponse(id=1, body=tweet_body.body)


@router.put("/tweets/{tweet_id}")
async def update_tweet(tweet_id: int):
    pass


@router.delete("/tweets/{tweet_id}")
async def delete_tweet(tweet_id: int):
    pass
