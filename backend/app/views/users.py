from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, Form

from sqlalchemy.orm import Session

from app.dependecies import get_db

from app.schemas import Token, TokenData, FullUser

from app.controllers.security_controller import authenticate_user, create_access_token, get_current_user,\
    register_user, get_role, get_user_info


users = APIRouter(
    prefix='/api/users',
    tags=['users']
)


@users.get('/me', response_model=FullUser)
def api_me(db: Annotated[Session, Depends(get_db)],
           current_user: Annotated[TokenData, Depends(get_current_user)]):
    return get_user_info(db, current_user.user_id)


@users.post('/login', response_model=Token)
def api_login(db: Annotated[Session, Depends(get_db)], email: Annotated[str, Form()], password: Annotated[str, Form()]):
    try:
        user = authenticate_user(db, email, password)
        role, juridical = get_role(user)
        access_token = create_access_token(
            data={'user_id': user.id, 'email': user.email, 'role': role, 'juridical': juridical}
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException as e:
        raise e


@users.post('/register', response_model=Token)
def api_register(db: Annotated[Session, Depends(get_db)],
                 email: Annotated[str, Form()], password: Annotated[str, Form()],
                 juridical: Annotated[bool, Form()], landlord: Annotated[bool, Form()],
                 repeat_password: Annotated[str, Form()],
                 first_name: Annotated[str, Form()],
                 second_name: Annotated[str, Form()],
                 phone: Annotated[str, Form()],
                 surname: Annotated[Optional[str], Form()] = None,
                 position: Annotated[Optional[str], Form()] = None,
                 title: Annotated[Optional[str], Form()] = None,
                 inn: Annotated[Optional[int], Form()] = None):
    try:
        user = register_user(
            db,
            email,
            password,
            repeat_password,
            landlord, juridical,
            first_name,
            second_name,
            surname,
            phone,
            position,
            title,
            inn
        )
        role, juridical = get_role(user)
        access_token = create_access_token(
            data={'user_id': user.id, 'email': user.email, 'role': role, 'juridical': juridical}
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException as e:
        print(e)
        raise e
