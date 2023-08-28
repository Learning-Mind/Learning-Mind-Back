from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_async_session
from app.models.user import UserModel


router = APIRouter()

@router.get("/")
async def asdf(
    session: AsyncSession = Depends(get_async_session)
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
