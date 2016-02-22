"""
This suite includes tests which verify an implementation of embedded
Cluster API for the Service Orchestration Kit.

All tests in this suite must be passed.
"""
import unittest
from sok.models import Product, Environment
from sok.services.inventory.server.manager import ResourceManager


class ResourceManagerTest(unittest.TestCase):
    """
    A suite of tests to verify deserialization models (products, environments, resources ...)
     from YAML manifest.
    """

    def test_get_default_product(self):
        """
        Verifies that the 'sok' product is imported from YAML declaration by default.
        """

        product = ResourceManager().get().product
        self.assertIsInstance(product, Product, "Product type must be dictionary")

        self.assertIsInstance(product.name, str, "Product name must have string type")
        self.assertEqual('sok', product.name, "Name is incorrect for default product")

        self.assertIsInstance(product.namespace, str, "Product namespace must have string type")
        self.assertEqual('', product.namespace, "Namespace is incorrect for default product")

        self.assertIsInstance(product.note, str, "Product notes must have string type")
        self.assertEqual('The Service Orchestration Kit product',
                         product.note, "Description is incorrect for default product")

        # env_schema = product['env-schema']
        # self.assertIsInstance(env_schema, list, "Schema for environments must have a list type")
        # self.assertEqual([], env_schema, "Schema for SOK environment must be an empty list")
        #
        # schemas = product['role-schemas']
        # self.assertIsInstance(schemas, list, "Schema for roles must have a list type")
        #
        # schema = list(filter(lambda i: i['name'] == 'inventory', schemas))
        # self.assertEqual(1, len(schema), "Schema for inventory service must be declared")
        #
        # schema = list(filter(lambda i: i['name'] == 'registry', schemas))
        # self.assertEqual(1, len(schema), "Schema for task registry service must be declared")
        #
        # schema = list(filter(lambda i: i['name'] == 'executor', schemas))
        # self.assertEqual(1, len(schema), "Schema for task executor service must be declared")
        #
        # schema = list(filter(lambda i: i['name'] == 'console', schemas))
        # self.assertEqual(1, len(schema), "Schema for user console must be declared")

    def test_get_default_env(self):
        env = ResourceManager().get()
        self.assertIsInstance(env, Environment, "Environment type must be sok.models.Environment")

        self.assertIsInstance(env.name, str, "Environment name must have string type")
        self.assertEqual('local', env.name, "Name is incorrect for default environment")

        self.assertIsInstance(env.uid, str, "Unique identifier must have string type")
        self.assertEqual(':sok:local', env.uid, "Unique identifier is incorrect for default environment")

        self.assertIsInstance(env.note, str, "Environment notes must have string type")
        self.assertEqual('A single server environment, all services are located on the localhost',
                         env.note, "Description is incorrect for default environment")

        self.assertIsInstance(env.workspace, str, "Workspace for default environment must be a string")
        self.assertEqual('./local', env.workspace, "Path to workspace is incorrect for default environment")
