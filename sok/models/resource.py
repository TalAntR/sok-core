import os
from urllib.parse import urlparse


class Resource(object):
    """
    The class represents user defined information about particular
    service or file in deployed environment. It's supposed that each
    resource has an URI that identifies the resource.
    """

    __slots__ = ('_manager', '_uri', 'weight', 'islocal')

    MODULE_DELIMITER = '+'

    @classmethod
    def create_subtype(cls, name, *attributes):
        """
        Create a type with specified name to store configuration parameters.
        """
        return type('Rsc' + name.capitalize(), (cls,), dict(__slots__=attributes))

    @staticmethod
    def create_internal_config_name(service, template_name):
        """
        """
        return "{0}-{1}.{2}".format(service.name, template_name, service.index)

    def __init__(self, uri, module, **settings):
        """
        Creates a new endpoint for specified URI.
        """
        self._uri = uri if isinstance(uri, URI) else URI(uri)
        self._manager = module
        self.weight = settings.pop('weight', 1)
        self.islocal = 'false'

    @property
    def uri(self):
        """
        Returns URI instance for this service.
        """
        return self._uri

    @property
    def manager(self):
        return self._manager

    @property
    def hostname(self):
        """
        Returns URI instance for this service.
        """
        return self._uri.host.hostname

    @property
    def port(self):
        """
        Returns port number for service this endpoint
        """
        return self._uri.port

    def __repr__(self):
        return "<Rsc: {0}, {1}:{2}{3}>".format(self.manager.name, self.host.hostname, self.port, self._uri.path)

    def __hash__(self):
        return hash(str(self.index) + self.name + self.host.hostname + str(self.port))

    def __eq__(self, other):
        return self.name == other.name and self._uri == other.uri and self.index == other.index

