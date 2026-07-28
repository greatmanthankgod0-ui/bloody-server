from sqlalchemy.orm import Session
from fastapi import Depends

from app.database.session import get_db
from app.repositories.user_repository import UserRepository


def get_user_repository(
    db: Session = Depends(get_db),
):
    return UserRepository()
