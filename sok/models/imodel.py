import zope.interface


class IModel(zope.interface.Interface):
    """
    Common definitions for all objects of the orchestration kit
    """

    __slots__ = ('_context', )

    classifier = zope.interface.Attribute("""Get classifier for this class""")

    def jsonify(self):
        """
        Get a dictionary which defines JSON representation for an object
        :return:
        """

    @staticmethod
    def create_property(key):
        """
        Create a property to extract specified value from internal dictionary
        """
        return property(lambda x: x._context[key])

    def __getitem__(self, item):
        """
        Get an attribute from internal storage like dictionary mode.
        """
        return self._context[item]
