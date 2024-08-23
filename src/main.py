from enum import Enum
from fastapi import FastAPI
from shared.infrastructure import http_global

app = FastAPI()

for element in http_global.http_list:
    app.include_router(element)
