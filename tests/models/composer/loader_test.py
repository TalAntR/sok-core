"""

This is implementation of a test suite to check the implementation for JobRunnerPool class

All tests in this suite sould be passed.
"""
import unittest

import sok
from services.clusters.server.manager import ResourceManager


class YamlLoaderTest(unittest.TestCase):
    """
    A suite of tests to verify deserialization models (products, environments, resources ...)
     from YAML manifest.
    """

    def load_product_test(self):
        """
        Verifies that product is imported correctly from YAML declaration.
        """
        loader = ResourceManager(sok.product_path(), 'local')
        for d in loader.get():
            print(d)


