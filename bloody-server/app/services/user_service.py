from app.core.logger import logger
from sqlalchemy.orm import Session
from app.events.event_bus import event_bus
from app.events.events import USER_REGISTERED
from app.database.models import User
from app.schemas.user import UserRegister
from app.services.auth_service import hash_password


def create_user(db: Session, user: UserRegister):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        return {"error": "Email already exists"}

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    logger.info(
    f"User registered: {new_user.email}"
)
    event_bus.emit(
    USER_REGISTERED,
    new_user,
)

    return {
        "message": "User created",
        "id": new_user.id,
        "username": new_user.username,
    }


def get_users(
    db: Session,
    page: int = 1,
    limit: int = 10,
    username: str | None = None,
):
    query = db.query(User)

    if username:
        query = query.filter(
            User.username.contains(username)
        )

    return (
        query.offset((page - 1) * limit)
        .limit(limit)
        .all()
    )


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
