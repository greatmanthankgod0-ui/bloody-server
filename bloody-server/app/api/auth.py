from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserRegister, UserLogin
from app.services.user_service import create_user
from app.services.auth_service import login
from app.core.tasks import log_registration

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(
    user: UserRegister,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    result = create_user(db, user)

    if "id" in result:
        background_tasks.add_task(
            log_registration,
            user.username,
        )

    return result


@router.post("/login")
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db),
):
    return login(
        db,
        user.email,
        user.password,
    )
