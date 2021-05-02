from core.odoorpc import OdooRPC
from typing import List
from app.models import TelegramUser

MODEL_NAME = "x_telegram_user"


def crud_get_telegram_users(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20, change_id=True) -> List[TelegramUser]:
    telegram_users: List[TelegramUser] = []

    result = odoo.search_read(MODEL_NAME, domain, [], offset, limit)

    for row in result:
        if change_id:
            row["id"] = row["x_user_id"]

        telegram_users.append(TelegramUser(**row))

    return telegram_users


def crud_search_telegram_user(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[int]:
    result = odoo.search(MODEL_NAME, domain, offset, limit)

    return result


def crud_create_telegram_user(odoo: OdooRPC, telegram_user: TelegramUser) -> int:
    user = crud_get_telegram_users(
        odoo, [["x_user_id", "=", telegram_user.x_user_id]], change_id=False)

    if len(user) > 0:
        result = crud_update_telegram_user(odoo, user[0].x_user_id, telegram_user)
    else:
        result = odoo.create(MODEL_NAME, telegram_user.dict())

    return result


def crud_update_telegram_user(odoo: OdooRPC, user_id: int, telegram_user: TelegramUser) -> bool:
    result = odoo.write(MODEL_NAME, user_id, telegram_user.dict())

    return result


def crud_delete_telegram_user(odoo: OdooRPC, id: int) -> bool:
    result = odoo.unlink(MODEL_NAME, id)

    return result
