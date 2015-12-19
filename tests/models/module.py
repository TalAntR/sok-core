import unittest
from core.common import Module
from core.common.factory import EntryFactory


class ModuleTest(unittest.TestCase):
    """
    A suite of tests to check job processing by pool of executors.
    """

    def test_creation_module_without_namespace(self):
        """
        """
        home, logs = '/opt/nginx', '/var/log/nginx'
        version = '1.6.2'
        m_type = Module.create_subtype('Nginx', 'log_files', home=home)
        module = m_type('nginx', version=version)
        module.log_files = logs

        self.assertEqual("nginx", module.uid)
        self.assertEqual("nginx", module.name)
        self.assertEqual("", module.namespace)
        self.assertEqual(home, module.home)
        self.assertEqual(logs, module.log_files)
        self.assertEqual(version, module.version)

    def test_creation_module_with_namespace(self):
        """
        """
        home = '/opt/nginx'
        m_type = Module.create_subtype('Nginx', home=home)
        module = m_type('my.nginx')

        self.assertEqual("my.nginx", module.uid)
        self.assertEqual("nginx", module.name)
        self.assertEqual("my", module.namespace)
        self.assertEqual(home, module.home)

    def test_creation_module_with_empty_name(self):
        """
        """
        home = '/opt/nginx'
        m_type = Module.create_subtype('Nginx', home=home)
        module = m_type('my.')

        self.assertEqual('my.', module.uid)
        self.assertEqual('', module.name)
        self.assertEqual('my', module.namespace)
        self.assertEqual(home, module.home)

    # def test_creation_modules_with_same_uid(self):
    #     """
    #     """
    #     module = EntryFactory().create_module('my.nginx', home="/opt/nginx")
    #     other = EntryFactory().create_module('my.nginx', sources="git://...")
    #     self.assertEqual(module, other)
    #     self.assertEqual(type(module), type(other))
    #     # print(EntryFactory()._modules)

