from core.odoorpc import OdooRPC
from typing import List
from core.models import Attachment

MODEL_NAME = "ir.attachment"


def crud_get_attachment(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[Attachment]:
    attachments: List[Attachment] = []

    result = odoo.search_read(MODEL_NAME, domain, ["name", "type", "datas", "url", "mimetype"], offset, limit)

    for row in result:
        attachments.append(Attachment(**row))

    return attachments


def crud_search_attachment(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[int]:
    result = odoo.search(MODEL_NAME, domain, offset, limit)

    print(result)

    return result


def crud_create_attachment(odoo: OdooRPC, attachment: Attachment) -> int:
    result = odoo.create(MODEL_NAME, attachment.dict())

    return result


def crud_delete_attachment(odoo: OdooRPC, id: int) -> bool:
    result = odoo.unlink(MODEL_NAME, id)

    return result
