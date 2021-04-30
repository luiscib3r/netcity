import os
from dotenv import load_dotenv

load_dotenv()

# Testing
ODOO_TEST_URL = os.getenv("ODOO_TEST_URL")
ODOO_TEST_DB = os.getenv("ODOO_TEST_DB")
ODOO_TEST_USERNAME = os.getenv("ODOO_TEST_USERNAME")
ODOO_TEST_PASSWORD = os.getenv("ODOO_TEST_PASSWORD")
