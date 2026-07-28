from datetime import datetime, timedelta, timezone

from fastapi import HTTPException
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logger import logger
from app.core.response import success
from app.database.models import User

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def login(db: Session, email: str, password: str):
    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        logger.warning(f"Failed login: {email}")

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if not verify_password(password, user.password):
        logger.warning(f"Failed login: {email}")

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    token = create_access_token(
        {
            "sub": str(user.id),
            "email": user.email,
        }
    )

    logger.info(f"User logged in: {user.email}")

    return success(
        {
            "access_token": token,
            "token_type": "bearer",
        },
        "Login successful",
    )
