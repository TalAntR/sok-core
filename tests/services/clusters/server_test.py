"""

This is implementation of a test suite to check the implementation for JobRunnerPool class

All tests in this suite sould be passed.
"""
import threading
import unittest
from sok import Cluster
from sok.services.clusters.server import application
from wsgiref import simple_server


class ClusterApiTest(unittest.TestCase):
    """
    A suite of tests to verify deserialization models (products, environments, resources ...)
     from YAML manifest.
    """

    def setUp(self):
        self.httpd = simple_server.make_server("127.0.0.1", 14008, application)
        self.server = threading.Thread(target=self.httpd.serve_forever)
        self.server.start()
        self.client = Cluster("127.0.0.1", 14008)

    def tearDown(self):
        self.httpd.shutdown()
        self.server.join()

    def test_get_product(self):
        """
        Verifies that product is imported correctly from YAML declaration.
        """
        product = self.client.get_product('.sok')
        print(product)
        self.assertEqual('sok',  product.name)
        self.assertEqual('.',    product.namespace)
        self.assertEqual('.sok', product.uid)


