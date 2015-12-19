from .imodel import IModel


class OpsEnv(IModel):
    """
    This class provides settings for build or deployment operations.

    It always contains several required attributes:
      - name is an string identification of an environment
      - deployer is an instance of the Credential class to provide credentials on remote hosts
      during deployment process.
      - templates contains a list of paths where templates for cofiguration and other files are looked for.
      - workspace - a working directory on the local host.
    """

    __slots__ = ('_name', '_product', '_roles', 'workspace', 'templates', 'hosts')


    def __init__(self, name, product, roles, **kwargs):
        self.hosts = {}
        self._name = name
        self._product = product
        self._roles = roles
        self.workspace = kwargs.pop('workspace', os.getcwd())
        # for k, v in kwargs.iteritems():
        #     setattr(self, k, v)
        #TODO: convert passed or default value to list
        self.templates = kwargs.pop('templates', os.path.join(self.workspace, 'templates'))

    @property
    def product(self):
        """
        Gets a product, the environment belongs to
        """
        return self._product

    @property
    def name(self):
        """
        Gets short name of the environment
        """
        return self._name

    @property
    def uid(self):
        """
        Gets unique identifier of the environment
        """
        return self.make_uid(self._name, self._product.name, self._product.namespace)

    def _template_locations(self):
        """
        This generator returns full path for each directory in the templates_home property.
        Just for Linux hosts.
        """
        for path in self.templates_home:
            yield path if path[0] == '/' else self.workspace + '/' + path

    def __iter__(self):
        """
        Gets an iterator by all roles in the environment
        """
        return self._roles.itervalues()