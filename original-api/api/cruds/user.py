from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

import api.models.user as user_model
import api.schemas.user as user_schema
from sqlalchemy import select
from sqlalchemy.engine import Result

from passlib.context import CryptContext

async def sigin_up_user(
    db: AsyncSession, user_create: user_schema.UserCreate
) -> user_model.User:
    user = user_model.User(**user_create.dict())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_user(
    db: AsyncSession, user_id: int
) -> Optional[user_model.User]:

    result: Result = await (
        db.execute(
            select(user_model.User).filter(user_model.User.id == user_id)
        )
    )
    user: Optional[user_model.User] = result.first()
    return user[0] if user is not None else None
