from fastapi import Depends, HTTPException

from app.core.security import get_current_user
from app.database.models import User


def require_roles(*roles: str):
    def checker(
        current_user: User = Depends(get_current_user),
    ):
        if current_user.role not in roles:
            raise HTTPException(
                status_code=403,
                detail="Permission denied",
            )
        return current_user

    return checker
