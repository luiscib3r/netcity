from fastapi import FastAPI
from app.api import router as api_router
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

app = FastAPI(title="NetCity")
app.include_router(api_router)
