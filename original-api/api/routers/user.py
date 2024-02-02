from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.user as user_crud
from api.db import get_db
import api.schemas.user as user_schema


router = APIRouter()


@router.post("/user/sign_up", response_model=user_schema.UserCreateResponse)
async def sign_up_user(user_create: user_schema.UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_crud.sigin_up_user(db, user_create)


@router.post("/user/sign_in", response_model=user_schema.UserCreateResponse)
async def sign_in_user():
    return user_schema.UserCreateResponse(email="hoge", password="fuga", name="yuki", id=1)


@router.get("/user/{user_id}", response_model=user_schema.User)
async def get_user(id: int, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get_user(db, id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user