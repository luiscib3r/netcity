from config import odoo

from core.odoorpc import OdooRPC

from core.models import ActionWindow

from core.crud.action_window import crud_create_action_window, crud_search_action_window, crud_delete_action_window


def install_x_rent_house_action():
    x_rent_house_action = ActionWindow(
        name="Casas de renta",
        res_model="x_rent_house"
    )

    crud_create_action_window(odoo, x_rent_house_action)


def uninstall_x_rent_house_action():
    action_id = crud_search_action_window(
        odoo, [["name", "=", "Casas de renta"]])[0]

    crud_delete_action_window(odoo, action_id)
