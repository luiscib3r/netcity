from core.odoorpc import OdooRPC
from typing import List
from core.models import Menu

MODEL_NAME = "ir.ui.menu"


def crud_get_menu(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[Menu]:
    menu: List[Menu] = []

    result = odoo.search_read(MODEL_NAME, domain, [], offset, limit)

    for row in result:
        menu.append(Menu(**row))

    return menu


def crud_search_menu(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[int]:
    result = odoo.search(MODEL_NAME, domain, offset, limit)

    return result


def crud_create_menu(odoo: OdooRPC, menu: Menu) -> int:
    result = odoo.create(MODEL_NAME, menu.dict())

    return result


def crud_delete_menu(odoo: OdooRPC, id: int) -> bool:
    result = odoo.unlink(MODEL_NAME, id)

    return result
