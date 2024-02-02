from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Tuple, Optional

import api.models.tweet as tweet_model
import api.schemas.tweet as tweet_schema
from sqlalchemy import select
from sqlalchemy.engine import Result


async def list_tweets(
    db: AsyncSession
) -> List[Tuple[int, str]]:
    ret: Result = await (
        db.execute(
            select(
                tweet_model.Tweet.id,
                tweet_model.Tweet.body
            )
        )
    )
    return ret.all()


async def get_tweet(
    db: AsyncSession, tweet_id: int
) -> Optional[tweet_model.Tweet]:

    result: Result = await (
        db.execute(
            select(tweet_model.Tweet).filter(tweet_model.Tweet.id == tweet_id)
        )
    )
    tweet: Optional[tweet_model.Tweet] = result.first()
    return tweet[0] if tweet is not None else None


async def create_tweet(
    db: AsyncSession, tweet_create: tweet_schema.TweetCreate
) -> tweet_model.Tweet:
    tweet = tweet_model.Tweet(**tweet_create.dict())
    db.add(tweet)
    await db.commit()
    await db.refresh(tweet)
    return tweet


async def update_tweet(
    db: AsyncSession, tweet_id: int, tweet_update: tweet_schema.TweetCreate
) -> tweet_model.Tweet:
    tweet = await db.get(tweet_model.Tweet, tweet_id)
    tweet.body = tweet_update.body
    await db.commit()
    await db.refresh(tweet)
    return tweet


async def delete_tweet(
    db: AsyncSession, tweet: tweet_model.Tweet
) -> None:
    await db.delete(tweet)
    await db.commit()
