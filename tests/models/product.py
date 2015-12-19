


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
