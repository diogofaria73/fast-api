from enum import Enum
from fastapi import FastAPI
from shared.infrastructure.http import http_global as http_requests
from shared.infrastructure.database import postgresql
from shared.infrastructure.database.schemas import user_schema

# Load FastAPI server
app = FastAPI()

# Load endpoints
for element in http_requests.routes_list:
    app.include_router(element)

user_schema.postgresql.Base.metadata.create_all(bind=postgresql.engine)
