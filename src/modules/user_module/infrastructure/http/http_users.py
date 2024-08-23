from typing import Optional
from fastapi import APIRouter

users_routes = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}, 200: {"description": "Request successful"}})


@users_routes.post("/create")
def create():
    return {"message": "User created"}


@users_routes.get("/get-all")
def get_all():
    return {"message": "Showing all users"}


@users_routes.get("/get-by-id")
def get_by_id(id: Optional[int] = 1):
    return {"message": f"Showing user with id {id}"}


@users_routes.get("/get-by-name")
def get_by_name(name: Optional[str] = "John Doe"):
    return {"message": f"Showing user with name {name}"}


@users_routes.put("/update")
def update():
    return {"message": "User updated"}


@users_routes.delete("/delete")
def delete():
    return {"message": "User deleted"}
