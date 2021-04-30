from unittest import TestCase
from core.crud.model import crud_get_models, crud_create_model, crud_search_model, crud_delete_model
from core.odoorpc import OdooRPC
from config import ODOO_TEST_URL, ODOO_TEST_DB, ODOO_TEST_USERNAME, ODOO_TEST_PASSWORD
from core.models import Model


class CrudTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(CrudTest, self).__init__(*args, **kwargs)

        self.odoo = OdooRPC(
            ODOO_TEST_URL,
            ODOO_TEST_DB,
            ODOO_TEST_USERNAME,
            ODOO_TEST_PASSWORD,
        )

    def test_get_models(self):
        result = crud_get_models(self.odoo)

        self.assertEqual(len(result), 20)

    def test_create_search_delete_model(self):
        model = Model(
            name="Test model",
            model="x_test_model",
        )

        model_created = crud_create_model(self.odoo, model)

        model_id = crud_search_model(
            self.odoo, domain=[["model", "=", "x_test_model"]]
        )[0]

        result = crud_delete_model(self.odoo, model_id)

        self.assertEqual(type(model_created), int)
        self.assertEqual(type(model_id), int)
        self.assertEqual(result, True)
