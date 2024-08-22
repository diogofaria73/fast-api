from typing import Optional
from fastapi import APIRouter

router = APIRouter(
    prefix="/user", tags=["user"], responses={404: {"description": "Not found"}})


@router.get("/")
def index():
    return {"message": "Welcome to the user page!"}


@router.get("/profile")
def profile(limit: Optional[int] = 10):
    return {"message": f"Showing {limit} lines of user profile"}


@router.get("/about")
def about(limit: Optional[int] = 10):
    return {"message": f"Showing {limit} about user"}
