from pydantic import BaseModel

# from pydantic.fields import ModelField
# from pydantic.typing import is_union, get_args, get_origin

from datetime import datetime

from typing import Optional


class TokenData(BaseModel):
    user_id: int
    email: str
    role: str
    juridical: bool


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


class Roles(BaseDB):
    title: str
    juridical: bool


class UsersInfo(BaseDB):
    first_name: str
    second_name: str
    surname: Optional[str] = None
    phone: str
    email: str


class JuridicalInfo(BaseDB):
    position: str
    title: str
    inn: str


class FullUser(BaseModel):
    user_id: int
    role: Roles
    info: UsersInfo
    juridical: Optional[JuridicalInfo] = None


class Metro(BaseDB):
    title: str
    color: str
    branch: str


class Industry(BaseDB):
    title: str


class Equipments(BaseDB):
    title: str
    price: int


class Accessibilities(BaseDB):
    title: str


class Facilities(BaseDB):
    title: str
    price: int


class Platform(BaseModel):
    platform_id: int
    title: str
    description: str
    capacity: int
    area: int
    phone: str
    address: str
    metro: list[Metro]
    industry: list[Industry]
    equipments: list[Equipments]
    accessibilitie: list[Accessibilities]
    facilities: list[Facilities]
