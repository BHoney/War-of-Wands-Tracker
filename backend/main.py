from fastapi import FastAPI
from database.config import engine
from routers import users, games, posts
from models import models


db_metadata = models.Base.metadata.create_all(bind=engine)

#FastAPI set up
app = FastAPI()
app.include_router(users.router)
app.include_router(games.router)
app.include_router(posts.router)

@app.get('/')
async def root():
    return {"message" : "Hello World"}