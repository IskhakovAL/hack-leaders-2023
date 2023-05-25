from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Form

from sqlalchemy.orm import Session

from app.dependecies import get_db

from app.schemas import Token, TokenData

from app.controllers.security_controller import authenticate_user, create_access_token, get_current_user,\
    register_user_tenant_juridical, get_role


users = APIRouter(
    prefix='/api/users',
    tags=['users']
)


@users.get('/me', response_model=TokenData)
def api_me(current_user: Annotated[TokenData, Depends(get_current_user)]):
    return current_user


@users.post('/login', response_model=Token)
def api_login(db: Annotated[Session, Depends(get_db)], email: Annotated[str, Form()], password: Annotated[str, Form()]):
    try:
        user = authenticate_user(db, email, password)
        access_token = create_access_token(
            data={'user_id': user.id, 'email': user.email}
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException as e:
        raise e


@users.post('/register/tenant/juridical', response_model=Token)
def api_register(db: Annotated[Session, Depends(get_db)],
                 email: Annotated[str, Form()], password: Annotated[str, Form()],
                 repeat_password: Annotated[str, Form()]):
    try:
        user = register_user_tenant_juridical(db, email, password, repeat_password)
        access_token = create_access_token(
            data={'user_id': user.id, 'email': user.email, 'role': get_role(user)}
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException as e:
        raise e
