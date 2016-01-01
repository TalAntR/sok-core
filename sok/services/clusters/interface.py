import http.client
import urllib3
from abc import ABCMeta, abstractmethod


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

    def __init__(self, host, port):
        self._conn = http.client.HTTPConnection(host, port)

    def get_product(self, uid):
        self._conn.request("GET", "/registry/product/" + uid)
        response = self._conn.getresponse()
        return response.read()

    def get_environment(self, uid):
        pass

    def get_role(self, uid):
        pass
