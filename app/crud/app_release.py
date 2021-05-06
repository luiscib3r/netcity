from core.odoorpc import OdooRPC
from typing import List
from app.models import AppRelease

MODEL_NAME = "x_app_release"


def crud_get_app_release(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[AppRelease]:
    app_releases: List[AppRelease] = []

    result = odoo.search_read(MODEL_NAME, domain, [], offset, limit)

    for row in result:
        app_releases.append(AppRelease(**row))

    return app_releases


def crud_search_app_release(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[int]:
    result = odoo.search(MODEL_NAME, domain, offset, limit)

    return result


def crud_create_app_release(odoo: OdooRPC, app_release: AppRelease) -> int:
    result = odoo.create(MODEL_NAME, app_release.dict())

    return result


def crud_delete_app_release(odoo: OdooRPC, id: int) -> bool:
    result = odoo.unlink(MODEL_NAME, id)

    return result
