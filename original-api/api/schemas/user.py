from typing import Optional

from pydantic import BaseModel, Field

# Userで全部共通なやつ
class UserBase(BaseModel):
    email: str = Field(None, example="hoeg@email.co.jp")
    password: str = Field(None, example="p@ssw0rd")
    name: str = Field(None, example="Taro")

# 作成時だけ渡すやつ。今回はUserBaseと同じなのでpass
class UserCreate(UserBase):
    pass

# 作成時のレスポンス。idを返す。
class UserCreateResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

# 取得時のレスポンス
class User(UserBase):
    id: int

    class Config:
        orm_mode = True
