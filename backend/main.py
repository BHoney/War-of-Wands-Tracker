from fastapi import FastAPI
from routers import users, games, posts

#FastAPI set up
app = FastAPI()
app.include_router(users.router)
app.include_router(games.router)
app.include_router(posts.router)

@app.get('/')
async def root():
    return {"message" : "Hello World"}