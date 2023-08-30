from fastapi import APIRouter


router = APIRouter()

@router.get('/')
async def post_index():
    pass