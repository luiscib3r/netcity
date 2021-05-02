from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKey
from core.models import Version
from config import odoo

from app.auth.api_key import get_api_key
from app.api.v1 import router as v1

router = APIRouter(prefix="/api")


@router.get("/version", response_model=Version, tags=["Info"])
async def get_version(
    api_key: APIKey = Depends(get_api_key)
):
    return odoo.version()


router.include_router(v1)
