from datetime import datetime
from pydantic import BaseModel, EmailStr, NonNegativeInt

class UserSimple(BaseModel):
    username: str
    avatar_url: str | None = None
    signup_date: datetime
    last_online: datetime | None = None

class UserOut(UserSimple):
    email: EmailStr 
    rank_points: NonNegativeInt

    class Config:
        orm_mode = True

class UserIn(UserOut):
    password: str