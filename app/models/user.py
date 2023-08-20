import uuid
from sqlalchemy import Column, Integer, String, Uuid
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.models.base import Base


class UserModel(Base):
    __tablename__ = "user"
    # __table_args__ = { "schema": "myapi" }

    # user_id: Mapped[int] = mapped_column("user_id", primary_key=True, autoincrement=True)
    # user_id: Mapped[Uuid] = mapped_column("user_id", primary_key=True, default=uuid.uuid4)
    # nickname: Mapped[str] = mapped_column("nickname", unique=True)
    # email: Mapped[str] = mapped_column("email", unique=True)
    # hashed_password: Mapped[str] = mapped_column("hashed_password")
    # name: Mapped[str] = mapped_column("name")

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String, unique=True)
    name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)