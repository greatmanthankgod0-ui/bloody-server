from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserRegister, UserLogin
from app.services.user_service import create_user
from app.services.auth_service import login

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    return create_user(db, user)

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
