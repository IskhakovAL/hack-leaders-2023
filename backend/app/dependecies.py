from typing import Annotated

from fastapi import Depends

from app.models import SessionLocal

from app.schemas import TokenData

from app.controllers.security_controller import get_current_user


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# class RoleChecker:
#     def __init__(self, allowed_roles: list):
#         self.allowed_roles = allowed_roles
#
#     def __call__(self, user: Annotated[TokenData, get_current_user]:
#         if user.role not in self.allowed_roles:
#             raise HTTPException(status_code=403, detail="Operation not permitted")
