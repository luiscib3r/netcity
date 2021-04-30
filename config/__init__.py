import os
from dotenv import load_dotenv
from core.odoorpc import OdooRPC

load_dotenv()

# Testing
ODOO_TEST_URL = os.getenv("ODOO_TEST_URL")
ODOO_TEST_DB = os.getenv("ODOO_TEST_DB")
ODOO_TEST_USERNAME = os.getenv("ODOO_TEST_USERNAME")
ODOO_TEST_PASSWORD = os.getenv("ODOO_TEST_PASSWORD")

# Odoo server setup
ODOO_URL = os.getenv("ODOO_URL")
ODOO_DB = os.getenv("ODOO_DB")

# For installation
ODOO_INSTALL_USERNAME = os.getenv("ODOO_INSTALL_USERNAME")
ODOO_INSTALL_PASSWORD = os.getenv("ODOO_INSTALL_PASSWORD")
