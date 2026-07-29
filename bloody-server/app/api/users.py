from app.core.permissions import require_roles
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database.models import User
from app.database.session import get_db
from app.services.user_service import get_users, get_user

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/")
def list_users(
    page: int = 1,
    limit: int = 10,
    username: str | None = None,
    db: Session = Depends(get_db),
):
    return get_users(
        db,
        page,
        limit,
        username,
    )


# Static route MUST come before /{user_id}
@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role,
    }
@router.get("/admin")
def admin_test(
    current_user: User = Depends(require_roles("admin")),
):
    return {
        "message": "Welcome admin!"
    }

@router.get("/{user_id}")
def single_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    return get_user(db, user_id)
