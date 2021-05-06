from fastapi import APIRouter, Query, Depends
from fastapi.security.api_key import APIKey
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from typing import List

from config import odoo
from core.errors import OdooException
from app.crud.app_release import crud_create_app_release, crud_get_app_release
from app.models import AppRelease
from app.auth.api_key import get_api_key


router = APIRouter(prefix="/app_release", tags=["App Releases"])


@router.get("/", response_model=List[AppRelease])
async def get_app_releases(
    api_key: APIKey = Depends(get_api_key),
    limit: int = Query(20),
    offset: int = Query(0),
    domain: List = Query([]),
):
    domain = [filter.strip("[]").replace(" ", "").split(",")
              for filter in domain]
    try:
        return crud_get_app_release(odoo, domain, limit=limit, offset=offset)
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )


@router.post("/")
async def create_attachment(
    app_release: AppRelease,
    api_key: APIKey = Depends(get_api_key),
):
    try:
        return crud_create_app_release(odoo, app_release)
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )
