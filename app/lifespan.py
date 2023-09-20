from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from neo4j import AsyncDriver
from sqlalchemy.ext.asyncio import AsyncEngine

from app.db.engine import set_db_engines


@asynccontextmanager
async def lifespan(app: FastAPI):
    await set_db_engines(app)

    yield
    postgres_engine: AsyncEngine = app.state.postgres_db_engine
    neo4j_driver: AsyncDriver = app.state.neo4j_driver
    
    await postgres_engine.dispose()
    await neo4j_driver.close()
