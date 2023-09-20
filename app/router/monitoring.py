from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession as SqlAsyncSession

from app.db.session import get_psql_session


router = APIRouter()

@router.get("/")
async def asdf(
    session: SqlAsyncSession = Depends(get_psql_session)
):
    # obj = UserModel(
    #     nickname="dkㅇdkd",
    #     name="qwer",
    #     email="dkfjwkㅇ@email.com",
    #     hashed_password="salkdfjwie",
    # )
    # session.add(obj)
    # await session.flush()
    
    return 'obj'
