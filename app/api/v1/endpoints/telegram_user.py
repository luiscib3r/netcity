from fastapi import APIRouter, Query, Depends
from fastapi.security.api_key import APIKey
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from typing import List

from config import odoo
from core.errors import OdooException
from app.crud.telegram_user import crud_get_telegram_users, crud_create_telegram_user
from app.models import TelegramUser
from app.auth.api_key import get_api_key


router = APIRouter(prefix="/telegram_user", tags=["Telegram Users"])


@router.get("/", response_model=List[TelegramUser])
async def get_telegram_users(
    api_key: APIKey = Depends(get_api_key),
    limit: int = Query(20),
    offset: int = Query(0),
    domain: List = Query([]),
):
    domain = [filter.strip("[]").replace(" ", "").split(",")
              for filter in domain]
    try:
        return crud_get_telegram_users(odoo, domain, limit=limit, offset=offset)
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )


@router.post("/")
async def create_telegram_user(
    user: TelegramUser,
    api_key: APIKey = Depends(get_api_key),
):
    try:
        return crud_create_telegram_user(odoo, user)
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )
