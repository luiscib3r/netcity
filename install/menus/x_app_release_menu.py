from config import odoo

from core.odoorpc import OdooRPC

from core.models import Menu

from core.crud.menu import crud_create_menu, crud_search_menu, crud_delete_menu, crud_get_menu
from core.crud.action_window import crud_search_action_window

from core.utils import load_image


def install_x_app_release_menu():
    x_app_release_action = crud_search_action_window(
        odoo, [["name", "=", "App Releases"]])[0]

    x_net_city_menu = crud_search_menu(odoo, [["name", "=", "NetCity"]])[0]

    x_app_release_menu = Menu(
        name="App Releases",
        action=f"ir.actions.act_window,{x_app_release_action}",
        parent_id=x_net_city_menu,
    )

    crud_create_menu(odoo, x_app_release_menu)


def uninstall_x_app_release_menu():
    menu_id = crud_search_menu(
        odoo, [["name", "=", "App Releases"]])[0]

    crud_delete_menu(odoo, menu_id)
