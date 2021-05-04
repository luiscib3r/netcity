from config import odoo

from core.odoorpc import OdooRPC

from core.models import ActionWindow

from core.crud.action_window import crud_create_action_window, crud_search_action_window, crud_delete_action_window


def install_x_app_release_action():
    x_app_release_action = ActionWindow(
        name="App Releases",
        res_model="x_app_release"
    )

    crud_create_action_window(odoo, x_app_release_action)


def uninstall_x_app_release_action():
    action_id = crud_search_action_window(
        odoo, [["name", "=", "App Releases"]])[0]

    crud_delete_action_window(odoo, action_id)
