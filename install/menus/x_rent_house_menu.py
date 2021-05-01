from config import odoo

from core.odoorpc import OdooRPC

from core.models import Menu

from core.crud.menu import crud_create_menu, crud_search_menu, crud_delete_menu, crud_get_menu
from core.crud.action_window import crud_search_action_window

from core.utils import load_image


def install_x_rent_house_menu():
    x_rent_house_action = crud_search_action_window(
        odoo, [["name", "=", "Casas de renta"]])[0]

    image = load_image("assets/logo_fastapi.png")

    x_rent_house_menu = Menu(
        name="NetCity",
        action=f"ir.actions.act_window,{x_rent_house_action}",
        web_icon_data=image
    )

    crud_create_menu(odoo, x_rent_house_menu)


def uninstall_x_rent_house_menu():
    menu_id = crud_search_menu(
        odoo, [["name", "=", "NetCity"]])[0]

    crud_delete_menu(odoo, menu_id)
