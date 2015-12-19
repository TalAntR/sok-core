"""
product: !!Product
  workspace: &workspace
  env-schema:
    - field: workspace
      required: true
      type: list
      default: *workspace
  role-schemas:
      - name: web-ui
        schema:

"""
from abc import ABCMeta, abstractmethod


class ProductBuilder(metaclass=ABCMeta):

    @abstractmethod
    def build(self, name, namespace='*'):
        pass


class YamlProductBuilder(ProductBuilder):
    """
    Builds a product model from YAML description
    """

    def __init__(self, stream, validator):
        self._validator = validator
        from yaml import load

    def build(self, name, namespace='*'):
        pass
