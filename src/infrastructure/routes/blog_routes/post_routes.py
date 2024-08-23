from typing import Optional
from fastapi import APIRouter

router = APIRouter(
    prefix="/blog", tags=["blog"], responses={404: {"description": "Not found"}, 200: {"description": "Request successful"}})


@router.post("/posts")
def posts(limit: Optional[int] = 10):
    return {"message": f"Showing {limit} posts"}
