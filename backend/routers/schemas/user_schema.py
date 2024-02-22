from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserSimple(BaseModel):
    username: str
    avatar_url: str | None = None
    signup_date: datetime
    last_online: datetime | None = None

class UserOut(UserSimple):
    email: EmailStr 

    class Config:
        orm_mode = True

class UserIn(UserOut):
    password: str