"""
This is implementation of a test suite to check the implementation for JobRunnerPool class

All tests in this suite sould be passed.
"""
import unittest
from ploy.core.common import Product, OpsEnvironment
from ploy.examples.inventory import InventoryProviderEx


class TestInventoryProviderEx(unittest.TestCase):
    """
    A suite of tests to check job processing by pool of executors.
    """

    @staticmethod
    def create_inventory_provider(name):
        return InventoryProviderEx(name)

    def test_product_names(self):
        """
        """
        exp_name = "D-Ploy"
        inventory = self.create_inventory_provider(exp_name)
        self.assertListEqual([exp_name], list(inventory.list_products()))

    def test_product_iteration(self):
        """
        """
        exp_name = "PloyEx"
        inventory = self.create_inventory_provider(exp_name)
        for e in inventory.environments():
            self.assertIsInstance(e, OpsEnvironment)
            self.assertIsInstance(e.product, Product)
            self.assertEqual(inventory.NAMESPACE, e.product.namespace)
            self.assertEqual(exp_name, e.product.name)
            self.assertEqual("", e.product.description)





