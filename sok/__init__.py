import os
from .services.clusters import ClusterClient as Cluster

# Full path to local repository where product declarations are located
REPOSITORY = os.path.join(os.path.dirname(__file__), "..", 'products')


def product_path(product='sok'):
    """
    Get a full path to given product in the local repository
    :param product:
    :return:
    """
    return os.path.abspath(os.path.join(REPOSITORY, product))
