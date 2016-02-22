import requests
from abc import ABCMeta, abstractmethod
from sok.models import Product


class ICluster(metaclass=ABCMeta):
    """

    """

    @abstractmethod
    def get_product(self, uid):
        pass

    @abstractmethod
    def get_environment(self, uid):
        pass


class ClusterClient(ICluster):
    """
    HTTP client for the SOK Cluster Registry
    """

    def __init__(self, host, port=80):
        self.session = requests.Session()
        self.url_prefix = 'http://{0}:{1}'.format(host, port)

    def get(self, path, **kwargs):
        return self.session.get(self.url_prefix + path, **kwargs)

    def get_product(self, uid):
        resp = self.get("/registry/product/" + uid)
        return Product(**resp.json())

    def get_environment(self, uid):
        pass

    def get_role(self, uid):
        pass
