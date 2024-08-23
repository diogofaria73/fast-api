from enum import Enum
from fastapi import FastAPI
from infrastructure.routes.http_routes import router_list

app = FastAPI()

for element in router_list:
    app.include_router(element.router)
