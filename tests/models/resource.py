import unittest
from core.common import Resource
from core.common.factory import EntryFactory


class ResourceTest(unittest.TestCase):
    """
    A suite of tests to check job processing by pool of executors.
    """

    def test_creation_resource(self):
        """
        """
        EntryFactory().create_module("git")
        rsc = EntryFactory().create_resource("git+https://bitbucket.org/talantr/d-ploy.git")
        self.assertIsInstance(rsc, Resource)
        self.assertEqual("git", rsc.module.name)
        self.assertEqual("https", rsc.uri.scheme)
        self.assertEqual("bitbucket.org", rsc.uri.hostname)

