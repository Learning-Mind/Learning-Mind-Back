# https://hackernoon.com/adopting-the-repository-pattern-for-enhanced-backend-development-with-fastapi

from typing import Any, List, Sequence, Type
from sqlalchemy import Executable, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.base import Base


class SessionMixin:
    """Provides instance of database session."""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session


class BaseDataManager(SessionMixin):
    """Base data manager class responsible for operations over database."""

    async def add_one(self, model: Any) -> Any:
        self.session.add(model)
        await self.session.flush()
        return model

    async def add_all(self, models: Sequence[Any]) -> List[Any]:
        self.session.add_all(models)
        await self.session.flush()
        return models

    async def get_one(self, select_stmt: Executable) -> Any:
        executed = await self.session.execute(select_stmt)
        return executed.fetchone()

    async def get_all(self, select_stmt: Executable) -> List[Any]:
        executed = await self.session.execute(select_stmt)
        return list(executed.all())
    
    # TODO pagination

    async def get_from_tvf(self, model: Type[Base], *args: Any) -> List[Any]:
        """Query from table valued function.

        This is a wrapper function that can be used to retrieve data from
        table valued functions.

        Examples:
            from app.models.base import SQLModel

            class MyModel(SQLModel):
                __tablename__ = "function"
                __table_args__ = {"schema": "schema"}

                x: Mapped[int] = mapped_column("x", primary_key=True)
                y: Mapped[str] = mapped_column("y")
                z: Mapped[float] = mapped_column("z")

            # equivalent to "SELECT x, y, z FROM schema.function(1, "AAA")"
            BaseDataManager(session).get_from_tvf(MyModel, 1, "AAA")
        """

        fn = getattr(getattr(func, model.schema()), model.table_name())
        stmt = select(fn(*args).table_valued(*model.fields()))
        exc = await self.get_all(select(model).from_statement(stmt))
        return exc
