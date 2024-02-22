from sqlalchemy import update, values
from models import models
from sqlalchemy.orm import Session

from routers.schemas import user_schema as user, games_schema as game


def get_users(db:Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def update_user_rank(db: Session, user_id: int, points_gained:int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        
        user.rank_points += points_gained # this line throws a fit for some reason #type: ignore
        db.commit()

def create_user(db: Session, user: user.UserIn):
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

# def create_game_data(db:Session, game: SimpleGameData)