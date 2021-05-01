from config import odoo

from core.odoorpc import OdooRPC

from core.crud.model import crud_create_model, crud_search_model, crud_delete_model
from core.crud.model_field import crud_create_model_field, crud_update_model_field, crud_search_model_fields, crud_get_model_fields
from core.crud.model_access import crud_create_model_access

from core.models import Model, ModelField, ModelAccess


def install_x_rent_house():
    x_rent_house_model = Model(
        name="Casa de renta",
        model="x_rent_house",
    )

    model_id = crud_create_model(odoo, x_rent_house_model)

    x_name_field = crud_get_model_fields(odoo, [["name", "=", "x_name"]])[0]

    x_name_field.field_description = "Nombre"
    x_name_field.required = True
    x_name_field.model_id = model_id

    crud_update_model_field(odoo, x_name_field.id, x_name_field)

    x_rent_house_fields = [
        ModelField(
            model_id=model_id,
            name="x_description",
            field_description="Descripción",
            ttype="text",
            required=True,
        ),
        ModelField(
            model_id=model_id,
            name="x_coordinates",
            field_description="GPS",
            ttype="char",
        ),
        ModelField(
            model_id=model_id,
            name="x_address",
            field_description="Dirección",
            ttype="text",
        ),
        ModelField(
            model_id=model_id,
            name="x_images",
            field_description="Fotos",
            ttype="many2many",
            relation="ir.attachment"
        )
    ]

    for field in x_rent_house_fields:
        crud_create_model_field(odoo, field)

    x_rent_house_access = ModelAccess(
        model_id=model_id,
        name="x_rent_house_access"
    )

    crud_create_model_access(odoo, x_rent_house_access)


def uninstall_x_rent_house():
    model_id = crud_search_model(odoo, [["model", "=", "x_rent_house"]])[0]

    crud_delete_model(odoo, model_id)
