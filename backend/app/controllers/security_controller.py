from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy import select

from fastapi.security import OAuth2PasswordBearer

from fastapi import Depends

from typing import Annotated, Optional

from app.models import Users, UsersRoles, UsersInfo, TenantUsers, LandlordUsers, JuridicalUsers

from app.schemas import Users as UsersSchema
from app.schemas import TokenData

from passlib.context import CryptContext
from jose import jwt, JWTError

from datetime import timedelta, datetime

from app.config import SECRET_KEY, ALGORITHM

from app.controllers.errors_controller import wrong_credentials_exception, wrong_token_exception, \
    user_not_found_exception, wrong_password_exception, passwords_match_exception, \
    user_not_create_exception, user_exists_exception

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def get_user(db: Session, email: str):
    if user := db.scalars(select(Users).where(Users.email == email)).first():
        return UsersSchema(**user.__dict__)


def get_role(user: Users):
    return user.users_roles[0].role.title, user.users_roles[0].role.juridical


def authenticate_user(db: Session, email: str, password: str):
    user = db.scalars(select(Users).where(Users.email == email)).first()
    if not user:
        raise user_not_found_exception
    if not verify_password(password, user.password):
        raise wrong_password_exception
    return user


def register_user(db: Session, email: str, password: str, repeat_password: str,
                  landlord: bool, juridical: bool, first_name: str, second_name: str,
                  surname: str, phone: str, position: str, title: str, inn: int):
    user = get_user(db, email)
    if not user:
        if password != repeat_password:
            raise passwords_match_exception
        try:
            new_user = Users(
                email=email,
                password=get_password_hash(password)
            )
            db.add(new_user)
            db.commit()
            user_info = UsersInfo(
                user_id=new_user.id,
                first_name=first_name,
                second_name=second_name,
                surname=surname,
                phone=phone
            )
            db.add(user_info)
            db.commit()
            # ЕСЛИ ПОЛЬЗОВАТЕЛЬ - АРЕНДОДАТЕЛЬ
            if landlord:
                db.add_all([UsersRoles(
                    user_id=new_user.id,
                    role_id=1
                ), LandlordUsers(
                    user_id=new_user.id
                ), JuridicalUsers(
                    user_id=new_user.id,
                    position=position,
                    title=title,
                    inn=inn
                )])
            # ЕСЛИ ПОЛЬЗОВАТЕЛЬ - АРЕНДАТОР ЮРЛИЦО
            elif juridical:
                db.add_all([UsersRoles(
                    user_id=new_user.id,
                    role_id=2
                ), TenantUsers(
                    user_id=new_user.id
                )])
            # ЕСЛИ ПОЛЬЗОВАТЕЛЬ - АРЕНДАТОР ФИЗЛИЦО
            else:
                db.add_all([UsersRoles(
                    user_id=new_user.id,
                    role_id=3
                ), TenantUsers(
                    user_id=new_user.id
                )])
            db.commit()
            return new_user
        except SQLAlchemyError as e:
            print(e)

            db.rollback()
            raise user_not_create_exception
    raise user_exists_exception


def create_access_token(data: dict):
    to_encode = data.copy()
    # Поменять при необходимости на нужный период времени
    expire = datetime.utcnow() + timedelta(days=365)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get('user_id')
        email = payload.get('email')
        role = payload.get('role')
        juridical = payload.get('juridical')
        if not email or not user_id:
            raise wrong_credentials_exception
        token_data = TokenData(user_id=user_id, email=email, role=role, juridical=juridical)
        return token_data
    except JWTError:
        raise wrong_token_exception


def get_user_info(db: Session, user_id: int):
    user = db.scalars(select(Users).where(Users.id == user_id)).first()
    return {
        'user_id': user_id,
        'role': user.users_roles[0].role,
        'info': {**user.users_info[0].__dict__, 'email': user.email},
        'juridical': user.juridical_users[0] if user.juridical_users else None
    }
