from fastapi import APIRouter
from core.models import Version
from config import odoo

from app.api.v1 import router as v1

router = APIRouter(prefix="/api")


@router.get("/version", response_model=Version, tags=["Info"])
async def get_version():
    return odoo.version()


router.include_router(v1)
