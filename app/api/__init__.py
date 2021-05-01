from fastapi import APIRouter
from core.models import Version
from config import odoo

router = APIRouter(prefix="/api")


@router.get("/version", response_model=Version, tags=["Info"])
async def get_version():
    return odoo.version()
