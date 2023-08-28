
from fastapi import APIRouter


from app.router import post, monitoring


router = APIRouter()
router.include_router(
    router=monitoring.router,
    prefix="/monitoring",
    tags=["monitoring"]
)
router.include_router(
    router=post.router,
    prefix="/post",
    tags=["post"]
)