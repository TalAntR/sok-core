import tempfile


class Product(object):
    """
    This class represents an information system (IS).

    YAML definition
    product: !!Product
      name: <product-name>
      namespace: <product-namespace>
      note: <some comments about product>
      workspace: <working directory on build server during deployment phase>
      ...
    """

    __slots__ = ('_name', '_namespace', '_note', '_workspace', '_e_schema', '_r_schema')

    def __init__(self, namespace, name, **kwargs):
        """
        Initialize product with given name and user-defined settings

        """
        self._namespace = namespace
        self._name = name
        self._note = kwargs.pop('note', '')
        self._e_schema = kwargs.pop('env-schema', [])
        self._r_schema = kwargs.pop('role-schema', [])
        self._workspace = kwargs.pop('workspace', tempfile.gettempdir())

    @property
    def name(self):
        """
        Gets a short name of a product.
        :return:
        """
        return self._name

    @property
    def namespace(self):
        """
        Gets product namespace which composes unique identifier
        together with product name and may define an owner for the set of products
        :return:
        """
        return self._namespace

    @property
    def note(self):
        """
        Gets a user-friendly description for a product
        :return:
        """
        return self._note

    @property
    def uid(self):
        """
        Gets unique identifier for the product
        :return:
        """
        return '.'.join((self._namespace, self._name))

    @property
    def workspace(self):
        """
        Get a global workspace for current product
        :return:
        """
        return self._workspace

    def __repr__(self):
        return "<Product: {0}:{1}>".format(self._namespace, self._name)
