from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncEngine

from app.db.engine import set_db_engines


@asynccontextmanager
async def lifespan(app: FastAPI):
    await set_db_engines(app)

    yield
    engine: AsyncEngine = app.state.postgres_db_engine
    await engine.dispose()
