from enum import Enum
from fastapi import FastAPI
from infrastructure.routes.blog_routes.get_routes import router as blog_router
from infrastructure.routes.user_routes.get_routes import router as user_router

app = FastAPI()
app.include_router(blog_router)
app.include_router(user_router)
