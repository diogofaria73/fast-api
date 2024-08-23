from sqlalchemy import Column, Integer, String, Boolean
import shared.infrastructure.database.postgresql as postgresql


class user_schema(postgresql.Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    is_active = Column(Boolean, default=True)
