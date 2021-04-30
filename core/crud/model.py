from core.odoorpc import OdooRPC
from typing import List
from core.models import Model

MODEL_NAME = "ir.model"


def crud_get_models(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[Model]:
    models: List[Model] = []

    result = odoo.search_read(MODEL_NAME, domain, [], offset, limit)

    for row in result:
        models.append(Model(**row))

    return models


def crud_search_model(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[int]:
    result = odoo.search(MODEL_NAME, domain, offset, limit)

    return result


def crud_create_model(odoo: OdooRPC, model: Model) -> int:
    result = odoo.create(MODEL_NAME, model.dict())

    return result


def crud_delete_model(odoo: OdooRPC, id: int) -> bool:
    result = odoo.unlink(MODEL_NAME, id)

    return result
