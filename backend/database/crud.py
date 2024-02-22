from datetime import datetime
from routers import users
from models import models
from sqlalchemy.orm import Session

from routers.schemas.user_schema import UserIn

def get_users(db:Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: UserIn):
    fake_hashed_password = user.password + "hashbrowns"
    db_user = models.User(
        username = user.username,
        email = user.email,
        password_hash = fake_hashed_password,
        avatar = user.avatar_url,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user