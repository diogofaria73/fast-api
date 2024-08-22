from typing import Optional
from fastapi import APIRouter

router = APIRouter(
    prefix="/blog", tags=["blog"], responses={404: {"description": "Not found"}})


@router.get("/")
def index():
    return {"message": "Welcome to the blog!"}


@router.get("/posts")
def posts(limit: Optional[int] = 10):
    return {"message": f"Showing {limit} posts"}


@router.get("/comments")
def comments(limit: Optional[int] = 10):
    return {"message": f"Showing {limit} comments"}
