from fastapi import FastAPI
from neo4j import AsyncDriver, AsyncGraphDatabase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine

from app.config import settings
from app.models.base import Base


async def set_db_engines(app: FastAPI) -> None:
    postgres_engine: AsyncEngine = create_async_engine(
        settings.psql_async_db_dsn,
        echo=True,
    )
    
    neo4j_driver: AsyncDriver = AsyncGraphDatabase.driver(
        settings.neo4j_bolt_uri,
        auth=(settings.neo4j_user, settings.neo4j_password)
    )
    
    # async_sessionmaker: a factory for new AsyncSession objects.
    # expire_on_commit - don't expire objects after transaction commit
    postgres_session_factory = async_sessionmaker(postgres_engine, expire_on_commit=False)

    app.state.postgres_db_engine = postgres_engine
    app.state.postgres_session_factory = postgres_session_factory

    app.state.neo4j_driver = neo4j_driver

    async with postgres_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
