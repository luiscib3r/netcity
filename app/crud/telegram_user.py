from core.odoorpc import OdooRPC
from typing import List
from app.models import TelegramUser

MODEL_NAME = "x_telegram_user"


def crud_get_telegram_users(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[TelegramUser]:
    telegram_users: List[TelegramUser] = []

    result = odoo.search_read(MODEL_NAME, domain, [], offset, limit)

    for row in result:
        row["id"] = row["x_user_id"]
        telegram_users.append(TelegramUser(**row))

    return telegram_users


def crud_search_telegram_user(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[int]:
    result = odoo.search(MODEL_NAME, domain, offset, limit)

    return result


def crud_create_telegram_user(odoo: OdooRPC, telegram_user: TelegramUser) -> int:
    result = odoo.create(MODEL_NAME, telegram_user.dict())

    return result


def crud_delete_telegram_user(odoo: OdooRPC, id: int) -> bool:
    result = odoo.unlink(MODEL_NAME, id)

    return result
