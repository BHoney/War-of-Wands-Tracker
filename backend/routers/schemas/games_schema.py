
from datetime import datetime
from pydantic import BaseModel
from models.models import User
from schemas import user_schema


class SimpleGameData(BaseModel):
    id: int
    match_date: datetime
    players: list[user_schema.UserSimple]
    winner: user_schema.UserSimple