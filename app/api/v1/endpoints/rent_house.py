from fastapi import APIRouter, Query
from typing import List
from app.models import RentHouse
from config import odoo
from app.crud.rent_house import crud_get_rent_house
from core.errors import OdooException
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

router = APIRouter(prefix="/rent_house", tags=["Casas de renta"])


@router.get("/", response_model=List[RentHouse])
async def get_rent_houses(
    limit: int = Query(20),
    offset: int = Query(0),
    domain: List = Query([]),
):
    domain = [filter.strip("[]").replace(" ", "").split(",")
              for filter in domain]
    try:
        return crud_get_rent_house(odoo, domain, limit=limit, offset=offset)
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )
