import os
from .services.inventory import ClusterClient as Cluster
from .version import __version__

DEFAULT_PRODUCT = 'sok'
# Full path to local repository where product declarations are located
REPOSITORY = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", 'products'))


def product_path(product=DEFAULT_PRODUCT, repository=REPOSITORY):
    """
    Get a full path to given product in the local repository
    """
    return os.path.abspath(os.path.join(repository, product))
