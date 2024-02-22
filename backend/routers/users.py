from sqlalchemy.orm import Session
from typing import Any
from fastapi import APIRouter, HTTPException, Depends
from database import crud
from .schemas import user_schema

from database.config import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description" : "User not found"}}
)

@router.get('/')
async def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)


@router.get("/me")
async def get_user_me():
    return {"username": "currentUser"}

@router.get("/error_code_test")
async def returnNotFound():
    raise HTTPException(status_code=404)

@router.get("/{username}")
async def get_user(username: str):
    return {"username": username}

@router.post("/signup", response_model=user_schema.UserOut)
async def create_user(user: user_schema.UserIn, db: Session = Depends(get_db)) -> Any:
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return crud.create_user(db=db, user=user)