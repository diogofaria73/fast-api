from enum import Enum
from fastapi import FastAPI
from shared.infrastructure import http_global as http_requests

app = FastAPI()

for element in http_requests.routes_list:
    app.include_router(element)
