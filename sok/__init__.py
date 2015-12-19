import os

REPOSITORY = os.path.join(os.path.dirname(__file__), "..", 'products')


def product_path(product='sok'):
    return os.path.abspath(os.path.join(REPOSITORY, product))
