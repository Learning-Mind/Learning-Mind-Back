from fastapi import FastAPI


app = FastAPI(
    # title=OPEN_API_TITLE,
    # description=OPEN_API_DESCRIPTION,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)