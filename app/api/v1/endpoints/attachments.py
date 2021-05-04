from config import odoo

from fastapi import APIRouter, Depends, Query
from fastapi.security.api_key import APIKey
from app.auth.api_key import get_api_key
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from core.models import Attachment
from core.crud.attachment import crud_get_attachment, crud_create_attachment
from core.errors.odoo_exception import OdooException

from typing import List


router = APIRouter(prefix="/attachments", tags=["Attachments"])


@router.get("/", response_model=List[Attachment])
async def get_attachments(
    api_key: APIKey = Depends(get_api_key),
    limit: int = Query(20),
    offset: int = Query(0),
    domain: List = Query([]),
):
    domain = [filter.strip("[]").replace(" ", "").split(",")
              for filter in domain]
    try:
        return crud_get_attachment(odoo, domain, limit=limit, offset=offset)
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )


@router.post("/")
async def create_attachment(
    attachment: Attachment,
    api_key: APIKey = Depends(get_api_key),
):
    try:
        return crud_create_attachment(odoo, attachment)
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )
