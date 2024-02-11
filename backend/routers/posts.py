
from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from routers.users import UserSimple


router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Post not found"}}
)

class Comment(BaseModel):
    author: UserSimple
    tags: Optional[List[str]]
    body: str
    date_posted: datetime
    kudos: int

class Post(Comment):
    comments: List[Comment] = []


POSTS = {
    "1": {
    "post_id": 1,
    "post": {
        "author": {
        "username": "BestMaggieEver",
        "avatar_url": "pedro.jpg"
        },
    "tags": [
      "food",
      "baking"
    ],
    "body": "I like baking but I hate that I can't eat the raw dough 😭",
    "date_posted": "2024-02-10T00:45:50.522000Z",
    "kudos": 0,
    "comments": []
  },
} }

@router.get("/")
async def get_all_posts():
    return POSTS

@router.post("/{id}")
async def new_post(id: int, post: Post ):
    result = {"post_id": id, "post": post}
    POSTS[str(id)] = result

@router.post("/{id}/comments")
async def new_comment(id: str, comment: Post):
    if id and id in POSTS:
        POSTS[id]["post"]["comments"].append(comment)
        return POSTS[id]
    raise HTTPException(status_code=400)

@router.put("/{id}/kudos")
async def add_kudos(id):
    if id and id in POSTS:
        POSTS[id]["post"]["kudos"] = POSTS[id]["post"]["kudos"] + 1
        return POSTS[id]
    raise HTTPException(status_code=400)