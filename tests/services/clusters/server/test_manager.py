"""
This suite includes tests which verify an implementation of embedded
Cluster API for the Service Orchestration Kit.

All tests in this suite must be passed.
"""
import unittest
from falcon import Request, Response
from sok.services.clusters.server import HandlerFactory
from sok.services.clusters.server.manager import ResourceManager


class ResourceManagerTest(unittest.TestCase):
    """
    A suite of tests to verify deserialization models (products, environments, resources ...)
     from YAML manifest.
    """

    def test_get_default_product(self):
        """
        Verifies that the 'sok' product is imported from YAML declaration by default.
        """

        product = ResourceManager().get()
        self.assertIsInstance(product, dict, "Product type must be dictionary")

        name = product['name']
        self.assertIsInstance(name, str, "Product name must have string type")
        self.assertEqual('sok', name, "Name is incorrect for default product")

        namespace = product['namespace']
        self.assertIsInstance(namespace, str, "Product namespace must have string type")
        self.assertEqual('', namespace, "Namespace is incorrect for default product")

        note = product['note']
        self.assertIsInstance(note, str, "Product notes must have string type")
        self.assertEqual('The Service Orchestration Kit product',
                         note, "Description is incorrect for default product")

        env_schema = product['env-schema']
        self.assertIsInstance(env_schema, list, "Schema for environments must have a list type")
        self.assertEqual([], env_schema, "Schema for SOK environment must be an empty list")

        schemas = product['role-schemas']
        self.assertIsInstance(schemas, list, "Schema for roles must have a list type")

        schema = list(filter(lambda i: i['name'] == 'inventory', schemas))
        self.assertEqual(1, len(schema), "Schema for inventory service must be declared")

        schema = list(filter(lambda i: i['name'] == 'registry', schemas))
        self.assertEqual(1, len(schema), "Schema for task registry service must be declared")

        schema = list(filter(lambda i: i['name'] == 'executor', schemas))
        self.assertEqual(1, len(schema), "Schema for task executor service must be declared")

        schema = list(filter(lambda i: i['name'] == 'console', schemas))
        self.assertEqual(1, len(schema), "Schema for user console must be declared")

    @unittest.skip("is not implemented yet")
    def test_get_default_product_env(self):
        product = ResourceManager().get()

