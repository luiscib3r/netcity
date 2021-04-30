from core.odoorpc import OdooRPC
from typing import List
from core.models import ModelAccess

MODEL_NAME = "ir.model.access"


def crud_get_model_access(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[ModelAccess]:
    model_access: List[ModelAccess] = []

    result = odoo.search_read(MODEL_NAME, domain, [], offset, limit)

    for row in result:
        model_access.append(ModelAccess(**row))

    return model_access


def crud_search_model_access(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[int]:
    result = odoo.search(MODEL_NAME, domain, offset, limit)

    return result


def crud_create_model_access(odoo: OdooRPC, model_access: ModelAccess) -> int:
    result = odoo.create(MODEL_NAME, model_access.dict())

    return result


def crud_delete_model_access(odoo: OdooRPC, id: int) -> bool:
    result = odoo.unlink(MODEL_NAME, id)

    return result
