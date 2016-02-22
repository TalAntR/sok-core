import glob
import os
import sok.models
import yaml
from fileinput import FileInput
from .product import ProductHandler
from .environment import EnvHandler


def load_all(stream, env, product=None):
    """
    Parse all YAML documents in a stream
    and produce corresponding Python objects.
    """
    loader = IncludeResourceLoader(env, stream, product)
    try:
        while loader.check_data():
            yield loader.get_data()
    finally:
        loader.dispose()


class IncludeResourceLoader(yaml.Loader):

    TAG_INCLUDE = '!SOK:Include'
    TAG_PRODUCT = '!SOK:Product'
    TAG_ENVIRON = '!SOK:Environment'
    TAG_ROLE = '!SOK:Role'

    def __init__(self, environment, path, product=None):
        self.product = product
        self.environment = environment
        self.includes = {}
        self.caller = None
        self.add_constructor(self.TAG_INCLUDE, self.include_constructor)
        self.add_constructor(self.TAG_PRODUCT, self.product_constructor)
        self.add_constructor(self.TAG_ENVIRON, self.environment_constructor)
        self.add_constructor(self.TAG_ROLE, self.role_constructor)

        if os.path.isdir(path):
            self._path = path
            super().__init__(_YamlFileInput(files=glob.glob(os.path.join(path, '*'))))
        else:
            self._path = os.path.dirname(path)
            with open(path, 'r') as rsc:
                super().__init__(rsc)

    def include_constructor(self, loader, node):
        path = loader.construct_scalar(node)
        if not os.path.isabs(path):
            path = os.path.abspath(os.path.join(self._path, path))
        if os.path.isfile(path):
            loader = IncludeResourceLoader(self.environment, path, self.product)
            try:
                body = loader.get_single_data()
            finally:
                loader.dispose()
            return body
        raise ValueError("Path doesn't exist: " + path)

    def product_constructor(self, loader, node):
        product = loader.construct_mapping(node)
        self.product = sok.models.Product(product.pop('namespace'), product.pop('name'), **product)
        return self.product

    def environment_constructor(self, loader, node):
        env = loader.construct_mapping(node)
        product = env.pop('product', self.product)
        if not product:
            raise ValueError("Product object isn't defined in YAML configuration.")
        environment = sok.models.Environment(env.pop('name', 'default'), product, **env)
        return environment

    def role_constructor(self, loader, node):
        role = loader.construct_sequence(node, True)
        self._roles.append(sok.models.Role('hey', role))
        # print(self._roles, role, node)
        return self._roles


class _YamlFileInput(FileInput):
    """
    This class extends the FileInput class to use its functionality for working
    with collection of YAML files. The input represents such collection as a single
    stream.

    It's internal class which is used in this package only.
    """

    def read(self, _):
        """
        Just delegate a call to FileInput.readline method
        :param _: unused parameter, should a reference on buffer_size
        :return:
        """
        return self.readline()


class ResourceManager(object):
    """
    Loads an environment definition from YAML file.
    """

    def __init__(self, repo=sok.REPOSITORY):
        self._repo_path = repo
        self._product = self._environment = (None, None)
        self._roles = []

    def get(self, product=sok.DEFAULT_PRODUCT, env='local'):
        self._product = (product, None)
        self._environment = (env, None)

        path = sok.product_path(product, self._repo_path)
        meta = next(load_all(os.path.join(path, env), self._environment), {})
        return meta['environment']


class HandlerFactory(object):

    def __init__(self, manager=ResourceManager()):
        self._manager = manager

    def get_product_handler(self):
        return ProductHandler(self._manager)

    def get_environment_handler(self):
        return EnvHandler(self._manager)
