import glob
import os
import sok
from fileinput import FileInput
from yaml import load_all


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

    def __init__(self, path, env='local'):
        product = [os.path.join(path, 'product.yml')]
        env = glob.glob(os.path.join(sok.product_path(), env, '*'))
        common = glob.glob(os.path.join(sok.product_path(), self.SHARED_YML_FOLDER, '*'))
        self._inputs = _YamlFileInput(files=product + env + common)

    def load(self):
        return load_all(self._inputs)

