from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from app.db.session import get_async_session

from app.schema.memo import CreateMemoSchema
from app.service.memo import MemoService


router = APIRouter()

@router.post("/")
async def index(
    body: CreateMemoSchema,
    se: AsyncSession = Depends(get_async_session)
):
    result = await MemoService(se).create_memo(body)
    
    return 