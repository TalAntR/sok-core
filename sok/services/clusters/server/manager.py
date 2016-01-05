import glob
import os
import sok
from fileinput import FileInput
from yaml import load_all
from .product import ProductHandler
from .environment import EnvHandler


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

    SHARED_YML_FOLDER = '.env'

    def __init__(self, repo=sok.REPOSITORY, filter='product'):
        self._repo_path = repo
        self._filter = filter

    def get(self, env='local', product=None):
        product = [os.path.join(sok.product_path(), 'product.yml')]
        env = glob.glob(os.path.join(sok.product_path(), env, '*'))
        common = glob.glob(os.path.join(sok.product_path(), self.SHARED_YML_FOLDER, '*'))
        meta = next(load_all(_YamlFileInput(files=product + env + common)), {})
        return meta[self._filter]

    def set_filter(self, key='product'):
        self._filter = key


class HandlerFactory(object):

    def __init__(self, manager=ResourceManager()):
        self._manager = manager

    def get_product_handler(self):
        return ProductHandler(self._manager)

    def get_environment_handler(self):
        return EnvHandler(self._manager)
