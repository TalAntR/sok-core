import unittest
from ploy.core.common import EntryError, Product, OpsEnvironment
from ploy.core.resolvers import Registry
from ploy.examples.inventory import InventoryProviderEx


class TestRegistry(unittest.TestCase):
    """
    A suite of tests to check how to work registry of supported products
    """

    def test_get_unique_product(self):
        """
        """
        registry = Registry()
        registry.add_inventories(InventoryProviderEx("ploy"))
        env = registry.get_environment("ploy:uat")
        self.assertIsInstance(env, OpsEnvironment)
        self.assertEqual(env.product.name, "ploy")
        self.assertEqual(env.name, "uat")

    def test_get_unsupported_product(self):
        """
        Expects that get_inventory method throws EntryError exception
        when a project with specified name hasn't been registered
        """
        registry = Registry()
        self.assertRaises(EntryError, registry.get_environment, "Unsupported")


