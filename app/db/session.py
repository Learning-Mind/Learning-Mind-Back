from typing import AsyncGenerator
from neo4j import AsyncSession as GraphAsyncSession
from sqlalchemy.ext.asyncio import AsyncSession as SqlAsyncSession
from starlette.requests import Request


async def get_psql_session(request: Request) -> AsyncGenerator[SqlAsyncSession, None]:
    session: SqlAsyncSession = request.app.state.postgres_session_factory()

    # async with session as session:
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()

async def get_graph_session(request: Request) -> AsyncGenerator[GraphAsyncSession, None]:
    session: GraphAsyncSession = request.app.state.neo4j_driver.session()
    
    try:
        yield session
    except Exception:
        session.cancel()
        raise
    finally:
        await session.close()