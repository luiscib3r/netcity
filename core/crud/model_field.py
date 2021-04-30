from core.odoorpc import OdooRPC
from typing import List
from core.models import ModelField

MODEL_NAME = "ir.model.fields"


def crud_get_model_fields(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[ModelField]:
    model_fields: List[ModelField] = []

    result = odoo.search_read(MODEL_NAME, domain, [], offset, limit)

    for row in result:
        model_fields.append(ModelField(**row))

    return model_fields


def crud_search_model_fields(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[int]:
    result = odoo.search(MODEL_NAME, domain, offset, limit)

    return result


def crud_create_model_field(odoo: OdooRPC, model_field: ModelField) -> int:
    if model_field.field_description == "":
        model_field.field_description = model_field.name

    result = odoo.create(MODEL_NAME, model_field.dict())

    return result


def crud_update_model_field(odoo: OdooRPC, field_id: int, model_field: ModelField) -> bool:
    result = odoo.write(MODEL_NAME, field_id, model_field.dict())

    return result


def crud_delete_model_field(odoo: OdooRPC, id: int) -> bool:
    result = odoo.unlink(MODEL_NAME, id)

    return result
