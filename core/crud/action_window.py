from core.odoorpc import OdooRPC
from typing import List
from core.models import ActionWindow

MODEL_NAME = "ir.actions.act_window"


def crud_get_action_window(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[ActionWindow]:
    action_window: List[ActionWindow] = []

    result = odoo.search_read(MODEL_NAME, domain, [], offset, limit)

    for row in result:
        action_window.append(ActionWindow(**row))

    return action_window


def crud_search_action_window(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[int]:
    result = odoo.search(MODEL_NAME, domain, offset, limit)

    return result


def crud_create_action_window(odoo: OdooRPC, action_window: ActionWindow) -> int:
    result = odoo.create(MODEL_NAME, action_window.dict())

    return result


def crud_delete_action_window(odoo: OdooRPC, id: int) -> bool:
    result = odoo.unlink(MODEL_NAME, id)

    return result
