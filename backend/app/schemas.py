from pydantic import BaseModel

# from pydantic.fields import ModelField
# from pydantic.typing import is_union, get_args, get_origin

from datetime import datetime

from typing import Optional


class TokenData(BaseModel):
    user_id: int
    email: str
    role: str


class Token(BaseModel):
    access_token: str
    token_type: str


class BaseDB(BaseModel):
    id: int
    created_at: datetime
    deleted: bool

    class Config:
        orm_mode = True


class Users(BaseDB):
    email: str
    password: str

