from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request


async def get_async_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    session: AsyncSession = request.app.state.postgres_session_factory()

    # async with session as session:
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()

