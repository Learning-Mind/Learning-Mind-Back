from fastapi import FastAPI

from app.lifespan import lifespan
from app.router import router


def app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
        docs_url="/api/docs",
        redoc_url="/api/redoc",
    )

    app.include_router(
        router=router,
        # prefix='/'
    )
    
    return app