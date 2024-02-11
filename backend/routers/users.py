
from typing import Any, List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr

class UserSimple(BaseModel):
    username: str
    avatar_url: str

class UserOut(UserSimple):
    email: EmailStr
    friends_list: List[str] = []
    block_list: List[str] = []

class UserIn(UserOut):
    hashWord: str
    

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description" : "User not found"}}
)

@router.get('/')
async def get_users():
    return [
        {"username": "BlackMagic666"},
        {"username": "BlueEyedNeverBrokeAgain"},
        {"username": "EyesOnMillenium"}
    ]


@router.get("/me")
async def get_user_me():
    return {"username": "currentUser"}

@router.get("/error_code_test")
async def returnNotFound():
    raise HTTPException(status_code=404)

@router.get("/{username}")
async def get_user(username: str):
    return {"username": username}

@router.post("/signup", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user