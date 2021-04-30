from xmlrpc.client import ServerProxy
from xmlrpc.client import Fault
from core.models import Version
from core.errors import OdooException
from typing import List


class OdooRPC:
    """
    OdooRPC
    """

    def __init__(self, url: str, db: str, username: str, password: str):
        self.url = url
        self.db = db
        self.username = username
        self.password = password

        self.common = ServerProxy(f"{self.url}/xmlrpc/2/common")
        self.models = ServerProxy(f"{self.url}/xmlrpc/2/object")

        self.uid = self.authenticate()

    def version(self) -> Version:
        """
            Return Odoo version info

            Returns:
                version_info (Version): Version object
        """
        result = self.common.version()
        return Version(**result)

    def authenticate(self) -> int:
        """
            Authenticate user in odoo server

            Returns:
                uid (int): user id or False
        """
        return self.common.authenticate(
            self.db, self.username, self.password, {})

    def check_access_rights(self, model: str, operations: []) -> bool:
        """
            Check access rights in a model

            Parameters:
                model (str): Model name
                operations (List): List of strings with operation name (read, create, write, unlink)

            Returns:
                uid (int): user id or False
        """
        try:
            return self.call(model, "check_access_rights", operations)
        except Fault as e:
            raise OdooException(e.faultString)

    def search(self, model: str, domain: List = [], offset: int = 0, limit: int = 20) -> List[int]:
        """
            Search records by domain in a model an return ids

            Parameters:
                model (str): Model name
                domain (List): List of conditions ex: [['is_company', '=', True]]
                offset (int): Offset
                limit (int): Limit

            Returns:
                A list of ids
        """
        try:
            return self.call(model, "search", [domain], {
                "offset": offset,
                "limit": limit
            })
        except Fault as e:
            raise OdooException(e.faultString)

    def search_read(self, model: str, domain: List = [], fields: List[str] = [], offset: int = 0, limit: int = 20) -> List[dict]:
        """
            Search records by domain in a model an return data

            Parameters:
                model (str): Model name
                domain (List): List of conditions ex: [['is_company', '=', True]]
                fields (List): List of fields name that are return
                offset (int): Offset
                limit (int): Limit

            Returns:
                A list of records in model
        """
        try:
            return self.call(model, "search_read", [domain], {
                "fields": fields,
                "offset": offset,
                "limit": limit
            })
        except Fault as e:
            raise OdooException(e.faultString)

    def read(self, model: str, ids: List[int] = [], fields: List[str] = []) -> List[dict]:
        """
            Search records by ids in a model an return data

            Parameters:
                model (str): Model name
                ids (List[int]): List of conditions ex: [['is_company', '=', True]]
                fields (List): List of fields name that are return

            Returns:
                A list of records in model
        """
        try:
            return self.call(model, "read", [ids], {
                "fields": fields,
            })
        except Fault as e:
            raise OdooException(e.faultString)

    def fields_get(self, model: str, domain: List = [], attributes: List[str] = ["string", "help", "type"]) -> dict:
        """
            Return fields of a model

            Parameters:
                model (str): Model name
                domain (List): List of conditions ex: [['is_company', '=', True]]
                attributes (List): List of attributes name that are return

            Returns:
                A list of fields in model
        """
        try:
            return self.call(model, "fields_get", [domain], {
                "attributes": attributes,
            })
        except Fault as e:
            raise OdooException(e.faultString)

    def create(self, model: str, data: dict) -> int:
        """
            Create object in model

            Parameters:
                model (str): Model name
                data (dict): Object data

            Returns:
                Object id
        """
        try:
            return self.call(model, "create", [data])
        except Fault as e:
            raise OdooException(e.faultString)

    def write(self, model: str, id: int, data: dict) -> bool:
        """
            Write (Edit) object in model

            Parameters:
                model (str): Model name
                id (int): Object id
                data (dict): Object data

            Returns:
                True or False
        """
        try:
            return self.call(model, "write", [[id], data])
        except Fault as e:
            raise OdooException(e.faultString)

    def unlink(self, model: str, id: int) -> bool:
        """
            Unlink (Delete) object in model

            Parameters:
                model (str): Model name
                id (int): Object id                

            Returns:
                True or False
        """
        try:
            return self.call(model, "unlink", [[id]])
        except Fault as e:
            raise OdooException(e.faultString)

    def call(self, model: str, method: str, kargs: List = [], args: dict = {}):
        """
            Call model method

            Parameters:
                model (str) : Model name
                method (str) : Method name
                kargs (List) : Method arguments
                args (List) : Method arguments
        """
        try:
            return self.models.execute_kw(self.db, self.uid, self.password, model, method, kargs, args)
        except Fault as e:
            raise OdooException(e.faultString)
