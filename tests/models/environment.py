"""
This is implementation of a test suite to check the implementation for JobRunnerPool class

All tests in this suite sould be passed.
"""
import unittest
from ploy.core.common.environment import OpsEnvironment


class OpsEnvironmentTest(unittest.TestCase):
    """
    A suite of tests to check job processing by pool of executors.
    """

    def env_attributes_test(self):
        """
        """
        env = OpsEnvironment("test-env")
        self.assertEqual("test-env", env.name)
        self.assertEqual("test-env", env.workspace)
        self.assertEqual("test-env", env.buildfarm)

