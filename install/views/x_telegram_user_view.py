from config import ODOO_URL, ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD

from core.odoorpc import OdooRPC

from core.models import View

from core.crud.view import crud_create_view, crud_delete_view, crud_search_view


def load_view(name: str) -> str:
    with open(f"install/views/xml/{name}.xml") as xml:
        return xml.read()


def install_x_telegram_user_view():
    tree = load_view("x_telegram_user_tree")
    form = load_view("x_telegram_user_form")

    odoo = OdooRPC(
        ODOO_URL, ODOO_DB,
        ODOO_USERNAME,
        ODOO_PASSWORD
    )

    x_telegram_user_view_tree = View(
        name="x_telegram_user_view_tree",
        type="tree",
        model="x_telegram_user",
        arch_base=tree
    )

    x_telegram_user_view_form = View(
        name="x_telegram_user_view_form",
        type="form",
        model="x_telegram_user",
        arch_base=form
    )

    crud_create_view(odoo, x_telegram_user_view_tree)
    crud_create_view(odoo, x_telegram_user_view_form)


def uninstall_x_telegram_user_view():
    odoo = OdooRPC(
        ODOO_URL, ODOO_DB,
        ODOO_USERNAME,
        ODOO_PASSWORD
    )

    tree_id = crud_search_view(
        odoo, [["name", "=", "x_telegram_user_view_tree"]])[0]

    form_id = crud_search_view(
        odoo, [["name", "=", "x_telegram_user_view_form"]])[0]

    crud_delete_view(odoo, tree_id)
    crud_delete_view(odoo, form_id)
