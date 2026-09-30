from sqlalchemy.orm import Session
from passlib.context import CryptContext

from ..database import User


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_user(
    db: Session,
    username: str,
    email: str,
    password: str
):

    existing_user = (
        db.query(User)
        .filter(
            (User.username == username) |
            (User.email == email)
        )
        .first()
    )

    if existing_user:
        return None


    hashed_password = hash_password(password)


    user = User(
        username=username,
        email=email,
        password_hash=hashed_password
    )


    db.add(user)
    db.commit()
    db.refresh(user)


    return user


def authenticate_user(
    db: Session,
    username: str,
    password: str
):

    user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )


    if user is None:
        return None


    if not verify_password(
        password,
        user.password_hash
    ):
        return None


    return user