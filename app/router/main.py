
from fastapi import APIRouter


from app.router import post, monitoring, roadmap, memo


router = APIRouter()
router.include_router(
    router=monitoring.router,
    prefix="/monitoring",
    tags=["monitoring"]
)
router.include_router(
    router=roadmap.router,
    prefix="/roadmap",
    tags=["roadmap"]
)
router.include_router(
    router=post.router,
    prefix="/post",
    tags=["post"]
)
router.include_router(
    router=memo.router,
    prefix="/memo",
    tags=["memo"]
)