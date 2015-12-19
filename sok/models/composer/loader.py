import glob
import os
from abc import ABCMeta, abstractmethod
from yaml import load_all
from fileinput import FileInput


class ModelLoader(metaclass=ABCMeta):
    """

    """

    @abstractmethod
    def load_product_attributes(self, uid):
        pass

    @abstractmethod
    def load_env_attributes(self, uid):
        pass

    @abstractmethod
    def load_role_attributes(self, uid):
        pass

    @abstractmethod
    def load_resource_attributes(self, uid):
        pass


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


class YamlLoader(object):

    SHARED_YML_FOLDER = '.env'

    def __init__(self, path, env):
        product = [os.path.join(path, 'product.yml')]
        env = glob.glob(os.path.join(product_path(), env, '*'))
        common = glob.glob(os.path.join(product_path(), self.SHARED_YML_FOLDER, '*'))
        self._inputs = _YamlFileInput(files=product + env + common)

    def load(self):
        return load_all(self._inputs)

from sok import product_path

loader = YamlLoader(product_path(), 'local')
for d in loader.load():
    print(d)

