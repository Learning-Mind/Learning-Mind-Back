from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.config import settings

from app.models.base import Base


async def set_db_engines(app: FastAPI) -> None:
    postgres_engine = create_async_engine(
        settings.psql_async_db_dsn,
        echo=True,
    )
    
    # async_sessionmaker: a factory for new AsyncSession objects.
    # expire_on_commit - don't expire objects after transaction commit
    postgres_session_factory = async_sessionmaker(postgres_engine, expire_on_commit=False)

    app.state.postgres_db_engine = postgres_engine
    app.state.postgres_session_factory = postgres_session_factory

    async with postgres_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

