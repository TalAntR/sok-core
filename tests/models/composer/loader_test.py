
"""
This is implementation of a test suite to check the implementation for JobRunnerPool class

All tests in this suite sould be passed.
"""
import unittest
import os
from sok.models.composer.loader import YamlLoader


class YamlLoaderTest(unittest.TestCase):
    """
    A suite of tests to check job processing by pool of executors.
    """


    def load_files_test(self):
        """
        """
        stream = open('products/sok/product.yml')
        loader = YamlLoader(stream)
        print(loader.load_all())
        print("load result")


