import unittest
from core.common import Module
from core.registry import ModuleRegistry
from core.registry.registry import UnsupportedRegistryObject, DuplicatedRegistryObject
from examples.module import ModuleYamlProvider


class ModuleRegistryTest(unittest.TestCase):
    """
    """

    def test_add_module(self):
        """
        Add a module in a registry.
        """
        module_uid = 'test.mysql-server'
        registry = ModuleRegistry()

        mysql_type = Module.create_subtype('mysql', daemon='mysqld')
        registry.add(mysql_type(module_uid))

        mysql = registry.get(module_uid)

        self.assertEqual('mysql-server', mysql.name)
        self.assertEqual('mysqld', mysql.daemon)
        self.assertEqual(module_uid, mysql.uid)

    def test_add_non_module(self):
        """
        Check that exception is thrown when added instance hasn't Module subtype
        """
        registry = ModuleRegistry()
        self.assertRaises(UnsupportedRegistryObject, registry.add, 'I am string object')

    def test_add_module_again(self):
        """
        Try to add certain module twice.
        """
        module_uid = 'test.mysql-server'
        registry = ModuleRegistry()

        mysql_type = Module.create_subtype('mysql-server', daemon='mysqld')
        registry.add(mysql_type(module_uid))
        self.assertRaises(DuplicatedRegistryObject, registry.add, mysql_type(module_uid, daemon='mysql'))


class ModuleProviderTest(unittest.TestCase):
    """
    """

    def test_import_modules_in_registry(self):
        """
        Import modules from YAML configuration and add their in a module registry
        """
        registry = ModuleRegistry()
        ModuleYamlProvider.MODULE_STORAGE_FILE = "../ploy-modules.yml"

        mp = ModuleYamlProvider(registry)
        self.assertEqual(registry, mp.registry)
        mp.initialize()
        for m in mp.get_modules():
            self.assertIsInstance(m, Module)
        mp.enroll()

        m = registry.get('app-00-svc')
        self.assertEqual('app00d', m.daemon)
        self.assertEqual('/opt/app00', m.home)
        print(m.demands)
        self.assertEqual('/var/log/app-00/*', m.log_files)
        self.assertEqual('0.1', m.version)
        self.assertEqual('An application', m.description)

        m = registry.get('app-01-svc')
        self.assertEqual('app01d', m.daemon)
        self.assertEqual('/opt/app01', m.home)

        m = registry.get('app-bin')
        self.assertEqual('/opt/application', m.home)
