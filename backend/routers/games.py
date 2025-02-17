
from ast import List
from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel

from database.config import SessionLocal
from .schemas import user_schema as user, games_schema as game

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/games",
    tags=["games"],
    responses={404: {"description": "Game data not found"}}
)



    

@router.get("/")
async def get_all_games():
    return [
        {
            "id": 1234,
            "players": [
                "BlackMagic666", 
                "BlueEyedNeverBrokeAgain"
                ],
            "date": "Feb 9 2024",
            "winner": "BlackMagic666"
         },
         {
            "gameId": 5678,
            "players": [
                "BlackMagic666", 
                "EyesOnMillenium"
                ],
            "date": "Feb 7 2024",
            "winner": "BlackMagic666"
         },
         {
            "gameId": 7890,
            "players": [
                "BlackMagic666", 
                "BlueEyedNeverBrokeAgain"
                ],
            "date": "Feb 1 2024",
            "winner": "BlackMagic666"
         }
         
    ]

@router.post("/insert-game")
async def insert_game_data(data: game.SimpleGameData):
    return data.model_dump()

@router.get("/{game_id}")
async def get_game_data(game_id: int):
    return {"game_id": game_id, "players": [
                "BlackMagic666", 
                "BlueEyedNeverBrokeAgain"
                ],
            "date": "Feb 1 2024",
            "winner": "BlackMagic666" }