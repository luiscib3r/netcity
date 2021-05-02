from config import odoo

from core.odoorpc import OdooRPC

from core.models import ActionWindow

from core.crud.action_window import crud_create_action_window, crud_search_action_window, crud_delete_action_window


def install_x_telegram_user_action():
    x_telegram_user_action = ActionWindow(
        name="Telegram Users",
        res_model="x_telegram_user"
    )

    crud_create_action_window(odoo, x_telegram_user_action)


def uninstall_x_telegram_user_action():
    action_id = crud_search_action_window(
        odoo, [["name", "=", "Telegram Users"]])[0]

    crud_delete_action_window(odoo, action_id)
