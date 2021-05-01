from core.odoorpc import OdooRPC
from typing import List
from app.models import RentHouse

MODEL_NAME = "x_rent_house"


def crud_get_rent_house(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[RentHouse]:
    rent_houses: List[RentHouse] = []

    result = odoo.search_read(MODEL_NAME, domain, [], offset, limit)

    for row in result:
        rent_houses.append(RentHouse(**row))

    return rent_houses


def crud_search_rent_house(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[int]:
    result = odoo.search(MODEL_NAME, domain, offset, limit)

    return result


def crud_create_rent_house(odoo: OdooRPC, rent_house: RentHouse) -> int:
    result = odoo.create(MODEL_NAME, rent_house.dict())

    return result


def crud_delete_rent_house(odoo: OdooRPC, id: int) -> bool:
    result = odoo.unlink(MODEL_NAME, id)

    return result
