from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.tweet as tweet_crud
from api.db import get_db
import api.schemas.user as user_schema


router = APIRouter()


@router.post("/user/sign_up", response_model=user_schema.UserCreateResponse)
async def sign_up_user():
    return user_schema.UserCreateResponse(email="hoge", password="fuga", name="yuki", id=1)


@router.post("/user/sign_in", response_model=user_schema.UserCreateResponse)
async def sign_in_user():
    return user_schema.UserCreateResponse(email="hoge", password="fuga", name="yuki", id=1)


@router.get("/user/{user_id}", response_model=user_schema.User)
async def get_user():
    return user_schema.UserCreateResponse(email="hoge", password="fuga", name="yuki", id=1)
