from core.odoorpc import OdooRPC
from typing import List
from core.models import View

MODEL_NAME = "ir.ui.view"


def crud_get_view(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[View]:
    views: List[View] = []

    result = odoo.search_read(MODEL_NAME, domain, [], offset, limit)

    for row in result:
        views.append(View(**row))

    return views


def crud_search_view(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[int]:
    result = odoo.search(MODEL_NAME, domain, offset, limit)

    return result


def crud_create_view(odoo: OdooRPC, view: View) -> int:
    result = odoo.create(MODEL_NAME, view.dict())

    return result


def crud_delete_view(odoo: OdooRPC, id: int) -> bool:
    result = odoo.unlink(MODEL_NAME, id)

    return result
