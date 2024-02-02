from sqlalchemy.ext.asyncio import AsyncSession

import api.models.tweet as tweet_model
import api.schemas.tweet as tweet_schema


async def create_tweet(
    db: AsyncSession, tweet_create: tweet_schema.TweetCreate
) -> tweet_model.Tweet:
    tweet = tweet_model.Tweet(**tweet_create.dict())
    db.add(tweet)
    await db.commit()
    await db.refresh(tweet)
    return tweet
