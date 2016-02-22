
class Component(object):

    __slots__ = ('_manager', '_resources')

    def __init__(self, manager, resources=[]):
        """
        """
        #TODO: Add description for this constructor
        self._manager = manager
        self._resources = resources

    def manager(self):
        """
        Returns a manager object which defines how to perform different tasks
        for collection of resources in this component
        """
        return self._manager

    def __iter__(self):
        """
        Get an iterator by all resources in this component
        """
        #TODO: delegate this to manager: self._manager.get_iterator(self._resources)
        return iter(self._resources)


class Role(object):
    """
    The class represents a set of resources which are used together to provide some service.
    It is a logical unit for a system.

    Examples:
        - HDFS cluster may contain several severs and include few type software components (name nodes, data nodes),
        but it can be a single component on the logic level.
    """

    __slots__ = ('name', '_components')

    def __init__(self, name, components=[]):
        """
        Creates a collection of components with given name.
        """
        self.name = name
        self._components = components

    def __iter__(self):
        """
        This is an iterator by all components which this role includes.
        """
        return iter(self._components)

    def __getitem__(self, key):
        """
        Get an unit/particle with specified name.
        """
        key = key.name if isinstance(key, Module) else key
        if key in self._settings:
            return self._settings[key]
        raise KeyError("The role {0} doesn't contain module {1}".format(self.name, key))

    def __contains__(self, item):
        """
        Check that the role contains a specified unit/particle.
        """
        if isinstance(item, Module):
            return item.name in self._settings
        else:
            return item in self._settings

    def __repr__(self):
        """
        Returns string representation for a role
        """
        return "<Role: {0}>".format(self.name)
