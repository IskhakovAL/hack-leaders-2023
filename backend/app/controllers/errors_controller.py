from fastapi import HTTPException, status

wrong_credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials"
)

wrong_token_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Wrong token'
)

user_not_found_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='User not found'
)

wrong_password_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Wrong password'
)

passwords_match_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Passwords do not match'
)

user_not_create_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Could not create user'
)

user_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='User with this email already exists'
)

permission_denied = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail='Operation not permitted'
)

metro_not_create_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='Could not create metro'
)

metro_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='This metro is already exists'
)

industry_not_create_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='Could not create industry'
)

industry_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='This industry is already exists'
)

equipment_not_create_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='Could not create equipment'
)

equipment_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='This equipment is already exists'
)

accessibility_not_create_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='Could not accessibility industry'
)

accessibility_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='This accessibility is already exists'
)

facility_not_create_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='Could not create facility'
)

facility_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='This facility is already exists'
)

platform_not_create_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='Could not create platform'
)


