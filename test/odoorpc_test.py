from unittest import TestCase
from core.odoorpc import OdooRPC
from core.models import Version

from config import ODOO_TEST_URL, ODOO_TEST_DB, ODOO_TEST_USERNAME, ODOO_TEST_PASSWORD


class OdooRPCTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(OdooRPCTest, self).__init__(*args, **kwargs)

        self.odoo = OdooRPC(
            ODOO_TEST_URL,
            ODOO_TEST_DB,
            ODOO_TEST_USERNAME,
            ODOO_TEST_PASSWORD,
        )

    def test_version(self):

        result = self.odoo.version()

        self.assertEqual(type(result), Version)

    def test_authenticate(self):
        result = self.odoo.authenticate()

        self.assertEqual(type(result), int)

    def test_check_access_right(self):
        result = self.odoo.check_access_rights("res.partner", ["read"])

        self.assertEqual(result, True)

    def test_search(self):
        result = self.odoo.search("res.partner")

        self.assertEqual(type(result), list)

    def test_search_limit(self):
        result = self.odoo.search("res.partner", limit=1)

        self.assertEqual(len(result), 1)

    def test_search_domain(self):
        result = self.odoo.search("res.partner", domain=[
                                  ["is_company", "=", True]])

        self.assertEqual(len(result), 1)

    def test_search_read(self):
        result = self.odoo.search_read("res.partner")

        self.assertEqual(type(result), list)

    def test_search_read_limit(self):
        result = self.odoo.search_read("res.partner", limit=1)

        self.assertEqual(len(result), 1)

    def test_search_read_domain(self):
        result = self.odoo.search_read(
            "res.partner", domain=[["is_company", "=", True]])

        self.assertEqual(len(result), 1)

    def test_search_read_fields(self):
        result = self.odoo.search_read(
            "res.partner", fields=["name", "email"], limit=1)

        self.assertEqual(str(result[0].keys()),
                         "dict_keys(['id', 'name', 'email'])")

    def test_read(self):
        result = self.odoo.read("res.partner", [3], fields=["name", "email"])

        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0].keys()),
                         "dict_keys(['id', 'name', 'email'])")

    def test_fields_get(self):
        result = self.odoo.fields_get("res.partner")

        self.assertEqual(type(result), dict)

    def test_create_write_unlink(self):
        id = self.odoo.create("res.partner", {
            "name": "New Partner"
        })

        self.assertEqual(type(id), int)

        result = self.odoo.write("res.partner", id, {
            "name": "Newer Parner",
            "email": "partner@example.com",
        })

        self.assertEqual(result, True)

        result_delete = self.odoo.unlink("res.partner", id)

        self.assertEqual(result_delete, True)
