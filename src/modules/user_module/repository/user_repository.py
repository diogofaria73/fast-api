from sqlalchemy.orm.session import Session
from modules.user_module.entities.user import User
from shared.infrastructure.database.schemas import user_schema


def create_user(db: Session, request: User):
    new_user = user_schema.user_schema(
        name=request.name,
        email=request.email,
        password=request.password,
        is_active=request.is_active)

    db.add(new_user)
