import os


class Environment(object):
    """
    This class represents an single- or multi server environment where
    all product components should be installed. Also it may provide global
    settings which can be defined by users for configuration the components
    and services.

    YAML definition
    environment: !SOK:Environment
        name: <>
        note: <some comments about product>
        product: <a reference on a related product>
        workspace: <working directory on build server during deployment phase>
        ...
        auth:
            user:
            password:
            key:
        ...


    It always contains several required attributes:
      - name is an string identification of an environment
      - deployer is an instance of the Credential class to provide credentials on remote hosts
      during deployment process.
      - templates contains a list of paths where templates for cofiguration and other files are looked for.
      - workspace - a working directory on the local host.
    """

    __slots__ = ('_name', '_product', '_roles', '_note', '_workspace')

    def __init__(self, name, product, roles=[], **kwargs):
        self._name = name
        self._product = product
        self._roles = roles
        self._note = kwargs.pop('note', '')
        self._workspace = kwargs.pop('workspace', os.path.join(product.workspace, self._name))

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
    def note(self):
        """
        Gets user-friendly description for this environment.
        """
        return self._note

    @property
    def workspace(self):
        """
        A path to workspace for current environment
        """
        return self._workspace

    @property
    def uid(self):
        """
        Gets unique identifier of the environment
        """
        return ':'.join((self._product.uid, self._name))

    def __iter__(self):
        """
        Gets an iterator by all roles in the environment
        """
        return iter(self._roles)

    def __repr__(self):
        """
        Gets an iterator by all roles in the environment
        """
        return "<Environment: {0}:{1}>".format(self._product.uid, self._name)