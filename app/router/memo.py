from sqlalchemy.ext.asyncio import AsyncSession as SqlAsyncSession
from fastapi import APIRouter, Depends
from app.db.session import get_psql_session

from app.schema.memo import CreateMemoSchema
from app.service.memo import MemoService


router = APIRouter()

@router.post("/")
async def index(
    body: CreateMemoSchema,
    se: SqlAsyncSession = Depends(get_psql_session),
):
    result = await MemoService(se).create_memo(body)
    
    return 